# CIS-DF Key Concepts Study Guide

## Exam Overview

| Domain | Weight | ~Questions (of 75) |
|--------|--------|---------------------|
| **Configuration** | 15% | ~11 |
| **Ingest** | 19% | ~14 |
| **Govern** | **35%** | **~26** |
| **Insight** | 20% | ~15 |
| **CSDM Fundamentals** | 11% | ~8 |

- 75 multiple-choice questions, scenario-heavy
- Platform: Pearson VUE (physical center recommended)
- Primarily tests practical/implementation knowledge, not theory

---

## 1. Configuration (15%)

### CI Class Manager

The **centralized hub** for managing CMDB class definitions. Access requires `itil_admin` or `admin` role.

| Tab | Purpose |
|-----|---------|
| Class Hierarchy | Tree-view of all CI classes and parent-child relationships |
| Identification Rules | Configure matching criteria per class |
| Reconciliation Rules | Set data source priorities per attribute |
| Dependent Relationships | Configure hosting/dependency relationships |
| CMDB Health | View health metrics (Completeness, Correctness, Compliance) per class |
| Class Attributes | View/manage attributes on each class |

### Principal Classes

- Designated in **CI Class Manager**
- When set, the filter auto-applies to CI fields on Incident, Change, and Problem records
- **Does NOT inherit to child classes** -- each must be set individually
  - Setting "Computer" as principal does NOT make "Server" or "Windows Server" principal

### CMDB 360 / Multisource CMDB

- Provides **attribute-level tracking** of which discovery source provided which value
- Key table: `cmdb_multisource_data`
- Only populated when data flows through the **IRE** (not direct table writes)
- Key property: `glide.identification_engine.multisource_enabled = true`
- Capabilities:
  - Compare attribute values across sources side-by-side
  - See which source "won" for each attribute
  - **Recompute** CI values while excluding a specific source
  - View full history of source contributions

### Dynamic Reconciliation Rule Types

- **Most Reported** -- value reported most frequently across sources (good for stable attributes like serial_number)
- **Last Updated** -- most recently updated value (good for changing attributes like IP address)

### IRE Rules (Identification and Reconciliation Engine)

The IRE is the **gatekeeper** for all data entering the CMDB. Three phases:

#### Phase 1: Identification

1. Payload arrives via RTE, Discovery, ACC, etc. (`createOrUpdateCI()` API)
2. IRE retrieves Identifier Entries for the target CI class
3. Entries tried in **priority order** (lowest number = highest priority)
4. Each entry specifies unique attribute combinations (e.g., `serial_number + model_id`)
5. **ALL criteria** within an entry must match -- partial matches don't count

**Outcomes:**
- No match = **INSERT** (new CI)
- Exactly one match = **UPDATE** (existing CI)
- Multiple matches = **UPDATE oldest** + mark others as **duplicates** + create De-Duplication Task

After first match, the "unique key" is stored in `sys_object_source` for faster subsequent lookups.

#### Phase 2: Reconciliation

- Determines which data source "wins" for conflicting attribute values
- Rules specify: CI class, attributes, discovery sources, and priorities
- **Higher priority value = greater authority** (e.g., Discovery at 100 beats Manual at 50)
- Child class rules **override** parent class rules
- **Static** = fixed source priority; **Dynamic** = "last updated wins" or "most reported wins"

#### Phase 3: Data Refresh (Staleness)

- Defines when a CI is considered **stale** for a specific source
- Config: Discovery Source + Effective Duration (days)
- When stale, a **lower-priority** source is allowed to update the locked attributes
- Prevents outdated data when the primary source stops reporting

#### Independent vs Dependent CIs

| Type | Description | Identification |
|------|-------------|----------------|
| **Independent** | Can be uniquely identified on its own | Own attributes only (e.g., server by name) |
| **Dependent** | Requires relationship to a parent CI | Own attributes + parent relationship (e.g., Tomcat by name + host server) |

---

## 2. Ingest (19%)

### Discovery (Agentless)

- IP-based, Network, and Cloud discovery types
- Uses **MID Server** as proxy to reach target infrastructure
- Connects using stored credentials
- Discovers based on schedules, Patterns, and Credentials

### Agent Client Collector (ACC)

