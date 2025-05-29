from graphviz import Digraph


def render_graphviz(model: dict, output_file: str, output_format: str = "svg"):
    """
    Render the BiB model as a Graphviz diagram.

    Args:
        model (dict): Parsed BiB YAML model
        output_file (str): File path without extension (Graphviz adds it)
        output_format (str): Output format, e.g., 'svg', 'png', 'pdf'
    """
    dot = Digraph(format=output_format)
    dot.attr("node", shape="box", style="filled", fillcolor="lightgrey")

    for node, props in model.items():
        # Extract label (fall back to node name)
        label = next((p.get("common_name") for p in props if "common_name" in p), node)
        dot.node(node, label)

        # Draw parent-child relationship
        parent = next((p.get("parent") for p in props if "parent" in p), None)
        if parent:
            dot.edge(parent, node)

    dot.render(output_file, cleanup=True)
    print(f"Rendered: {output_file}.{output_format}")
