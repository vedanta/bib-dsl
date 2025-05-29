# BiB DSL (Box-in-Box)

**BiB (Box-in-Box)** is a YAML-based open modeling language for defining hierarchical structures like capability maps, architecture views, and org charts. This CLI renders BiB models into visual diagrams.

---

## ✨ Features

- ✅ YAML-first modeling
- ✅ Parent-child hierarchy with levels
- ✅ Semantic tags, types, dependencies
- ✅ Graph rendering via Graphviz (SVG, PNG, PDF)
- 🔜 Box-in-Box layout (LeanIX-style) via HTML/SVG

---

## 📦 Project Structure

| Folder        | Purpose                              |
|---------------|---------------------------------------|
| `bibcli/`     | CLI logic, parser, renderers          |
| `examples/`   | Sample YAML models                    |
| `tests/`      | Unit tests                            |
| `spec/`       | DSL specification and documentation   |

---

## 🚀 Getting Started

### Install Dependencies

```bash
conda env create -f environment.yml
conda activate bib-dsl
```

Install Graphviz system binary:

```bash
brew install graphviz        # macOS
# OR
sudo apt-get install graphviz  # Ubuntu
```

---

## 🧪 Usage

Render a BiB model to SVG:

```bash
python3 -m bibcli.main --input examples/retail.yaml --output out/retail --format svg
```

Outputs: `out/retail.svg`

---

## 🧾 BiB YAML Example

```yaml
retail:
  - level: 0
  - common_name: Retail Org

product_mgmt:
  - level: 1
  - parent: retail
  - common_name: Product Management

catalog:
  - level: 2
  - parent: product_mgmt
  - common_name: Catalog Management
```

---

## 📍 Roadmap

- [x] Graphviz output
- [ ] HTML-based box-in-box rendering
- [ ] Mermaid diagram support
- [ ] Validation and schema checks
- [ ] Interactive web viewer

---

## 🔖 License

MIT License © Vedanta Barooah