# BiB DSL Specification v2.0

**BiB (Box-in-Box)** is a language-agnostic, YAML-based domain-specific language (DSL) for modeling hierarchical structures (e.g., capability maps, organization models, architecture views) and their inter-relationships. This specification defines the syntax, semantics, and rendering logic needed to implement a full-featured BiB-compatible engine in any language.

---

## 1. Overview

BiB DSL enables:

* Hierarchical modeling (nested boxes, trees, parent-child)
* Tagging and semantic metadata
* Explicit dependency and relationship definitions
* Separation of content from visual styling
* Rule-based dynamic theming and multi-view rendering
* Extensible modeling constructs for advanced use cases

---

## 2. Core Concepts

### 2.1 Node

Each node represents a named entity within a hierarchy.

```yaml
<node_name>:
  - level: <integer>            # Required. 0 for root, increasing with depth
  - parent: <node_name>         # Optional. Required for level > 0
  - common_name: <string>       # Optional. Friendly display name
  - tags:                       # Optional. Key-value metadata
      - name: <tag_name>
        value: <tag_value>
  - depends: <node_name|list>   # Optional. Cross-node relationships
  - type: <string>              # Optional. Classification (e.g. business, tech, app)
  - description: <string>       # Optional. Tooltip or long-form text
  - weight: <float>             # Optional. Relative importance for sizing
```

### 2.2 Hierarchy

* Nodes are organized by `level` and `parent`.
* Level 0 is considered the top-level/root.
* Child nodes must reference their parent's name.

### 2.3 Tags

Tags are user-defined key-value pairs used for metadata, filtering, and styling.

### 2.4 Dependencies

Dependencies define non-hierarchical links between nodes (e.g., relies\_on, supports).

```yaml
node_a:
  - depends: node_b
```

Dependencies can also be named for semantic modeling:

```yaml
node_a:
  - depends:
      - node: node_b
        type: supports
      - node: node_c
        type: blocks
```

---

## 3. Structure File (bib.yaml)

A complete, non-visual representation of the graph.

```yaml
cloud:
  - level: 0
  - type: domain

foundations:
  - level: 1
  - parent: cloud
  - type: capability

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

---

## 4. Styling File (bib.style.yaml)

Defines how nodes should be visually rendered based on rules.

```yaml
styles:
  defaults:
    fill: "#f8f8f8"
    border: "1px solid #ccc"
    font_size: "12px"
    shape: "rectangle"

  rules:
    - match: name == "cloud"
      fill: "#cce5ff"
      font_weight: "bold"

    - match: level == 1
      fill: "#d9f2e6"

    - match: tags[status] == "active"
      fill: "#ffcccc"
      border: "2px solid #e60000"

    - match: type == "capability"
      shape: "rounded"
```

### 4.1 Match Rules

Match can evaluate:

* `name`, `parent`, `level`, `type`
* `tags[<key>]`
* Boolean logic: `and`, `or`, `not`

---

## 5. Short Syntax

For rapid prototyping and visualization:

```yaml
cloud
  foundations
    accounts
  security
    mfa
    pki
```

This format infers:

* Level from indentation
* Parent from nesting
* No metadata or relationships

---

## 6. Rendering Specification

A compliant rendering engine must:

* Parse `bib.yaml` into an in-memory graph
* Parse `bib.style.yaml` and apply rules
* Respect hierarchy and layout nesting
* Render as:

  * Nested boxes (SVG, HTML, Canvas)
  * Directed graphs with relationships
  * Exportable formats (PDF, PNG, Mermaid)

Optional features:

* Zoom/pan
* Tooltips and labels from `common_name` / `description`
* Highlighting via `tags` or view filters

---

## 7. Extensibility and View Control

Support extensions like:

* `view: <string>` — group nodes into multiple views
* `visible: true/false` — show/hide by filter
* `group: <name>` — semantic grouping within layout

Future DSL keywords:

* `computed_tags:` — runtime evaluated tags
* `annotations:` — user notes or change history
* `links:` — external documentation/URLs

---

## 8. JSON Schema (Optional for Tooling)

To validate structure programmatically, a JSON Schema can be defined for both:

* `bib.yaml`
* `bib.style.yaml`

---

## 9. Implementation Notes

Language-agnostic implementations may use:

* YAML parser (e.g., PyYAML, js-yaml)
* Graph engines (e.g., D3.js, Graphviz, Mermaid, HTML DOM)
* Rule engines for matching style rules

Support libraries:

* Frontend: React, D3, SVG.js
* Backend: Python, Node.js, Go

---

## 10. License & Attribution

BiB DSL was originally authored by Vedanta Barooah. It is released under the MIT License and intended for open use, extension, and implementation across modeling tools.

---

## Appendix: Example Multi-Level Model

```yaml
business:
  - level: 0
  - type: domain

sales:
  - level: 1
  - parent: business
  - type: capability

crm:
  - level: 2
  - parent: sales
  - depends:
      - node: analytics
        type: supports
  - tags:
      - name: priority
        value: high

analytics:
  - level: 2
  - parent: business
```

---
