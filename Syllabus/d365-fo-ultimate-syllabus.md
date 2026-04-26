# ═══════════════════════════════════════════════════════════════
# DYNAMICS 365 FINANCE & OPERATIONS — COMPLETE DEVELOPER SYLLABUS
# Sequential Hierarchical Tree | Beginner → Advanced
# Every Concept Has a Lab | 80/20 Rule Applied
# ═══════════════════════════════════════════════════════════════

> **WHO THIS IS FOR:** Senior .NET developer, completely new to D365 F&O & ERP
> **END GOAL:** Seasoned D365 F&O Developer / Consultant
> **METHOD:** Theory → Understand → Lab → Build → Prove (at every node)
> **TIMELINE:** 20–24 weeks (2–3 hrs/day)
> **CERTIFICATION TARGET:** MB-500 (Developer) + MB-300 (Core)

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 1: ABSOLUTE FOUNDATION (Weeks 1–3)       │
# │  "Understand the WORLD before you write code"    │
# └─────────────────────────────────────────────────┘

## 1. WHAT IS ERP — THE BIG PICTURE

### 1.1 Understanding Enterprise Software
#### 1.1.1 What is ERP (Enterprise Resource Planning)
- What problem does ERP solve — manual spreadsheets vs integrated system
- History of ERP — MRP → MRP II → ERP → Cloud ERP
- How ERP connects departments — Finance ↔ Procurement ↔ Inventory ↔ Sales ↔ Manufacturing ↔ HR
- 🔬 **LAB:** Draw a diagram: company without ERP (silos) vs company with ERP (integrated)

#### 1.1.2 ERP vs CRM — Know the Difference
- ERP = back-office (money, goods, manufacturing)
- CRM = front-office (leads, sales pipeline, customer service)
- Where they overlap (customer data, orders)
- 🔬 **LAB:** List 20 business processes → classify each as ERP or CRM

#### 1.1.3 Core ERP Modules Overview
- **General Ledger (GL)** — the financial backbone (all money flows here)
- **Accounts Payable (AP)** — money you OWE (vendors/suppliers)
- **Accounts Receivable (AR)** — money OWED TO YOU (customers)
- **Inventory Management** — tracking physical goods
- **Procurement** — buying goods and services
- **Sales** — selling goods and services
- **Manufacturing** — making goods from raw materials
- **Project Management** — tracking project costs and revenue
- **Human Resources** — employee management and payroll
- 🔬 **LAB:** Take a real company (e.g., a furniture manufacturer) — map their daily operations to each ERP module

#### 1.1.4 Key ERP Concepts You Must Internalize
- **Transaction** — a single business event (invoice, payment, receipt)
- **Posting** — recording a transaction permanently in the books
- **Journal** — a batch of transactions to be posted together
- **Master Data** — long-lived reference data (customers, vendors, items)
- **Transaction Data** — event data (orders, invoices, payments)
- **Setup/Configuration Data** — system settings (tax rates, payment terms)
- **Legal Entity / Company** — a separate legal/financial unit (can have multiple in one system)
- **Fiscal Year / Period** — financial time boundaries
- 🔬 **LAB:** Categorize 30 data examples as Master Data, Transaction Data, or Setup Data

---

### 1.2 Microsoft Dynamics 365 — The Ecosystem
#### 1.2.1 D365 Product Family
- D365 Finance — GL, AP, AR, Budgeting, Fixed Assets
- D365 Supply Chain Management — Inventory, Procurement, Manufacturing, Warehousing
- D365 Commerce — Retail, POS, e-Commerce
- D365 Human Resources — HR, Benefits, Leave
- D365 Project Operations — Project accounting
- D365 Business Central — ERP for small/medium businesses (DIFFERENT product)
- D365 Customer Engagement (CE) — Sales, Service, Marketing (this is CRM)
- **F&O = Finance + Supply Chain + Commerce + HR + Project Ops** (all run on SAME platform)
- 🔬 **LAB:** Create a comparison chart: F&O vs Business Central vs CE — target company size, deployment, technology

#### 1.2.2 D365 F&O Architecture — How It Works
- **Cloud-only** — runs on Microsoft Azure (no on-premise since 2019)
- **Three-tier architecture:**
  ```
  Browser (Client)  →  AOS (Application Object Server)  →  Azure SQL Database
       ↑                        ↑                                ↑
  HTML5 + JS           X++ Business Logic                   Data Storage
  ```
- **Single codebase, multi-company** — one installation serves multiple legal entities
- **Metadata-driven** — everything defined as metadata objects (tables, forms, classes)
- **Application Object Tree (AOT)** — the repository of ALL application objects
- **Model-based development** — code organized into Models and Packages
- **Extension-only model** — NO modifying Microsoft code directly (unlike AX 2012)
- 🔬 **LAB:** Draw the 3-tier architecture diagram with labels. List 5 things at each tier.

#### 1.2.3 D365 F&O vs AX 2012 (Historical Context)
- AX 2012: on-premise, overlayering allowed, MorphX IDE, AOS + SQL Server
- D365 F&O: cloud-only, extensions-only, Visual Studio, Azure-hosted
- Why it matters: many online resources still reference AX 2012 patterns — know the difference
- Key mindset shifts:
  - Overlayering → Extension & Chain of Command
  - MorphX → Visual Studio
  - On-premise deployment → LCS cloud deployment
  - X++ forms → form patterns enforced by system
- 🔬 **LAB:** Read 3 old AX 2012 blog posts — identify what has changed in D365 F&O

#### 1.2.4 Licensing & User Types
- **Operations license** — full access user
- **Activity license** — limited access (approve, time entry)
- **Team Member license** — read-only + basic tasks
- **Device license** — shared device (e.g., warehouse scanner)
- 🔬 **LAB:** For a 200-person manufacturing company, estimate license needs by role

---

### 1.3 Navigating D365 F&O — The User Interface
> *You MUST know the UI before you build the UI*

#### 1.3.1 Global Navigation
- Navigation pane — modules listed on left
- Search bar — global search across entities
- Company picker — switching legal entities (top-right)
- User settings — language, date format, timezone
- Help pane — context-sensitive help
- Notifications — alerts and workflow approvals
- 🔬 **LAB:** Open D365 F&O environment → navigate to every module → note what each module contains

#### 1.3.2 Page Types (You Will Build These)
- **List Page** — browse and search records (e.g., "All customers")
  - Filters, sorting, column chooser
  - Action pane at top
  - Grid showing records
- **Details Page** — view/edit single record (e.g., "Customer details")
  - Header section with key fields
  - FastTabs with grouped fields
  - Related information panels (FactBoxes)
- **Workspace** — role-based dashboard (e.g., "Accounts Payable workspace")
  - Tiles showing counts/KPIs
  - Lists of pending items
  - Charts and graphs
- **Dialog / Wizard** — step-by-step parameter input
- **Setup/Parameters Page** — module configuration
- 🔬 **LAB:** For each page type above, find 3 examples in D365 F&O → screenshot and annotate

#### 1.3.3 Common UI Elements
- **Action Pane** — the toolbar (New, Edit, Delete, Post, etc.)
- **FastTabs** — collapsible sections on detail pages
- **Grid** — table of records (sortable, filterable)
- **FactBox pane** — right-side contextual info
- **Filters** — Quick Filter, Filter Pane, Advanced Filter
- **Personalization** — users can rearrange fields (developer must understand this)
- **Saved Views** — user-saved filter/layout combinations
- 🔬 **LAB:** On the "All Sales Orders" page:
  ```
  □ Use Quick Filter to find orders for a specific customer
  □ Use Filter Pane to filter by status + date range
  □ Add a column to the grid using column chooser
  □ Sort by amount descending
  □ Save a view called "My Open Orders"
  □ Use Action Pane to create a new sales order
  □ Explore every FastTab on the sales order detail
  □ Read the FactBox pane — what contextual info is shown?
  ```

---

### 1.4 Functional Foundation — Finance Module
> *You cannot build an ERP app without understanding WHAT the app does*

#### 1.4.1 General Ledger (GL) — The Financial Backbone
##### 1.4.1.1 Chart of Accounts
- What is a Chart of Accounts — the list of all financial accounts
- Account types: Asset, Liability, Equity, Revenue, Expense
- Main account number structure (e.g., 100000 = Cash, 200000 = AP, 400000 = Revenue)
- Account categories — grouping accounts for reporting
- Shared Chart of Accounts — multiple legal entities sharing same accounts
- 🔬 **LAB:**
  ```
  □ Navigate to GL > Chart of Accounts
  □ Review the existing account structure
  □ Create 5 new main accounts:
    - 110100 — Bank Account (Asset)
    - 210100 — Accounts Payable (Liability)
    - 310100 — Retained Earnings (Equity)
    - 410100 — Product Revenue (Revenue)
    - 510100 — Office Supplies (Expense)
  □ Assign each to the correct account category
  ```

##### 1.4.1.2 Legal Entities & Companies
- What is a Legal Entity — a legally registered organization
- One D365 installation can have MANY legal entities
- DataAreaId — the company identifier in every transaction record
- Shared data vs company-specific data
- Cross-company transactions
- 🔬 **LAB:**
  ```
  □ View existing legal entities (Organization Admin > Organizations > Legal entities)
  □ Note the DataAreaId for each
  □ Switch between companies using the company picker
  □ Observe: same customer table, different data per company
  ```

##### 1.4.1.3 Fiscal Calendar
- Fiscal Year — 12 months (or custom periods)
- Periods — monthly, quarterly, or custom
- Period status: Open, On Hold, Permanently Closed
- Opening period — year-end adjustments
- Closing period — year-end closing entries
- 🔬 **LAB:**
  ```
  □ Navigate to GL > Ledger > Fiscal calendars
  □ Create a new fiscal calendar for the current year
  □ Define 12 monthly periods
  □ Open all periods for the current year
  ```

##### 1.4.1.4 Currency & Exchange Rates
- Accounting currency — the "home" currency for GL
- Reporting currency — secondary currency for multi-currency reporting
- Transaction currency — the currency of a specific transaction
- Exchange rate types — Spot, Budget, etc.
- Exchange rate providers — auto-download rates
- 🔬 **LAB:**
  ```
  □ Navigate to GL > Currencies > Currencies
  □ Verify USD, EUR, GBP exist
  □ Navigate to GL > Currencies > Currency exchange rates
  □ Enter exchange rates: EUR/USD = 1.10, GBP/USD = 1.27
  □ Understand: what happens when you post an invoice in EUR in a USD company?
  ```

##### 1.4.1.5 Journal Entries — The Core Financial Transaction
- What is a journal — a batch of debit/credit entries
- Journal types: General, Allotment, Periodic
- Journal names — templates with default settings
- Journal lines: Account, Debit/Credit, Currency, Dimensions, Description
- Validate → Post — two-step process
- Voucher — the unique ID for a posted journal
- **THE GOLDEN RULE: Total Debits MUST = Total Credits (balanced entry)**
- 🔬 **LAB:**
  ```
  □ Navigate to GL > Journal entries > General journals
  □ Create a new journal using a journal name
  □ Add 2 lines:
    - Line 1: Debit Account 510100 (Office Supplies) — $500
    - Line 2: Credit Account 110100 (Bank) — $500
  □ Validate the journal — should be balanced
  □ Post the journal
  □ Navigate to GL > Inquiries > Voucher transactions
  □ Find your voucher — verify the entry
  □ Run Trial Balance — verify account balances changed
  ```

##### 1.4.1.6 Financial Dimensions — CRITICAL CONCEPT
- What are dimensions — additional classification on transactions
- Standard dimensions: Department, Cost Center, Business Unit
- Custom dimensions: Project, Region, Product Line
- Every transaction can carry dimension values
- Dimensions enable analysis: "How much did the Marketing department spend on travel?"
- Default dimensions — auto-filled from master data
- Ledger dimensions — account + dimension combination
- 🔬 **LAB:**
  ```
  □ Navigate to GL > Chart of Accounts > Dimensions > Financial dimensions
  □ View existing dimensions
  □ Create a new dimension: "Region" with values: North, South, East, West
  □ Post a journal entry WITH dimensions:
    - Debit Office Supplies / Department=Sales / Region=North — $300
    - Credit Bank — $300
  □ Run a dimension-based report to see the breakdown
  ```

---

#### 1.4.2 Accounts Payable — Procure-to-Pay (P2P)
> *The process of BUYING things and PAYING for them*

