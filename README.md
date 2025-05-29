# BiB DSL (Box-in-Box)

**BiB (Box-in-Box) DSL** is a YAML-based, open modeling language designed for defining hierarchical systems such as capability maps, architecture views, and organizational models. It focuses on structure, metadata, and semantic relationships — deliberately excluding rendering and presentation logic.

---

## ✨ Key Features

- ✅ YAML-first: easy to author, version, and diff
- 🔁 Semantic modeling: hierarchy, tags, dependencies
- 🎯 Rendering-agnostic: output handled by external tools
- 🧱 Extensible: add computed fields, annotations, and views

---

## 🗂️ Core Artifacts

| File            | Purpose                                           |
|-----------------|---------------------------------------------------|
| `bib.yaml`      | Canonical model definition (structure + semantics)|
| `spec.md`       | Full specification of BiB DSL                     |
| `examples/`     | Use cases like capability maps, org charts        |

---

## 🧩 Syntax Highlights

### Full Syntax

```yaml
cloud:
  - level: 0
  - type: domain

security:
  - level: 1
  - parent: cloud
  - type: capability

mfa:
  - level: 2
  - parent: security
  - depends:
      - node: foundations
        type: supports
  - tags:
      - name: status
        value: active
```

### Short Syntax (Optional)

```yaml
cloud
  foundations
    accounts
  security
    mfa
    pki
```

---

## 📦 Getting Started

1. Define your model in `bib.yaml`
2. Validate using JSON Schema (optional)
3. Choose or build a renderer to visualize or export
4. Extend with tags, views, and computed metadata

---

## 🚫 Out of Scope

- Rendering formats (SVG, HTML, Mermaid)
- Presentation rules or style definitions
- Visual layout semantics

These are left to downstream tooling, libraries, or frameworks.

---

## 🛠 Implementation Notes

BiB DSL is intended to be parsed and interpreted in any language. Parsers, validators, and exporters can be built in Python, JavaScript, Go, or others.

---

## 🔖 License

MIT License © Vedanta Barooah
Built for open modeling, analysis, and future-proof tooling.
