# Dynamics 365 Finance & Operations — Developer Mastery Syllabus
### From Senior .NET Developer → Seasoned D365 F&O Developer
#### Built on the 80/20 Rule: Master the 20% that delivers 80% of real-world value

---

## How This Syllabus Works

- **CONCEPT** = Theory & understanding (read, watch, absorb)
- **BUILD** = Guided project / mini-build
- **HANDS-ON LAB** = You do it yourself, from scratch
- **⭐ 80/20 CORE** = The critical items — master these FIRST
- **🔶 SECONDARY** = Important but learn after core is solid
- Each phase ends with a **Checkpoint Project** to prove competency

**Estimated Timeline:** 12–16 weeks (2–3 hours/day)

---

## PHASE 0: ENVIRONMENT & MINDSET SETUP (Week 1)
> *Before writing a single line of X++, understand the ecosystem*

### 0.1 ⭐ Understanding D365 F&O Architecture
| Type | Topic |
|------|-------|
| CONCEPT | What is D365 F&O — ERP vs CRM, Finance vs Supply Chain vs Commerce |
| CONCEPT | Cloud-first architecture — Azure-hosted, LCS (Lifecycle Services) |
| CONCEPT | How D365 F&O differs from AX 2012 (legacy mindset shift) |
| CONCEPT | The layering system — Microsoft base → ISV → Customer customizations |
| CONCEPT | Application Object Tree (AOT) — the backbone of D365 development |
| HANDS-ON | Explore a D365 F&O environment — navigate all modules (GL, AP, AR, Inventory, Procurement) |

### 0.2 ⭐ Development Environment Setup
| Type | Topic |
|------|-------|
| CONCEPT | Cloud-hosted dev VMs vs local OneBox VMs vs Unified Dev Experience |
| CONCEPT | Visual Studio 2019/2022 + D365 F&O extension |
| BUILD | Provision a dev environment via LCS (or use a trial/partner environment) |
| HANDS-ON | Connect Visual Studio to D365 F&O, explore AOT, build & deploy your first model |
| HANDS-ON | Navigate LCS — understand environments, deployments, asset library |

### 0.3 ⭐ Functional Foundation (Developer MUST Know)
| Type | Topic |
|------|-------|
| CONCEPT | Chart of Accounts, Ledger, Fiscal Calendars, Legal Entities |
| CONCEPT | Procure-to-Pay cycle (Purchase Orders → Receipts → Invoices → Payments) |
| CONCEPT | Order-to-Cash cycle (Sales Orders → Picking → Packing → Invoicing) |
| CONCEPT | Inventory Management basics (Sites, Warehouses, Items, Item Groups) |
| HANDS-ON | Walk through a full P2P cycle in the UI — create vendor, PO, receive, invoice, pay |
| HANDS-ON | Walk through a full O2C cycle — create customer, SO, pick, pack, invoice |

> **Checkpoint:** You can navigate the D365 F&O UI, understand the ERP domain, and have a working dev environment.

---

## PHASE 1: X++ LANGUAGE MASTERY (Weeks 2–4)
> *X++ is your bread and butter — it's C# with ERP superpowers*

### 1.1 ⭐ X++ Fundamentals (Your .NET Skills Transfer Here)
| Type | Topic |
|------|-------|
| CONCEPT | X++ vs C# — similarities & key differences |
| CONCEPT | Data types — str, int, real, date, container, anytype, guid |
| CONCEPT | Classes, methods, access modifiers, static vs instance |
| CONCEPT | Exception handling — try/catch/finally, throw, infolog |
| CONCEPT | The `Global` class and helper methods |
| BUILD | Create a simple X++ class that calculates tax on an amount |
| HANDS-ON | Write 10 X++ programs covering: loops, conditionals, string manipulation, date math, containers |
| HANDS-ON | Convert 5 of your C# snippets to X++ — feel the difference |

