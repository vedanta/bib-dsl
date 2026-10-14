"""Export BiB models to Mermaid flowchart syntax.

Mermaid is used as an interoperable rendering format; BiB YAML remains the
canonical source of model data.
"""

from html import escape
from pathlib import Path
import re
from typing import Any, Dict, Optional


def _properties(items: Any) -> Dict[str, Any]:
    """Flatten BiB's list-of-single-key mappings into one property mapping."""
    result: Dict[str, Any] = {}
    if isinstance(items, dict):
        return items
    if not isinstance(items, list):
        return result
    for item in items:
        if isinstance(item, dict):
            result.update(item)
    return result


def _safe_id(name: str, index: int) -> str:
    stem = re.sub(r"[^A-Za-z0-9_]", "_", str(name)).strip("_") or "node"
    if not stem[0].isalpha():
        stem = f"n_{stem}"
    return f"bib_{stem}_{index}"


def _label(value: Any) -> str:
    return escape(str(value), quote=True).replace("\n", "<br/>")


def render_mermaid(model: dict, output_file: Optional[str] = None) -> str:
    """Convert BiB's hierarchy and dependencies to Mermaid flowchart syntax.

    Args:
        model: BiB model mapping node identifiers to their property lists.
        output_file: Optional path to write the generated Mermaid source.

    Returns:
        Mermaid source text, suitable for a Markdown ```mermaid block.
    """
    if not isinstance(model, dict):
        raise TypeError("BiB model must be a mapping of node names to properties")

    node_ids = {
        str(name): _safe_id(str(name), index)
        for index, name in enumerate(model.keys(), start=1)
    }
    props_by_name = {
        str(name): _properties(props) for name, props in model.items()
    }
    used_ids = set(node_ids.values())

    lines = ["flowchart TD"]

    for name, props in props_by_name.items():
        label = props.get("common_name") or name
        if props.get("type"):
            label = f"{label} ({props['type']})"
        lines.append(f'    {node_ids[name]}["{_label(label)}"]')

    for name, props in props_by_name.items():
        parent = props.get("parent")
        if parent is not None and str(parent) in node_ids:
            lines.append(f"    {node_ids[str(parent)]} --> {node_ids[name]}")

    external_ids: Dict[str, str] = {}
    for name, props in props_by_name.items():
        dependencies = props.get("depends", [])
        if isinstance(dependencies, (str, dict)):
            dependencies = [dependencies]
        if not isinstance(dependencies, list):
            continue

        for dependency in dependencies:
            if isinstance(dependency, dict):
                target = dependency.get("node")
                relationship = dependency.get("type") or "depends on"
            else:
                target = dependency
                relationship = "depends on"
            if target is None:
                continue

            target_name = str(target)
            if target_name in node_ids:
                target_id = node_ids[target_name]
            else:
                if target_name not in external_ids:
                    index = len(node_ids) + len(external_ids) + 1
                    target_id = _safe_id(f"external_{target_name}", index)
                    while target_id in used_ids:
                        index += 1
                        target_id = _safe_id(f"external_{target_name}", index)
                    external_ids[target_name] = target_id
                    used_ids.add(target_id)
                    lines.append(f'    {target_id}["{_label(target_name)} (external)"]')
                target_id = external_ids[target_name]
            lines.append(
                f"    {node_ids[name]} -. {_label(relationship)} .-> {target_id}"
            )

    source = "\n".join(lines) + "\n"
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(source, encoding="utf-8")
    return source
