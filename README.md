# BiB DSL (Box-in-Box)

**BiB (Box-in-Box) DSL** is a YAML-based, language-independent specification for modeling hierarchical structures (like capability maps, architecture views, and organizational models) with visual and semantic clarity.

This project defines both the modeling language (`bib.yaml`) and styling system (`bib.style.yaml`) as well as export formats such as `bibDiagram` for visualization.

---

## ✨ Key Features

- ✅ Simple YAML-based syntax for hierarchy, tags, and relationships
- 🎨 Externalized styling via a CSS-like rules engine (`bib.style.yaml`)
- 🔁 Support for dependencies and metadata across nodes
- 🧱 Flexible rendering model (SVG, HTML, Canvas, or export to Mermaid)
- 🔄 Extensible design for views, filtering, annotations, and more

---

## 🗂️ File Structure

| File / Folder        | Purpose                                       |
|----------------------|-----------------------------------------------|
| `bib.yaml`           | Authoritative source model (hierarchy, tags)  |
| `bib.style.yaml`     | Visual styling rules (colors, shapes, etc.)   |
| `spec.md`            | Full formal specification of BiB DSL          |
| `examples/`          | Real-world use cases like capability maps     |
| `render/`            | Optional renderers or format converters       |

---

## 📦 Getting Started

1. Define your hierarchy in `bib.yaml`
2. Optionally create styling rules in `bib.style.yaml`
3. Use a renderer to visualize it (HTML/SVG/PNG/Mermaid)
4. (Optional) Export to `bibDiagram` for Mermaid-compatible visualization

---

## 📘 Specification

The complete syntax and rendering rules are described in `spec.md`.

---

## 📊 Example

### `bib.yaml`

```yaml
retail:
  - level: 0
  - type: domain

product_mgmt:
  - level: 1
  - parent: retail
  - type: capability
```

### `bib.style.yaml`

```yaml
styles:
  rules:
    - match: level == 0
      fill: "#ccddee"
```

---

## 📤 Mermaid Compatibility (`bibDiagram`)

BiB includes a proposed syntax extension for Mermaid:

```mermaid
bibDiagram
retail "Retail" {
  product_mgmt "Product Management"
}
```

---

## 🔖 License

MIT License © Vedanta Barooah  
Designed for open modeling, visualization, and extensibility.
