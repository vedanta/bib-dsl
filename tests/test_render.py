from bibcli.render.mermaid import render_mermaid


def test_render_mermaid_preserves_hierarchy_and_dependency_edges():
    model = {
        "retail": [
            {"level": 0},
            {"common_name": "Retail & Co"},
            {"type": "domain"},
        ],
        "catalog": [
            {"level": 1},
            {"parent": "retail"},
            {"common_name": 'Catalog "Core"'},
            {"type": "sub-capability"},
            {
                "depends": [
                    {"node": "inventory", "type": "consumes"},
                    {"node": "pricing", "type": "influenced by"},
                ]
            },
        ],
        "inventory": [{"level": 1}, {"parent": "retail"}],
    }

    source = render_mermaid(model)

    assert source.startswith("flowchart TD\n")
    assert "Retail &amp; Co (domain)" in source
    assert "Catalog &quot;Core&quot; (sub-capability)" in source
    assert "-->" in source
    assert "consumes" in source
    assert "influenced by" in source
    assert "pricing (external)" in source


def test_render_mermaid_writes_source_when_path_is_provided(tmp_path):
    output = tmp_path / "capability-map.mmd"
    source = render_mermaid({"root": [{"common_name": "Root"}]}, str(output))

    assert output.read_text(encoding="utf-8") == source