### 1.2 ⭐ X++ Data Access (THE Most Critical Skill)
| Type | Topic |
|------|-------|
| CONCEPT | `select` statements — the X++ way to query data (not LINQ, not SQL) |
| CONCEPT | `while select`, `firstOnly`, `firstFast`, `forUpdate`, `crossCompany` |
| CONCEPT | Table buffers — how X++ binds data to table variables |
| CONCEPT | `insert_recordset`, `update_recordset`, `delete_from` — set-based operations |
| CONCEPT | Query objects — `Query`, `QueryBuildDataSource`, `QueryRun` (dynamic queries) |
| CONCEPT | Joins in X++ — inner, outer, exists, notExists |
| BUILD | Write a class that reads all open Sales Orders for a customer and calculates total value |
| BUILD | Write a batch job that updates a field on all records matching a condition |
| HANDS-ON | 15 X++ select exercises — increasing complexity (filters, joins, aggregations, cross-company) |
| HANDS-ON | Rewrite 5 SQL queries you know into X++ select statements |
| HANDS-ON | Build a Query object dynamically based on user input |

### 1.3 ⭐ X++ OOP & Patterns
| Type | Topic |
|------|-------|
| CONCEPT | Inheritance in X++ — `extends`, `implements` |
| CONCEPT | Abstract classes and interfaces |
| CONCEPT | `SysExtension` framework — the D365 factory pattern (VERY important) |
| CONCEPT | Chain of Command (CoC) — THE way to extend standard code |
| CONCEPT | Event handlers — pre/post event handlers, delegates |
| BUILD | Create a class hierarchy: `PaymentBase` → `PaymentCash`, `PaymentBank`, `PaymentCard` |
| BUILD | Use `SysExtension` to create a pluggable strategy pattern |
| HANDS-ON | Extend a standard D365 class using Chain of Command |
| HANDS-ON | Subscribe to an event handler on a standard table's `insert()` method |

### 1.4 🔶 X++ Advanced
| Type | Topic |
|------|-------|
| CONCEPT | Attributes in X++ — `[SysEntryPointAttribute]`, `[DataContractAttribute]` |
| CONCEPT | `RunBase` framework vs `SysOperation` framework |
| CONCEPT | Best practices & BP rules — naming conventions, performance |
| CONCEPT | X++ compiler warnings and how to fix them |
| HANDS-ON | Build a RunBase job with dialog and validate |

> **Checkpoint Project:** Build a console-style X++ job that reads vendor invoices, groups them by vendor, calculates totals, and outputs a summary to infolog. Use proper OOP, select statements, and error handling.

---

## PHASE 2: DATA MODEL & TABLE FRAMEWORK (Weeks 4–6)
> *Tables are EVERYTHING in D365 — the entire system revolves around them*

### 2.1 ⭐ Table Fundamentals
| Type | Topic |
|------|-------|
| CONCEPT | Table types — Regular, InMemory, TempDB |
| CONCEPT | Fields, field groups, indexes (unique vs non-unique) |
| CONCEPT | EDT (Extended Data Types) — reusable field definitions (like typedef) |
| CONCEPT | Base Enums — system-wide enumerations |
| CONCEPT | Table properties — `TableGroup`, `CacheLookup`, `ClusterIndex`, `PrimaryIndex` |
| CONCEPT | Relations — foreign keys in D365 |
| BUILD | Create a custom table `MyExpenseHeader` with proper EDTs and enums |
| BUILD | Create a child table `MyExpenseLine` with relation to header |
| HANDS-ON | Create 5 tables with proper indexes, relations, field groups, EDTs |

### 2.2 ⭐ Table Methods & Events
| Type | Topic |
|------|-------|
| CONCEPT | `initValue()`, `validateWrite()`, `validateDelete()`, `insert()`, `update()`, `delete()` |
| CONCEPT | `find()` and `exist()` static methods — the D365 pattern |
| CONCEPT | `modifiedField()` — reacting to field changes |
| CONCEPT | Table method overrides vs event handlers |
| BUILD | Add `find()`, `exist()`, `initValue()`, `validateWrite()` to your expense tables |
| HANDS-ON | Override `insert()` to auto-generate a number sequence |
| HANDS-ON | Add `modifiedField()` logic to recalculate line totals |

### 2.3 ⭐ Number Sequences
| Type | Topic |
|------|-------|
| CONCEPT | How number sequences work in D365 F&O |
| CONCEPT | `NumberSeqModule`, `NumberSeqParametersTable`, scope |
| BUILD | Configure a number sequence for your expense header table |
| HANDS-ON | Generate numbers programmatically using `NumberSeq` class |