- **Agent-based** -- installed on Windows, Linux, macOS
- Deploys Ruby scripts with OS Query commands
- Agents send data to MID Servers **without needing credentials at runtime**
- Advantages over agentless:
  - No stored admin credentials required
  - Works behind firewalls (no firewall exceptions needed)
  - Less network bandwidth
  - Higher fidelity for Service Mapping (detects processes, ports, connections)
- Use when servers are unreachable by Horizontal Discovery

### Service Graph Connectors (SGC)

- **Pre-built integrations** from ServiceNow Store for third-party sources
- Built on top of **IntegrationHub ETL**
- Leverage IRE for data insertion -- ensuring identification & reconciliation
- **Always preferred** over custom Import Sets (pre-built IRE mappings, certified by ServiceNow)
- Categories: **Cloud** (AWS, Azure, GCP) and **Observability** (Datadog, Dynatrace, AppDynamics)
- Dependencies: Integration Commons, System Import Sets, ITOM Discovery License, IntegrationHub ETL 2.1.0

### IntegrationHub ETL (IH-ETL)

- UI-based Extract, Transform, Load tool
- Visual mapping interface for third-party sources into CMDB
- Underpins Service Graph Connectors
- Uses **Robust Transform Engine (RTE)** to pass data through IRE
- **Recommended method** to ensure IRE is not bypassed

### Import Sets & Transform Maps

- Traditional bulk data loading mechanism
- Data lands in import set staging table first, then transformed to target tables
- To ensure IRE processing, use **onAfter** transform script to call IRE API
- `sys_object_source` table = "Rosetta Stone" -- maps external Native Key to ServiceNow Sys ID

### Application Service Types

| Type | Description |
|------|-------------|
| Service Mapping (Top-down) | Mission-critical services using discovery patterns |
| Tag-Based | Cloud-native/container environments using cloud tags |
| Service Mapping (Connection Suggestions) | Custom apps using ML-based connection suggestions |
| Dynamic CI Group | Small services using filter-based CI grouping |

### Asset CI Field Mapping

- Use the **Asset CI Field Mapping module** to sync field values between CI records and related Asset records (e.g., "Assigned to" field)
- Out-of-box, supported approach -- no custom scripting needed

---

## 3. Govern (35%) -- HEAVIEST DOMAIN

### CMDB Health Dashboard -- The 3 Cs

Health jobs are **disabled by default** -- must be enabled via: All > Configuration > Health Preference.

#### Completeness (Does the data exist?)

| Sub-metric | What it checks |
|------------|----------------|
| **Required Fields** | Mandatory fields that are NOT populated |
| **Recommended Fields** | % of CIs missing recommended attributes |

#### Correctness (Is the data accurate?)

| Sub-metric | What it checks |
|------------|----------------|
| **Duplicates** | Same CI discovered multiple times. Only independent CIs evaluated. Uses identification rules. |
| **Orphan CIs** | CIs without required relationships or missing data in parent tables |
| **Stale CIs** | CIs not updated within the Effective Duration (default: 60 days). Falls under **Compliance** in some documentation. |

#### Compliance (Does the data meet standards?)

- Evaluates CIs against **Desired State audits**
- Compares actual values against expected values
- Audits for SOX, HIPAA, and other standards

> **Exam trap:** Know which sub-metrics belong to which C. Duplicates/Orphans/Stale = Correctness. Required/Recommended fields = Completeness. Audit results = Compliance.

### CMDB Data Manager -- Lifecycle Policies

Policy-driven framework for CI lifecycle operations. Managed in **CMDB Workspace > Management tab**.

| Policy Type | Purpose | Creates Tasks? |
|-------------|---------|----------------|
| **Attestation** | Verify data accuracy -- owners update CI fields | Yes -- assigned to CI owners |
| **Certification** | Verify CI existence -- does it still exist? | Yes -- assigned to validators |
| **Archive** | Move CIs to archive for historical reference | No |
| **Retire** | Mark CIs as retired in lifecycle | No |
| **Delete** | Permanently remove CIs from CMDB | No |

Key rules:
- CI limit per task: **10,000** (excess generates additional tasks)
- Attestation, Certification, and Archive require an active **Life Cycle Rule (Retirement Definition)** before publishing
- Publishing a policy creates a **scheduled job** for automated runs
- "Periodically" scheduling available for Attestation and Certification

**Attestation vs Certification:**
- Attestation = "Is this data correct?" (owners update fields)
- Certification = "Does this CI still exist?" (validators confirm existence)

### Deduplication

