# Dynamics 365 Finance & Operations — Complete Developer Syllabus
### Basic → Intermediate → Advanced (Sequential Learning Path)
### Category > Sub-Category > Individual Concept — Micro-Detailed Breakdown
#### 80/20 Rule Applied | ⭐ = Core 20% | 🔶 = Secondary

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEVEL 1: BASIC (Weeks 1–6)
# Foundation — Understand the Platform, Language & Data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## MODULE 1: ERP & D365 F&O FUNDAMENTALS
> *Before touching code, understand WHAT you're building and WHY*

### 1.1 ⭐ What is ERP — Big Picture
#### 1.1.1 ERP Core Concepts
- What is ERP (Enterprise Resource Planning) — definition, purpose, history
- Why businesses need ERP — manual processes vs integrated systems
- ERP vs CRM — scope differences (back-office vs front-office)
- Key ERP modules overview — Finance, Supply Chain, Manufacturing, HR, Project
- How data flows across ERP modules — the integration backbone
- ERP implementation lifecycle — Discover → Analyze → Design → Develop → Deploy → Operate

#### 1.1.2 D365 F&O in the Microsoft Ecosystem
- Microsoft Dynamics product family — F&O, Business Central, CE, HR
- D365 F&O vs Business Central — enterprise vs SMB
- D365 F&O vs AX 2012 — what changed (cloud, no overlayering, extensions)
- D365 F&O vs SAP — positioning and architecture differences
- Where D365 F&O sits in Azure — PaaS, Azure SQL, Azure DevOps
- Licensing model — base license, attach license, user types (Full, Activity, Team Member)

#### 1.1.3 D365 F&O Architecture Overview
- Three-tier architecture — Client (browser) → AOS (Application Object Server) → Database
- Cloud-only deployment model — why no on-premise anymore
- Single-instance multi-company — Legal Entities concept
- Kernel vs Application layer — what Microsoft owns vs what you customize
- Model-driven architecture — metadata defines everything
- Update cadence — Microsoft releases (monthly quality, annual feature updates)

**HANDS-ON LAB 1.1:**
```
□ Navigate a D365 F&O environment end-to-end (every module)
□ Identify which module handles: invoice, purchase order, journal, production order
□ Draw the data flow diagram: Quote → Order → Invoice → Payment
□ List 10 real-world business scenarios and map them to D365 modules
```

---

### 1.2 ⭐ Functional Domain Knowledge (Developer MUST Know)
> *You cannot write good code without understanding the business process*

#### 1.2.1 General Ledger (GL) Basics
- What is General Ledger — the financial backbone
- Chart of Accounts — account structure, main accounts, account types (P&L, Balance Sheet)
- Legal Entity vs Company — multi-company setup
- Fiscal Calendar — fiscal years, periods, opening/closing
- Currency & Exchange Rates — accounting currency, reporting currency, transaction currency
- Financial Dimensions — Department, Cost Center, Business Unit (used EVERYWHERE)
- Journal Entry concept — Debit = Credit, balanced entries
- Posting profiles — how transactions hit GL accounts
- Subledger to GL reconciliation
- Trial Balance, Balance Sheet, Income Statement — what they mean

**HANDS-ON LAB 1.2.1:**
```
□ Set up a new Legal Entity from scratch
□ Create a Chart of Accounts with 20 accounts (Assets, Liabilities, Revenue, Expense)
□ Configure a Fiscal Calendar with 12 periods
□ Create and post a General Journal entry (debit/credit)
□ View the Trial Balance and verify your entry
```

#### 1.2.2 Accounts Payable (AP) — Procure-to-Pay
- Vendor master data — vendor groups, payment terms, payment methods
- Purchase Requisition → Purchase Order flow
- PO lifecycle — Draft → Confirmed → Received → Invoiced → Paid
- Product Receipt (Packing Slip) — what it does to inventory and GL
- Vendor Invoice — matching concepts (2-way, 3-way matching)
- Vendor Payment — payment journals, payment proposals, bank reconciliation
- AP aging — tracking what you owe
- Charges (Misc charges) on purchase orders

**HANDS-ON LAB 1.2.2:**
```
□ Create a Vendor with payment terms Net30
□ Create a Purchase Order with 3 lines
□ Confirm the PO
□ Post a Product Receipt
□ Create and post a Vendor Invoice (3-way match)
□ Generate a payment proposal and pay the vendor
□ View the vendor balance and AP aging report
```

#### 1.2.3 Accounts Receivable (AR) — Order-to-Cash
- Customer master data — customer groups, payment terms, credit limits
- Sales Order lifecycle — Draft → Confirmed → Picked → Packed → Invoiced → Paid
- Sales Quotation → Sales Order conversion
- Picking List & Packing Slip — warehouse operations
- Sales Invoice — revenue recognition, tax calculation
- Customer Payment — payment journals, settlement
- AR aging — tracking what customers owe
- Free text invoices — invoicing without sales orders
- Credit notes and returns

**HANDS-ON LAB 1.2.3:**
```
□ Create a Customer with credit limit of $50,000
□ Create a Sales Quotation and convert to Sales Order
□ Confirm the Sales Order
□ Post Picking List, then Packing Slip
□ Post the Sales Invoice
□ Receive customer payment and settle against invoice
□ View customer balance and AR aging
```

#### 1.2.4 Inventory Management Basics
- Item master — Released Products, Product types (Item, Service, BOM)
- Item Model Groups — FIFO, LIFO, Standard Cost, Weighted Average
- Storage Dimensions — Site, Warehouse, Location, Batch, Serial
- Tracking Dimensions — Batch number, Serial number
- On-hand inventory — available physical, available ordered, reserved
- Inventory transactions — physical vs financial updates
- Inventory journals — Movement, Adjustment, Count, Transfer
- Inventory closing — cost calculation process

**HANDS-ON LAB 1.2.4:**
```
□ Create 5 Released Products (mix of items and services)
□ Set up Sites and Warehouses
□ Perform inventory adjustment journal (add stock)
□ Perform inventory movement journal (move between warehouses)
□ View on-hand inventory for your items
□ Understand physical vs financial status on transactions
```

#### 1.2.5 Procurement Basics
- Procurement categories — organizing what you buy
- Vendor selection — approved vendor lists
- Purchase agreements — blanket orders
- Request for Quotation (RFQ) — competitive bidding
- Purchasing policies — approval limits, auto-approval rules

#### 1.2.6 Basic Tax & Compliance
- Sales tax groups and Item sales tax groups
- Tax calculation — how D365 determines tax on transactions
- Withholding tax basics
- Tax reporting overview

**HANDS-ON LAB 1.2.5-6:**
```
□ Set up procurement categories
□ Create a purchase agreement with a vendor
□ Configure sales tax group and item sales tax group
□ Create a PO and verify tax is calculated correctly
```

---

### 1.3 ⭐ Development Environment Setup

#### 1.3.1 Understanding Development Environments
- Cloud-hosted environment (CHE) — provisioned via LCS on Azure
- Tier-1 (OneBox) vs Tier-2+ (multi-box) — when to use which
- Unified Development Experience (preview) — the future of D365 dev
- Cost management — start/stop VMs, deallocate when not coding
- Environment components — AOS, SQL Server, SSRS, Management Reporter, Batch service

#### 1.3.2 Visual Studio for D365
- Visual Studio 2019/2022 — D365 extension installation
- Dynamics 365 menu in Visual Studio — what each option does
- Application Explorer (AOT browser) — navigating the entire application
- Projects and Solutions — organizing your work
- Models — what they are, how to create them, model layering
- Build process — full build vs incremental build
- Synchronize database — when and why
- Label files — multi-language support from day 1
- Best Practice (BP) checks — compile-time quality enforcement

#### 1.3.3 Lifecycle Services (LCS)
- What is LCS — the portal for everything D365
- LCS Project — creating and configuring
- Environment management — deploy, start, stop, delete
- Asset Library — storing packages, data, licenses
- Issue Search — finding known Microsoft bugs
- Support requests — how to log tickets
- System diagnostics — environment health
- Database movement — copy prod to sandbox

#### 1.3.4 Your First D365 Development
- Create a new Model (e.g., "MyTraining")
- Create a new Project inside the model
- Create a simple Runnable class (X++ job)
- Build the project
- Run/debug the class
- View output in Infolog
- Understanding the compile → sync → deploy cycle

**HANDS-ON LAB 1.3:**
```
□ Provision or connect to a D365 dev environment
□ Open Visual Studio and explore Application Explorer
□ Create your training model: "MyD365Training"
□ Create your first project: "MyFirstProject"
□ Create a Runnable class that outputs "Hello D365 F&O!" to Infolog
□ Build, run, and see the output
□ Explore 10 standard tables in Application Explorer (CustTable, VendTable, etc.)
□ Explore 5 standard forms (CustTableListPage, SalesTable, PurchTable)
□ Set a breakpoint and debug your class
□ Explore LCS — find your environment, browse asset library
```

---

## MODULE 2: X++ LANGUAGE — BASICS
> *Your C# skills transfer here — learn the differences*

### 2.1 ⭐ X++ Syntax Fundamentals

#### 2.1.1 Primitive Data Types
- `str` — string type (no System.String, just str)
  - String functions: `strLen()`, `strFmt()`, `subStr()`, `strReplace()`, `strFind()`
  - String concatenation with `+`
  - `strFmt("Pattern %1 and %2", val1, val2)` — formatted strings
- `int` — 32-bit integer
  - `int64` — 64-bit integer (used for RecId)
  - Integer arithmetic, overflow behavior