### 2.4 ⭐ Data Entities & OData
| Type | Topic |
|------|-------|
| CONCEPT | What are Data Entities — the bridge between tables and integrations |
| CONCEPT | Data Entity types — aggregate, composite, standard |
| CONCEPT | Data Entity wizard — mapping tables to entities |
| CONCEPT | OData endpoints — REST API for D365 F&O |
| BUILD | Create a Data Entity for your expense tables |
| HANDS-ON | Expose entity via OData and call it from Postman |
| HANDS-ON | Create a composite data entity (header + lines) |

### 2.5 🔶 Views & Computed Columns
| Type | Topic |
|------|-------|
| CONCEPT | Views in D365 — computed data, query-based |
| CONCEPT | Computed columns and methods on views |
| BUILD | Create a view that shows open expense reports with totals |

> **Checkpoint Project:** Design and build a complete **Expense Management mini-module** — Header table, Lines table, Enums (status, category), Number sequence, Data entity, find/exist methods, validation logic.

---

## PHASE 3: FORMS & UI DEVELOPMENT (Weeks 6–8)
> *Forms are how users interact with your data — D365 has a unique form engine*

### 3.1 ⭐ Form Architecture
| Type | Topic |
|------|-------|
| CONCEPT | Form patterns — Detail Master, Simple List, List Page, Transaction, Workspace |
| CONCEPT | Form data sources — binding tables to forms |
| CONCEPT | Form controls — grids, groups, tabs, action panes, buttons |
| CONCEPT | Mandatory form patterns and sub-patterns (D365 enforces UI consistency) |
| BUILD | Create a Simple List form for your expense categories |
| BUILD | Create a Detail Master form for expense headers with lines grid |
| HANDS-ON | Apply correct form patterns and pass BP validation |

### 3.2 ⭐ Form Logic & Interactivity
| Type | Topic |
|------|-------|
| CONCEPT | Form methods — `init()`, `run()`, `close()`, `canClose()` |
| CONCEPT | Data source methods — `active()`, `init()`, `executeQuery()`, `validateWrite()` |
| CONCEPT | Control methods — `clicked()`, `modified()`, `lookup()` |
| CONCEPT | Form interaction classes — `FormNotifyHandler`, `FormDataUtil` |
| BUILD | Add buttons to change expense status (Draft → Submitted → Approved) |
| BUILD | Add filtering and sorting to your expense list |
| HANDS-ON | Create a custom lookup on a form field |
| HANDS-ON | Enable/disable fields based on status |

### 3.3 ⭐ Menu Items & Navigation
| Type | Topic |
|------|-------|
| CONCEPT | Display, Output, Action menu items |
| CONCEPT | Menus, Menu extensions, Navigation pane |
| CONCEPT | Security — Privileges, Duties, Roles (tie to menu items) |
| BUILD | Create menu items for all your expense forms |
| BUILD | Add your module to the navigation pane |
| HANDS-ON | Set up security: Expense Clerk (view/create), Expense Manager (approve) |

### 3.4 🔶 Workspaces
| Type | Topic |
|------|-------|
| CONCEPT | Workspace pattern — tiles, lists, charts, links |
| CONCEPT | Business intelligence tiles — count tiles, KPI tiles |
| BUILD | Create an "Expense Management Workspace" with pending approvals, my expenses, totals |

> **Checkpoint Project:** Build a fully functional **Expense Management UI** — List page, detail form with header/lines, action pane buttons for status workflow, lookups, validation, menu items, and security roles. A user should be able to create, edit, submit, and approve expenses entirely through the UI.

---

## PHASE 4: BUSINESS LOGIC FRAMEWORK (Weeks 8–10)
> *Where your .NET architecture skills shine — D365 has robust patterns for business logic*