- De-duplication tasks generated by IRE when multiple matches found
- Also generated by a **daily scheduled job**
- Tools for resolution:
  - **De-duplication Dashboard** in CMDB Workspace (preferred)
  - **De-duplication Templates** for bulk remediation
  - **Duplicate CI Remediator** for guided record-by-record resolution
- De-dup tasks found under **My Work tab > Total status** in CMDB Workspace

### Remediation Playbooks

- Structured, prescriptive guidance from dashboard findings to resolution
- Two key plays: **Analyze Data** (identify specific CIs with issues) + **Fix Data** (remediate)
- Available from CMDB Data Foundations Dashboard

### CMDB Data Foundations Dashboard

Four tabs:

| Tab | Content |
|-----|---------|
| **Hardware CIs** | Serial numbers, adherence tracking |
| **Customization** | Custom tables, modified relationships |
| **Data Management** | CI processing, duplicates, naming gaps |
| **ITSM Processes** | Incident/Change Request CI usage |

Metrics refreshed by scheduled jobs: **"CSDM Get Well Metric Collection"** and **"CMDB Get Well Metric Collection"** -- must be manually executed for off-schedule updates.

---

## 4. Insight (20%)

### CMDB Query Builder

- Build complex multi-class queries **without code**
- Drag-and-drop CI classes and non-CMDB tables onto canvas
- Define relationship properties between nodes
- Filter on attributes, select property columns for results
- Results exportable or usable in reports

### Unified Map

- Integrates Dependency Views and Service Mapping into **one experience**
- Top-down hierarchical view of CIs and relationships
- Expand upstream/downstream from any CI
- **Zoom in/out** and **filter nodes** by CI class, relationship type, lifecycle state
- Accessed from CMDB Workspace via Quick Links

### NLQ Search (Natural Language Query)

- Query CMDB using **plain English** (e.g., "show me all Linux servers in US data center")
- No need to understand query syntax
- If query spans multiple tables, "**View in Query Builder**" button appears
- Part of CMDB Intelligent Search

### Dashboards

- CMDB Health Dashboard (3 Cs)
- CMDB Data Foundations Dashboard (4 tabs)
- CSDM Data Foundations Dashboard (Get Well Playbooks)

### Get Well Playbooks (CSDM Data Foundations Dashboard)

- **Application Services Playbook** -- Service Mapping readiness
- **Business Services Playbook** -- Service Portfolio alignment
- **Technology Management Services Playbook** -- Technical service maturity
- **Business Application Playbook** -- APM, Vulnerability/Security context

---

## 5. CSDM Fundamentals (11%)

### The 5 CSDM Domains

| # | Domain | Purpose | Key Tables | Owner |
|---|--------|---------|------------|-------|
| 1 | **Foundation** | Core reference data | Company, Location, Users, Groups, Departments, Cost Centers, Contracts, Products/Models | Process Owners, Platform Admin |
| 2 | **Design** | Strategic portfolio planning | Business Application [`cmdb_ci_business_app`], Business Capability, Information Object, Business Process | Enterprise Architects, APM |
| 3 | **Build** | Development/DevOps visibility | SDLC Components, development artifacts | Development Teams, DevOps |
| 4 | **Manage Technical** | IT Operations (Service Mapping, Discovery) | Technical Service [`cmdb_ci_service_technical`], Application Service [`cmdb_ci_service_auto`], Dynamic CI Group | IT Ops Manager, Service Owner |
| 5 | **Sell/Consume** | Business services consumed by users | Business Service [`cmdb_ci_service`], Business Service Offering, Service Portfolio | BRM, Service Portfolio Manager |

### Critical Table Distinctions

#### Business Application vs Application Service

| Aspect | Business Application | Application Service |
|--------|---------------------|---------------------|
| **Table** | `cmdb_ci_business_app` | `cmdb_ci_service_auto` |
| **Domain** | Design | Manage Technical |
| **Nature** | Conceptual/strategic (something bought or built) | Operational/deployed instance |
| **Used in ITSM?** | **NO** -- not for Incident/Problem/Change | **YES** -- what users select |
| **Multiplicity** | One per application | Multiple per BA (dev/qa/prod, per region) |
| **Example** | "SAP ERP" (the product concept) | "SAP ERP - Production - NA" |

#### Business Service vs Technical Service