##### 1.4.2.1 The P2P Process Flow
```
Need identified
    ↓
Purchase Requisition (optional — internal request)
    ↓
Purchase Order (PO) — the contract with vendor
    ↓
PO Confirmation — sent to vendor
    ↓
Product Receipt — goods arrive at warehouse
    ↓
Vendor Invoice — vendor sends bill
    ↓
Invoice Matching — compare Invoice vs PO vs Receipt (3-way match)
    ↓
Invoice Posting — record the liability in GL
    ↓
Payment — send money to vendor
    ↓
Bank Reconciliation — match payment with bank statement
```
- 🔬 **LAB:** Draw this flow on paper. For each step, write: (1) which D365 page you'd use, (2) what tables are affected, (3) what GL entries are created

##### 1.4.2.2 Vendor Master Data
- Vendor account — unique identifier
- Vendor name, address, contact info
- Vendor group — classification (Domestic, International, Intercompany)
- Payment terms — when to pay (Net30, Net60, 2%10Net30)
- Payment method — how to pay (Check, Wire, ACH)
- Tax settings — 1099 reporting, withholding tax
- Bank accounts — for electronic payments
- Default financial dimensions — auto-fill on vendor transactions
- 🔬 **LAB:**
  ```
  □ Navigate to AP > Vendors > All vendors
  □ Create 3 vendors:
    - V-001: "Office Supplies Co" — Domestic, Net30, Check
    - V-002: "Tech Equipment Ltd" — Domestic, Net60, Wire
    - V-003: "European Parts GmbH" — International, Net45, Wire, EUR currency
  □ Set default dimensions for each vendor
  □ Add bank account info for wire payment vendors
  ```

##### 1.4.2.3 Purchase Order Lifecycle
- Create PO → select vendor → add lines (item, qty, price, delivery date)
- PO status: Draft → Confirmed → Received → Invoiced
- PO types: Purchase Order, Blanket Order (agreement), Return Order
- Charges — additional costs on PO (freight, handling)
- 🔬 **LAB:**
  ```
  □ Create a Purchase Order for V-001 with 3 lines:
    - 100x Paper (Item: standard item) — $2.00 each
    - 50x Pens — $1.50 each
    - 10x Binders — $5.00 each
  □ Add a $25 freight charge
  □ Confirm the PO (status → Confirmed)
  □ Print the PO confirmation document
  □ Examine: what happened in GL? (NOTHING yet — PO is a commitment, not a transaction)
  ```

##### 1.4.2.4 Product Receipt (Receiving Goods)
- Product receipt = goods have arrived
- Updates: Inventory ON HAND increases, Accrued purchase liability created
- GL impact: Debit Inventory → Credit Accrual
- 3-way match starts here: Receipt qty recorded
- 🔬 **LAB:**
  ```
  □ On your PO, click Receive > Product receipt
  □ Enter product receipt number (packing slip #)
  □ Post the product receipt
  □ Check: Inventory on-hand increased?
  □ Check: GL entries created? (Inventory Dr / Accrual Cr)
  □ Check: PO status changed to "Received"?
  ```

##### 1.4.2.5 Vendor Invoice & Matching
- Invoice = vendor's bill for goods/services
- 2-way match: Invoice vs PO (qty and price)
- 3-way match: Invoice vs PO vs Receipt (qty, price, and received qty)
- Match discrepancies — price tolerance, quantity tolerance
- Posting an invoice: Debit Expense/Inventory → Credit Accounts Payable
- 🔬 **LAB:**
  ```
  □ Navigate to AP > Invoices > Pending vendor invoices
  □ Match to your PO
  □ Enter invoice number and date
  □ Run matching validation — verify no discrepancies
  □ Post the invoice
  □ Check GL: AP liability now exists
  □ Check: PO status changed to "Invoiced"
  □ Intentionally create a price mismatch — see the warning
  ```

##### 1.4.2.6 Vendor Payment
- Payment proposal — system suggests which invoices to pay
- Payment journal — batch of payments
- Payment methods: Check, Wire/ACH, Credit card
- Settlement — linking payment to specific invoice(s)
- GL impact: Debit Accounts Payable → Credit Bank
- 🔬 **LAB:**
  ```
  □ Navigate to AP > Payments > Vendor payment journal
  □ Create new journal
  □ Use "Payment proposal" to auto-select due invoices
  □ Review proposed payments
  □ Approve and post
  □ Check GL: AP cleared, Bank decreased
  □ Check: Invoice status = Paid
  □ Run AP Aging report — vendor balance should be zero
  ```

---

#### 1.4.3 Accounts Receivable — Order-to-Cash (O2C)
> *The process of SELLING things and COLLECTING payment*

##### 1.4.3.1 The O2C Process Flow
```
Customer inquiry / Quote
    ↓
Sales Quotation (optional)
    ↓
Sales Order (SO) — the contract with customer
    ↓
SO Confirmation — order is committed
    ↓
Picking List — warehouse picks items
    ↓
Packing Slip — items packed and shipped
    ↓
Sales Invoice — bill sent to customer
    ↓
Customer Payment — receive money
    ↓
Settlement — match payment to invoice
```
- 🔬 **LAB:** Walk through the entire O2C cycle in D365 — create a customer, sell items, invoice, receive payment

##### 1.4.3.2 Customer Master Data
- Customer account, name, address, contact
- Customer group — classification
- Payment terms, credit limit, collection letter sequences
- Default dimensions
- 🔬 **LAB:**
  ```
  □ Create 3 customers:
    - C-001: "Acme Corp" — Net30, credit limit $50,000
    - C-002: "Beta Industries" — Net60, credit limit $100,000
    - C-003: "Small Shop LLC" — COD (cash on delivery), credit limit $5,000
  □ Set default dimensions for each
  ```

##### 1.4.3.3 Sales Order Complete Walkthrough
- 🔬 **LAB:**
  ```
  □ Create a Sales Order for C-001 with 3 item lines
  □ Confirm the SO
  □ Post Picking List
  □ Post Packing Slip
  □ Post Sales Invoice
  □ At EACH step, check: What GL entries were created? What inventory changed?
  □ Create Customer Payment Journal
  □ Settle payment against the invoice
  □ Verify: AR balance = 0, Bank increased
  □ Run AR Aging report
  ```

---

#### 1.4.4 Inventory Management Basics
> *Tracking physical goods through the system*

##### 1.4.4.1 Product & Item Setup
- Product vs Released Product — product master vs company-specific
- Product types: Item (physical), Service (non-physical), BOM (assembly)
- Item number — unique identifier
- Item Group — classification for GL posting
- Item Model Group — costing method (FIFO, Standard Cost, Weighted Average)
- 🔬 **LAB:**
  ```
  □ Navigate to Product Information Management > Products
  □ Create 5 products:
    - ITEM-001: "Widget A" — Standard Cost, $10
    - ITEM-002: "Widget B" — FIFO
    - ITEM-003: "Assembly C" — BOM type
    - ITEM-004: "Consulting Service" — Service type
    - ITEM-005: "Raw Material D" — FIFO
  □ Release products to your legal entity
  ```

##### 1.4.4.2 Storage & Tracking Dimensions
- **Site** — a physical location (Factory, Distribution Center)
- **Warehouse** — building within a site
- **Location** — specific spot in warehouse (Aisle-Rack-Shelf)
- **Batch Number** — track production batches (food, pharma)
- **Serial Number** — track individual items (electronics, equipment)
- 🔬 **LAB:**
  ```
  □ Create Site: "Main Campus"
  □ Create 2 Warehouses: "WH-MAIN", "WH-RAW"
  □ Set default site/warehouse on your items
  □ Adjust inventory for ITEM-001: add 100 units to WH-MAIN
  □ View on-hand inventory — verify 100 available
  ```

##### 1.4.4.3 Inventory Transactions & On-Hand
- On-hand = how much you have right now
- Available Physical — physically in warehouse
- Available Ordered — expected from POs
- Reserved Physical — committed to SOs
- Inventory transactions — every movement is tracked
  - Physical update — goods moved
  - Financial update — cost recorded
- 🔬 **LAB:**
  ```
  □ Check on-hand for ITEM-001
  □ Create a PO for 50 more — check "Available Ordered" increased
  □ Create a SO for 30 — check "Reserved" increased
  □ Receive the PO — check "Available Physical" increased
  □ Ship the SO — check "Available Physical" decreased
  □ View inventory transactions — trace every movement
  ```

##### 1.4.4.4 Inventory Journals
- **Movement Journal** — ad-hoc increase/decrease
- **Transfer Journal** — move between warehouses
- **Counting Journal** — physical count reconciliation
- **Adjustment Journal** — cost adjustments
- 🔬 **LAB:**
  ```
  □ Post a Movement Journal: add 200 units of ITEM-002 to WH-MAIN
  □ Post a Transfer Journal: move 50 units from WH-MAIN to WH-RAW
  □ Post a Counting Journal: count shows 148 units (expected 150) — post the difference
  □ Verify on-hand after each journal
  ```

---

### 1.5 Functional Foundation — Tax & Basic Compliance
#### 1.5.1 Sales Tax Configuration
- Sales Tax Groups — which taxes apply to a CUSTOMER/VENDOR
- Item Sales Tax Groups — which taxes apply to an ITEM
- Tax = intersection of Sales Tax Group + Item Sales Tax Group
- Tax codes — individual tax rates (State tax 6%, Federal tax 0%)
- Tax calculation on transactions
- 🔬 **LAB:**
  ```
  □ Create Tax Code: STATE-TAX at 6%
  □ Create Tax Code: CITY-TAX at 1.5%
  □ Create Sales Tax Group: TAXABLE — includes both codes
  □ Create Item Sales Tax Group: ALL-ITEMS — includes both codes
  □ Create a PO — verify tax is calculated (6% + 1.5% = 7.5%)
  □ Create a SO — verify tax is calculated
  □ Create an exempt scenario: Item Sales Tax Group with no codes
  ```

---

> ### ✅ STAGE 1 CHECKPOINT
> **You should now be able to:**
> ```
> ✓ Explain what ERP is and why businesses need it
> ✓ Navigate D365 F&O confidently
> ✓ Execute a complete P2P cycle (PO → Receipt → Invoice → Payment)
> ✓ Execute a complete O2C cycle (SO → Pick → Pack → Invoice → Payment)
> ✓ Manage inventory (receipts, movements, transfers, counting)
> ✓ Understand GL, Chart of Accounts, Journal Entries, Dimensions
> ✓ Configure basic tax
> ✓ Explain D365 F&O architecture at a high level
> ```
> **PROVE IT:** Execute both cycles from scratch with NO guidance. If you can't, repeat Stage 1.

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 2: DEVELOPMENT ENVIRONMENT (Weeks 3–4)   │
# │  "Set up your workshop before you build"         │
# └─────────────────────────────────────────────────┘

## 2. DEVELOPER ENVIRONMENT & TOOLS

### 2.1 Development Environment Types
#### 2.1.1 Cloud-Hosted Environment (CHE)
- Provisioned via LCS on Azure
- Full dev VM: Visual Studio + AOS + SQL + SSRS
- Cost: runs on your Azure subscription
- Start/Stop/Deallocate — manage costs
- 🔬 **LAB:** Provision a CHE via LCS (or use partner/trial environment)

#### 2.1.2 Tier-1 (OneBox) Development VM
- All components on single VM
- Used for: development, unit testing
- NOT for performance testing or UAT
- 🔬 **LAB:** RDP into your dev VM. Explore: where is AOS? SQL? SSRS?

