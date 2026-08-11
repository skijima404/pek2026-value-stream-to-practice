#!/usr/bin/env python3
"""Validate governed Markdown structure without third-party dependencies."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_NOTE_ID_PATTERN = r"RN-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*"
NODE_DIRS = {
    "01_working/raw-notes": ("raw_note", RAW_NOTE_ID_PATTERN),
    "02_analysis/observations": (
        "observation",
        r"OBS-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
    "02_analysis/hypothesis-episodes": (
        "hypothesis_episode",
        r"HYP-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
    "02_analysis/patterns": (
        "pattern",
        r"PAT-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
    "04_decisions/risk-decisions": (
        "risk_decision",
        r"RSK-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
}
TEMPLATE_SPECS = {
    "templates/raw-note.md": "raw_note",
    "templates/observation.md": "observation",
    "templates/hypothesis-episode.md": "hypothesis_episode",
    "templates/pattern.md": "pattern",
    "templates/risk-decision.md": "risk_decision",
}
RAW_REQUIRED = {
    "id",
    "type",
    "title",
    "content_language",
    "created_at",
    "content_origin",
    "created_by",
    "source_platform",
    "capture_mode",
    "imported_by",
    "review_status",
    "sanitization_status",
    "sanitization_checked_at",
    "sanitization_checked_by",
    "tags",
}
DERIVED_REQUIRED = {
    "id",
    "type",
    "title",
    "content_language",
    "created_at",
    "created_by",
    "status",
    "confidence",
    "knowledge_basis",
    "relations",
}
DERIVED_REVIEW_REQUIRED = {
    "reviewed_at",
    "reviewed_by",
    "review_scope",
}
RISK_DECISION_REQUIRED = {
    "id",
    "type",
    "title",
    "content_language",
    "created_at",
    "created_by",
    "decision_status",
    "target_node",
    "target_component_id",
    "risk_response",
    "decision_sufficiency",
    "decided_by",
    "decided_at",
    "relations",
}
ENUMS = {
    "content_language": {"ja"},
    "content_origin": {"human_direct", "assist_a_generated", "mixed"},
    "source_platform": {"local", "chatgpt", "codex", "other"},
    "capture_mode": {"direct", "copy_paste", "transcript", "import", "assisted"},
    "review_status": {"unreviewed", "reviewed", "corrected"},
    "sanitization_status": {"not_reviewed", "not_needed", "sanitized"},
    "status": {"proposed", "reviewed", "rejected", "superseded"},
    "confidence": {"low", "medium", "high", "not_assessed"},
    "hypothesis_scope": {"session", "practice", "not_assessed"},
    "hypothesis_level": {"value", "solution", "feature", "not_assessed"},
    "review_scope": {"intent_alignment"},
    "decision_status": {"current", "superseded", "withdrawn"},
    "risk_response": {
        "investigate_more",
        "mitigate",
        "proceed_with_risk",
        "avoid",
        "transfer",
    },
    "decision_sufficiency": {
        "insufficient",
        "sufficient_for_next_step",
        "sufficient_with_conditions",
        "sufficient_for_current_scope",
    },
}
RELATION_TYPES = {
    "derived_from",
    "tests",
    "supports",
    "challenges",
    "adopted_from",
    "corrects",
    "supersedes",
    "rejected_by",
    "superseded_by",
    "references",
    "evaluates",
    "informed_by",
}
KNOWLEDGE_BASES = {
    "recorded_statement",
    "practitioner_experience",
    "case_recollection",
    "external_research",
    "direct_observation",
    "explicit_validation",
    "reasoned_synthesis",
}
TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$"
)
JAPANESE_TEXT = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
COMPONENT_ID = re.compile(r"U[1-9][0-9]*")
DECISION_IMPORTANCE = {"critical", "high", "medium", "low"}
COVERAGE_STATES = {"not_checked", "partially_checked", "checked_for_current_scope"}
COMPONENT_FINDINGS = {"unknown", "supports", "challenges", "mixed", "inconclusive"}
APPLICABILITY = {"direct", "analogous", "contextual", "unknown"}
VALIDATION_APPROACHES = {"experiment", "research", "interview", "not_selected"}
VALIDATION_DISPOSITIONS = {
    "proceed",
    "revise",
    "validate_further",
    "stop_for_current_scope",
    "not_decided",
}
HYPOTHESIS_LEVEL_ORDER = {"value": 0, "solution": 1, "feature": 2}
GENERATED_VIEW_SCRIPT = ROOT / "scripts/generate_analysis_views.py"


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, ["missing opening YAML frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing YAML frontmatter delimiter"]

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line.startswith((" ", "\t", "#")):
            continue
        match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if match:
            fields[match.group(1)] = (match.group(2) or "").strip().strip("\"'")
    return fields, errors


def parse_relations(path: Path) -> list[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        end = lines.index("---", 1)
    except (ValueError, IndexError):
        return []

    relations: list[tuple[str, str]] = []
    in_relations = False
    relation_type = ""
    for line in lines[1:end]:
        if line == "relations:":
            in_relations = True
            continue
        if in_relations and line and not line.startswith((" ", "\t")):
            break
        type_match = re.match(r"^\s+- type:\s*([a-z_]+)\s*$", line)
        if in_relations and type_match:
            relation_type = type_match.group(1)
            continue
        target_match = re.match(r"^\s+target:\s*([A-Za-z0-9-]+)\s*$", line)
        if in_relations and target_match and relation_type:
            relations.append((relation_type, target_match.group(1)))
            relation_type = ""
    return relations


def parse_list_field(path: Path, field_name: str) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        end = lines.index("---", 1)
    except (ValueError, IndexError):
        return []

    values: list[str] = []
    in_field = False
    for line in lines[1:end]:
        if line == f"{field_name}:":
            in_field = True
            continue
        if in_field and line and not line.startswith((" ", "\t")):
            break
        value_match = re.match(r"^\s+-\s+([a-z_]+)\s*$", line)
        if in_field and value_match:
            values.append(value_match.group(1))
    return values


def parse_hypothesis_result(path: Path) -> str:
    document = path.read_text(encoding="utf-8")
    match = re.search(
        r"^## 結果\s*$\n+\s*`(not_tested|supports|challenges|inconclusive)`\s*$",
        document,
        re.MULTILINE,
    )
    return match.group(1) if match else ""


def parse_validation_approach(path: Path) -> tuple[str, list[str]]:
    """Parse the optional lightweight validation approach from a HYP body."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        heading = lines.index("## 検証")
    except ValueError:
        return "", []
    block: list[str] = []
    for line in lines[heading + 1 :]:
        if line.startswith("## "):
            break
        block.append(line)
    matches = [
        re.fullmatch(r"- アプローチ:\s*`([^`]+)`\s*", line)
        for line in block
    ]
    values = [match.group(1) for match in matches if match]
    if len(values) != 1:
        return "", ["lightweight validation requires exactly one approach"]
    approach = values[0]
    if approach not in VALIDATION_APPROACHES:
        return approach, [f"non-canonical validation approach: {approach}"]
    return approach, []


