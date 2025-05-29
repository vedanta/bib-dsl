import click

from bibcli.parser.loader import load_yaml
from bibcli.render.graphviz import render_graphviz


@click.command()
@click.option('--input', '-i', required=True, help='Path to input BiB YAML file')
@click.option('--output', '-o', default='out/diagram', help='Output file path (no extension)')
@click.option('--format', '-f', default='svg', type=click.Choice(['svg', 'png', 'pdf']), help='Output format')
def render(input, output, format):
    """Render a BiB YAML file to a graphic (SVG, PNG, etc)."""
    click.echo(f"📦 Loading model from: {input}")
    model = load_yaml(input)

    click.echo(f"🎨 Rendering as: {format.upper()} → {output}.{format}")
    render_graphviz(model, output_file=output, output_format=format)