### 4.1 ⭐ SysOperation Framework (Replaces RunBase)
| Type | Topic |
|------|-------|
| CONCEPT | `SysOperation` architecture — Controller, Service, Data Contract, UI Builder |
| CONCEPT | `DataContractAttribute`, `DataMemberAttribute` — parameter classes |
| CONCEPT | `SysOperationServiceController` — orchestrating batch operations |
| CONCEPT | Batch processing — reliable asynchronous execution |
| BUILD | Create a batch job to auto-approve expenses over 7 days old |
| HANDS-ON | Build a report parameter dialog with SysOperation |
| HANDS-ON | Schedule your batch job to run nightly |

### 4.2 ⭐ Chain of Command (CoC) & Extensions
| Type | Topic |
|------|-------|
| CONCEPT | Why CoC replaced overlayering — upgrade-safe customizations |
| CONCEPT | `[ExtensionOf]` attribute — extending classes, tables, forms |
| CONCEPT | `next` keyword — calling the base implementation |
| CONCEPT | Table extensions — adding fields, methods, events to standard tables |
| CONCEPT | Form extensions — adding controls, data sources, logic to standard forms |
| BUILD | Extend the standard `PurchTable` to add a custom approval field |
| BUILD | Extend the Purchase Order form to show your new field |
| HANDS-ON | Use CoC to modify standard posting logic (add validation before PO confirmation) |
| HANDS-ON | Add a custom field to Sales Order header via extension |

### 4.3 ⭐ Event Handlers & Delegates
| Type | Topic |
|------|-------|
| CONCEPT | Pre-event handlers, post-event handlers |
| CONCEPT | Delegates and subscribing to delegates |
| CONCEPT | Form events — `OnInitialized`, `OnPostRun`, `OnClicked` |
| CONCEPT | Table events — `onInserting`, `onInserted`, `onUpdating`, `onValidatingWrite` |
| BUILD | Use event handler to send an alert when a high-value PO is created |
| HANDS-ON | Subscribe to 5 different standard events and add custom logic |

### 4.4 ⭐ Workflow Development
| Type | Topic |
|------|-------|
| CONCEPT | D365 Workflow architecture — types, categories, elements |
| CONCEPT | Workflow document class, `canSubmitToWorkflow()` |
| CONCEPT | Approval elements, task elements, conditional decisions |
| CONCEPT | Event handlers for workflow — started, completed, approved, rejected |
| BUILD | Create a complete Expense Approval Workflow |
| HANDS-ON | Configure workflow with multi-level approval based on amount |

### 4.5 🔶 Business Events & Alerts
| Type | Topic |
|------|-------|
| CONCEPT | Business events framework — trigger events from X++ |
| CONCEPT | Alert rules — user-configurable notifications |
| BUILD | Create a custom business event for expense approval |
| HANDS-ON | Subscribe to business event from Power Automate |

> **Checkpoint Project:** Extend the standard **Purchase Order module** — add a custom compliance check field, extend the PO form with CoC, add validation via event handlers, create a batch job for auto-flagging POs above threshold, and build an approval workflow. All using extensions (ZERO overlayering).

---

## PHASE 5: INTEGRATIONS & DATA MANAGEMENT (Weeks 10–12)
> *D365 never lives alone — it connects to everything*

### 5.1 ⭐ Data Management Framework (DMF/DIXF)
| Type | Topic |
|------|-------|
| CONCEPT | Import/Export architecture — data projects, data entities, staging tables |
| CONCEPT | Recurring integrations — automated data push/pull |
| CONCEPT | Data packages — templates for migration |
| BUILD | Import 1000 vendor records via data entity and DMF |
| BUILD | Set up a recurring export of expense data |
| HANDS-ON | Handle import errors, staging validation, error logs |

### 5.2 ⭐ OData & REST APIs
| Type | Topic |
|------|-------|
| CONCEPT | OData endpoints — CRUD via REST |
| CONCEPT | Authentication — Azure AD, OAuth2, service-to-service auth |
| CONCEPT | Batch requests and changesets |
| BUILD | Build a .NET console app that reads and creates records via OData |
| HANDS-ON | Use Postman to perform CRUD operations on your data entities |
| HANDS-ON | Build a C# integration that syncs data from an external API into D365 |

