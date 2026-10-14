import click

from bibcli.parser.loader import load_yaml
from bibcli.render.graphviz import render_graphviz
from bibcli.render.mermaid import render_mermaid


@click.command()
@click.option('--input', '-i', required=True, help='Path to input BiB YAML file')
@click.option('--output', '-o', default=None, help='Output path (defaults to out/diagram.<format>)')
@click.option(
    '--format',
    '-f',
    default='svg',
    type=click.Choice(['svg', 'png', 'pdf', 'mmd']),
    help='Output format: Graphviz image or Mermaid source',
)
def render(input, output, format):
    """Render a BiB YAML model to an image or Mermaid source."""
    click.echo(f"📦 Loading model from: {input}")
    model = load_yaml(input)

    extension = 'mmd' if format == 'mmd' else format
    output = output or f'out/diagram.{extension}'
    click.echo(f"🎨 Rendering as: {format.upper()} → {output}")

    if format == 'mmd':
        render_mermaid(model, output_file=output)
    else:
        output_prefix = output
        if output_prefix.lower().endswith(f'.{format}'):
            output_prefix = output_prefix[: -(len(format) + 1)]
        render_graphviz(model, output_file=output_prefix, output_format=format)
