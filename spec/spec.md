# BiB DSL Specification v2.0

**BiB (Box-in-Box)** is a language-agnostic, YAML-based domain-specific language (DSL) for modeling hierarchical structures such as capability maps, organizational charts, architecture views, and more. This specification defines the core syntax, semantics, and structural logic of BiB DSL. It deliberately excludes presentation or rendering formats, which are considered implementation details.

---

## 1. Overview

BiB DSL enables:

* Hierarchical modeling with explicit levels and parent relationships
* Semantic tagging for metadata and filtering
* Explicit dependency and relationship modeling
* External styling and view logic (out of scope for this spec)
* Support for extensible metadata and typed entities

This specification formalizes the modeling structure. Rendering (e.g., SVG, HTML, Mermaid) is intentionally left to downstream implementations.

---

## 2. Core Concepts

### 2.1 Node

A node is a uniquely named entity in the model.

```yaml
<node_name>:
  - level: <integer>            # Required. 0 for root, increments by depth
  - parent: <node_name>         # Optional. Required for level > 0
  - common_name: <string>       # Optional. Display label
  - tags:                       # Optional. Key-value metadata pairs
      - name: <tag_name>
        value: <tag_value>
  - depends: <node_name|list>   # Optional. Relationships to other nodes
  - type: <string>              # Optional. Domain-specific type or class
  - description: <string>       # Optional. Human-readable annotation
  - weight: <float>             # Optional. For relative sizing or sorting
```

### 2.2 Hierarchy

* Defined using `level` and `parent` attributes
* Root node has `level: 0`
* Parent must exist and precede the child

### 2.3 Tags

* Tags are arbitrary key-value pairs
* May be used for classification, filtering, or inference

### 2.4 Dependencies

* Defined via `depends` field
* Can be a string or list of dependency objects
* Named relationships supported via `type`

```yaml
node_a:
  - depends:
      - node: node_b
        type: supports
```

---

## 3. Structure File (bib.yaml)

> **Note:** YAML is the authoritative modeling format in BiB DSL. All structural definitions, metadata, and relationships must originate from `bib.yaml` (or its short syntax variant).

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

---

## 4. Short Syntax (Optional)

For quick modeling and prototyping:

```yaml
cloud
  foundations
    accounts
  security
    mfa
    pki
```

This form infers:

* `level` from indentation
* `parent` from nesting
* Metadata must be added later via full syntax

---

## 5. Extensibility

BiB DSL supports future enhancements by allowing the inclusion of new optional fields. These must not alter the semantics of core fields like `level`, `parent`, or `depends`.

Optional constructs include:

* `view: <name>` – logical grouping for rendering or filtering
* `group: <name>` – semantic subgroup classification
* `computed_tags:` – tags generated at runtime or evaluation
* `links:` – external documentation or integration references
* `annotations:` – user comments or version notes

---

## 6. Validation Rules

Implementations may enforce the following:

* Node names must be unique
* Level 0 nodes cannot have a parent
* Parent must exist and precede a child
* Dependencies must reference existing nodes
* Tags must be a list of name/value pairs

---

## 7. Implementation Guidelines (Non-normative)

Although rendering is out of scope, implementers may:

* Parse YAML into a typed AST or graph
* Validate against a JSON schema
* Create adapters for rendering engines (HTML, SVG, JSON)
* Support live editing environments or notebooks

Implementations may optionally generate:

* Visual diagrams (e.g., box-in-box, graph)
* Reports, audits, and change tracking
* Exporters (to Graphviz, Mermaid, etc.)

---

## 8. License & Attribution

BiB DSL was authored by Vedanta Barooah and is released under the MIT License. It is intended for open use, standardization, and collaborative development.

---

## Appendix: Example Model (Retail Capability Map)

```yaml
retail:
  - level: 0
  - type: domain
  - common_name: Retail Organization

product_mgmt:
  - level: 1
  - parent: retail
  - type: capability
  - common_name: Product Management

catalog:
  - level: 2
  - parent: product_mgmt
  - type: sub-capability
  - common_name: Catalog Management

inventory:
  - level: 2
  - parent: product_mgmt
  - type: sub-capability
  - common_name: Inventory Management

sales:
  - level: 1
  - parent: retail
  - type: capability
  - common_name: Sales & Marketing

seo:
  - level: 2
  - parent: sales
  - type: sub-capability
  - common_name: SEO and SEM

campaigns:
  - level: 2
  - parent: sales
  - type: sub-capability
  - common_name: Campaign Management

customer:
  - level: 1
  - parent: retail
  - type: capability
  - common_name: Customer Experience

support:
  - level: 2
  - parent: customer
  - type: sub-capability
  - common_name: Customer Support

recommend:
  - level: 2
  - parent: customer
  - type: sub-capability
  - common_name: Product Recommendations

recommend:
  - depends:
      - node: catalog
        type: consumes
      - node: campaigns
        type: influenced_by
```

---