def parse_validation_disposition(path: Path) -> tuple[str, list[str]]:
    """Parse the optional lightweight validation disposition from a HYP body."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        heading = lines.index("## 次の判断")
    except ValueError:
        return "", []
    block: list[str] = []
    for line in lines[heading + 1 :]:
        if line.startswith("## "):
            break
        block.append(line)
    matches = [
        re.fullmatch(r"- 判断:\s*`([^`]+)`\s*", line)
        for line in block
    ]
    values = [match.group(1) for match in matches if match]
    if len(values) != 1:
        return "", ["lightweight validation requires exactly one disposition"]
    disposition = values[0]
    if disposition not in VALIDATION_DISPOSITIONS:
        return disposition, [
            f"non-canonical validation disposition: {disposition}"
        ]
    return disposition, []


def parse_validation_components(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    components: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    try:
        heading = lines.index("## 検証対象の分解")
    except ValueError:
        return components, errors

    table_lines: list[str] = []
    for line in lines[heading + 1 :]:
        if line.startswith("## "):
            break
        if line.strip().startswith("|"):
            table_lines.append(line.strip())
    if len(table_lines) < 3:
        return components, ["validation component section requires a Markdown table"]

    expected_header = [
        "ID",
        "Uncertainty",
        "Decision importance",
        "Evidence refs",
        "Coverage state",
        "Finding",
        "Applicability",
        "Residual uncertainty",
    ]
    header = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    if header != expected_header:
        errors.append("validation component table has non-canonical columns")

    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(expected_header):
            errors.append("validation component row must contain exactly eight columns")
            continue
        component = dict(zip(expected_header, cells))
        component_id = component["ID"]
        if component_id in components:
            errors.append(f"duplicate validation component ID: {component_id}")
            continue
        components[component_id] = component
    if not components:
        errors.append("validation component table requires at least one component")
    return components, errors


def validate_validation_components(
    components: dict[str, dict[str, str]], node_ids: set[str]
) -> list[str]:
    errors: list[str] = []
    for component_id, component in components.items():
        if not COMPONENT_ID.fullmatch(component_id):
            errors.append(f"invalid validation component ID: {component_id}")
        importance = component["Decision importance"]
        if importance not in DECISION_IMPORTANCE:
            errors.append(
                f"{component_id} has non-canonical decision importance: {importance}"
            )
        coverage = component["Coverage state"]
        if coverage not in COVERAGE_STATES:
            errors.append(f"{component_id} has non-canonical coverage state: {coverage}")
        finding = component["Finding"]
        if finding not in COMPONENT_FINDINGS:
            errors.append(f"{component_id} has non-canonical finding: {finding}")
        applicability = component["Applicability"]
        if applicability not in APPLICABILITY:
            errors.append(
                f"{component_id} has non-canonical applicability: {applicability}"
            )
        if not component["Uncertainty"]:
            errors.append(f"{component_id} requires an uncertainty description")
        if not component["Residual uncertainty"]:
            errors.append(
                f"{component_id} requires a residual uncertainty description"
            )

        evidence_field = component["Evidence refs"]
        evidence_refs = [] if evidence_field == "none" else [
            value.strip() for value in evidence_field.split(",") if value.strip()
        ]
        if coverage == "not_checked":
            if evidence_refs or finding != "unknown" or applicability != "unknown":
                errors.append(
                    f"{component_id} not_checked requires no evidence, unknown finding, "
                    "and unknown applicability"
                )
        elif not evidence_refs:
            errors.append(f"{component_id} checked coverage requires Observation evidence")
        elif finding == "unknown":
            errors.append(
                f"{component_id} checked coverage requires a non-unknown finding"
            )
        for evidence_id in evidence_refs:
            if not evidence_id.startswith("OBS-"):
                errors.append(
                    f"{component_id} evidence must reference an Observation: {evidence_id}"
                )
            elif evidence_id not in node_ids:
                errors.append(
                    f"{component_id} evidence Observation does not exist: {evidence_id}"
                )
    return errors


def find_hypothesis_path(node_id: str) -> Path | None:
    directory = ROOT / "02_analysis/hypothesis-episodes"
    for path in directory.glob("*.md"):
        fields, _ = parse_frontmatter(path)
        if fields.get("id") == node_id:
            return path
    return None


def contains_japanese_content(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0] == "---":
        try:
            lines = lines[lines.index("---", 1) + 1 :]
        except ValueError:
            return False
    return JAPANESE_TEXT.search("\n".join(lines)) is not None


def discover_node_ids() -> tuple[set[str], list[tuple[Path, str]]]:
    node_ids: set[str] = set()
    failures: list[tuple[Path, str]] = []
    search_roots = [ROOT / relative_dir for relative_dir in NODE_DIRS]
    for directory in search_roots:
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            fields, _ = parse_frontmatter(path)
            node_id = fields.get("id")
            if not node_id:
                continue
            if node_id in node_ids:
                failures.append((path, f"duplicate node id: {node_id}"))
            node_ids.add(node_id)
    external_inputs = ROOT / "10_external-inputs"
    if external_inputs.is_dir():
        for path in sorted(external_inputs.rglob("*.md")):
            if path.name == "README.md":
                continue
            fields, _ = parse_frontmatter(path)
            node_id = fields.get("id")
            if not node_id:
                continue
            if node_id in node_ids:
                failures.append((path, f"duplicate node id: {node_id}"))
            node_ids.add(node_id)
    return node_ids, failures


def validate_node(
    path: Path, expected_type: str, id_pattern: str, node_ids: set[str]
) -> list[str]:
    fields, errors = parse_frontmatter(path)
    if errors:
        return errors
    if expected_type == "raw_note":
        required = RAW_REQUIRED
    elif expected_type == "risk_decision":
        required = RISK_DECISION_REQUIRED
    else:
        required = DERIVED_REQUIRED
    missing = sorted(required - fields.keys())
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    node_id = fields.get("id", "")
    if node_id != path.stem:
        errors.append(f"id must match filename stem: {path.stem}")
    if node_id and not re.fullmatch(id_pattern, node_id):
        errors.append("id does not match naming convention")
    if fields.get("type") != expected_type:
        errors.append(f"type must be {expected_type}")
    if fields.get("created_at") and not TIMESTAMP.fullmatch(fields["created_at"]):
        errors.append("created_at must be ISO 8601 with timezone")
    if fields.get("content_language") == "ja" and not contains_japanese_content(path):
        errors.append("content_language is ja but body contains no Japanese text")
    for field, allowed in ENUMS.items():
        value = fields.get(field)
        if value is not None and value not in allowed:
            errors.append(f"{field} has non-canonical value: {value}")
    if expected_type == "raw_note":
        sanitization_status = fields.get("sanitization_status")
        checked_at = fields.get("sanitization_checked_at")
        checked_by = fields.get("sanitization_checked_by")
        if sanitization_status == "not_reviewed":
            if checked_at != "none" or checked_by != "none":
                errors.append(
                    "not_reviewed sanitization must have no checker or timestamp"
                )
        elif sanitization_status in {"not_needed", "sanitized"}:
            if not checked_at or not TIMESTAMP.fullmatch(checked_at):
                errors.append(
                    "completed sanitization check requires an ISO 8601 timestamp"
                )
            if not checked_by or checked_by == "none":
                errors.append("completed sanitization check requires a checker")
    if expected_type == "hypothesis_episode":
        if "hypothesis_scope" not in fields:
            errors.append("hypothesis episode requires hypothesis_scope")
        if "hypothesis_level" not in fields:
            errors.append("hypothesis episode requires hypothesis_level")
    if expected_type not in {"raw_note", "risk_decision"}:
        knowledge_bases = parse_list_field(path, "knowledge_basis")
        if not knowledge_bases:
            errors.append("knowledge_basis must contain at least one value")
        for basis in knowledge_bases:
            if basis not in KNOWLEDGE_BASES:
                errors.append(f"knowledge_basis has non-canonical value: {basis}")
        if len(knowledge_bases) != len(set(knowledge_bases)):
            errors.append("knowledge_basis must not contain duplicate values")
        if expected_type == "hypothesis_episode":
            result = parse_hypothesis_result(path)
            if not result:
                errors.append("hypothesis episode requires a canonical result")
            elif result == "not_tested" and "explicit_validation" in knowledge_bases:
                errors.append(
                    "not_tested hypothesis must not declare explicit_validation"
                )
            elif result in {"supports", "challenges", "inconclusive"} and (
                "explicit_validation" not in knowledge_bases
            ):
                errors.append(
                    "completed hypothesis result requires explicit_validation"
                )
            approach, approach_errors = parse_validation_approach(path)
            errors.extend(approach_errors)
            disposition, disposition_errors = parse_validation_disposition(path)
            errors.extend(disposition_errors)
            if approach and not disposition:
                errors.append(
                    "lightweight validation requires a next-decision disposition"
                )
            if approach == "not_selected" and result != "not_tested":
                errors.append(
                    "completed lightweight validation requires a selected approach"
                )
            if result in {"supports", "challenges", "inconclusive"} and (
                disposition == "not_decided"
            ):
                errors.append(
                    "completed lightweight validation requires a decided disposition"
                )
            components, component_errors = parse_validation_components(path)
            errors.extend(component_errors)
            errors.extend(validate_validation_components(components, node_ids))
            relation_targets = {target for _, target in parse_relations(path)}
            for component_id, component in components.items():
                evidence_field = component["Evidence refs"]
                evidence_refs = (
                    []
                    if evidence_field == "none"
                    else [
                        value.strip()
                        for value in evidence_field.split(",")
                        if value.strip()
                    ]
                )
                for evidence_id in evidence_refs:
                    if evidence_id not in relation_targets:
                        errors.append(
                            f"{component_id} evidence requires a typed frontmatter "
                            f"relation: {evidence_id}"
                        )
            checked_components = any(
                component["Coverage state"] != "not_checked"
                for component in components.values()
            )
            if checked_components and result == "not_tested":
                errors.append(
                    "checked validation components are incompatible with not_tested result"
                )
        if fields.get("status") == "reviewed":
            missing_review = sorted(DERIVED_REVIEW_REQUIRED - fields.keys())
            if missing_review:
                errors.append(
                    "reviewed derived node missing review fields: "
                    + ", ".join(missing_review)
                )
            reviewed_at = fields.get("reviewed_at")
            if reviewed_at and not TIMESTAMP.fullmatch(reviewed_at):
                errors.append("reviewed_at must be ISO 8601 with timezone")
            reviewed_by = fields.get("reviewed_by", "")
            if reviewed_by and not re.fullmatch(
                r"human:[a-z0-9][a-z0-9._-]*", reviewed_by
            ):
                errors.append("reviewed_by must use a human:* identifier")
        relations = parse_relations(path)
        if not relations:
            errors.append("derived node must contain at least one relation")
        for relation_type, target in relations:
            if relation_type not in RELATION_TYPES:
                errors.append(f"unknown relation type: {relation_type}")
            if target not in node_ids:
                errors.append(f"relation target does not exist: {target}")
    elif expected_type == "risk_decision":
        decided_at = fields.get("decided_at", "")
        if decided_at and not TIMESTAMP.fullmatch(decided_at):
            errors.append("decided_at must be ISO 8601 with timezone")
        decided_by = fields.get("decided_by", "")
        if decided_by and not re.fullmatch(r"human:[a-z0-9][a-z0-9._-]*", decided_by):
            errors.append("decided_by must use a human:* identifier")
        target_node = fields.get("target_node", "")
        if not target_node.startswith("HYP-") or target_node not in node_ids:
            errors.append("target_node must reference an existing Hypothesis Episode")
        target_component_id = fields.get("target_component_id", "")
        if not COMPONENT_ID.fullmatch(target_component_id):
            errors.append("target_component_id must use the U<number> form")
        target_path = find_hypothesis_path(target_node)
        if target_path:
            components, component_errors = parse_validation_components(target_path)
            if component_errors:
                errors.append("target Hypothesis Episode has an invalid component table")
            elif target_component_id not in components:
                errors.append(
                    f"target component does not exist in {target_node}: {target_component_id}"
                )

        relations = parse_relations(path)
        if not relations:
            errors.append("risk decision must contain relations")
        evaluates_targets = [target for kind, target in relations if kind == "evaluates"]
        if evaluates_targets != [target_node]:
            errors.append(
                "risk decision requires exactly one evaluates relation matching target_node"
            )
        for relation_type, target in relations:
            if relation_type not in RELATION_TYPES:
                errors.append(f"unknown relation type: {relation_type}")
            if target not in node_ids:
                errors.append(f"relation target does not exist: {target}")
            if relation_type == "informed_by" and not target.startswith("OBS-"):
                errors.append("informed_by must reference an Observation")
        relation_kinds = {kind for kind, _ in relations}
        decision_status = fields.get("decision_status")
        if decision_status == "superseded" and "superseded_by" not in relation_kinds:
            errors.append("superseded risk decision requires superseded_by")
        if decision_status == "current" and "superseded_by" in relation_kinds:
            errors.append("current risk decision must not declare superseded_by")
    return errors


def validate_raw_note_for_projection(path: Path) -> list[str]:
    """Apply the canonical Raw Note schema before any metadata is projected."""
    return validate_node(path, "raw_note", RAW_NOTE_ID_PATTERN, set())


def validate_hypothesis_test_edge(
    source_id: str,
    source_fields: dict[str, str],
    target_id: str,
    target_fields: dict[str, str],
) -> list[str]:
    """Validate a reserved HYP-to-HYP immediate hierarchy edge."""
    errors: list[str] = []
    source_scope = source_fields.get("hypothesis_scope")
    target_scope = target_fields.get("hypothesis_scope")
    source_level = source_fields.get("hypothesis_level")
    target_level = target_fields.get("hypothesis_level")
    if source_scope != target_scope:
        errors.append(
            "tests hierarchy must stay in one hypothesis_scope: "
            f"{source_id} -> {target_id}"
        )
    if (
        source_level not in HYPOTHESIS_LEVEL_ORDER
        or target_level not in HYPOTHESIS_LEVEL_ORDER
        or HYPOTHESIS_LEVEL_ORDER[source_level]
        != HYPOTHESIS_LEVEL_ORDER[target_level] + 1
    ):
        errors.append(
            "tests hierarchy must target the immediately higher level: "
            f"{source_id} -> {target_id}"
        )
    return errors


def validate_generated_views() -> list[str]:
    """Check that disposable graph and Markdown navigation match source nodes."""
    if not GENERATED_VIEW_SCRIPT.is_file():
        return ["generated view script is missing"]
    result = subprocess.run(
        [sys.executable, str(GENERATED_VIEW_SCRIPT), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return []
    messages = [line for line in result.stdout.splitlines() if line.strip()]
    messages.extend(line for line in result.stderr.splitlines() if line.strip())
    return messages or ["generated view check failed without diagnostics"]


def main() -> int:
    node_ids, failures = discover_node_ids()
    checked = 0
    templates_checked = 0
    for relative_path, expected_type in TEMPLATE_SPECS.items():
        path = ROOT / relative_path
        if not path.is_file():
            failures.append((path, "required template is missing"))
            continue
        fields, errors = parse_frontmatter(path)
        for error in errors:
            failures.append((path, error))
        if expected_type == "raw_note":
            required = RAW_REQUIRED
        elif expected_type == "risk_decision":
            required = RISK_DECISION_REQUIRED
        else:
            required = DERIVED_REQUIRED
        missing = sorted(required - fields.keys())
        if missing:
            failures.append(
                (path, f"template missing required fields: {', '.join(missing)}")
            )
        if fields.get("type") != expected_type:
            failures.append((path, f"template type must be {expected_type}"))
        if (
            expected_type == "hypothesis_episode"
            and "hypothesis_level" not in fields
        ):
            failures.append((path, "hypothesis template requires hypothesis_level"))
        if (
            expected_type == "hypothesis_episode"
            and "hypothesis_scope" not in fields
        ):
            failures.append((path, "hypothesis template requires hypothesis_scope"))
        if expected_type not in {"raw_note", "risk_decision"}:
            knowledge_bases = parse_list_field(path, "knowledge_basis")
            if not knowledge_bases:
                failures.append(
                    (path, "template knowledge_basis must contain at least one value")
                )
            for basis in knowledge_bases:
                if basis not in KNOWLEDGE_BASES:
                    failures.append(
                        (path, f"template knowledge_basis has non-canonical value: {basis}")
                    )
        if expected_type == "hypothesis_episode":
            approach, approach_errors = parse_validation_approach(path)
            for error in approach_errors:
                failures.append((path, error))
            if approach != "not_selected":
                failures.append(
                    (path, "hypothesis template must start with not_selected approach")
                )
            disposition, disposition_errors = parse_validation_disposition(path)
            for error in disposition_errors:
                failures.append((path, error))
            if disposition != "not_decided":
                failures.append(
                    (path, "hypothesis template must start with not_decided disposition")
                )
            components, component_errors = parse_validation_components(path)
            for error in component_errors:
                failures.append((path, error))
            for error in validate_validation_components(components, set()):
                if "does not exist" not in error:
                    failures.append((path, error))
        if not contains_japanese_content(path):
            failures.append((path, "template body must contain Japanese text"))
        templates_checked += 1

    for path in sorted((ROOT / "03_artifacts").rglob("*.md")):
        fields, errors = parse_frontmatter(path)
        for error in errors:
            failures.append((path, error))
        if fields.get("content_language") != "ja":
            failures.append((path, "artifact Markdown must declare content_language: ja"))
        if not contains_japanese_content(path):
            failures.append((path, "artifact Markdown body must contain Japanese text"))

    for relative_dir, (expected_type, id_pattern) in NODE_DIRS.items():
        directory = ROOT / relative_dir
        if not directory.is_dir():
            failures.append((directory, "required directory is missing"))
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            checked += 1
            for error in validate_node(path, expected_type, id_pattern, node_ids):
                failures.append((path, error))

    hypothesis_paths = {
        path.stem: path
        for path in sorted((ROOT / "02_analysis/hypothesis-episodes").glob("HYP-*.md"))
    }
    for source_id, source_path in hypothesis_paths.items():
        source_fields, _ = parse_frontmatter(source_path)
        for relation_type, target_id in parse_relations(source_path):
            if relation_type != "tests" or target_id not in hypothesis_paths:
                continue
            target_fields, _ = parse_frontmatter(hypothesis_paths[target_id])
            for error in validate_hypothesis_test_edge(
                source_id, source_fields, target_id, target_fields
            ):
                failures.append((source_path, error))

    current_risk_targets: dict[tuple[str, str], Path] = {}
    risk_directory = ROOT / "04_decisions/risk-decisions"
    if risk_directory.is_dir():
        for path in sorted(risk_directory.glob("*.md")):
            if path.name == "README.md":
                continue
            fields, _ = parse_frontmatter(path)
            if fields.get("decision_status") != "current":
                continue
            target = (
                fields.get("target_node", ""),
                fields.get("target_component_id", ""),
            )
            previous = current_risk_targets.get(target)
            if previous:
                failures.append(
                    (
                        path,
                        "multiple current risk decisions target the same component: "
                        f"{previous.stem}",
                    )
                )
            else:
                current_risk_targets[target] = path

    for error in validate_generated_views():
        failures.append((ROOT / "02_analysis/README.md", error))

    if failures:
        for path, error in failures:
            print(f"ERROR {path.relative_to(ROOT)}: {error}")
        print(
            "Validation failed: "
            f"{len(failures)} error(s), {checked} node(s), "
            f"{templates_checked} template(s) checked."
        )
        return 1
    print(
        "Validation passed: "
        f"{checked} governed node(s), {templates_checked} template(s) checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