### 5.3 ⭐ Power Platform Integration
| Type | Topic |
|------|-------|
| CONCEPT | Virtual Entities — D365 F&O data in Dataverse (no copy needed) |
| CONCEPT | Dual-write — real-time sync between F&O and Dataverse |
| CONCEPT | Power Automate flows with D365 F&O connector |
| BUILD | Create a Power App that shows D365 F&O data via Virtual Entities |
| BUILD | Create a Power Automate flow triggered by a D365 business event |
| HANDS-ON | Set up dual-write for a custom entity |

### 5.4 🔶 Electronic Reporting (ER)
| Type | Topic |
|------|-------|
| CONCEPT | ER framework — configurable document formats |
| CONCEPT | ER data model, format, mapping |
| BUILD | Create a simple invoice format using ER |

### 5.5 🔶 Custom Services & SOAP
| Type | Topic |
|------|-------|
| CONCEPT | Custom service classes — expose X++ as web services |
| CONCEPT | Service groups and deployment |
| BUILD | Create a custom web service that returns expense data as JSON |

> **Checkpoint Project:** Build an **end-to-end integration scenario**: External system sends expense data via REST API → D365 processes and creates records → Workflow triggers approval → Business event fires → Power Automate sends Teams notification → Report generated via ER.

---

## PHASE 6: REPORTING & ANALYTICS (Week 12–13)
> *Stakeholders care about reports — this is your visibility*

### 6.1 ⭐ SSRS Reports
| Type | Topic |
|------|-------|
| CONCEPT | SSRS architecture in D365 — RDP classes, data contracts, controller |
| CONCEPT | Report Data Provider (RDP) — X++ class that feeds data to reports |
| CONCEPT | Precision design vs auto design |
| BUILD | Create an Expense Summary Report with RDP class |
| HANDS-ON | Add parameters, grouping, totals to your report |
| HANDS-ON | Deploy and run report from a menu item |

### 6.2 🔶 Power BI Integration
| Type | Topic |
|------|-------|
| CONCEPT | Entity Store — aggregate measurements for analytics |
| CONCEPT | Embedding Power BI in workspaces |
| BUILD | Create a Power BI dashboard for expense analytics |

> **Checkpoint:** You can build parameterized SSRS reports and know how to connect Power BI.

---

## PHASE 7: DEVOPS & DEPLOYMENT (Week 13–14)
> *Production-grade development — the professional workflow*

### 7.1 ⭐ ALM (Application Lifecycle Management)
| Type | Topic |
|------|-------|
| CONCEPT | Models & packages — how code is organized |
| CONCEPT | Build pipelines — compiling X++ in Azure DevOps |
| CONCEPT | Deployable packages — what gets deployed to environments |
| CONCEPT | LCS — environments, code deployment, hotfixes |
| CONCEPT | Version control with Azure DevOps — branching strategy for D365 |
| BUILD | Set up an Azure DevOps project with a D365 repo |
| BUILD | Create a build pipeline that compiles your model |
| HANDS-ON | Deploy a package from dev → UAT → prod via LCS |

### 7.2 ⭐ Testing & Quality
| Type | Topic |
|------|-------|
| CONCEPT | SysTest framework — unit testing in X++ |
| CONCEPT | RSAT (Regression Suite Automation Tool) — automated UI testing |
| CONCEPT | Best practices — code review checklist for D365 |
| BUILD | Write unit tests for your expense validation logic |
| HANDS-ON | Set up RSAT for automated testing of your expense workflow |