#### 2.1.3 Tier-2+ Environments
- Multi-box: separate AOS, SQL, SSRS
- Used for: UAT, Pre-Production, Performance Testing, Production
- Managed by Microsoft (you can't RDP into prod)
- 🔬 **LAB:** In LCS, view environment topology for Tier-2 vs Tier-1

#### 2.1.4 Unified Development Experience (UDE) — Future
- Docker-based local development
- No full VM needed
- Currently in preview — be aware of it

---

### 2.2 Visual Studio for D365 F&O

#### 2.2.1 D365 Extension in Visual Studio
- Installing the extension (pre-installed on CHE)
- Dynamics 365 menu — Build, Synchronize, Deploy, Flush caches
- Application Explorer — the AOT browser in Visual Studio
- 🔬 **LAB:**
  ```
  □ Open Visual Studio on your dev VM
  □ Find the "Dynamics 365" menu — note every option
  □ Open Application Explorer (View > Application Explorer)
  □ Browse: AOT > Data Dictionary > Tables → find CustTable
  □ Browse: AOT > User Interface > Forms → find SalesTable
  □ Browse: AOT > Classes → find SalesFormLetter
  ```

#### 2.2.2 Application Explorer — Deep Dive
- **Data Dictionary** — Tables, Views, EDTs, Base Enums, Table Collections
- **Classes** — X++ classes
- **User Interface** — Forms, Menus, Menu Items, Tiles
- **Reports** — SSRS Reports
- **Security** — Roles, Duties, Privileges
- **Queries** — Reusable query objects
- **Resources** — Images, files, templates
- **Service Groups** — Web service definitions
- **Data Entities** — Integration layer objects
- **Workflow** — Workflow types, categories, approvals
- 🔬 **LAB:**
  ```
  □ In Application Explorer, navigate to and examine:
    - Table: CustTable — note fields, indexes, relations, methods
    - Table: SalesTable — note the field count, relations to SalesLine
    - Form: CustTableListPage — note data sources, design
    - Class: SalesFormLetter — note inheritance
    - EDT: CustAccount — note properties (string size, label)
    - Base Enum: SalesStatus — note values (None, Backorder, Delivered, Invoiced, Canceled)
  □ For each object, right-click > "Open designer" — explore the metadata
  ```

#### 2.2.3 Models & Packages
- **Package** = the deployment unit (what gets compiled and deployed)
- **Model** = a container for your code, INSIDE a package
- Standard packages: ApplicationSuite, ApplicationPlatform, ApplicationFoundation
- You create YOUR OWN model for custom development
- Model properties:
  - Name, Publisher, Layer, Description
  - Referenced models — declare dependencies
- Naming: `CompanyName_ModuleName` (e.g., `Contoso_ExpenseManagement`)
- 🔬 **LAB:**
  ```
  □ Dynamics 365 > Model management > Create model
  □ Name: "MyTraining"
  □ Publisher: "[Your Name]"
  □ Select referenced models: ApplicationPlatform, ApplicationFoundation, ApplicationSuite
  □ Create a new package for this model
  □ Verify: model appears in Application Explorer filter
  ```

#### 2.2.4 Projects & Solutions
- **Solution** = Visual Studio container for projects
- **Project** = organizes objects you're working on
- Project types: Dynamics 365 > Finance Operations
- Adding objects to a project — drag from AOT or create new
- Build project vs Build model vs Full build
- 🔬 **LAB:**
  ```
  □ File > New > Project > Dynamics 365 > Finance Operations
  □ Name: "MyFirstProject"
  □ Ensure model is set to "MyTraining"
  □ Right-click project > Properties — review settings
  □ Set "Synchronize database on build" = True (for now)
  ```

#### 2.2.5 Labels — Multi-Language Support
- Every user-facing string MUST use a label (not hardcoded text)
- Label files — `.label` resource files
- Label syntax: `@MyLabel:MyText`
- Label search — `Dynamics 365 > Label search`
- Why: D365 is used globally — labels enable translation
- 🔬 **LAB:**
  ```
  □ Create a label file: MyTraining_en-us
  □ Add 10 labels:
    - @MyTraining:ExpenseId → "Expense ID"
    - @MyTraining:ExpenseDescription → "Description"
    - @MyTraining:ExpenseAmount → "Amount"
    - @MyTraining:ExpenseDate → "Date"
    - @MyTraining:ExpenseStatus → "Status"
    - (5 more relevant labels)
  □ Build the label file
  ```

---

### 2.3 Lifecycle Services (LCS)

#### 2.3.1 LCS Overview
- LCS = lifecycle management portal for D365 F&O
- URL: lcs.dynamics.com
- 🔬 **LAB:** Log into LCS → explore the dashboard

#### 2.3.2 LCS Project
- Implementation project — for real deployments
- Trial / partner projects — for learning
- Project dashboard — overview of everything
- 🔬 **LAB:** Create or join an LCS project

#### 2.3.3 Environment Management in LCS
- View all environments
- Start / Stop / Deallocate dev environments
- Database movement API — copy prod to sandbox
- Environment history — track deployments
- 🔬 **LAB:**
  ```
  □ Navigate to your project > Environments
  □ View your dev environment details
  □ Stop the environment (save costs)
  □ Start the environment
  □ Note the environment URL for browser access
  ```

#### 2.3.4 Asset Library
- Storing deployable packages
- Storing data packages
- Storing process recordings (RSAT)
- Uploading licenses
- 🔬 **LAB:** Upload a dummy file to Asset Library → understand the categories

#### 2.3.5 Issue Search
- Search for known Microsoft bugs/issues
- KB articles and hotfixes
- 🔬 **LAB:** Search for a common error message you've encountered

---

### 2.4 Your First X++ Code

#### 2.4.1 Create a Runnable Class (X++ Job)
- Runnable class = simplest way to execute X++ code
- No UI, no form — just code that runs
- Output goes to Infolog (message window)
- 🔬 **LAB:**
  ```
  □ Right-click project > Add New Item > Runnable Class (Job)
  □ Name: "MyFirstJob"
  □ Write:
      internal final class MyFirstJob
      {
          public static void main(Args _args)
          {
              info("Hello D365 F&O! I am an X++ developer now!");
              info(strFmt("Today is %1", today()));
              info(strFmt("Current user is %1", curUserId()));
              info(strFmt("Current company is %1", curExt()));
          }
      }
  □ Build the project (Ctrl+Shift+B)
  □ Set as startup object (right-click > Set as Startup Object)
  □ Run (Ctrl+F5) — see output in Infolog
  ```

#### 2.4.2 The Build → Sync → Run Cycle
- **Build** — compile X++ to .NET CIL
- **Synchronize** — update database schema (tables, views)
- **Run** — execute the code
- When to sync: after adding/modifying tables, fields, indexes, views
- When build is enough: class, form logic, method changes
- Full build vs incremental build — when to use each
- 🔬 **LAB:**
  ```
  □ Modify your class — add a warning() and error() message
  □ Build (incremental) — observe speed
  □ Run — see info (blue), warning (yellow), error (red) in Infolog
  □ Try: Build > Rebuild model — observe it takes longer (full build)
  □ Try: Dynamics 365 > Synchronize database — observe what it does
  ```

#### 2.4.3 Debugging
- Set breakpoint — click left margin in code editor (red dot)
- Start debugging — F5 (attach debugger)
- Step Over — F10 (execute line, don't go inside methods)
- Step Into — F11 (go inside method calls)
- Step Out — Shift+F11 (exit current method)
- Continue — F5 (run to next breakpoint)
- Watch window — inspect variable values
- Immediate window — evaluate expressions during debug
- Locals window — all local variables
- Call Stack — execution path that led here
- 🔬 **LAB:**
  ```
  □ Add 5 variables to your class:
      str name = "D365 Developer";
      int count = 42;
      real amount = 1234.56;
      date today = today();
      boolean isReady = true;
  □ Set a breakpoint on the first variable
  □ F5 to start debugging
  □ F10 step through each line
  □ Watch window: add all 5 variables — observe values
  □ Immediate window: type "name + " is great"" — see result
  □ Immediate window: type "amount * 2" — see result
  □ Step through to end — observe Infolog messages appear
  ```

---

> ### ✅ STAGE 2 CHECKPOINT
> **You should now be able to:**
> ```
> ✓ Navigate your dev environment (VM, Visual Studio, LCS)
> ✓ Browse the AOT and find any standard object
> ✓ Create a model, project, label file
> ✓ Write and run a basic X++ class
> ✓ Debug X++ code with breakpoints and watch
> ✓ Understand the Build → Sync → Run cycle
> ```
> **PROVE IT:** Create a new X++ class from scratch that outputs your name, today's date, and company — debug it step by step.

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 3: X++ LANGUAGE MASTERY (Weeks 4–7)       │
# │  "Learn to speak the language fluently"           │
# └─────────────────────────────────────────────────┘

## 3. X++ LANGUAGE — COMPLETE REFERENCE

### 3.1 Data Types

#### 3.1.1 Primitive Types — Strings
- `str` — string type
- Declaration: `str name = "John";`
- Concatenation: `str full = firstName + " " + lastName;`
- `strFmt()` — formatted strings: `strFmt("Hello %1, you have %2 items", name, count)`
- `strLen(s)` — length of string
- `subStr(s, start, length)` — substring (1-based!)
- `strFind(s, searchFor, startPos, searchLength)` — find position
- `strReplace(s, old, new)` — replace text (v10.0.38+)
- `strLwr(s)`, `strUpr(s)` — lowercase/uppercase
- `strRTrim(s)`, `strLTrim(s)` — trim whitespace
- `strSplit(s, delimiter)` — not built-in, use `SysString::split()` or loop
- `match(pattern, s)` — regex-like matching
- `like` operator — wildcard matching (`*` = any chars, `?` = single char)
- 🔬 **LAB:**
  ```
  □ Write X++ code for each string function above
  □ Exercise 1: Given "John Michael Smith" — extract first, middle, last name
  □ Exercise 2: Given "Hello World" — reverse the string character by character
  □ Exercise 3: Given a list of 10 names — find those containing "son"
  □ Exercise 4: Format: "Invoice INV-00042 for $1,234.56 due on 12/31/2024"
  □ Exercise 5: Check if email format is valid using basic string operations
  ```

#### 3.1.2 Primitive Types — Numbers
- `int` — 32-bit integer (-2.1B to 2.1B)
- `int64` — 64-bit integer (used for RecId — EVERY table's primary key)
- `real` — decimal number (for amounts, quantities, rates)
- Arithmetic: `+`, `-`, `*`, `/`
- Integer division: `div` → `7 div 2 = 3` (not 3.5)
- Modulo: `mod` → `7 mod 2 = 1`
- `round(value, decimals)` — round to N decimal places
- `decRound(value, decimals)` — banker's rounding
- `trunc(value)` — truncate decimals
- `abs(value)` — absolute value
- `min(a, b)`, `max(a, b)` — minimum/maximum
- `power(base, exp)` — exponentiation
- 🔬 **LAB:**
  ```
  □ Calculate: total price = qty * unitPrice, with 2 decimal rounding
  □ Calculate: tax = amount * taxRate, rounded to 2 decimals
  □ Calculate: discount = original * discountPct / 100
  □ Check if a number is even/odd using mod
  □ Find the largest of 5 numbers without using arrays
  □ Convert real to int (observe truncation vs rounding)
  □ Test: what happens with int overflow? (int x = maxInt() + 1)
  ```

#### 3.1.3 Primitive Types — Dates & Time
- `date` — date only (no time)
  - `today()` — current date
  - `mkDate(day, month, year)` — create a date
  - `dayOfMon(d)`, `mthOfYr(d)`, `year(d)` — extract parts
  - `dayOfWk(d)` — day of week (1=Mon, 7=Sun)
  - `dayOfYr(d)` — day of year (1-366)
  - Date arithmetic: `date + 30` adds 30 days, `date1 - date2` = days between
  - `dateNull()` — empty/null date
  - `maxDate()`, `minDate()` — boundary values
  - `endMth(d)` — last day of month
- `utcdatetime` — date + time + timezone
  - `DateTimeUtil::utcNow()` — current datetime
  - `DateTimeUtil::newDateTime(date, timeOfDay, timezone)` — construct
  - `DateTimeUtil::addDays()`, `addHours()`, `addMinutes()`, `addSeconds()`
  - `DateTimeUtil::date()` — extract date part
  - `DateTimeUtil::time()` — extract time part
  - `DateTimeUtil::applyTimeZoneOffset()` — timezone conversion
  - `DateTimeUtil::getSystemDateTime()` — system time
- `timeOfDay` — seconds since midnight (int, 0-86399)
  - `timeNow()` — current time as seconds
  - `str2Time("14:30:00")` — parse time string
- 🔬 **LAB:**
  ```
  □ Display today's date in format: "Monday, January 15, 2024"
  □ Calculate: how many days until end of current month?
  □ Calculate: what date is 90 business days from today? (skip weekends)
  □ Find: the first Monday of next month
  □ Calculate: age in years given a birthdate
  □ Convert UTC time to Central Time (Iowa timezone!)
  □ Calculate: hours between two utcdatetime values
  □ Build a function: isWeekend(date d) returns boolean
  □ Build a function: addBusinessDays(date d, int days) returns date
  ```

#### 3.1.4 Primitive Types — Boolean & Enum
- `boolean` — `true` / `false`
- `NoYes` enum — used instead of boolean in table fields (0=No, 1=Yes)
- Boolean logic: `&&` (AND), `||` (OR), `!` (NOT)
- Ternary: `result = condition ? trueValue : falseValue;`
- 🔬 **LAB:**
  ```
  □ Write 5 boolean expressions using &&, ||, !
  □ Use ternary to set a discount: amount > 1000 ? 10 : 0
  □ Use NoYes enum: NoYes isActive = NoYes::Yes;
  □ Convert: boolean to NoYes and back
  ```

#### 3.1.5 Container — The Swiss Army Knife
- `container` — ordered collection of mixed types
- Immutable: every operation returns a NEW container
- `conPeek(con, pos)` — read element at position (1-based)
- `conIns(con, pos, value)` — insert at position (returns new container)
- `conDel(con, pos, count)` — delete from position (returns new container)
- `conLen(con)` — number of elements
- `conFind(con, value)` — find position of value (0 if not found)
- `conNull()` — empty container
- Pack/unpack pattern: `[var1, var2, var3] = myContainer;` (destructuring)
- Container in table fields — store structured data in a single field
- **PERFORMANCE WARNING:** Containers are slow for large data — use List/Map instead
- 🔬 **LAB:**
  ```
  □ Create a container with mixed types: ["John", 42, 1234.56, today()]
  □ Read each element with conPeek — note you must know the type
  □ Insert an element at position 2
  □ Delete element at position 3
  □ Find the position of a value
  □ Destructure: [str name, int age, real salary, date hireDate] = myContainer;
  □ Loop through a container using conLen and conPeek
  □ Build a function that packs employee data into a container and unpacks it
  □ Performance test: add 10,000 elements to a container — observe speed
  ```

#### 3.1.6 Collections — List, Set, Map
##### List (Ordered Collection)
- `List list = new List(Types::String);` — typed list
- `list.addEnd(value)` — add to end
- `list.addStart(value)` — add to start
- `list.elements()` — count
- `list.empty()` — is empty?
- `ListEnumerator enum = list.getEnumerator();`
- `while (enum.moveNext()) { info(enum.current()); }`
- 🔬 **LAB:**
  ```
  □ Create a List of 20 city names
  □ Iterate with ListEnumerator — print all
  □ Count elements, check if empty
  □ Create a List of integers — calculate sum and average
  ```

##### Set (Unique Unordered Collection)
- `Set set = new Set(Types::String);`
- `set.add(value)` — add (no duplicates)
- `set.in(value)` — check existence
- `set.elements()` — count
- `SetEnumerator` for iteration
- 🔬 **LAB:**
  ```
  □ Add 30 items to a Set (with some duplicates) — verify uniqueness
  □ Check if a value exists using .in()
  □ Build a function: given a List, return a Set of unique values
  ```

##### Map (Key-Value Pairs)
- `Map map = new Map(Types::String, Types::Real);`
- `map.insert(key, value)` — add/update
- `map.exists(key)` — check if key exists
- `map.lookup(key)` — get value (throws if not found!)
- `map.find(key)` — returns MapEnumerator positioned at key
- `map.elements()` — count
- `MapEnumerator` — iterate key-value pairs
- 🔬 **LAB:**
  ```
  □ Create a Map: ItemId → Price for 10 items
  □ Look up a price by ItemId
  □ Check if an item exists before looking up
  □ Iterate all entries and print key=value
  □ Build a function: given a list of sales, group by item and sum quantities using Map
  □ Build a function: count word frequency in a string using Map
  ```

---

### 3.2 Control Flow & Logic

#### 3.2.1 Conditional Statements
- `if` / `else if` / `else`
- `switch` / `case` / `default` (MUST use `break;`)
- Ternary: `condition ? trueVal : falseVal`
- 🔬 **LAB:**
  ```
  □ Write a grade calculator: score → letter grade (A/B/C/D/F) using if/else
  □ Rewrite using switch/case
  □ Write a tax calculator: different rates for different income brackets
  □ Write a shipping cost calculator: weight-based with zone multiplier
  □ Nested conditions: eligibility checker with 5 criteria
  ```

#### 3.2.2 Loops
- `while (condition) { }` — pre-check loop
- `do { } while (condition);` — post-check loop
- `for (int i = 0; i < n; i++) { }` — counter loop
- `break;` — exit loop immediately
- `continue;` — skip to next iteration
- No `foreach` in X++ (use `while select` for tables, enumerators for collections)
- 🔬 **LAB:**
  ```
  □ Print multiplication table (1-12) using nested for loops
  □ Find all prime numbers up to 1000 using while loop
  □ Build a Fibonacci sequence generator (first 20 numbers)
  □ Use break: find the first item in a list that matches a condition
  □ Use continue: sum all numbers 1-100 except multiples of 7
  □ Convert a C# foreach to X++ ListEnumerator pattern
  ```

#### 3.2.3 Operators — Complete Reference
- Arithmetic: `+`, `-`, `*`, `/`, `div`, `mod`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `&&`, `||`, `!`
- String: `+` (concat), `like` (wildcard), `match` (regex)
- Assignment: `=`, `+=`, `-=`, `*=`, `++`, `--`
- Type: `is` (type check), `as` (safe cast)
- Null: `== null`, `!= null`
- 🔬 **LAB:**
  ```
  □ Write expressions using every operator above
  □ Short-circuit evaluation: demonstrate && and || short-circuiting
  □ Use 'like' operator: "Cont*" matches "Contoso", not "Microsoft"
  □ Use 'is' and 'as': cast a base class to derived class safely
  ```

---

### 3.3 Classes & Object-Oriented Programming

#### 3.3.1 Class Declaration & Methods
- Class syntax: `class MyClass { }`
- Constructor: `public void new() { }` (or `public void new(str _param)`)
- Instance method: `public str getName() { return this.name; }`
- Static method: `public static MyClass construct() { return new MyClass(); }`
- Access modifiers: `public`, `protected`, `private`, `internal`
- `this` — reference to current instance
- `final` — cannot be overridden/extended
- Method parameter modes: by value (default), by reference (no explicit ref keyword in X++)
- Parm pattern: `public str parmName(str _name = name) { name = _name; return name; }`
- 🔬 **LAB:**
  ```
  □ Create class "Employee":
    - Private fields: name, employeeId, salary, hireDate
    - Constructor accepting name and ID
    - Parm methods for each field
    - Method: calculateBonus() — 10% of salary
    - Method: yearsOfService() — years since hireDate
    - Static construct() method
  □ Create a Runnable class that creates 3 employees and displays their info
  ```

#### 3.3.2 Inheritance
- `extends` keyword: `class Manager extends Employee { }`
- Method overriding — same signature in child class
- `super()` — call parent method
- `abstract` classes — cannot be instantiated
- `abstract` methods — must be implemented by child
- Constructor chaining — child `new()` calling parent `new()` via `super()`
- 🔬 **LAB:**
  ```
  □ Create class hierarchy:
    - abstract class Shape
      ├── method: abstract real area()
      ├── method: abstract real perimeter()
      └── method: str describe() → "Shape with area X and perimeter Y"
    - class Circle extends Shape
      ├── field: real radius
      └── implements area() and perimeter()
    - class Rectangle extends Shape
      ├── fields: real width, real height
      └── implements area() and perimeter()
    - class Square extends Rectangle
      └── constructor takes single side length
  □ Create a List of Shapes — calculate total area using polymorphism
  ```

#### 3.3.3 Interfaces
- `interface IMyInterface { str getName(); void process(); }`
- `implements` keyword: `class MyClass implements IMyInterface { }`
- Multiple interfaces: `class MyClass implements IInterfaceA, IInterfaceB { }`
- Interface vs abstract class — interface = contract, abstract = partial implementation
- 🔬 **LAB:**
  ```
  □ Create interface IExportable:
    - str exportToCSV()
    - str exportToJSON()
  □ Implement on Employee class
  □ Implement on a new class "Product"
  □ Write a method that accepts IExportable and exports any object
  □ Create interface IApprovable:
    - boolean approve(str _approverName)
    - boolean reject(str _reason)
    - str getStatus()
  □ Implement on 2 different classes (ExpenseReport, PurchaseRequest)
  ```

#### 3.3.4 Design Patterns in D365
##### Construct Pattern (Factory)
- Static `construct()` method — standard D365 pattern
- Why: encapsulates construction logic
- `public static MyClass construct() { return new MyClass(); }`
- 🔬 **LAB:** Add construct() to all your classes. Use it instead of `new`.

##### Find/Exist Pattern (Data Access)
- `public static MyTable find(MyKey _key, boolean _forUpdate = false)`
- `public static boolean exist(MyKey _key)`
- THE most common pattern in D365 — you'll write this hundreds of times
- 🔬 **LAB:** (You'll implement this on tables in Stage 4)

##### SysExtension Factory Pattern (Pluggable Strategy)
- `SysExtensionAppClassFactory::getClassFromSysAttribute()`
- Attribute-based class resolution — no switch/case
- Adding new types WITHOUT modifying existing code
- 🔬 **LAB:**
  ```
  □ Create:
    - Base abstract class: TaxCalculator with method calculate(real amount) returns real
    - Extensible enum: TaxType (Standard, Reduced, Exempt)
    - Attribute class: TaxTypeAttribute
    - Implementation: StandardTaxCalculator (20%), ReducedTaxCalculator (5%), ExemptTaxCalculator (0%)
    - Each implementation decorated with [TaxTypeAttribute(TaxType::Standard)] etc.
    - Factory: use SysExtension to resolve TaxType → calculator instance
  □ Add a 4th tax type (Luxury = 35%) WITHOUT touching existing code
  ```

---

### 3.4 Exception Handling & Transactions

#### 3.4.1 Try / Catch / Finally
- `try { } catch (Exception::Error) { } finally { }`
- Exception types:
  - `Exception::Info` — informational (rarely caught)
  - `Exception::Warning` — warning
  - `Exception::Error` — business error
  - `Exception::Deadlock` — database deadlock (should retry)
  - `Exception::UpdateConflict` — optimistic concurrency conflict (should retry)
  - `Exception::DuplicateKeyException` — unique index violation
  - `Exception::CLRError` — .NET exception from CLR interop
- `throw error("message")` — throw an error
- Multiple catch blocks — most specific first
- 🔬 **LAB:**
  ```
  □ Write try/catch for each exception type
  □ Build a validator class that collects all errors before throwing
  □ Handle CLRError: call a .NET method that throws, catch and display
  □ Build a retry pattern for Deadlock: try 3 times with delay
  ```

#### 3.4.2 Infolog — Messaging System
- `info("message")` — blue information (user sees it)
- `warning("message")` — yellow warning
- `error("message")` — red error
- `checkFailed("message")` — like error() but returns false (useful in validate methods)
- `Global::info()`, `Global::warning()`, `Global::error()` — same thing, explicit class
- Infolog window — where messages appear in UI
- Clearing infolog: `infolog.clear()`
- 🔬 **LAB:**
  ```
  □ Output 5 info, 3 warning, 2 error messages
  □ Use checkFailed in a validation scenario
  □ Build a method that validates 10 rules and accumulates ALL errors (doesn't stop at first)
  ```

#### 3.4.3 Transactions (ttsBegin / ttsCommit / ttsAbort)
- `ttsBegin` — start a database transaction
- `ttsCommit` — commit the transaction (save all changes)
- `ttsAbort` — rollback the transaction (undo all changes)
- RULES:
  - ttsBegin/ttsCommit must be paired
  - They can NEST (D365 uses a counter: outermost commit saves)
  - If exception occurs between ttsBegin/ttsCommit → auto-rollback
  - `update()`, `insert()`, `delete()` REQUIRE active transaction
- 🔬 **LAB:**
  ```
  □ Write a transaction that inserts 3 records — all succeed
  □ Write a transaction that fails on record 2 — verify record 1 was rolled back
  □ Demonstrate nested transactions (ttsBegin inside ttsBegin)
  □ Try calling update() without ttsBegin — see the error
  □ Build a "bank transfer" function: debit account A, credit account B — atomic
  ```

---

### 3.5 X++ Data Access — SELECT Statements
> *THE single most important X++ skill — you will write these EVERY DAY*

#### 3.5.1 Table Buffers
- Table buffer = a variable that holds ONE record from a table
- Declaration: `CustTable custTable;` (type = table name)
- Buffer IS the record — `custTable.AccountNum` reads the field
- Empty check: `if (custTable)` — true if buffer has a record
- `custTable.RecId` — system-generated unique ID (int64)
- `custTable.DataAreaId` — company identifier
- `custTable.clear()` — empty the buffer
- 🔬 **LAB:**
  ```
  □ Declare buffers for: CustTable, VendTable, SalesTable, PurchTable
  □ Select a record into each buffer
  □ Display key fields from each
  □ Check if buffer has data using if(buffer)
  □ Clear buffer and check again
  ```

#### 3.5.2 Basic Select
- `select custTable;` — selects FIRST record (arbitrary order)
- `select custTable where custTable.AccountNum == "US-001";` — with filter
- `select firstOnly custTable where ...;` — explicit single record (performance)
- `select firstFast custTable where ...;` — skip overhead for read-only
- 🔬 **LAB:**
  ```
  □ Select a customer by AccountNum — display name and group
  □ Select a vendor by VendAccount — display name and currency
  □ Select a sales order by SalesId — display status and amount
  □ Try: select with non-existent key — verify buffer is empty
  □ Compare: with and without firstOnly — understand the difference
  ```

#### 3.5.3 While Select — Iterating Multiple Records
- `while select custTable where custTable.CustGroup == "10" { info(custTable.Name); }`
- This is your "foreach for tables"
- Each iteration loads NEXT matching record into buffer
- 🔬 **LAB:**
  ```
  □ List all customers — display AccountNum and Name
  □ List all vendors — count total
  □ List all sales orders with status = Open
  □ List all items in a specific warehouse
  □ Count records: use int counter inside while select
  ```

#### 3.5.4 Field Lists & Aggregates
- `select count(RecId) from custTable;` → `custTable.RecId` has the count
- `select sum(CreditMax) from custTable;` → sum of credit limits
- `select avg(LineAmount) from salesLine;` → average line amount
- `select minOf(CreatedDateTime) from salesTable;` → earliest order
- `select maxOf(LineAmount) from salesLine;` → largest line
- Field list: `select AccountNum, Name from custTable;` — only fetch needed fields
- 🔬 **LAB:**
  ```
  □ Count total customers
  □ Sum all vendor balances
  □ Find the average sales order amount
  □ Find the earliest and latest sales order dates
  □ Find the highest single line amount across all sales lines
  □ Select only 2 fields (AccountNum, Name) — verify other fields are empty
  ```

#### 3.5.5 Sorting & Grouping
- `select ... order by Name asc;` — sort ascending
- `select ... order by Amount desc;` — sort descending
- `select CustGroup, count(RecId) from custTable group by CustGroup;` — group by
- Combining: group by + sum + order by
- 🔬 **LAB:**
  ```
  □ List customers sorted by Name A-Z
  □ List top 10 sales orders by amount (descending)
  □ Group customers by CustGroup — count per group
  □ Group sales lines by ItemId — sum quantity and amount per item
  □ Group invoices by month — total revenue per month
  ```

#### 3.5.6 Joins
- **Inner Join** — only matching records from both tables
  ```
  while select custTable
      join custTrans
      where custTrans.AccountNum == custTable.AccountNum
  ```
- **Outer Join** — all from left, matching from right (right fields empty if no match)
  ```
  while select custTable
      outer join custTrans
      where custTrans.AccountNum == custTable.AccountNum
  ```
- **Exists Join** — filter left table where match EXISTS (no right fields returned)
  ```
  while select custTable
      exists join custTrans
      where custTrans.AccountNum == custTable.AccountNum
  ```
- **NotExists Join** — filter left table where NO match exists
  ```
  while select custTable
      notexists join custTrans
      where custTrans.AccountNum == custTable.AccountNum
  ```
- **Multi-table joins** — chain 3+ tables
- Performance: exists join > join when you don't need right-table fields
- 🔬 **LAB:**
  ```
  □ Inner join: Customers WITH transactions — show customer name + transaction amount
  □ Outer join: ALL customers with transaction count (0 for those without)
  □ Exists join: Customers who have at least one open order
  □ NotExists join: Customers who have NEVER placed an order
  □ 3-way join: SalesTable → SalesLine → InventTable — show order + item details
  □ 4-way join: PurchTable → PurchLine → InventTable → VendTable
  □ Performance test: exists join vs inner join for "do customers have orders?" — which is faster?
  ```

#### 3.5.7 Insert, Update, Delete
##### Insert
```
MyTable record;
record.clear();
record.Field1 = "value";
record.Field2 = 42;
record.insert();  // requires ttsBegin/ttsCommit
```
- `insert()` triggers: `initValue()`, `validateWrite()`, events
- `doInsert()` — skips business logic (AVOID unless you know why)
- 🔬 **LAB:**
  ```
  □ Insert 10 records into a custom table (you'll create tables in Stage 4)
  □ For now, use a temporary Runnable class that demonstrates the pattern
  ```

##### Update
```
ttsBegin;
select forUpdate myTable where myTable.Key == "X";
myTable.Field1 = "new value";
myTable.update();
ttsCommit;
```
- `forUpdate` — REQUIRED to lock the record
- Without `forUpdate`, `update()` throws an error
- 🔬 **LAB:** (Detailed labs in Stage 4 after creating custom tables)

##### Delete
```
ttsBegin;
select forUpdate myTable where myTable.Key == "X";
myTable.delete();
ttsCommit;
```
- `validateDelete()` — validation before delete
- Delete actions — cascade behavior
- 🔬 **LAB:** (Detailed labs in Stage 4 after creating custom tables)

#### 3.5.8 CrossCompany & ChangeCompany
- `select crossCompany custTable;` — query ALL legal entities
- `changecompany("DAT") { /* code runs in context of company DAT */ }`
- When to use: reporting across companies, data migration
- 🔬 **LAB:**
  ```
  □ Select customers across all companies — display company + customer
  □ Use changecompany to insert a record into a different company
  □ Count customers per company using crossCompany + group by
  ```

---

### 3.6 Query Framework — Dynamic Queries
> *When your query structure isn't known at compile time*

#### 3.6.1 Query Object
- `Query query = new Query();`
- `QueryBuildDataSource qbds = query.addDataSource(tableNum(CustTable));`
- `qbds.addRange(fieldNum(CustTable, CustGroup)).value("10");`
- `QueryRun queryRun = new QueryRun(query);`
- `while (queryRun.next()) { CustTable cust = queryRun.get(tableNum(CustTable)); }`
- 🔬 **LAB:**
  ```
  □ Build a dynamic query on CustTable with 3 ranges
  □ Add a join to CustTrans
  □ Execute and iterate results
  □ Modify query at runtime — change ranges
  ```

#### 3.6.2 QueryBuildRange — Filter Expressions
- Simple: `.value("US-001")` — exact match
- Wildcard: `.value("US-*")` — starts with
- Range: `.value("100..200")` — between
- Not: `.value("!US-001")` — exclude
- Or: `.value("US-001,US-002,US-003")` — multiple values
- `SysQueryRangeUtil` — dynamic ranges:
  - `SysQueryRangeUtil::currentCompany()` — current company
  - `SysQueryRangeUtil::currentUserId()` — current user
  - `SysQueryRangeUtil::day(0)` — today
  - `SysQueryRangeUtil::monthRange(-1, 0)` — last month
  - `SysQueryRangeUtil::dateRange(startDate, endDate)` — date range
- 🔬 **LAB:**
  ```
  □ Build queries using each range expression type above
  □ Use SysQueryRangeUtil for: "all orders created by current user in last 30 days"
  □ Use SysQueryRangeUtil for: "all invoices from current company"
  □ Build a reusable "query builder" that accepts parameters and constructs query dynamically
  ```

#### 3.6.3 QueryBuildDataSource — Joins
- `qbds.addDataSource(tableNum(CustTrans))` — adds join
- `.joinMode(JoinMode::InnerJoin)` — join type
- `.addLink(fieldNum(CustTable, AccountNum), fieldNum(CustTrans, AccountNum))` — join condition
- Join modes: InnerJoin, OuterJoin, ExistsJoin, NoExistsJoin
- 🔬 **LAB:**
  ```
  □ Build a 3-table query dynamically: SalesTable → SalesLine → InventTable
  □ Set join modes
  □ Add ranges on each data source
  □ Sort by SalesTable.CreatedDateTime desc
  □ Execute and display results
  ```

---

> ### ✅ STAGE 3 CHECKPOINT
> **You should now be able to:**
> ```
> ✓ Write X++ fluently — all data types, control flow, collections
> ✓ Build classes with inheritance, interfaces, design patterns
> ✓ Handle exceptions and transactions properly
> ✓ Write select statements with joins, aggregates, grouping, sorting
> ✓ Build dynamic queries with the Query framework
> ✓ Use containers, List, Set, Map appropriately
> ✓ Use the SysExtension factory pattern
> ```
> **PROVE IT:** Write an X++ job that reads ALL sales orders for the last 90 days,
> groups them by customer, calculates totals per customer, stores results in a Map,
> sorts by total descending, and displays the top 10. Use proper exception handling
> and transactions. Time limit: 30 minutes.

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 4: DATA MODEL & TABLE FRAMEWORK (Wk 7–9)  │
# │  "Tables are EVERYTHING in D365"                   │
# └─────────────────────────────────────────────────┘

## 4. BUILDING THE DATA LAYER

### 4.1 Extended Data Types (EDTs)

#### 4.1.1 What is an EDT
- Reusable field type definition — like a typedef
- Defines: data type, size, label, help text, format
- ALL table fields should use EDTs (never raw types)
- EDTs enable: consistent labels, consistent validation, referencing
- EDT inheritance: `CustAccount` extends `CustVendAC` extends `AccountNum`
- 🔬 **LAB:**
  ```
  □ Examine standard EDTs: CustAccount, ItemId, AmountCur, Description, Name, Qty
  □ Note properties: StringSize, Label, HelpText, DisplayLength
  □ Create 10 custom EDTs for your Expense module:
    - MyExpenseId (str 20, label "Expense ID")
    - MyExpenseDescription (str 200, label "Description")  
    - MyExpenseAmount (real, label "Amount")
    - MyExpenseDate (date, label "Expense Date")
    - MyExpenseNotes (str 1000, label "Notes")
    - MyExpenseLineNum (real, label "Line Number")
    - MyExpenseCategoryId (str 20, label "Category ID")
    - MyExpenseCategoryName (str 100, label "Category Name")
    - MyExpenseMaxAmount (real, label "Maximum Amount")
    - MyExpenseReceiptRequired (NoYes, label "Receipt Required")
  □ Build and verify — check in Application Explorer
  ```

#### 4.1.2 EDT Properties Deep Dive
- `StringSize` — max length (string EDTs)
- `Label` — display label (MUST use label reference @MyLabel:xxx)
- `HelpText` — tooltip/help text
- `DisplayLength` — visible width on forms (auto if 0)
- `Alignment` — Left, Right, Center
- `FormHelp` — form to open for lookup
- `ReferenceTable` — table this EDT points to (for auto-lookup)
- `Extends` — inherit from another EDT
- 🔬 **LAB:**
  ```
  □ Create EDT "MyExpenseId" that extends a base EDT
  □ Set ReferenceTable to your expense header table (after creating it)
  □ Verify: when used on a form, does it auto-lookup?
  ```

### 4.2 Base Enums

#### 4.2.1 Creating Enums
- Enum = fixed set of named values
- Each element: Name (code identifier) + Label (display text) + Value (integer)
- `IsExtensible` property — allows others to add values via extension
- 🔬 **LAB:**
  ```
  □ Create Base Enum: MyExpenseStatus
    - Draft (0)
    - Submitted (1)
    - Approved (2)
    - Rejected (3)
    - Cancelled (4)
    - Paid (5)
  □ Create Base Enum: MyExpenseType
    - Travel (0)
    - Meals (1)
    - Accommodation (2)
    - Transportation (3)
    - Office (4)
    - Communication (5)
    - Other (6)
  □ Create Base Enum: MyExpensePaymentMethod
    - Cash (0)
    - CreditCard (1)
    - BankTransfer (2)
    - CompanyCard (3)
  □ Mark MyExpenseType as Extensible = Yes
  □ Write X++ to iterate enum values using DictEnum class
  ```

### 4.3 Tables — Complete Guide

#### 4.3.1 Creating a Table
- Right-click project > Add New Item > Table
- Table properties:
  - `TableGroup`: Group (setup), Main (master), Transaction, WorksheetHeader, WorksheetLine, Miscellaneous
  - `CacheLookup`: None, NotInTTS, Found, FoundAndEmpty, EntireTable
  - `ClusterIndex` — physical sort order
  - `PrimaryIndex` — logical primary key
  - `CreatedBy`, `CreatedDateTime`, `ModifiedBy`, `ModifiedDateTime` — auto tracking (set to Yes)
  - `SaveDataPerCompany` — Yes for company-specific data, No for shared
  - `DeveloperDocumentation` — describe the table's purpose
- 🔬 **LAB:**
  ```
  □ Create table: MyExpenseCategory (Setup/Reference Data)
    Properties: TableGroup=Group, CacheLookup=Found, SaveDataPerCompany=Yes
    Fields:
    - CategoryId (EDT: MyExpenseCategoryId) — key field
    - Name (EDT: MyExpenseCategoryName)
    - MaxAmount (EDT: MyExpenseMaxAmount)
    - ReceiptRequired (EDT: MyExpenseReceiptRequired)
    - ExpenseType (Enum: MyExpenseType)
    - Active (Enum: NoYes)
    Indexes:
    - CategoryIdx — CategoryId (Unique, Primary, Clustered)
    Field Groups:
    - AutoReport: CategoryId, Name, ExpenseType
    - AutoLookup: CategoryId, Name
    - Overview: CategoryId, Name, ExpenseType, MaxAmount, Active
    - Details: CategoryId, Name, ExpenseType, MaxAmount, ReceiptRequired, Active
  □ Build and synchronize — verify table in SQL Server
  ```

#### 4.3.2 Building the Expense Header Table
- 🔬 **LAB:**
  ```
  □ Create table: MyExpenseHeader (Transaction Header)
    Properties: TableGroup=WorksheetHeader, CacheLookup=NotInTTS
    Fields:
    - ExpenseId (EDT: MyExpenseId) — key, auto-numbered
    - Description (EDT: MyExpenseDescription)
    - ExpenseDate (EDT: MyExpenseDate)
    - Status (Enum: MyExpenseStatus)
    - TotalAmount (EDT: MyExpenseAmount)
    - EmployeeId (EDT: HcmPersonnelNumberId or str)
    - EmployeeName (EDT: Name)
    - PaymentMethod (Enum: MyExpensePaymentMethod)
    - Notes (EDT: MyExpenseNotes)
    - SubmittedDate (EDT: TransDate)
    - ApprovedDate (EDT: TransDate)
    - ApprovedBy (EDT: UserId)
    Indexes:
    - ExpenseIdx — ExpenseId (Unique, Primary, Clustered)
    - StatusIdx — Status (non-unique, for filtering)
    - EmployeeDateIdx — EmployeeId, ExpenseDate (non-unique)
    Field Groups:
    - AutoReport: ExpenseId, Description, ExpenseDate, Status, TotalAmount
    - AutoLookup: ExpenseId, Description
    - Overview: ExpenseId, Description, ExpenseDate, EmployeeName, TotalAmount, Status
    - Identification: ExpenseId
    - Details: (all fields)
    Enable: CreatedBy, CreatedDateTime, ModifiedBy, ModifiedDateTime
  □ Build and synchronize
  ```

#### 4.3.3 Building the Expense Line Table
- 🔬 **LAB:**
  ```
  □ Create table: MyExpenseLine (Transaction Lines)
    Properties: TableGroup=WorksheetLine, CacheLookup=NotInTTS
    Fields:
    - HeaderRecId (EDT: RefRecId) — FK to header
    - LineNum (EDT: MyExpenseLineNum)
    - CategoryId (EDT: MyExpenseCategoryId) — FK to category
    - Description (EDT: MyExpenseDescription)
    - Amount (EDT: MyExpenseAmount)
    - ExpenseType (Enum: MyExpenseType)
    - ExpenseDate (EDT: MyExpenseDate)
    - ReceiptAttached (Enum: NoYes)
    - Notes (EDT: MyExpenseNotes)
    Indexes:
    - HeaderLineIdx — HeaderRecId, LineNum (Unique, Primary, Clustered)
    - CategoryIdx — CategoryId (non-unique)
    Relations:
    - MyExpenseHeader: HeaderRecId → MyExpenseHeader.RecId (Cascade delete)
    - MyExpenseCategory: CategoryId → MyExpenseCategory.CategoryId (Restricted)
    Delete Actions:
    - From MyExpenseHeader: Cascade (delete lines when header deleted)
    Field Groups:
    - AutoReport: LineNum, CategoryId, Description, Amount
    - Overview: LineNum, CategoryId, Description, ExpenseType, Amount, ReceiptAttached
  □ Build and synchronize
  □ Verify in SQL: tables exist, indexes created, FK relationships
  ```

#### 4.3.4 Relations — Deep Dive
- Normal relation: FK from child to parent
- Fixed relation: includes a constant (e.g., where TransType == 1)
- Related field fixed: parent table has the constant
- Cascade delete: delete children when parent is deleted
- Restricted delete: prevent parent delete if children exist
- Navigation: form opens related record
- EDT relations vs table relations — prefer table relations
- 🔬 **LAB:**
  ```
  □ Verify your relations work:
    - Navigate from expense line to its header
    - Navigate from expense line to its category
  □ Test cascade delete: delete a header → lines should auto-delete
  □ Test restricted delete: try deleting a category used by a line → should fail
  □ Create a cross-reference: which tables reference MyExpenseCategory?
  ```

### 4.4 Table Methods

#### 4.4.1 find() and exist() — THE D365 Pattern
- 🔬 **LAB:**
  ```
  □ Add to MyExpenseHeader:
    
    public static MyExpenseHeader find(MyExpenseId _expenseId, boolean _forUpdate = false)
    {
        MyExpenseHeader header;
        if (_expenseId)
        {
            header.selectForUpdate(_forUpdate);
            select firstOnly header
                where header.ExpenseId == _expenseId;
        }
        return header;
    }
    
    public static boolean exist(MyExpenseId _expenseId)
    {
        return _expenseId && (select firstOnly RecId from myExpenseHeader
                              where myExpenseHeader.ExpenseId == _expenseId).RecId != 0;
    }
  
  □ Add find() and exist() to MyExpenseCategory and MyExpenseLine
  □ Test: call find() with valid and invalid keys
  □ Test: call exist() — verify true/false
  □ Test: find() with _forUpdate = true — verify lock
  ```

#### 4.4.2 initValue() — Setting Defaults
- Called when a NEW record is initialized (before user fills fields)
- Always call `super()` first
- 🔬 **LAB:**
  ```
  □ Add to MyExpenseHeader:
    public void initValue()
    {
        super();
        this.ExpenseDate = today();
        this.Status = MyExpenseStatus::Draft;
        this.EmployeeId = HcmWorkerHelper::userId2Worker(curUserId());
    }
  
  □ Add to MyExpenseLine:
    public void initValue()
    {
        super();
        this.ExpenseDate = today();
        this.LineNum = MyExpenseLine::nextLineNum(this.HeaderRecId);
    }
  
  □ Create helper: static real nextLineNum(RefRecId _headerRecId)
  □ Test: create records — verify defaults are populated
  ```

#### 4.4.3 validateWrite() — Validation Before Save
- Called before insert() and update()
- Return true to allow, false to block
- Accumulate validations: `ret = ret && condition;`
- 🔬 **LAB:**
  ```
  □ Add to MyExpenseHeader:
    public boolean validateWrite()
    {
        boolean ret = super();
        
        ret = checkFailed(this.Description != "" ? "" : "Description is required") && ret;
        // Wait — that's wrong. The correct pattern is:
        
        if (!this.Description)
        {
            ret = checkFailed("Description is required");
        }
        if (this.TotalAmount < 0)
        {
            ret = checkFailed("Total amount cannot be negative");
        }
        if (this.ExpenseDate > today())
        {
            ret = checkFailed("Expense date cannot be in the future");
        }
        return ret;
    }
  
  □ Add to MyExpenseLine: Amount > 0, CategoryId must exist
  □ Test: try saving invalid records — verify errors shown
  □ Test: try saving valid records — verify success
  □ Verify ALL validations run (not just first failure)
  ```

#### 4.4.4 validateDelete() — Validation Before Delete
- 🔬 **LAB:**
  ```
  □ Add to MyExpenseHeader:
    public boolean validateDelete()
    {
        boolean ret = super();
        if (this.Status == MyExpenseStatus::Approved || this.Status == MyExpenseStatus::Paid)
        {
            ret = checkFailed("Cannot delete approved or paid expenses");
        }
        return ret;
    }
  □ Test: delete a Draft expense → should succeed
  □ Test: delete an Approved expense → should fail with message
  ```

#### 4.4.5 modifiedField() — React to Field Changes
- Called when user changes a field value on a form
- Uses `switch` on `fieldId` parameter
- `fieldNum(TableName, FieldName)` — get field ID
- 🔬 **LAB:**
  ```
  □ Add to MyExpenseLine:
    public void modifiedField(FieldId _fieldId)
    {
        super(_fieldId);
        switch (_fieldId)
        {
            case fieldNum(MyExpenseLine, CategoryId):
                MyExpenseCategory category = MyExpenseCategory::find(this.CategoryId);
                if (category)
                {
                    this.ExpenseType = category.ExpenseType;
                }
                break;
            case fieldNum(MyExpenseLine, Amount):
                // Trigger header total recalculation
                MyExpenseHeader::recalcTotalAmount(this.HeaderRecId);
                break;
        }
    }
  □ Create static method: MyExpenseHeader::recalcTotalAmount(RefRecId _headerRecId)
    - Sum all line amounts
    - Update header TotalAmount
  □ Test: change category → type auto-fills
  □ Test: change amount → header total recalculates
  ```

#### 4.4.6 insert() and update() Overrides
- 🔬 **LAB:**
  ```
  □ Add to MyExpenseHeader insert():
    - Auto-generate ExpenseId (use number sequence OR simple counter for now)
    - Set EmployeeName from EmployeeId lookup
    - Recalculate TotalAmount
  □ Add to MyExpenseLine insert():
    - Auto-assign next LineNum
    - Trigger header TotalAmount recalc
  □ Add to MyExpenseLine update():
    - Trigger header TotalAmount recalc
  □ Add to MyExpenseLine delete():
    - Trigger header TotalAmount recalc
  ```

### 4.5 Number Sequences

#### 4.5.1 Number Sequence Concepts
- What: auto-incrementing business identifiers (EXP-000001, EXP-000002, ...)
- Format segments: Constant ("EXP-") + Alphanumeric (######)
- Scope: Shared, Legal Entity, Operating Unit
- Continuous: no gaps allowed (slower) vs Non-continuous: gaps OK (faster)
- 🔬 **LAB:**
  ```
  □ Navigate to Organization Admin > Number sequences > Number sequences
  □ Examine existing number sequences — note format, scope, status
  ```

#### 4.5.2 Setting Up Number Sequence for Custom Module
- Create `NumberSeqModule` subclass
- Define number sequence references
- Link EDT to number sequence
- 🔬 **LAB:**
  ```
  □ Create class MyExpenseNumSeqModule extends NumberSeqModule
  □ Override loadModule() — define reference for MyExpenseId
  □ Run the number sequence wizard
  □ Configure format: EXP-###### 
  □ Assign to your legal entity
  □ Modify MyExpenseHeader.insert() to use number sequence:
    NumberSeq numSeq = NumberSeq::newGetNum(MyExpenseParameters::numRefExpenseId());
    this.ExpenseId = numSeq.num();
  □ Create 5 expense records — verify sequential numbering
  ```

### 4.6 Data Entities — Basic

#### 4.6.1 What is a Data Entity
- Abstraction over tables — the INTEGRATION layer
- Consumers (Power Platform, DMF, OData) use entities, NOT tables
- Entity maps table fields to a flat/denormalized structure
- Entity handles: validation, defaults, security
- 🔬 **LAB:** Examine standard entity: CustomerV3 — note how it maps to CustTable + DirPartyTable

#### 4.6.2 Creating a Data Entity
- 🔬 **LAB:**
  ```
  □ Create Data Entity: MyExpenseHeaderEntity
    - Primary data source: MyExpenseHeader
    - Public: Yes
    - Data Management Enabled: Yes
    - Entity Category: Document
    - Key: ExpenseId (natural key, not RecId)
    - Map fields: ExpenseId, Description, ExpenseDate, Status, TotalAmount, EmployeeName
    - Computed field: DaysSinceSubmission
  □ Build and synchronize
  □ Verify: entity appears in Data Management workspace
  □ Test: Import 20 expense records via CSV
  □ Test: Export all expenses to CSV
  ```

---

> ### ✅ STAGE 4 CHECKPOINT PROJECT
> **Build "Expense Tracker v1 — Data Layer Complete"**
> ```
> □ 3 tables: Category, Header, Lines — with proper EDTs, enums, indexes, relations
> □ All table methods: find, exist, initValue, validateWrite, validateDelete, modifiedField, insert, update
> □ Number sequence for ExpenseId
> □ Data entity for Header with import/export
> □ X++ test job that:
>   - Creates 5 expense categories
>   - Creates 10 expense headers with 3-5 lines each
>   - Queries by status, groups by category, calculates totals
>   - Tests all validations (positive and negative cases)
>   - Uses proper transactions (ttsBegin/ttsCommit)
> □ ALL labels used (no hardcoded strings)
> □ Zero best practice warnings
> ```

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 5: FORMS & UI (Weeks 9–11)                │
# │  "Build what users see and touch"                 │
# └─────────────────────────────────────────────────┘

## 5. FORM DEVELOPMENT

### 5.1 Form Patterns — THE Rules

#### 5.1.1 Why Patterns Exist
- Microsoft ENFORCES UI consistency — BP fails if pattern is wrong
- Patterns = templates that define required structure
- Every form MUST apply a top-level pattern
- Sub-patterns for sections within the form
- 🔬 **LAB:** Open 5 standard forms → identify which pattern each uses

#### 5.1.2 Pattern Types & When to Use Each
- **Simple List** → setup/reference data with few fields (Categories, Parameters)
- **Simple List and Details** → master data with moderate detail (Vendors, Items)
- **Details Master** → transaction documents with header + lines (PO, SO, Expense)
- **Details Transaction** → optimized data entry (Journals)
- **List Page** → browse/search entry point (All Customers, All Sales Orders)
- **Workspace** → role-based dashboard
- **Dialog / Drop Dialog** → parameter input
- **Table of Contents** → parameter/setup pages (tabbed)
- 🔬 **LAB:**
  ```
  □ For each pattern above, find 2 standard forms that use it
  □ Screenshot each and annotate the structural elements
  □ Decision table: given a requirement, which pattern to use?
  ```

### 5.2 Building Forms — Step by Step

#### 5.2.1 Simple List Form — Category Setup
- 🔬 **LAB:**
  ```
  □ Create form: MyExpenseCategorySetup
  □ Pattern: Simple List
  □ Data Source: MyExpenseCategory (AllowEdit=Yes, AllowCreate=Yes, AllowDelete=Yes)
  □ Design structure:
    - Action Pane
      - New button
      - Delete button
    - Grid (bind to MyExpenseCategory data source)
      - CategoryId
      - Name
      - ExpenseType
      - MaxAmount
      - ReceiptRequired
      - Active
  □ Apply SimpleList pattern
  □ Run BP validation — fix any pattern violations
  □ Build and test — create, edit, delete categories
  ```

#### 5.2.2 List Page — Expense List
- 🔬 **LAB:**
  ```
  □ Create form: MyExpenseListPage
  □ Pattern: List Page
  □ Data Source: MyExpenseHeader
  □ Design structure:
    - Filter Group
      - Quick Filter on ExpenseId and Description
    - Action Pane
      - Action Pane Tab: "Expenses"
        - Button Group: "New"
          - New button
        - Button Group: "Maintain"  
          - Edit button (opens detail form)
          - Delete button
        - Button Group: "Actions"
          - Submit button
    - Grid (bind to overview field group)
      - ExpenseId, Description, ExpenseDate, EmployeeName, TotalAmount, Status
  □ Apply ListPage pattern
  □ Build and test
  □ Filter by status, sort by date, search by description
  ```

#### 5.2.3 Detail Form — Expense Detail (Header + Lines)
- 🔬 **LAB:**
  ```
  □ Create form: MyExpenseDetail
  □ Pattern: Details Master
  □ Data Sources:
    - MyExpenseHeader (primary)
    - MyExpenseLine (child, joined to header via HeaderRecId)
  □ Design structure:
    - Action Pane
      - Tab: "Expense"
        - Group: "Maintain" — Save, Delete
        - Group: "Actions" — Submit, Approve, Reject, Cancel
      - Tab: "View" — Refresh
    - Header Group (top section)
      - ExpenseId (read-only after creation)
      - Description
      - ExpenseDate
      - Status (read-only)
      - EmployeeName (read-only)
      - PaymentMethod
    - Tab (FastTabs):
      - Tab Page: "Lines"
        - Grid (MyExpenseLine data source)
          - LineNum, CategoryId, Description, ExpenseType, Amount, ReceiptAttached
        - Line Details section below grid
          - Notes, ExpenseDate
      - Tab Page: "Totals"
        - TotalAmount (read-only, calculated)
        - Line count (calculated)
      - Tab Page: "Notes"
        - Notes (multi-line text)
      - Tab Page: "History"
        - SubmittedDate, ApprovedDate, ApprovedBy
  □ Apply DetailsMaster pattern + sub-patterns for each section
  □ Build and test extensively:
    - Create new expense
    - Add 5 lines
    - Edit amounts — verify total recalculates
    - Change category — verify type auto-fills
    - Try invalid data — verify validation messages
  ```

### 5.3 Form Logic & Interactivity

#### 5.3.1 Form Methods
- `init()` — setup when form opens
- `run()` — after init, form is visible
- `close()` / `canClose()` — cleanup, unsaved data check
- 🔬 **LAB:**
  ```
  □ Override init() on your detail form:
    - Display info message with expense count
  □ Override canClose():
    - If status is Draft and changes made, ask "Save changes?"
  ```

#### 5.3.2 Data Source Methods
- `init()` — modify query before execution
- `executeQuery()` — run/re-run the query
- `active()` — active record changed (enable/disable controls!)
- `validateWrite()` — form-level validation
- 🔬 **LAB:**
  ```
  □ Override MyExpenseHeader data source active():
    - Enable/disable action buttons based on Status:
      - Draft: Show Submit, hide Approve/Reject
      - Submitted: Show Approve/Reject, hide Submit
      - Approved: Hide all action buttons
    - Make fields read-only when Status != Draft
  □ Override init():
    - Default filter: only show current user's expenses
  □ Override executeQuery():
    - Add runtime filter based on user's role
  ```

#### 5.3.3 Control Methods & Events
- Button `clicked()` — handle button clicks
- Field `modified()` — field value changed
- Field `lookup()` — custom dropdown lookup
- 🔬 **LAB:**
  ```
  □ Submit button clicked():
    - Validate: at least 1 line exists
    - Validate: all lines have amounts > 0
    - Change status to Submitted
    - Set SubmittedDate = today()
    - Refresh form
    - Show success message
  □ Approve button clicked():
    - Change status to Approved
    - Set ApprovedDate, ApprovedBy
    - Refresh form
  □ Reject button clicked():
    - Open a Drop Dialog for rejection reason
    - Change status to Rejected
    - Save reason to Notes
  □ Custom lookup on CategoryId:
    - Show only Active categories
    - Display CategoryId + Name + MaxAmount
  ```

### 5.4 Menu Items & Navigation

#### 5.4.1 Creating Menu Items
- 🔬 **LAB:**
  ```
  □ Create Display Menu Item: MyExpenseListPage → opens list page
  □ Create Display Menu Item: MyExpenseDetail → opens detail form
  □ Create Display Menu Item: MyExpenseCategorySetup → opens setup form
  □ Create Action Menu Item: MyExpenseAutoApprove → runs batch job (later)
  □ Set labels, help text, icons for each
  ```

#### 5.4.2 Building the Module Menu
- 🔬 **LAB:**
  ```
  □ Create Menu: MyExpenseManagement
    - Sub-menu: "Expenses"
      - MyExpenseListPage
      - MyExpenseDetail (open new)
    - Sub-menu: "Setup"
      - MyExpenseCategorySetup
    - Sub-menu: "Reports" (placeholder for now)
  □ Create a Menu Extension to add your module to the main navigation pane
  □ Build and test — navigate through the full module
  ```

### 5.5 Security — Basic

#### 5.5.1 Security Model
- Role → Duty → Privilege → Permission
- 🔬 **LAB:**
  ```
  □ Create Privileges:
    - MyExpenseView — read access to expense tables + list page menu item
    - MyExpenseCreate — create/edit access + detail form menu item
    - MyExpenseApprove — update status + approve button
    - MyExpenseSetup — CRUD on category table + setup form menu item
  □ Create Duties:
    - MyExpenseClerkDuty — includes View + Create
    - MyExpenseManagerDuty — includes View + Create + Approve
    - MyExpenseAdminDuty — includes all + Setup
  □ Create Roles:
    - MyExpenseClerk — assigned Clerk duty
    - MyExpenseManager — assigned Manager duty  
    - MyExpenseAdmin — assigned Admin duty
  □ Test: log in as each role — verify correct access
  ```

---

> ### ✅ STAGE 5 CHECKPOINT PROJECT
> **Build "Expense Tracker v2 — Full UI"**
> ```
> □ Category Setup form (Simple List)
> □ Expense List Page with filters and action pane
> □ Expense Detail form (Header + Lines, Details Master pattern)
> □ All button logic: Submit, Approve, Reject, Cancel
> □ Field interactivity: lookups, auto-fill, enable/disable
> □ Menu and navigation — full module in nav pane
> □ Security — 3 roles with proper access
> □ A user can perform COMPLETE expense lifecycle through UI alone
> □ ALL patterns pass BP validation
> ```

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 6: BUSINESS LOGIC (Weeks 11–14)           │
# │  "Extend the standard, build workflows, automate" │
# └─────────────────────────────────────────────────┘

## 6. EXTENSION MODEL & BUSINESS LOGIC

### 6.1 Chain of Command (CoC)
> *THE way to extend standard D365 code — NO overlayering*

#### 6.1.1 CoC Fundamentals
- What: wrap an existing method — add logic before/after without modifying original
- `[ExtensionOf(classStr(OriginalClass))]` attribute
- `next` keyword — calls the original method (MUST call exactly once)
- 🔬 **LAB:**
  ```
  □ Extend CustTable.validateWrite():
    - Add rule: CreditMax cannot exceed 500,000
  □ Extend CustTable.insert():
    - Log new customer creation with info()
  □ Extend SalesTable.initValue():
    - Set default delivery date to today + 7
  □ Extend PurchLine.validateWrite():
    - Block if quantity exceeds 10,000
  □ 5 more CoC extensions on different standard tables
  ```

#### 6.1.2 CoC on Forms & Data Sources
- 🔬 **LAB:**
  ```
  □ Extend SalesTable form init() — add a custom message
  □ Extend CustTable form data source active() — add custom logic
  □ Extend PurchTable form button clicked() — add pre/post logic
  ```

### 6.2 Event Handlers
#### 6.2.1 Table Events
- `[DataEventHandler(tableStr(CustTable), DataEventType::Inserted)]`
- Events: Inserting, Inserted, Updating, Updated, Deleting, Deleted, ValidatingWrite, etc.
- 🔬 **LAB:**
  ```
  □ Handle CustTable::Inserted — log new customer
  □ Handle PurchTable::ValidatingWrite — add custom check
  □ Handle SalesTable::ModifiedField — react to status change
  □ Handle VendTable::Deleting — prevent delete if custom flag set
  ```

#### 6.2.2 Form Events
- 🔬 **LAB:**
  ```
  □ Handle SalesTable form Initialized event
  □ Handle CustTable form data source SelectionChanged event
  □ Handle button clicked event on a standard form
  ```

#### 6.2.3 Delegates
- Custom extension points YOU create
- 🔬 **LAB:**
  ```
  □ Add a delegate to your expense submission logic:
    delegate void onExpenseSubmitted(MyExpenseHeader _header) {}
  □ Fire the delegate when expense is submitted
  □ Create a subscriber class that sends notification when delegate fires
  □ Add ANOTHER subscriber that logs to audit table — verify both run
  ```

### 6.3 Table & Form Extensions

#### 6.3.1 Table Extensions
- 🔬 **LAB:**
  ```
  □ Create CustTable extension:
    - Add field: MyExpenseVendorLink (str, for linking customer as expense vendor)
    - Add to Overview and AutoReport field groups
  □ Create PurchTable extension:
    - Add field: MyComplianceChecked (NoYes)
    - Add field: MyComplianceNotes (str 500)
  ```

#### 6.3.2 Form Extensions
- 🔬 **LAB:**
  ```
  □ Extend CustTable form:
    - Add your MyExpenseVendorLink field to a FastTab
  □ Extend PurchTable form:
    - Add compliance fields to header
    - Add compliance check button to action pane
  ```

### 6.4 SysOperation Framework
> *The standard pattern for batch-capable operations*

#### 6.4.1 Architecture: Controller → Service → Data Contract
- 🔬 **LAB:**
  ```
  □ Build: "Expense Auto-Approval" batch job
    Data Contract class:
    - parmDaysOld (int, default 7)
    - parmMaxAmount (real, default 500)
    
    Service class:
    - processAutoApproval(DataContract) — find matching expenses, approve them
    - Use SysOperationProgress for progress bar
    - Log results to infolog
    
    Controller class:
    - Caption: "Auto-Approve Expenses"
    - canGoBatch = true
    
  □ Run synchronously — verify results
  □ Schedule as nightly batch job
  □ Monitor batch execution in Batch Job list
  □ Build: "Expense Purge" operation — delete old cancelled expenses
  ```

### 6.5 Workflow Development
#### 6.5.1 Build Complete Expense Approval Workflow
- 🔬 **LAB:**
  ```
  □ Create Query: MyExpenseApprovalQuery
  □ Create Workflow Category: MyExpenseWorkflowCategory
  □ Create Workflow Document class with canSubmitToWorkflow()
  □ Create Workflow Type: MyExpenseApprovalWorkflow
  □ Create Approval Element with event handlers:
    - Started: status → Submitted
    - Approved: status → Approved, set date and approver
    - Rejected: status → Rejected
    - Completed: (final processing)
  □ Enable submit button on expense form
  □ Configure workflow: Manager approval, escalation at 48 hours
  □ Test complete cycle: Submit → Approve → Complete
  □ Test: Submit → Reject → Resubmit → Approve
  □ Test: Delegation
  ```

---

### 6.6 SSRS Reporting

#### 6.6.1 RDP Report — Expense Summary
- 🔬 **LAB:**
  ```
  □ Create Tmp table: MyTmpExpenseSummary
    - EmployeeName, CategoryName, TotalAmount, LineCount, AvgAmount
  □ Create Data Contract: MyExpenseReportContract
    - parmFromDate, parmToDate, parmStatus filter
  □ Create RDP class: MyExpenseReportDP
    - processReport() — populate tmp table with expense data
  □ Create SSRS Report: MyExpenseSummaryReport
    - Precision design: Company header, filter info, grouped by employee
    - Subtotals per employee, grand total
  □ Create Controller and Menu Item
  □ Run from expense module — export to PDF, Excel
  ```

---

> ### ✅ STAGE 6 CHECKPOINT PROJECT
> **Build "Expense Tracker v3 — Enterprise Grade"**
> ```
> □ Everything from v1 + v2 PLUS:
> □ 10+ CoC extensions on standard tables/forms
> □ 5+ Event handlers
> □ Custom delegate with 2 subscribers
> □ Table + form extensions on CustTable and PurchTable
> □ SysOperation batch job: auto-approve old expenses
> □ Complete workflow: submit → approve → complete
> □ SSRS Report: expense summary with parameters
> □ Full security model
> □ Zero BP warnings
> ```

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 7: ADVANCED (Weeks 14–18)                 │
# │  "Production-grade, performant, integrated"       │
# └─────────────────────────────────────────────────┘

## 7. ADVANCED TOPICS

### 7.1 Advanced Data Operations
#### 7.1.1 Set-Based Operations (Performance Critical)
- `insert_recordset` — bulk insert (10-100x faster than loop)
- `update_recordset` — bulk update
- `delete_from` — bulk delete
- 🔬 **LAB:**
  ```
  □ Convert a while-select-update loop to update_recordset — benchmark
  □ Bulk insert 50,000 records — compare loop vs insert_recordset
  □ Bulk delete old records — compare loop vs delete_from
  ```

#### 7.1.2 Temporary Tables
- InMemory vs TempDB — when to use which
- 🔬 **LAB:** Create both types, benchmark with 10,000 records

#### 7.1.3 Caching
- EntireTable, Found, FoundAndEmpty — when to use each
- 🔬 **LAB:** Configure caching on your category table, measure query speed

#### 7.1.4 Performance Optimization
- Trace Parser — find slow operations
- Missing indexes — identify and fix
- N+1 query problem — detect and fix
- 🔬 **LAB:** Profile your expense module → fix top 3 bottlenecks

### 7.2 Advanced Integration
#### 7.2.1 OData REST API
- 🔬 **LAB:** Build a .NET console app that CRUDs expenses via OData

#### 7.2.2 Custom Web Services
- 🔬 **LAB:** Create a custom service: accept expense JSON, create records

#### 7.2.3 Business Events
- 🔬 **LAB:** Create "Expense Approved" business event → trigger Power Automate → Teams notification

#### 7.2.4 Power Platform Integration
- Virtual Entities — D365 data in Dataverse without copying
- Power Automate flows with D365 connector
- Power Apps consuming D365 data
- 🔬 **LAB:** Build a Power App for mobile expense approval using Virtual Entities

### 7.3 DevOps & ALM
#### 7.3.1 Version Control
- 🔬 **LAB:** Set up Azure DevOps repo, check in all expense module code

#### 7.3.2 Build Pipeline
- 🔬 **LAB:** Create automated build pipeline — compile, test, package

#### 7.3.3 Deployment
- 🔬 **LAB:** Deploy package from Dev → UAT via LCS

#### 7.3.4 Testing
- SysTest unit tests
- 🔬 **LAB:** Write 20 unit tests for your expense validation logic

### 7.4 Financial Dimensions
- Add DefaultDimension to expense header
- Dimension control on form
- Dimension merge on posting
- 🔬 **LAB:** Add full dimension support to expense module

### 7.5 Electronic Reporting (ER)
- 🔬 **LAB:** Create ER format: expense claim as formatted PDF, emailed on approval

### 7.6 Workspace Development
- 🔬 **LAB:**
  ```
  □ Build MyExpenseWorkspace:
    - Tile: My Pending Expenses (count)
    - Tile: Awaiting My Approval (count)
    - Tile: This Month's Spend (amount)
    - List: Recent Expenses
    - List: Expenses Needing Approval
    - Chart: Spend by Category (pie chart)
    - Chart: Monthly Trend (bar chart)
    - Links: New Expense, Categories, Reports
  ```

---

> ### ✅ STAGE 7 CHECKPOINT
> **Full Production Module Complete**

---

# ┌─────────────────────────────────────────────────┐
# │  STAGE 8: CERTIFICATION & MASTERY (Weeks 18–20+) │
# │  "Prove it with credentials"                      │
# └─────────────────────────────────────────────────┘

## 8. CERTIFICATION PREPARATION

### 8.1 MB-500: D365 F&O Developer
#### 8.1.1 Exam Domains
- Architecture & Design (5-10%)
- Developer Tools (10-15%)
- AOT Elements (20-25%)
- Code Development & Testing (10-15%)
- Reporting (10-15%)
- Security (5-10%)
- Data Management (10-15%)
- Integrations (5-10%)
- 🔬 **LAB:**
  ```
  □ Complete ALL Microsoft Learn modules for MB-500
  □ Take 3 practice exams — score 80%+
  □ Build a fresh module from scratch in under 4 hours (exam simulation)
  □ Schedule and PASS MB-500
  ```

### 8.2 MB-300: D365 F&O Core
- 🔬 **LAB:**
  ```
  □ Complete Microsoft Learn modules for MB-300
  □ Take practice exams
  □ Schedule and PASS MB-300
  ```

---

# ┌─────────────────────────────────────────────────────────────┐
# │  FINAL CAPSTONE: BUILD A COMPLETE CUSTOM MODULE             │
# │  "Travel & Expense Management System"                       │
# │                                                             │
# │  This proves EVERY skill from Stage 1 to Stage 8            │
# │  Build it. Deploy it. It's your portfolio piece.            │
# └─────────────────────────────────────────────────────────────┘

## CAPSTONE REQUIREMENTS

### Data Model (8 tables):
```
MyTravelExpensePolicy → Policies & spending limits
MyTravelExpenseHeader → Expense reports
MyTravelExpenseLine → Line items  
MyTravelExpenseCategory → Categories
MyTravelMileageRate → Mileage rates (date-effective)
MyTravelPerDiemRate → Per diem rates by location (date-effective)
MyTravelExpenseAudit → Audit trail of all changes
MyTravelExpenseAttachment → Receipt/document attachments
```

### Business Logic:
```
□ Per diem auto-calculation based on travel dates + location
□ Mileage auto-calculation based on miles + vehicle type
□ Policy enforcement: max amounts per category
□ Receipt requirement enforcement
□ Duplicate detection: flag potential duplicate expenses
□ Multi-currency support with exchange rates
```

### Workflow:
```
□ Employee submits → Manager approves → Finance reviews (if > $5000) → Complete
□ Auto-approve expenses under $50
□ Escalation after 48 hours
□ Email notifications at each step
```

### UI:
```
□ Workspace with tiles, lists, charts
□ List page with advanced filters
□ Detail form (header + lines, Details Master pattern)
□ Category and policy setup forms
□ Rate setup forms (date-effective)
```

### Integration:
```
□ Data entities for import/export
□ OData API for external access
□ Custom service for travel booking system integration
□ Business event → Power Automate → Teams notification
□ Power App for mobile approval
```

### Reporting:
```
□ SSRS: Expense claim printout (precision design)
□ SSRS: Monthly expense summary by department
□ ER: Expense report as PDF email attachment
```

### DevOps:
```
□ Azure DevOps repo with proper branching
□ Build pipeline: compile, test, package
□ 20+ unit tests
□ Deployment to UAT environment
```

### Security:
```
□ Employee role — create/view own
□ Manager role — approve team expenses
□ Finance role — view all, override
□ Admin role — setup and configuration
```

---

# PROGRESS TRACKER

| Stage | Topic | Weeks | Status | Confidence |
|-------|-------|-------|--------|------------|
| 1 | ERP & Functional Foundation | 1-3 | ⬜ | /10 |
| 2 | Development Environment | 3-4 | ⬜ | /10 |
| 3 | X++ Language Mastery | 4-7 | ⬜ | /10 |
| 4 | Data Model & Tables | 7-9 | ⬜ | /10 |
| 5 | Forms & UI | 9-11 | ⬜ | /10 |
| 6 | Business Logic & Extensions | 11-14 | ⬜ | /10 |
| 7 | Advanced Topics | 14-18 | ⬜ | /10 |
| 8 | Certification | 18-20 | ⬜ | /10 |
| C | Capstone Project | 20-24 | ⬜ | /10 |

---

# DAILY ROUTINE

| Time | Activity | Duration |
|------|----------|----------|
| Block 1 | Theory — read concept, watch demo | 30 min |
| Block 2 | Hands-On LAB — practice the concept | 60 min |
| Block 3 | Build — apply to your expense module | 45 min |
| Block 4 | Review — notes, questions, plan tomorrow | 15 min |
| **Total** | | **2.5 hrs/day** |

---

# KEY RESOURCES

| Resource | URL / Location |
|----------|---------------|
| Microsoft Learn — MB-500 | learn.microsoft.com |
| D365 F&O Dev Documentation | docs.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro |
| Dynamics Community | community.dynamics.com |
| LCS | lcs.dynamics.com |
| D365 F&O GitHub Samples | github.com/microsoft/Dynamics365-FinOps-Samples |
| X++ Language Reference | learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-language-reference |

---

> **REMEMBER:**
> Stage 1 before Stage 2. Stage 2 before Stage 3. No skipping.
> Every concept has a LAB — do the LAB before moving on.
> If you can't do it without help, you haven't learned it yet.
> Your .NET skills give you a 40% head start on X++.
> The REAL learning curve is the ERP domain knowledge, not the code.