- `real` — decimal number (like C# decimal, not double)
  - Rounding: `round()`, `decRound()`, `trunc()`
  - Currency calculations — always use `real` not `int`
- `boolean` — true/false
  - X++ uses `true`/`false` (not True/False)
- `date` — date without time
  - Date functions: `today()`, `mkDate()`, `dayOfMon()`, `mthOfYr()`, `year()`
  - Date arithmetic: `date + 30` adds 30 days
  - `dateNull()` — empty date
- `utcdatetime` — date with time (UTC)
  - `DateTimeUtil::utcNow()`
  - `DateTimeUtil::addDays()`, `DateTimeUtil::addHours()`
  - Time zone conversion: `DateTimeUtil::applyTimeZoneOffset()`
- `guid` — globally unique identifier
  - `newGuid()` to generate
- `anytype` — can hold any type (use sparingly)
- `container` — ordered collection of any types
  - `conPeek()`, `conIns()`, `conDel()`, `conLen()`, `conFind()`
  - Containers are immutable — operations return new containers
  - Common pattern: `[var1, var2, var3] = container` (destructuring)
- `void` — no return value

**HANDS-ON LAB 2.1.1:**
```
□ Write X++ code using every data type above
□ Perform string operations: split a full name into first/last
□ Calculate date differences: days between two dates
□ Convert between utcdatetime and date
□ Store mixed data in a container; read it back with conPeek
□ Use strFmt to build a formatted message with 5 variables
```

#### 2.1.2 Variables & Declarations
- Variable declaration syntax: `TypeName variableName;`
- Multiple declarations: `int a, b, c;`
- Initialization: `int x = 10;` or `str name = "test";`
- `var` keyword — type inference (like C#)
- Constants — `#define` macros or `const` (prefer const)
- Scope rules — method-level, class-level
- Naming conventions — camelCase for variables, PascalCase for methods/classes

#### 2.1.3 Operators
- Arithmetic: `+`, `-`, `*`, `/`, `div` (integer division), `mod` (modulo)
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `&&`, `||`, `!`
- String: `+` (concatenation), `like` (pattern matching with wildcards)
- Assignment: `=`, `+=`, `-=`
- Ternary: `condition ? trueValue : falseValue`
- `is` and `as` — type checking and casting

#### 2.1.4 Control Flow
- `if` / `else if` / `else` — standard branching
- `switch` / `case` / `default` — multi-branch (each case needs explicit `break`)
- `while` loop — condition-first loop
- `for` loop — `for (int i = 0; i < 10; i++)`
- `do...while` loop — body-first loop
- `break` and `continue` — loop control
- No `foreach` in classic X++ (use `while select` for data, enumerators for collections)

**HANDS-ON LAB 2.1.2-4:**
```
□ Write a program with 5 different if/else scenarios
□ Write a switch/case for day-of-week logic
□ Use while, for, and do..while loops with break/continue
□ Use the ternary operator in 3 different scenarios
□ Use `like` operator for pattern matching: "Ven*" matches "Vendor"
□ Practice `div` and `mod` — build a function to check leap years
```

#### 2.1.5 Collections
- `List` — ordered collection (like C# List<T>)
  - `List::create()`, `addEnd()`, `addStart()`, `elements()`, `empty()`
  - `ListIterator` — iterating through a List
  - `ListEnumerator` — modern iteration
- `Set` — unique unordered collection
  - `Set::create()`, `add()`, `in()`, `elements()`
  - `SetIterator`, `SetEnumerator`
- `Map` — key-value pairs (like C# Dictionary)
  - `Map::create()`, `insert()`, `find()`, `exists()`, `elements()`
  - `MapIterator`, `MapEnumerator`
- `Array` — fixed or dynamic array
  - `Array::create()`, array indexing with `[]`
- `Stack` — LIFO collection
- `Struct` — named field collection (rarely used, prefer classes)
- Choosing the right collection: List vs Set vs Map vs Container

**HANDS-ON LAB 2.1.5:**
```
□ Create a List of 20 customer names, iterate and print
□ Create a Set of unique item IDs, check for existence
□ Create a Map of ItemId → Price, lookup prices
□ Store vendor data in containers vs Maps — compare approaches
□ Build a function that takes a List and returns only unique values using a Set
□ Combine List + Map: Group a list of sales lines by ItemId with totals
```

#### 2.1.6 Exception Handling
- `try` / `catch` / `finally` blocks
- Exception types: `Exception::Error`, `Exception::Warning`, `Exception::Info`
- `Exception::Deadlock` — database deadlock (auto-retry)
- `Exception::UpdateConflict` — optimistic concurrency
- `throw error("message")` — throwing exceptions
- `Global::error()`, `Global::warning()`, `Global::info()` — Infolog messages
- `ttsBegin` / `ttsCommit` / `ttsAbort` — transaction scope and exception interaction
- Retry statement — `retry` inside catch for deadlock handling
- Custom exception patterns using `SysInfoAction`

**HANDS-ON LAB 2.1.6:**
```
□ Write try/catch for each exception type
□ Build a method that validates input and throws appropriate errors
□ Use ttsBegin/ttsCommit with try/catch — understand rollback on exception
□ Simulate and handle an UpdateConflict scenario
□ Build an error-handling wrapper class with logging
```

---

### 2.2 ⭐ X++ Object-Oriented Programming

#### 2.2.1 Classes
- Class declaration syntax
- Constructor: `new()` method
- Static vs instance methods
- Access modifiers: `public`, `protected`, `private`
- `static` methods and fields
- `this` keyword — reference to current instance
- `abstract` classes — cannot be instantiated
- `final` classes and methods — cannot be extended/overridden
- Class inheritance: `extends` keyword
- Method overriding — `super()` to call parent
- `is` and `as` for type checking and safe casting
- Constructor pattern in D365: static `construct()` method
- `description()` method convention — human-readable class name

**HANDS-ON LAB 2.2.1:**
```
□ Create a base class "Vehicle" with properties (speed, fuel, name)
□ Create derived classes: Car, Truck, Motorcycle — override behavior
□ Use abstract methods — force derived classes to implement
□ Use `is`/`as` for runtime type checking
□ Build a factory method that returns the right vehicle type
□ Create a static utility class (like C# helper class)
```

#### 2.2.2 Interfaces
- Interface declaration: `interface IMyInterface`
- Implementing interfaces: `implements`
- Multiple interface implementation
- Interface vs abstract class — when to use which
- Common D365 interfaces: `SysPackable`, `SysRunnable`

#### 2.2.3 Enums & EDTs in Code
- Using Base Enums in X++ — `enum::value` syntax
- Enum to string: `enum2Str()`, `enum2Symbol()`
- String to enum: `str2Enum()`
- Integer to enum casting
- Using EDTs in variable declarations
- EDT default values and validation

**HANDS-ON LAB 2.2.2-3:**
```
□ Create an interface "IApprovable" with methods: approve(), reject(), getStatus()
□ Implement on 3 different classes
□ Write a method that accepts IApprovable and processes any approvable object
□ Use enums for status fields — convert between enum, int, and string
```

#### 2.2.4 Common Design Patterns in D365
- Singleton pattern — `instance()` method
- Factory pattern — `construct()` method with type parameter
- Strategy pattern — using interfaces for pluggable behavior
- `SysExtension` framework — attribute-based factory (★ CRITICAL)
  - `SysExtensionAppClassFactory`
  - Attribute classes for extensible enums
  - How to create extensible solutions
- Command pattern — used in workflow
- Observer pattern — delegates and event handlers

**HANDS-ON LAB 2.2.4:**
```
□ Build a payment processor using Strategy pattern
□ Implement SysExtension-based factory for payment types
□ Add a new payment type WITHOUT modifying existing code
□ Build a singleton configuration manager class
```

---

### 2.3 ⭐ X++ Data Access — Part 1 (Basic Queries)
> *THE most important X++ skill — you will write select statements every single day*

#### 2.3.1 Table Buffers
- What is a table buffer — a variable that holds one record
- Declaring: `CustTable custTable;` (variable type = table name)
- Buffer fields: `custTable.AccountNum`, `custTable.Name`
- Common system fields on EVERY table: `RecId`, `DataAreaId`, `Partition`, `RecVersion`
- `CreatedDateTime`, `ModifiedDateTime`, `CreatedBy`, `ModifiedBy`
- Buffer methods: `clear()`, `data()`, `equal()`
- Checking if buffer has data: `if (custTable)` or `if (custTable.RecId != 0)`

#### 2.3.2 Basic Select Statements
- Simple select: `select custTable;` — gets first record
- Select with where: `select custTable where custTable.AccountNum == "US-001";`
- `firstOnly` — explicit single record (performance hint)
- `firstFast` — skip some overhead for read-only
- `while select` — iterate through multiple records
- Field list: `select AccountNum, Name from custTable` — selective fields
- `count(RecId)` — counting records
- `sum()`, `avg()`, `minof()`, `maxof()` — aggregate functions
- `group by` — grouping results
- `order by` — sorting (field asc, field desc)

**HANDS-ON LAB 2.3.1-2:**
```
□ Select and display a single customer by AccountNum
□ While select ALL customers — display count
□ Select only AccountNum and Name fields (field list)
□ Count total customers using count(RecId)
□ Sum all credit limits using sum()
□ Group customers by CustGroup and count each group
□ Sort customers by Name descending
□ Select customers where name LIKE "Con*"
□ Select top 10 customers by credit limit
□ Check if a customer exists using firstOnly + if(buffer)
```

#### 2.3.3 Joins in Select
- `join` — inner join (matching records only)
- `outer join` — all from left, matching from right
- `exists join` — filter left table where match exists in right (no right fields)
- `notexists join` — filter left table where NO match in right
- Multi-table joins — chaining 3+ tables
- Alias — `join custTrans where custTrans.AccountNum == custTable.AccountNum`
- Performance: `exists join` vs `join` — when to use which

**HANDS-ON LAB 2.3.3:**
```
□ Inner join: CustTable + CustTrans — customers with transactions
□ Outer join: CustTable + CustTrans — ALL customers, transactions if any
□ Exists join: Customers who HAVE at least one transaction
□ NotExists join: Customers with ZERO transactions
□ Three-table join: SalesTable + SalesLine + InventTable
□ Compare performance: exists join vs join for filtering
```

#### 2.3.4 Insert, Update, Delete
- `insert()` — insert single record
  - Set field values on buffer → call `insert()`
  - `initValue()` — auto-called before insert
  - `validateWrite()` — validation before insert
- `update()` — update single record
  - `selectForUpdate` — lock record for update
  - `ttsBegin` / `ttsCommit` — transaction required for updates
  - Optimistic concurrency — `RecVersion` check
- `delete()` — delete single record
  - `validateDelete()` — validation before delete
- `doInsert()`, `doUpdate()`, `doDelete()` — skip business logic (DANGEROUS, avoid)
- Insert pattern: `buf.clear(); buf.Field1 = val; buf.insert();`
- Update pattern: `ttsBegin; select forUpdate buf where ...; buf.Field = val; buf.update(); ttsCommit;`

**HANDS-ON LAB 2.3.4:**
```
□ Insert 5 records into a custom table
□ Select forUpdate and modify a record — observe ttsBegin/ttsCommit requirement
□ Delete a record with validation
□ Try updating without ttsBegin — see the error
□ Try updating without forUpdate — see the error
□ Insert 100 records in a loop with proper transaction handling
```

---

### 2.4 ⭐ Application Object Tree (AOT) — Basic Elements

#### 2.4.1 Extended Data Types (EDTs)
- What is an EDT — reusable field type definition
- String EDT — size, label, help text
- Integer, Real, Date, Enum EDTs
- EDT extends EDT — inheritance (e.g., `AccountNum` extends `CustVendAC`)
- EDT properties: Label, HelpText, StringSize, Alignment, DisplayLength
- Reference EDTs — foreign key references
- Standard EDTs you MUST know: `AccountNum`, `ItemId`, `Description`, `Name`, `AmountCur`, `Qty`, `CustAccount`, `VendAccount`
- Creating custom EDTs — naming convention: `MyModuleMyFieldType`

#### 2.4.2 Base Enums
- What is a Base Enum — system-wide enumeration
- Creating enums — elements with Name, Label, Value
- Extensible enums — allow adding values without modifying base
- Standard enums you MUST know: `NoYes`, `SalesStatus`, `PurchStatus`, `ModuleInventPurchSales`
- Using enums in table fields and X++ code
- Naming convention: `MyModuleMyStatus`

#### 2.4.3 Tables — Basics
- Creating a table — properties overview
- Table types: Regular (persisted), InMemory (TempDB), TempDB
- Fields — adding fields using EDTs (always use EDTs, NEVER raw types)
- Field properties: Mandatory, AllowEdit, AllowEditOnCreate
- Field groups — organizing fields for forms
  - `AutoReport`, `AutoLookup`, `AutoIdentification` — special system groups
  - `Overview` — grid display, `Details` — detail display
- Indexes — creating for performance and uniqueness
  - Unique index — enforces uniqueness
  - Non-unique index — performance only
  - Clustered index — physical sort order (one per table)
  - Include columns in indexes
- Relations — foreign keys
  - Normal relation — single field FK
  - Fixed relation — includes a constant (e.g., TransType == Sales)
  - Related field fixed — the related table has a constant
  - Cascade delete, Restricted delete
- Delete actions — what happens when parent record is deleted
  - Cascade — delete children
  - Restricted — prevent delete if children exist
  - Cascade+Restricted — cascade some, restrict others

**HANDS-ON LAB 2.4:**
```
□ Create 5 EDTs: MyExpenseId, MyExpenseDescription, MyExpenseAmount, MyExpenseDate, MyExpenseCategory
□ Create 2 Base Enums: MyExpenseStatus (Draft, Submitted, Approved, Rejected), MyExpenseType (Travel, Meal, Office, Other)
□ Create table "MyExpenseHeader":
  - Fields using your EDTs: ExpenseId, Description, ExpenseDate, Status, TotalAmount
  - Field groups: AutoReport, Overview (grid), Details (form)
  - Unique index on ExpenseId
  - Created/Modified tracking enabled
□ Create table "MyExpenseLine":
  - Fields: LineNum, Category, Description, Amount, ExpenseType
  - Relation to MyExpenseHeader (FK)
  - Delete action: Cascade
  - Index on HeaderRecId + LineNum
□ Synchronize database and verify tables exist in SQL
```

---

### 2.5 ⭐ Table Methods & Standard Patterns

#### 2.5.1 Static Find/Exist Pattern (YOU WILL WRITE THIS 1000 TIMES)
```
public static MyExpenseHeader find(MyExpenseId _expenseId, boolean _forUpdate = false)
public static boolean exist(MyExpenseId _expenseId)
```
- `find()` — returns a single record by primary key
- `exist()` — returns true/false if record exists
- `_forUpdate` parameter — lock for update when needed
- This is THE most important pattern in D365 development

#### 2.5.2 Standard Table Methods
- `initValue()` — set default values when record is initialized
  - Called automatically before user fills in a new record
  - `super()` must be called first
- `validateWrite()` — validate before insert/update
  - Return `true` to allow, `false` to block
  - `ret = ret && (this.Amount > 0);` — accumulate validations
  - `super()` validates base rules
- `validateDelete()` — validate before delete
  - Check for dependent records
- `validateField(fieldId _fieldId)` — validate a single field change
  - Called when user modifies a field on a form
- `modifiedField(fieldId _fieldId)` — react to field change
  - Auto-calculate other fields
  - `switch (_fieldId) case fieldNum(Table, Field):` pattern
- `insert()` — override to add custom insert logic
  - Number sequence generation here
- `update()` — override to add custom update logic
- `delete()` — override to add custom delete logic
  - Delete child records if no cascade delete action
- `caption()` — return a display caption for the record
- `defaultRow()` — set defaults based on other field values

**HANDS-ON LAB 2.5:**
```
□ Add find() and exist() to MyExpenseHeader — test with X++ job
□ Add initValue() — default date = today(), status = Draft
□ Add validateWrite() — Amount must be > 0, Description cannot be empty
□ Add validateDelete() — cannot delete if Status == Approved
□ Add validateField() — if Amount > 10000, show warning
□ Add modifiedField() — when category changes, update default description
□ Add insert() — auto-generate ExpenseId using number sequence (or simple counter for now)
□ Write a test job that exercises ALL these methods
```

---

### 2.6 ⭐ Number Sequences

#### 2.6.1 Number Sequence Concepts
- What are number sequences — auto-incrementing business IDs
- Number sequence format — `#####`, `Exp-####-2024`, constant + variable segments
- Scope — Shared (global), Company (per legal entity), Operating Unit
- Continuous vs Non-continuous — gaps allowed or not
- Pre-allocation — performance for high-volume sequences

#### 2.6.2 Number Sequence Setup for Custom Module
- `NumberSeqModule` class — define parameters for your module
- `NumberSeqParametersTable` — where settings are stored
- EDT reference — connecting EDT to number sequence
- Number sequence wizard — UI setup

#### 2.6.3 Using Number Sequences in Code
- `NumberSeq::newGetNum()` — generate the next number
- `NumberSeq::newGetNumFromId()` — generate from a specific reference
- Aborting a number sequence — if transaction fails
- Handling in `insert()` method — typical pattern

**HANDS-ON LAB 2.6:**
```
□ Create a NumberSeqModule class for your Expense module
□ Define number sequence reference for MyExpenseId EDT
□ Configure the number sequence format: EXP-######
□ Modify MyExpenseHeader.insert() to auto-assign number
□ Test: create 5 records and verify sequential numbering
□ Test: abort a transaction and verify number is released (non-continuous)
```

---

### 2.7 Debugging & Troubleshooting

#### 2.7.1 Visual Studio Debugger
- Breakpoints — set, conditional breakpoints, hit count
- Watch window — inspect variables
- Immediate window — evaluate expressions
- Call stack — understand execution flow
- Step into (F11), Step over (F10), Step out (Shift+F11)
- Debug an X++ job vs debug a form action
- Attach to process — debugging running AOS
- Exception breakpoints — break on specific exceptions

#### 2.7.2 Infolog & Trace
- `info()`, `warning()`, `error()` — output messages
- `Global::exceptionTextFallThrough()` — getting error details
- Database trace — viewing SQL generated by X++
- Trace parser — analyzing performance traces
- Event Viewer — system-level error logs

**HANDS-ON LAB 2.7:**
```
□ Debug a while select loop — watch buffer values change
□ Set a conditional breakpoint (only break when Amount > 1000)
□ Debug through insert() → initValue() → validateWrite() flow
□ Use Immediate window to evaluate X++ expressions during debug
□ Enable SQL trace and view generated SQL for a select statement
□ Debug a form button click — trace from UI to business logic
```

---

> ### ✅ LEVEL 1 CHECKPOINT PROJECT
> **Build "Expense Tracker v1" — Data Layer Only**
> - 2 tables (Header + Lines) with proper EDTs, enums, indexes, relations
> - Complete table methods: find, exist, initValue, validateWrite, validateDelete, modifiedField
> - Number sequence for ExpenseId
> - X++ test job that: creates 10 expenses with lines, queries by status, calculates totals by category, validates error scenarios
> - All code uses proper naming conventions and passes BP checks

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEVEL 2: INTERMEDIATE (Weeks 7–12)
# Build Real UIs, Business Logic & Extend Standard Modules
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## MODULE 3: FORMS & UI DEVELOPMENT

### 3.1 ⭐ Form Architecture

#### 3.1.1 Form Structure
- Form metadata: Data Sources + Design
- Data sources — binding one or more tables to a form
  - Data source properties: Table, Index, AllowCreate, AllowDelete, AllowEdit
  - Multiple data sources — master-detail, joined data
  - Data source relations — how child data sources link to parent
  - InsertIfEmpty — auto-create first record
- Design node — the visual layout
  - Design patterns — Microsoft enforced UI consistency
  - Top-level pattern types and when to use each
  - Controls hierarchy — containers > groups > fields

#### 3.1.2 Form Patterns (★ CRITICAL — D365 ENFORCES THESE)
- **Simple List** — flat list of records (Categories, Parameters)
  - Structure: ActionPane → Grid → (optional details)
  - When to use: Setup/reference data with < 10 fields
- **Simple List and Details** — list + detail pane side by side
  - Structure: ActionPane → List/Details split → Grid | Tab
  - When to use: Master data with moderate detail
- **Details Master** — full detail form with header/lines
  - Structure: ActionPane → Header fields → Lines Grid → Line details Tab
  - When to use: Transaction documents (PO, SO, Invoice)
- **Details Transaction** — optimized for transaction entry
  - Structure: Optimized for speed of data entry
  - When to use: Journals, rapid entry screens
- **List Page** — searchable, filterable list for navigation
  - Structure: Filters → ActionPane → Grid
  - When to use: Entry point to browse records
- **Workspace** — operational dashboard
  - Structure: Tiles + Lists + Charts + Links
  - When to use: Role-based home pages
- **Dialog** — popup for parameters/confirmations
- **Drop Dialog** — lightweight inline dialog
- **Lookup** — selection popup
- **FactBox** — contextual information panel
- **Table of Contents** — parameter setup pages (tabbed)

#### 3.1.3 Form Controls In-Depth
- **Action Pane** — toolbar with buttons
  - Action Pane Tabs — group related actions
  - Button Groups — sub-grouping
  - Command buttons vs Menu buttons vs Menu item buttons
- **Grid** — table display of records
  - Grid properties: ShowRowLabels, AlternateRowShading
  - Grid columns — bound to data source fields
- **Groups** — layout containers
  - Group types: Regular, Tab, TabPage, FastTab, HeaderGroup
- **Field controls** — bound to data source fields
  - StringEdit, IntEdit, RealEdit, DateEdit, ComboBox, CheckBox
  - Control properties: DataSource, DataField, Mandatory, Enabled, Visible
- **Filter controls** — QuickFilter, Filter Pane
- **Tab controls** — organizing detail sections
  - Tab vs FastTab — when to use which
  - Tab page caption — auto-generated from field group
- **Buttons** — triggering actions
  - Button types: Regular, CommandButton, MenuItemButton, DropDialogButton
  - Button properties: MenuItemType, MenuItemName, DataSource
- **Images and Icons** — visual indicators

**HANDS-ON LAB 3.1:**
```
□ Create a Simple List form for Expense Categories
  - ActionPane with New/Delete buttons
  - Grid showing CategoryId, Name, Description
  - Apply SimpleList pattern — verify BP passes
□ Create a List Page for Expense Headers
  - Filters: Status, Date range
  - ActionPane: New, Edit, Delete, Submit, Approve
  - Grid: ExpenseId, Description, Date, Amount, Status
  - Apply ListPage pattern
□ Create a Details Master form for Expense Header/Lines
  - Header section: ExpenseId, Description, Date, Status, TotalAmount
  - Lines grid: LineNum, Category, Description, Amount, Type
  - Tab pages: Lines, Totals, History
  - Apply DetailsMaster pattern
  - Apply sub-patterns to each section
  - Verify ALL patterns pass BP validation
```

---

### 3.2 ⭐ Form Logic & Events

#### 3.2.1 Form Methods
- `init()` — form initialization (add dynamic controls, set defaults)
- `run()` — after init, form is visible (set focus, execute queries)
- `close()` — form closing (cleanup, save state)
- `canClose()` — validate before closing (unsaved changes?)
- `task()` — handle keyboard shortcuts and system tasks

#### 3.2.2 Data Source Methods
- `init()` — data source initialization (modify query programmatically)
- `executeQuery()` — run the query (call after modifying query ranges)
- `active()` — fires when active record changes (enable/disable controls)
- `initValue()` — set defaults for new record from data source
- `validateWrite()` — validate before save (form-level)
- `write()` — save record
- `delete()` — delete record from data source
- `selectionChanged()` — grid selection changes
- `validateDelete()` — validate before delete

#### 3.2.3 Control Methods & Events
- `clicked()` — button was clicked
- `modified()` — field value changed by user
- `lookup()` — custom lookup (dropdown) for a field
- `validate()` — validate field value
- `selectionChange()` — combo box selection changed
- `enter()` — control got focus
- `leave()` — control lost focus

#### 3.2.4 Form Interaction Patterns
- Enable/disable controls based on record status
  ```
  // In data source active():
  buttonApprove.enabled(record.Status == ExpenseStatus::Submitted);
  ```
- Mandatory fields based on conditions
- Field visibility based on type/status
- Refreshing data: `dataSource.research(true)` vs `dataSource.executeQuery()`
- Passing values between forms: `args`, `caller`, `record`
- Form → Form navigation: `MenuFunction` with `Args`
- Return value from dialog: `closedOk()` method pattern

**HANDS-ON LAB 3.2:**
```
□ Add init() logic to your expense form — set default filters
□ Override data source active() — disable Approve button unless Status == Submitted
□ Override modified() on Amount — recalculate line total
□ Create a custom lookup for Category field
□ Add Submit button: validate all lines exist → change status → refresh form
□ Add Approve button: validate submitter is not approver → change status
□ Add Cancel button: with confirmation dialog
□ Navigate from List Page to Detail form — pass selected record
□ Navigate from Detail form to Vendor form — pass vendor account
□ Build a Drop Dialog for expense rejection — reason field required
```

---

### 3.3 ⭐ Menus, Menu Items & Navigation

#### 3.3.1 Menu Items
- Display Menu Item — opens a form
  - Properties: Object (form name), Label, Parameters, EnumParameter
- Output Menu Item — runs a report
- Action Menu Item — runs a class/service
- Menu Item properties: Label, Security privileges, NormalImage
- Menu Item naming convention: `MyModule` + ObjectName

#### 3.3.2 Menus & Navigation
- Main Menu — the navigation pane
- Sub-menus — organizing menu items into categories
- Module navigation structure: Module → Section → Menu Items
- Menu extensions — adding to existing modules
- Favorites and recent items

#### 3.3.3 Security (Basic)
- Security architecture: Role → Duty → Privilege → Permission
- Roles — business roles (Accountant, Clerk, Manager)
- Duties — job functions (Process payments, Approve invoices)
- Privileges — specific actions (View customer, Edit vendor)
- Permissions — granular access (Table → CRUD)
- Entry point permissions — menu item → privilege mapping
- Policy framework — row-level security basics

**HANDS-ON LAB 3.3:**
```
□ Create Display Menu Items for all your expense forms
□ Create an Action Menu Item for your batch job
□ Create a Menu for "Expense Management" module
  - Sub-menus: Expenses (list, detail), Setup (categories, parameters), Reports
□ Add your module to the Navigation Pane
□ Create Security:
  - Privilege: MyExpenseView, MyExpenseCreate, MyExpenseApprove
  - Duty: MyExpenseClerk (view + create), MyExpenseManager (view + create + approve)
  - Role: ExpenseClerk, ExpenseManager
□ Test: Log in as each role — verify access restrictions work
```

---

## MODULE 4: DATA ENTITIES & INTEGRATIONS (Basic)

### 4.1 ⭐ Data Entities

#### 4.1.1 Data Entity Concepts
- What is a Data Entity — abstraction layer over tables
- Why entities — decouples consumers from physical tables
- Entity vs Table — when to use which
- Entity types: Standard, Composite (header + lines), Aggregate (analytics)
- Data Entity architecture: Entity → Staging Table → Target Table(s)
- Public vs Private entities — who can consume

#### 4.1.2 Creating Data Entities
- Data Entity wizard — walking through the wizard
  - Primary data source — main table
  - Additional data sources — joined tables
  - Field mapping — entity fields → table fields
  - Key — business key (not RecId)
- Data Entity properties:
  - IsPublic — exposed via OData
  - DataManagementEnabled — available in Data Management workspace
  - DataManagementStagingTable — auto-generated staging table
  - EntityCategory — Document, Reference, Master, Transaction, Parameter
- Computed and virtual fields — calculated at runtime
- Unmapped fields — exist on entity but not mapped to table
- Default values and transformations
- Validation on entity — `validateWrite()` equivalent

#### 4.1.3 Data Management Framework (DMF)
- Data Management workspace — import/export UI
- Data Projects — organizing import/export jobs
- Source data formats: CSV, XML, Excel, JSON
- Mapping — entity fields to source fields
- Staging table — intermediate storage before target
- Import execution: Source → Staging → Validate → Target
- Error handling — viewing and fixing import errors
- Export — extracting data from D365
- Data packages — bundled data for migration
- Recurring integrations — scheduled automated imports/exports

**HANDS-ON LAB 4.1:**
```
□ Create a Data Entity for MyExpenseHeader
  - Map to table, set key to ExpenseId
  - Make public and data management enabled
  - Add computed field: DaysSinceCreation
□ Create a Data Entity for MyExpenseLine
  - Join to header entity
□ Create a Composite Entity: ExpenseWithLines
□ Import 50 expense records via CSV using Data Management workspace
  - Handle 5 intentional errors — view error log, fix, re-import
□ Export all approved expenses to CSV
□ Set up a recurring export — every day at 6 PM
```

---

### 4.2 ⭐ OData & REST API Basics

#### 4.2.1 OData Endpoints
- What is OData — REST protocol for data access
- D365 F&O OData endpoint: `https://[environment].operations.dynamics.com/data/`
- Entity → OData resource mapping
- CRUD operations: GET, POST, PATCH, DELETE
- Query options: `$filter`, `$select`, `$expand`, `$top`, `$skip`, `$orderby`, `$count`
- Cross-company queries: `?cross-company=true`
- Batch requests — multiple operations in one call

#### 4.2.2 Authentication
- Azure AD App Registration — client ID, secret, tenant
- OAuth2 — client_credentials flow (service-to-service)
- Bearer token — using in REST calls
- Token caching and refresh

**HANDS-ON LAB 4.2:**
```
□ Get an OAuth token using Postman (or REST client)
□ GET: List all expenses via OData
□ GET: Filter expenses by status and date using $filter
□ GET: Expand lines with $expand=ExpenseLines
□ POST: Create a new expense via OData
□ PATCH: Update an expense status
□ DELETE: Remove a draft expense
□ Build a simple .NET Console app that does all CRUD operations
```

---

## MODULE 5: BUSINESS LOGIC — INTERMEDIATE PATTERNS

### 5.1 ⭐ Chain of Command (CoC)
> *THE most important extension mechanism — you'll use it daily*

#### 5.1.1 CoC Fundamentals
- What is CoC — wrapping existing methods without modifying them
- Why CoC replaced overlayering — upgrade-safe customizations
- `[ExtensionOf(classStr(OriginalClass))]` syntax
- `next` keyword — calling the original + other extensions
- Rules: `next` must be called exactly once
- CoC on classes — extending any class method
- CoC on tables — extending table methods (insert, update, validateWrite, etc.)
- CoC on forms — extending form methods
- CoC on data entities — extending entity logic
- What you CAN extend vs what you CANNOT
- Order of execution when multiple extensions exist

#### 5.1.2 CoC on Tables
- Extending `validateWrite()` — add custom validation
- Extending `insert()` — add post-insert logic
- Extending `modifiedField()` — add field change handling
- Extending `initValue()` — add default values
- Accessing `this` — the table buffer in extension

#### 5.1.3 CoC on Classes
- Extending business logic classes
- Extending controller classes
- Extending service classes
- Wrapping: pre-logic → `next` → post-logic
- Extracting return values from `next`

#### 5.1.4 CoC on Forms
- Extending form `init()`
- Extending form data source methods
- Extending form control methods
- Limitations of form CoC

**HANDS-ON LAB 5.1:**
```
□ Extend CustTable.validateWrite() — add custom validation (credit limit check)
□ Extend CustTable.insert() — log new customer creation to a custom table
□ Extend PurchTable.modifiedField() — auto-fill a custom field when vendor changes
□ Extend SalesTable.initValue() — set default delivery date to today + 7
□ Extend SalesLineType.validateWrite() — block sales of discontinued items
□ Extend the SalesTable form init() — add a custom info message
□ Extend the PurchTable form data source active() — disable button based on status
□ Build 3 more CoC extensions on different standard objects
```

---

### 5.2 ⭐ Event Handlers & Delegates

#### 5.2.1 Event Handler Types
- **Pre-event handler** — runs BEFORE the method
  - `[PreHandlerFor(tableStr(CustTable), tableMethodStr(CustTable, insert))]`
  - Cannot modify return value
  - Can modify parameters
- **Post-event handler** — runs AFTER the method
  - `[PostHandlerFor(tableStr(CustTable), tableMethodStr(CustTable, insert))]`
  - Can read return value via `EventHandlerResult`
  - Can modify `EventHandlerResult`
- **Table events** — attribute-based
  - `[DataEventHandler(tableStr(CustTable), DataEventType::Inserting)]`
  - `Inserting`, `Inserted`, `Updating`, `Updated`, `Deleting`, `Deleted`
  - `ValidatingWrite`, `ValidatedWrite`, `ValidatingDelete`
  - `ModifiedField`, `ValidatingField`
  - `InitializingRecord`, `InitializedRecord`
- **Form events** — form-level events
  - `[FormEventHandler(formStr(SalesTable), FormEventType::Initialized)]`
  - `Initializing`, `Initialized`, `Closing`, `Closed`
  - Form data source events and form control events

#### 5.2.2 Delegates
- What are delegates — custom extension points you define
- Creating a delegate — `delegate void myDelegate(str _param) {}`
- Subscribing to a delegate — `[SubscribesTo(classStr(MyClass), delegateStr(MyClass, myDelegate))]`
- Raising/firing a delegate — `this.myDelegate(_param)`
- Using `EventHandlerResult` to get subscriber return values
- Design pattern: add delegates to your custom code for future extensibility

#### 5.2.3 CoC vs Event Handlers — When to Use Which
- CoC: When you need to wrap/modify existing behavior
- Event handlers: When you need to react to something happening
- Pre/Post handlers: When you need fine-grained before/after control
- Delegates: When building extensible custom solutions
- Performance considerations

**HANDS-ON LAB 5.2:**
```
□ Create a post-event handler on VendTable.insert() — send notification
□ Create a table event handler: DataEventType::Inserting on PurchTable
□ Create pre-event handler that modifies a parameter before processing
□ Create a delegate in your expense header class
□ Subscribe to the delegate from a different class
□ Build a "pluggable notification system" using delegates
□ Create form event handler: log every time SalesTable form opens
□ Mix CoC + Event handler on same table — understand execution order
```

---

### 5.3 ⭐ Table Extensions & Form Extensions

#### 5.3.1 Table Extensions
- Creating a table extension — `CustTable.MyModel` naming
- Adding new fields via extension
- Adding new indexes via extension
- Adding new relations via extension
- Adding new field groups via extension
- Adding new methods via extension class (CoC class)
- Adding new events via extension
- What you CANNOT do: modify existing fields, remove fields, change properties of existing elements

#### 5.3.2 Form Extensions
- Creating a form extension — `SalesTable.MyModel`
- Adding new controls (fields, buttons, tabs)
- Adding new data sources
- Rearranging controls within pattern constraints
- Adding event handlers on form extension
- Limitations — cannot remove/modify existing controls
- Working with form patterns in extensions

#### 5.3.3 Other Extension Types
- EDT extensions — adding new elements to existing EDTs
- Enum extensions — adding new values to extensible enums
- Menu extensions — adding items to existing menus
- Security extensions — extending existing security objects
- View extensions
- Query extensions — adding data sources and ranges

**HANDS-ON LAB 5.3:**
```
□ Create CustTable extension:
  - Add field: MyCustomerRating (enum: Gold, Silver, Bronze)
  - Add index on MyCustomerRating
  - Add field to AutoReport and Overview field groups
□ Create SalesTable form extension:
  - Add your new field to the header section
  - Add a new button to the action pane
  - Add event handler on the new button's clicked event
□ Create PurchTable extension:
  - Add field: MyComplianceFlag (NoYes)
  - Add field: MyComplianceNote (str 200)
□ Extend PurchTable form to show compliance fields
□ Create an enum extension: add new value to an extensible enum
□ Create a menu extension: add your expense menu items to an existing module
```

---

### 5.4 ⭐ SysOperation Framework
> *The standard way to build batch-capable operations in D365*

#### 5.4.1 Architecture
- Why SysOperation — replaces RunBase with modern, testable pattern
- Four components:
  - **Data Contract** — parameter class (`DataContractAttribute`, `DataMemberAttribute`)
  - **Service** — business logic class
  - **Controller** — orchestration, batch integration
  - **UI Builder** (optional) — custom dialog logic
- How they connect: Controller → Service → Data Contract

#### 5.4.2 Data Contract Class
- `[DataContractAttribute]` on class
- `[DataMemberAttribute]` on parm methods
- `[SysOperationLabelAttribute('Label')]` — field labels
- `[SysOperationHelpTextAttribute('Help')]` — field help text
- `[SysOperationGroupMemberAttribute('GroupName')]` — grouping parameters
- `[SysOperationDisplayOrderAttribute(1)]` — parameter order
- Supported types: primitives, containers, `List`, query
- Query parameter: `[SysOperationQueryAttribute]`
- Validation in data contract: `validate()` method

#### 5.4.3 Service Class
- `[SysEntryPointAttribute(true)]` — marks as entry point
- Service method — receives data contract, executes logic
- Transaction handling — `ttsBegin` / `ttsCommit`
- Progress tracking — `SysOperationProgress`
- Infolog messages — reporting results
- Error handling — try/catch with meaningful messages

#### 5.4.4 Controller Class
- Extends `SysOperationServiceController`
- `new()` — set class, method, execution mode
- `caption()` — dialog title
- `canGoBatch()` — can this run as batch
- `parmDialogCaption()` — dialog caption
- Default parameter values
- Execution modes: Synchronous, Asynchronous, ScheduledBatch

#### 5.4.5 Batch Processing
- What is batch processing — background execution
- Batch groups — organizing batch jobs
- Batch job scheduling — recurrence, time windows
- Batch alerts — success/failure notifications
- Batch tasks — sub-units of a batch job
- Batch dependencies — task ordering
- Monitoring batch jobs — status, history, error log
- Performance: batch parallelism, task distribution

**HANDS-ON LAB 5.4:**
```
□ Build: "Expense Auto-Approval" batch job
  - Data Contract: DaysOld (int), MaxAmount (real), Category (enum)
  - Service: Find expenses matching criteria, auto-approve
  - Controller: Caption, enable batch
  - UI Builder: Custom validation (DaysOld must be > 0)
□ Run synchronously — verify results
□ Schedule as batch — run every night at midnight
□ Monitor batch execution — check history, status
□ Build: "Expense Report Generator" operation
  - Data Contract: DateFrom, DateTo, Status filter, Employee filter
  - Service: Query matching expenses, output summary to infolog
  - Controller: Set up with query parameter
□ Add SysOperationProgress — show progress bar during execution
```

---

### 5.5 ⭐ Workflow Development

#### 5.5.1 Workflow Architecture
- Workflow runtime engine — how D365 processes workflows
- Workflow types — Approval, Task, Conditional, Parallel
- Workflow components:
  - **Workflow Category** — groups related workflow types
  - **Workflow Type** — defines the workflow (e.g., Expense Approval)
  - **Workflow Document** — links workflow to table/query
  - **Workflow Elements**:
    - Approval element — approve/reject/delegate/request change
    - Task element — complete a task
    - Automated task — code runs automatically
    - Conditional decision — branch based on condition
    - Parallel activity — multiple branches simultaneously
    - Line-item workflow — workflow per line

#### 5.5.2 Building a Workflow — Developer Tasks
- Create Query for workflow document
- Create Workflow Category
- Create Workflow Document class
  - `getQueryName()` — return the query
  - `canSubmitToWorkflow()` — condition to enable submit button
- Create Workflow Type (in AOT wizard)
  - Properties: Category, Document, MenuItemType/Name
  - Started/Completed event handlers
- Create Approval Element
  - Properties: Workflow type, Participant provider
  - Event handlers: Started, Completed, Approved, Rejected, ChangeRequested, Delegated
- Create Event Handler classes
  - `WorkflowStartedEventHandler` — fires when submitted
  - `WorkflowCompletedEventHandler` — fires when fully approved
  - `WorkflowApprovalApprovedEventHandler` — approval step approved
  - `WorkflowApprovalRejectedEventHandler` — approval step rejected
  - `WorkflowWorkItemsStartedEventHandler` — work item created
- Enable submit button on form
  - `canSubmitToWorkflow()` on form
  - `WorkflowSubmitManager` — handle submit action

#### 5.5.3 Configuring Workflow — Functional Tasks
- Workflow editor — visual designer
- Approval step configuration — who approves
  - User-based, Hierarchy, Queue
  - Escalation rules — if not approved in X days
  - Delegation — out of office
- Conditional decisions — amount > threshold
- Notifications — email, in-app
- Due dates and escalation

**HANDS-ON LAB 5.5:**
```
□ Create expense approval workflow — complete developer artifacts:
  - Query: MyExpenseApprovalQuery
  - Category: MyExpenseWorkflowCategory
  - Document class: MyExpenseWorkflowDocument
  - Workflow Type: MyExpenseApproval
  - Approval Element: MyExpenseManagerApproval
  - Event handlers: Started (set status=Submitted), Approved (set status=Approved), 
    Rejected (set status=Rejected), Completed
□ Enable submit button on expense form
□ Configure the workflow in UI:
  - Single approval step assigned to "Manager" role
  - Add condition: if Amount > 5000, require Finance approval too
  - Set escalation: if not approved in 48 hours, escalate to VP
□ Test end-to-end:
  - Submit expense as Employee
  - Approve as Manager
  - Verify status changes at each step
  - Test rejection flow
  - Test delegation flow
```

---

## MODULE 6: REPORTING (Basic)

### 6.1 ⭐ SSRS Reports

#### 6.1.1 Report Architecture
- SSRS in D365 — how it works (RDP → SSRS → PDF/Excel/Word)
- Report types: Query-based, RDP-based (Report Data Provider)
- Report components:
  - **Report** — the AOT report object
  - **Report Design** — visual layout (Precision or Auto)
  - **Report Data Provider (RDP)** — X++ class that provides data
  - **Data Contract** — parameters for the report
  - **Controller** — orchestration (similar to SysOperation)
  - **UI Builder** (optional) — custom parameter dialog
- Precision Design vs Auto Design
  - Precision: full control, Visual Studio RDLC designer
  - Auto: auto-generated, less control, faster
- Report deployment — deploy to SSRS server

#### 6.1.2 Building an RDP Report
- RDP class: `[SRSReportParameterAttribute(classStr(MyContract))]`
- `processReport()` method — populate temp table
- Tmp table — temporary table to hold report data
- Data Contract — `[DataContractAttribute]` with `[DataMemberAttribute]` parms
- Controller — `[SRSReportQueryAttribute(queryStr(MyQuery))]`
- Menu item — Output type for reports

#### 6.1.3 Report Design
- Creating Precision Design in Visual Studio
- Datasets — connecting to RDP
- Report layout — headers, footers, body
- Expressions — calculated fields in RDLC
- Grouping and sorting in design
- Sub-reports
- Parameters — binding to data contract
- Images and logos
- Page size, margins, orientation
- Drill-through reports

**HANDS-ON LAB 6.1:**
```
□ Build: "Expense Summary Report"
  - Tmp Table: TmpExpenseSummary (Employee, Category, TotalAmount, Count)
  - RDP Class: Populate tmp table from expense header/lines
  - Data Contract: DateFrom, DateTo, Status filter
  - Controller: Link everything together
  - Precision Design: 
    - Company logo header
    - Group by employee, sub-group by category
    - Subtotals per employee, grand total
    - Filter parameters displayed in header
  - Menu Item: Output type
□ Run from expense workspace
□ Export to PDF, Excel, Word — verify formatting
□ Build: "Expense Detail Report" — individual expense with all lines
□ Deploy reports to SSRS
```

---

> ### ✅ LEVEL 2 CHECKPOINT PROJECT
> **Build "Expense Tracker v2" — Full Working Application**
> - Everything from Level 1 PLUS:
> - Complete UI: List Page, Detail Form, Setup Form, Workspace
> - Workflow: Submit → Approve → Complete
> - Security: 3 roles with proper privileges
> - Menu & Navigation: Full module in nav pane
> - Data Entity: Import/export capability
> - OData: REST API access
> - 2 SSRS Reports: Summary and Detail
> - CoC Extensions: Extend standard VendTable with expense link
> - Batch Job: Auto-approve old expenses
> - A functional user should be able to use your module end-to-end without touching X++

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEVEL 3: ADVANCED (Weeks 13–16+)
# Production-Grade Development, Performance & Architecture
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## MODULE 7: ADVANCED X++ & DATA ACCESS

### 7.1 ⭐ Advanced Data Operations

#### 7.1.1 Set-Based Operations (★ PERFORMANCE CRITICAL)
- Why set-based is 10-100x faster than row-by-row
- `insert_recordset` — bulk insert from query
  - Syntax: `insert_recordset targetTable (field1, field2) select field1, field2 from sourceTable`
  - Mapping fields, constants, expressions
  - Cross-company set operations
- `update_recordset` — bulk update matching records
  - Syntax: `update_recordset table setting field = value where condition`
  - Multi-field updates
  - Updates with joins
  - Setting field = calculated expression
- `delete_from` — bulk delete
  - Syntax: `delete_from table where condition`
  - Cascading implications
- When set-based falls back to row-by-row:
  - `insert()`, `update()`, `delete()` overrides exist on table
  - Database events exist
  - Alert rules configured
  - `skipDataMethods(true)` — force set-based (CAREFUL: skips business logic)
  - `skipDatabaseLog(true)` — skip database logging
  - `skipEvents(true)` — skip events

**HANDS-ON LAB 7.1.1:**
```
□ Convert a while-select-update loop to update_recordset — measure speed difference
□ Use insert_recordset to copy 10,000 records between tables
□ Use delete_from to purge old records — measure vs delete() in loop
□ Build a performance test: row-by-row vs set-based for 50,000 records
□ Use skipDataMethods when safe — understand the risk
□ Write set-based operation with joins — update based on related table
```

#### 7.1.2 Query Framework (Dynamic Queries)
- `Query` object — building queries programmatically
- `QueryBuildDataSource` — adding tables to query
  - `addDataSource()` — add root or child data source
  - `addRange()` — adding filters
  - `QueryBuildRange::value()` — range expressions
  - Range expressions: exact, wildcard, range (`1..10`), not (`!value`), or (`val1,val2`)
- `QueryBuildLink` — joins between data sources
  - Join types: InnerJoin, OuterJoin, ExistsJoin, NotExistsJoin
- `QueryBuildFieldList` — selecting specific fields
- `QueryRun` — executing the query
  - `next()` — iterate results
  - `get()` — get current record from data source
  - `getNo()` — get by data source position
  - `changed()` and `changedNo()` — detect group breaks
- `QueryOrderByField` — dynamic sorting
- `QueryHavingFilter` — HAVING clause for aggregates
- `SysQueryRangeUtil` — utility methods for dynamic ranges
  - `currentCompany()`, `currentUserId()`, `day(0)` (today), `monthRange(-1,0)` (last month)
- Saved queries — user-saved query configurations
- Query packing/unpacking — serialize query for batch jobs

**HANDS-ON LAB 7.1.2:**
```
□ Build a dynamic query: let user specify table, fields, and filters at runtime
□ Create a query with 3 data sources (3-way join)
□ Use SysQueryRangeUtil: date ranges, current user, current company
□ Build QueryRun with grouping — calculate aggregates dynamically
□ Pack/unpack a query — use in SysOperation data contract
□ Create a form with user-editable query — save and reload
```

#### 7.1.3 Direct SQL & Performance
- Direct SQL via `Statement` — when and why (RARE, avoid when possible)
- Temp tables — `InMemory` vs `TempDB`
  - `setTmpData()` — passing temp table between client/server
  - Temp table performance — when to use which type
  - `setTmpData()` vs `linkPhysicalTableInstance()`
- Record caching strategies:
  - `EntireTable` — small, rarely changing tables (< 1000 records)
  - `Found` — cache found records
  - `FoundAndEmpty` — cache found + not found
  - `RecordViewCache` — cache a query result set
  - Cache invalidation — when cache refreshes
- Optimistic Concurrency Control (OCC)
  - `RecVersion` field — version tracking
  - Update conflicts — how to handle
  - `selectForUpdate` — pessimistic locking when needed
- Index hints — forcing specific index usage
- Cross-company queries — `changecompany` and `crossCompany`

**HANDS-ON LAB 7.1.3:**
```
□ Create TempDB table — populate and use on a form (vs InMemory)
□ Configure table caching — EntireTable for small reference table
□ Simulate an update conflict — handle gracefully with retry
□ Write a cross-company query — read data from all legal entities
□ Use changecompany block to insert into a different company
□ Profile a slow query — identify missing index, add it, measure improvement
```

---

### 7.2 ⭐ Advanced Extensions & Patterns

#### 7.2.1 SysExtension Framework — Deep Dive
- Factory pattern with `SysExtensionAppClassFactory`
- `SysExtensionIAttribute` — custom attributes
- Extensible enums — adding new enum values and associated classes
- Multi-level extension: Base → Module → Customer
- Creating truly pluggable architectures
- Performance: attribute scanning and caching

#### 7.2.2 Plugin/Strategy Patterns
- `SysPluginFactory` — loading classes by attribute
- `SysPluginMetadataCollection` — discovering plugins
- Building a framework that ISVs/partners can extend
- Versioning and backward compatibility

#### 7.2.3 Advanced Table Patterns
- Inheritance in tables — table inheritance hierarchy
- Date effectivity — `ValidFrom` / `ValidTo` patterns
  - `ValidTimeStateAutoQuery` — automatic date filtering
  - Managing date-effective records
- Dimension framework — financial dimensions deep dive
  - `DimensionDefault` — default dimensions
  - `DimensionAttributeValueCombination` — ledger dimensions
  - `DimensionStorage` — programmatic dimension manipulation
  - Merging dimensions — combining defaults
  - Creating new dimension combinations from code
- Number sequence groups — advanced numbering patterns

**HANDS-ON LAB 7.2:**
```
□ Build an extensible framework:
  - Define an extensible enum: ExpenseCalculationType
  - Create base class with SysExtension attribute
  - Create 3 implementations: PerDiem, Mileage, Percentage
  - Add a 4th type WITHOUT touching existing code
□ Add financial dimensions to your expense module:
  - Default dimension field on expense header
  - Dimension merge on posting
  - Dimension display on form
□ Create date-effective pricing table: rates that change over time
```

---

## MODULE 8: INTEGRATION — ADVANCED

### 8.1 ⭐ Advanced Integration Patterns

#### 8.1.1 Custom Services
- Custom service class — `[SysEntryPointAttribute]`
- Service operation contracts — `[DataContractAttribute]`
- Service group — deployment unit
- JSON serialization — `FormJsonSerializer`, `RetailTransactionServiceUtilities`
- SOAP vs REST — custom services support both
- Error handling in services — returning meaningful errors
- Versioning services — backward compatibility

#### 8.1.2 Business Events
- Business Event framework architecture
- Standard business events — what's available out of the box
- Creating custom business events:
  - Business Event class — `BusinessEventsBase`
  - Data Contract — what data to send with event
  - Trigger point — where to fire the event
- Business Event configuration — endpoints (Azure, Flow, HTTPS)
- Consuming business events in Power Automate
- Consuming in Azure Logic Apps
- Consuming in Azure Functions
- Business Event catalog — registering and managing

#### 8.1.3 Dual-Write & Virtual Entities
- Dual-write concept — real-time sync between F&O and Dataverse
- Dual-write maps — table mapping configuration
- Conflict resolution — last writer wins vs custom
- Initial sync — bootstrapping data
- Error handling — dual-write errors
- Virtual Entities — Dataverse sees F&O data without copying
- Virtual Entity setup — entity registration
- Virtual Entity limitations — read-only vs read-write

#### 8.1.4 Power Platform Integration Deep Dive
- Power Automate connector for D365 F&O
- Power Apps with D365 F&O data (via Virtual Entities)
- Power BI with Entity Store
- Azure Data Lake integration — Synapse Analytics
- Embedded Power Apps in D365 forms
- Embedded Power BI in workspaces

**HANDS-ON LAB 8.1:**
```
□ Create a custom service:
  - Endpoint: accepts expense data as JSON, creates records
  - Service group with 3 operations: create, update, getStatus
  - Test via Postman
□ Create a custom business event:
  - "Expense Approved" event with amount, employee, expense ID
  - Trigger when workflow approval completes
  - Consume in Power Automate — send Teams notification
□ Set up Virtual Entity for expense data
  - Build a Power App that shows pending expenses
  - Manager can approve/reject from Power App
□ Power BI dashboard:
  - Connect to expense data via OData
  - Build dashboard: spend by category, trend, approval time
  - Embed in D365 workspace
```

---

## MODULE 9: DEVOPS, ALM & DEPLOYMENT

### 9.1 ⭐ Application Lifecycle Management

#### 9.1.1 Models & Packages
- Model architecture — how code is organized
  - Model vs Package — packages contain one or more models
  - Model properties: Name, Publisher, Layer, Referenced models
  - Creating a new model — model descriptor
  - Model dependencies — referencing other models
- Package — the deployment unit
  - Standard packages: ApplicationSuite, ApplicationPlatform, ApplicationFoundation
  - ISV packages — third-party solutions
  - Customer packages — your customizations
- Separation: one model per ISV/solution

#### 9.1.2 Version Control
- Azure DevOps (TFVC or Git) for D365
- TFVC in D365 — traditional version control
  - Workspace mapping — linking AOT to TFVC
  - Check-in, check-out, shelving, merging
- Git for D365 — modern approach
- Branching strategy — Dev → Build → Release
- Code review process — pull requests
- Merge conflicts — resolving in X++/metadata

#### 9.1.3 Build Automation
- Azure DevOps build pipeline for D365
- Build VM — dedicated build environment
- Pipeline steps: Prepare → Compile → Sync → Package
- Build definition YAML/classic
- Build artifacts — deployable packages
- Automated testing in pipeline — run SysTest tests
- Build notifications — success/failure alerts

#### 9.1.4 Release & Deployment
- Deployable packages — what they contain
- Deployment via LCS — applying packages to environments
- Deployment pipeline: Dev → Build → UAT → Pre-Prod → Prod
- Package validation — automated checks
- Downtime vs Zero-downtime deployments
- Rollback strategy — reverting a deployment
- Hotfix process — emergency fixes
- Microsoft updates — staying current with platform updates

#### 9.1.5 Environment Management
- Tier-1 (Dev), Tier-2 (UAT/Test), Tier-3+ (Pre-Prod, Prod)
- Database refresh — copy prod data to sandbox
- Point-in-time restore — disaster recovery
- Data anonymization — protecting PII in non-prod
- Environment planning — how many, what for

**HANDS-ON LAB 9.1:**
```
□ Create Azure DevOps project for your expense module
□ Connect D365 dev environment to version control
□ Check in all your code — proper change sets with comments
□ Create a build pipeline:
  - Automated compile
  - Run unit tests
  - Generate deployable package
□ Deploy package to a UAT environment via LCS
□ Practice database refresh from prod to sandbox
□ Create a release pipeline: Build → UAT → manual gate → Prod
□ Simulate a hotfix: fix bug → build → deploy to prod (fast-track)
```

---

### 9.2 ⭐ Testing Framework

#### 9.2.1 SysTest (Unit Testing)
- `SysTestCase` — base class for unit tests
- `SysTestRunner` — executing tests
- Assertions: `assertEquals()`, `assertTrue()`, `assertFalse()`, `assertNotNull()`
- `SysTestTransaction` — auto-rollback after each test
- Test methods: naming convention `testMethodName()`
- Setup and teardown — `setUp()`, `tearDown()`
- Test data — creating test data in `setUp()`
- Test categories — organizing tests
- Running tests from Visual Studio
- Running tests in build pipeline

#### 9.2.2 Integration Testing
- `SysTestSuite` — grouping tests
- Form testing — automating form interactions
- End-to-end scenarios — testing complete business flows
- Mock objects — isolating dependencies
- Test data management — `SysTestDataManager`

#### 9.2.3 RSAT (Regression Suite Automation Tool)
- What is RSAT — record/playback UI testing
- Task recorder — recording test cases
- BPM library — storing test recordings
- RSAT configuration — connecting to environments
- Test execution — automated regression testing
- Test parameters — data-driven testing with Excel
- Continuous testing strategy

**HANDS-ON LAB 9.2:**
```
□ Write unit tests for your expense validation logic:
  - Test: amount must be positive
  - Test: cannot delete approved expense
  - Test: status transitions are valid
  - Test: number sequence generates properly
□ Write integration test: create expense → submit → approve → verify status
□ Use SysTestTransaction — verify auto-rollback
□ Record a RSAT test case:
  - Create expense → add lines → submit → approve
  - Parameterize with Excel data
  - Run automated regression
□ Add tests to build pipeline — fail build if tests fail
```

---

### 9.3 ⭐ Performance Optimization

#### 9.3.1 Performance Analysis
- Trace Parser — capturing and analyzing traces
  - Capturing a trace — enabling trace on environment
  - Trace analysis — finding slow methods, N+1 queries, expensive operations
  - Call tree — understanding execution flow
  - SQL analysis — finding slow queries in trace
- LCS Environment Monitoring — live performance dashboards
  - SQL insights — expensive queries
  - Batch job performance
  - User session monitoring
- SQL Server tools — query execution plans
- Performance timer — `CodePerformanceTimer`

#### 9.3.2 Common Performance Problems & Solutions
- **N+1 select problem** — select inside a loop
  - Fix: Join, exists join, or set-based operations
- **Missing indexes** — full table scans
  - Fix: Add appropriate indexes
  - How to identify: SQL execution plan, index analysis
- **Row-by-row processing** — insert/update/delete in loops
  - Fix: Set-based operations (insert_recordset, update_recordset, delete_from)
- **Over-fetching** — selecting all fields when you need 2
  - Fix: Field lists in select statements
- **Unnecessary cross-company** — scanning all legal entities
  - Fix: Scope queries to relevant companies
- **Table caching misuse** — wrong cache setting
  - Fix: Choose correct cache level per table
- **Transaction scope too large** — holding locks too long
  - Fix: Minimize code between ttsBegin and ttsCommit
- **Non-SARGable queries** — functions in WHERE clause
  - Fix: Restructure filters to be index-friendly

#### 9.3.3 Optimization Techniques
- Batch parallelism — splitting work across tasks
- `SysOperationProgress` — showing progress for long operations
- Record sets vs cursors — when to use each
- Temp tables for intermediate processing
- Asynchronous processing — fire and forget
- Caching strategies — application vs database
- Lazy loading patterns
- Paging large data sets

**HANDS-ON LAB 9.3:**
```
□ Profile your expense module with Trace Parser
  - Identify top 3 slow operations
  - Fix each one
  - Re-profile and compare
□ Create an intentionally slow operation (N+1 select with 10,000 records)
  - Measure time
  - Fix with exists join
  - Measure improvement (target: 10x faster)
□ Create a set-based alternative for a row-by-row update on 50,000 records
  - Measure: row-by-row vs set-based
□ Add a missing index — show before/after query execution time
□ Split a large batch job into parallel tasks — measure improvement
□ Optimize your expense report generation for 100,000 records
```

---

## MODULE 10: ADVANCED FUNCTIONAL AREAS

### 10.1 🔶 Financial Dimensions — Deep Dive

#### 10.1.1 Dimension Framework Architecture
- Dimension Attribute — defining dimensions (Department, CostCenter, Project)
- Dimension Attribute Value — valid values for each dimension
- Default Dimensions — `DimensionDefault` data type
  - Merging defaults — which dimension wins
  - `DimensionMerge` class — programmatic merging
- Ledger Dimensions — `RecId` to `DimensionAttributeValueCombination`
  - Account + dimensions combined
  - `DimensionDefaultingService::serviceMergeDefaultDimensions()`
- `DimensionStorage` — reading and writing dimensions programmatically
- Financial dimension on custom tables — adding dimension support
- Dimension validation — valid dimension combinations

#### 10.1.2 Adding Dimensions to Custom Module
- Add `DefaultDimension` field (EDT: `DimensionDefault`)
- Add dimension control to form
- Merge dimensions during posting
- Validate dimension combinations

### 10.2 🔶 Electronic Reporting (ER)

#### 10.2.1 ER Framework
- ER vs SSRS — when to use which
- ER components: Data Model, Format, Mapping
- ER designer — visual configuration tool
- Data sources — tables, data entities, calculated fields
- Format designer — Excel, Word, PDF, XML, JSON, Text
- Formulas and expressions in ER
- ER destinations — email, SharePoint, archive

#### 10.2.2 Building ER Reports
- Creating a data model
- Mapping data model to D365 data
- Designing output format (e.g., invoice template)
- Testing and deploying ER configurations
- Versioning ER configurations
- Importing Microsoft-provided configurations

### 10.3 🔶 Warehouse Management (Advanced)

#### 10.3.1 WMS Architecture
- Warehouse Management module overview
- Location directives — where to put/pick inventory
- Work templates — what work to create
- Wave processing — batch picking
- Mobile device — warehouse worker app
- Containerization — packing logic
- Cycle counting — inventory accuracy

### 10.4 🔶 Production & Manufacturing

#### 10.4.1 Manufacturing Basics for Developers
- Bill of Materials (BOM) — product structure
- Routes — manufacturing steps
- Production orders — manufacturing execution
- MRP (Material Requirements Planning) — demand-driven planning
- Shop floor control — tracking production
- Product configurator — configure-to-order

### 10.5 🔶 Project Management & Accounting

#### 10.5.1 Project Module
- Project types: Time & Material, Fixed Price, Internal
- Project hierarchy — projects, sub-projects, activities
- Project transactions — hours, expenses, items, fees
- Project invoicing — WIP, revenue recognition
- Project budgeting and forecasting

**HANDS-ON LAB 10.1-10.5:**
```
□ Add financial dimensions to expense module
  - DefaultDimension on expense header
  - Dimension control on form
  - Merge with vendor default dimensions on posting
□ Build an ER format: Expense claim as formatted PDF
  - Company logo, employee details, line items, totals
  - Email the PDF when expense is approved
□ Walk through WMS: configure a warehouse, create work, process via mobile
□ Walk through Manufacturing: create BOM, route, production order, report as finished
□ Walk through Project: create project, enter timesheet, expense, invoice
```

---

## MODULE 11: ARCHITECTURE & BEST PRACTICES

### 11.1 ⭐ Solution Architecture

#### 11.1.1 Designing D365 Solutions
- Fit-to-standard — use out-of-box first, customize last
- Customization vs Configuration — when to code vs configure
- Extension-only approach — ZERO overlayering
- Solution design document — what to include
- Performance considerations in design
- Scalability — designing for growth
- Multi-company architecture — shared vs company-specific data
- Localization — multi-language, multi-currency, legal requirements

#### 11.1.2 Code Quality & Standards
- Microsoft coding standards for X++
- Naming conventions — complete reference
  - Tables: `MyModuleTableName` (PascalCase)
  - EDT: `MyModuleEDTName`
  - Enum: `MyModuleEnumName`
  - Classes: `MyModuleClassName`
  - Forms: `MyModuleFormName`
  - Menu Items: `MyModuleMenuItemName`
- Best practice (BP) rules — understand each rule
- Code review checklist:
  - No hardcoded strings (use labels)
  - No hardcoded company IDs
  - Set-based operations where possible
  - Proper error handling
  - Proper transaction handling
  - Security implemented
  - Unit tests written
  - Comments on complex logic
  - No deprecated APIs
  - Extension-only (no overlayering)

#### 11.1.3 Upgrade & Servicing
- Staying current with Microsoft updates
- Upgrade impact analysis — what to test
- Deprecation notices — planning ahead
- One Version policy — no more skipping updates
- ISV solution compatibility — testing third-party

**HANDS-ON LAB 11.1:**
```
□ Review your entire expense module against coding standards checklist
□ Fix ALL best practice violations
□ Replace all hardcoded strings with labels
□ Document your solution architecture — draw diagrams for:
  - Data model (tables, relations)
  - Module structure (classes, services, workflows)
  - Integration architecture (OData, business events, Power Platform)
  - Security model (roles, duties, privileges)
□ Peer review: have someone else review your code
```

---

## MODULE 12: CERTIFICATION PREPARATION

### 12.1 ⭐ MB-500: Microsoft Dynamics 365 Finance and Operations Apps Developer

#### 12.1.1 Exam Domains
- Plan Architecture and Solution Design (5-10%)
- Apply Developer Tools (10-15%)
- Design and Develop AOT Elements (20-25%)
- Develop and Test Code (10-15%)
- Implement Reporting (10-15%)
- Plan and Implement Security (5-10%)
- Implement Data Management (10-15%)
- Implement Integrations (5-10%)

#### 12.1.2 Study Strategy
- Microsoft Learn modules — complete all MB-500 learning paths
- Practice tests — identify weak areas
- Hands-on labs — the BEST preparation
- Focus on extension model, data entities, SysOperation, security

### 12.2 🔶 MB-300: Microsoft Dynamics 365 Finance and Operations Core

#### 12.2.1 Exam Domains
- Common features and implementation tools
- Configure security, processes, and options
- Perform data migration
- Validate and support the solution

**HANDS-ON LAB 12:**
```
□ Complete ALL Microsoft Learn modules for MB-500
□ Take 3 practice exams — score 80%+
□ Identify weak areas — create targeted study plan
□ Build a FRESH mini-module from scratch in under 4 hours (exam simulation)
□ Schedule and pass MB-500
□ Then pursue MB-300 for functional knowledge
```

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FINAL CAPSTONE PROJECT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Build a Complete "Travel & Expense Management" Module

### Requirements Specification:

**Data Model:**
| Table | Purpose | Key Fields |
|-------|---------|------------|
| TravelExpensePolicy | Policies & limits | PolicyId, MaxPerDiem, MaxMileageRate, CurrencyCode |
| TravelExpenseHeader | Expense reports | ExpenseId, EmployeeId, Status, TripPurpose, DepartureDate, ReturnDate, TotalAmount |
| TravelExpenseLine | Line items | LineNum, Category, Description, Amount, Currency, TaxAmount, Receipt |
| TravelExpenseCategory | Categories | CategoryId, Name, RequiresReceipt, MaxAmount, GLAccount |
| TravelMileageRate | Mileage rates | VehicleType, RatePerMile, EffectiveDate (date-effective) |
| TravelPerDiemRate | Per diem rates | Location, MealRate, HotelRate, EffectiveDate (date-effective) |

**Business Logic:**
- Per diem auto-calculation based on travel dates and location
- Mileage auto-calculation based on miles and vehicle type
- Currency conversion for international expenses
- Policy validation: amount limits per category, receipt requirements
- Duplicate detection: flag potential duplicate expenses
- Split expense across financial dimensions

**Workflow:**
- Employee submits → Manager approves → Finance reviews (if > threshold) → Complete
- Auto-approve under $50
- Escalation after 48 hours
- Delegation support
- Email notifications at each step

**Integration:**
- Data entity for bulk import of expenses (CSV/Excel)
- OData API for mobile app
- Custom service for external travel booking system
- Business event on approval → Power Automate → Teams notification
- Virtual Entity → Power App for manager approval on mobile

**Reporting:**
- SSRS: Expense claim printout (precision design, formatted)
- SSRS: Monthly expense summary by department
- ER: Expense report as PDF for email
- Power BI: Interactive dashboard embedded in workspace

**Security:**
- Employee: Create/view own expenses, submit
- Manager: View/approve team expenses
- Finance: View all expenses, override approval, run reports
- Admin: Setup (categories, policies, rates)

**DevOps:**
- Full Azure DevOps pipeline: build, test, package
- Unit tests: minimum 20 test methods
- BP validation: zero warnings
- Documentation: solution design document

**Performance:**
- Handle 100,000 expense records without slowdown
- Set-based operations for all bulk processes
- Proper indexing verified with trace parser

---

# PROGRESS TRACKER

| Module | Level | Status | Confidence |
|--------|-------|--------|------------|
| 1. ERP & D365 Fundamentals | Basic | ⬜ | /10 |
| 2. X++ Language Basics | Basic | ⬜ | /10 |
| 3. Forms & UI Development | Intermediate | ⬜ | /10 |
| 4. Data Entities & Integration (Basic) | Intermediate | ⬜ | /10 |
| 5. Business Logic Patterns | Intermediate | ⬜ | /10 |
| 6. SSRS Reporting | Intermediate | ⬜ | /10 |
| 7. Advanced X++ & Data Access | Advanced | ⬜ | /10 |
| 8. Advanced Integration | Advanced | ⬜ | /10 |
| 9. DevOps, ALM & Deployment | Advanced | ⬜ | /10 |
| 10. Advanced Functional Areas | Advanced | ⬜ | /10 |
| 11. Architecture & Best Practices | Advanced | ⬜ | /10 |
| 12. Certification Prep | Advanced | ⬜ | /10 |
| Capstone Project | All | ⬜ | /10 |

---

*Your .NET expertise gives you a 40% head start. X++ is C# with ERP patterns. 
Focus on the domain knowledge and D365-specific frameworks — that's where the real learning curve is.
Master the 80/20 items (⭐) first. They cover 80% of real-world D365 development work.*