### 7.3 ⭐ Performance Optimization
| Type | Topic |
|------|-------|
| CONCEPT | Set-based operations vs row-by-row (THE #1 performance killer) |
| CONCEPT | Indexes — when and how to create them |
| CONCEPT | `QueryRun` optimization — avoid full table scans |
| CONCEPT | Trace parser — finding slow code |
| CONCEPT | Caching — `RecordViewCache`, `EntireTable`, `Found`, `FoundAndEmpty` |
| HANDS-ON | Profile a slow operation with Trace Parser and optimize it |
| HANDS-ON | Convert a row-by-row operation to set-based |

> **Checkpoint:** You can manage code in DevOps, build and deploy packages, write tests, and optimize performance.

---

## PHASE 8: ADVANCED & SPECIALIZATION (Weeks 14–16)
> *Stand out from other D365 developers*

### 8.1 🔶 Warehouse Management (WMS)
| Type | Topic |
|------|-------|
| CONCEPT | Warehouse app, wave processing, work templates |
| CONCEPT | Location directives, mobile device menu items |
| BUILD | Configure basic warehouse receiving and picking |

### 8.2 🔶 Financial Dimensions
| Type | Topic |
|------|-------|
| CONCEPT | Default dimensions, ledger dimensions, dimension sets |
| CONCEPT | `DimensionAttributeValueCombination`, `DimensionStorage` |
| BUILD | Add financial dimension support to your expense module |

### 8.3 🔶 Retail / Commerce
| Type | Topic |
|------|-------|
| CONCEPT | Commerce architecture — CSU, POS, e-commerce |
| CONCEPT | Commerce extensibility model |

### 8.4 🔶 Feature Management & Flighting
| Type | Topic |
|------|-------|
| CONCEPT | Feature management framework — enable/disable features |
| BUILD | Create a feature flag for your custom functionality |

---

## FINAL CAPSTONE PROJECT (Week 16+)

### Build a Complete Custom Module: "Travel & Expense Management"

This should demonstrate ALL skills learned:

| Component | What to Build |
|-----------|---------------|
| **Data Model** | Header, Lines, Categories, Policies tables with proper EDTs, enums, indexes, relations, number sequences |
| **Business Logic** | Validation rules, policy checks, per-diem calculations, mileage rates, currency conversion |
| **Forms & UI** | List page, detail form with header/lines, workspace with tiles and charts, category setup form |
| **Workflow** | Multi-level approval (manager → finance), auto-approve under threshold |
| **Extensions** | Extend standard Vendor table to link to expense vendors, extend GL posting |
| **Integration** | Data entity for import/export, OData endpoint, Power Automate notification flow |
| **Reporting** | SSRS Expense Report with parameters, Power BI dashboard |
| **DevOps** | Full model in Azure DevOps, build pipeline, unit tests |
| **Security** | Employee role, Manager role, Finance role with proper privileges |
| **Performance** | Set-based operations, proper indexing, caching strategy |

---

## DAILY STUDY PLAN (Suggested)

| Time Block | Activity | Duration |
|------------|----------|----------|
| Morning | Theory / Concept Study (docs, videos) | 45 min |
| Afternoon | Hands-On Lab / BUILD | 90 min |
| Evening | Review, Notes, Plan Next Day | 15 min |

## KEY RESOURCES

| Resource | What For |
|----------|----------|
| Microsoft Learn — D365 F&O Developer | Official tutorials & certification path |
| docs.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro | Official dev documentation |
| MB-500 Certification | Target certification for D365 F&O Developer |
| MB-300 Certification | Finance & Operations core functional knowledge |
| Dynamics Community (community.dynamics.com) | Ask questions, learn from others |
| GitHub — Microsoft D365 samples | Real code examples |
| LCS (Lifecycle Services) | Your deployment & management hub |

## CERTIFICATION ROADMAP

```
MB-300 (Core F&O Functional) → MB-500 (F&O Developer) → MB-310 (Finance) or MB-330 (SCM)
         ↑                              ↑
    Start here                    Your primary goal
```

---

## TRACKING YOUR PROGRESS

After each phase, rate yourself:
- ⬜ **Not Started**
- 🟡 **In Progress**
- 🟢 **Confident — Can do independently**
- ⭐ **Mastered — Can teach others**

| Phase | Status | Confidence |
|-------|--------|------------|
| Phase 0: Environment & Mindset | ⬜ | /10 |
| Phase 1: X++ Mastery | ⬜ | /10 |
| Phase 2: Data Model & Tables | ⬜ | /10 |
| Phase 3: Forms & UI | ⬜ | /10 |
| Phase 4: Business Logic | ⬜ | /10 |
| Phase 5: Integrations | ⬜ | /10 |
| Phase 6: Reporting | ⬜ | /10 |
| Phase 7: DevOps | ⬜ | /10 |
| Phase 8: Advanced | ⬜ | /10 |
| Capstone Project | ⬜ | /10 |

---

*Remember: You're not starting from zero. Your .NET skills give you a 40% head start. X++ will feel familiar. Focus on the ERP domain knowledge and D365-specific patterns — that's where your real learning curve is.*