| Aspect | Business Service | Technical Service |
|--------|-----------------|-------------------|
| **Table** | `cmdb_ci_service` | `cmdb_ci_service_technical` |
| **Perspective** | Customer/consumer-facing | IT operations-facing |
| **Domain** | Sell/Consume | Manage Technical |
| **Examples** | "Email", "HR Self-Service" | "Active Directory", "DNS" |

#### Other Key Tables

- **Business Capability** [`cmdb_ci_business_capability`] -- What the org needs to do (strategic)
- **Business Process** [`cmdb_ci_business_process`] -- How work gets done (sequence of activities)
- **Information Object** [`cmdb_ci_information_object`] -- Data exchanged between apps/databases

### CSDM 4.0 Lifecycle Fields

Two fields on CI records:

| Field | Purpose |
|-------|---------|
| `life_cycle_stage` | High-level phase (macro) |
| `life_cycle_stage_status` | Granular status within that phase |

**Lifecycle Stages:**

| Stage | Example Statuses |
|-------|-----------------|
| Pipeline | Planned, Proposed |
| Sandbox | Development, Testing |
| Building | Under construction |
| Pre-Production | In Testing, In Staging |
| Production/Operational | In Use, In Maintenance, End of Support |
| End of Life | Retired, Disposed, Absent |
| To Be Determined | (default when mapping can't resolve) |

**Critical rules:**
- `life_cycle_stage_status` is **dependent on** `life_cycle_stage` -- only valid statuses shown
- Values **CANNOT be customized** -- ServiceNow products depend on them
- Enabling lifecycle stages migrates from legacy fields (`install_status`, `operational_status`) via predefined mappings
- **Life Cycle Mapping** table [`life_cycle_mapping`] maps legacy → new values

### Crawl / Walk / Run / Fly Maturity Model

| Stage | Focus | Key Activities | Outcome |
|-------|-------|----------------|---------|
| **Crawl** | Build foundation | Create Business Applications with ownership; basic app-to-infra connections | APM Foundation, basic ITSM alignment |
| **Walk** | Technical depth | Add Technical Services, Technical Service Offerings, Dynamic CI Groups; Service Mapping | Impact assessments for Incident/Problem/Change on Business Services |
| **Run** | Business alignment | Create Business Services & Offerings; link business and technical layers | Service Portfolio Management; full business-IT mapping |
| **Fly** | Strategic architecture | Business Capabilities, Information Objects, Request Catalog integration | Strategic business architecture; cost optimization; digital transformation |

---

## Quick Reference: Key Exam Traps

1. **Principal Classes don't inherit** to child classes
2. **Health jobs disabled by default** -- must be activated
3. **Business Applications are NOT used in ITSM** (Incident/Problem/Change) -- Application Services are
4. **Lifecycle values cannot be customized**
5. **IRE processing order:** Identification > Reconciliation > Data Refresh
6. **onAfter** script (not onBefore) ensures IRE processing in Import Sets
7. **SGCs preferred** over custom Import Sets
8. **Attestation** = data accuracy (update fields); **Certification** = CI existence
9. **CMDB Workspace** is the central hub for everything
10. **sys_object_source** maps external Native Key to ServiceNow Sys ID

---

## Study Resources

1. [CMDB Fundamentals On Demand](https://learning.servicenow.com/lxp/en/it-operations-management/configuration-management-database-cmdb)
2. [CSDM Fundamentals On Demand](https://learning.servicenow.com/lxp/en/now-platform/common-service-data-model-csdm-fundamentals)
3. [CMDB Health Deep Dive](https://learning.servicenow.com/lxp/en/it-operations-management/cmdb-health-deep-dive)
4. [CMDB Data Foundations - Live Session](https://www.servicenow.com/community/cmdb-events/live-on-servicenow-cmdb-data-foundations-set-the-foundation-for/ec-p/3417073)
5. [Introduction to CMDB Workspace](https://learning.servicenow.com/lxp/en/pages/learning-course?id=learning_course&course_id=0924537ac31086985c1b9ab4e40131e1)
6. [CIS-DF Exam Cheat Sheet - DEV Community](https://dev.to/bren67/the-ultimate-servicenow-cis-df-data-foundations-exam-cheat-sheet-38en)
7. [CIS-DF Exam Blueprint](https://learning.servicenow.com/lxp/en/credentials/certified-implentation-specialist-data-foundations-cmdb-and?id=kb_article_view&sysparm_article=KB0012913)
