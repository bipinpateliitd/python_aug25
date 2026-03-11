# CIS-DF Practice Questions

> 55 questions covering all 5 exam domains with answers and explanations.
> Sources: marks4sure, validexamdumps, dev.to, ServiceNow Community, SkillCertPro

---

## Domain 1: Configuration (15%) -- Questions 1-7

### Q1. Principal Classes Designation

A CMDB Administrator wants only Principal Classes CIs to appear in CI reference fields. Where does the administrator designate Principal Classes?

- A. CMDB Workspace
- B. CI Class Manager
- C. CMDB Data Manager
- D. System Properties

**Answer: B**

Principal Classes are designated in the **CI Class Manager**, which is the schema-level tool for controlling how CI classes appear in ITSM processes. Important: Principal Class designation does NOT inherit to child classes -- each must be set individually.

---

### Q2. Custom CI Class Roles

A new custom CI class is needed. Which roles are minimally required to add this custom class?

- A. sn_cmdb_admin and personalize_dictionary
- B. sn_cmdb_admin and personalize_form
- C. itil_admin and personalize_dictionary
- D. itil_admin and personalize_form

**Answer: A**

`sn_cmdb_admin` provides CMDB admin access, and `personalize_dictionary` is needed because adding a class involves creating/extending dictionary entries (tables and fields).

---

### Q3. Application Server to Application Relationship

A Data Center Manager defines the relationship between Application Servers and Applications they host. Multiple Application Servers host one or more Applications. Which describes this relationship?

- A. Many-to-many
- B. One-to-many
- C. Many-to-one
- D. One-to-one

**Answer: A**

Multiple servers can host multiple applications, and an application can span multiple servers. This bidirectional multiplicity = many-to-many, modeled via the `cmdb_rel_ci` relationship table.

---

### Q4. Unified Map vs Service Mapping Map

A CMDB Administrator compares the Unified Map to the Service Mapping map. What are additional capabilities of the Unified Map? (Choose Two)

- A. Number of levels displayed on a map can be modified
- B. Map can be zoomed in and out
- C. Map nodes can be filtered based on user preferences
- D. Visibility to an application and the host it is installed on

**Answer: B, C**

The Unified Map enables zoom functionality and supports filtering nodes by CI class, relationship type, lifecycle state, or user preferences -- capabilities not present in the legacy Service Mapping map.

---

### Q5. Dynamic Reconciliation Rule Types

With CMDB 360 and enabled Dynamic Reconciliation Rules, which Dynamic Rule Types are available? (Choose 2)

- A. Smallest Value
- B. Most Reported
- C. Last Updated
- D. Last Created

**Answer: B, C**

**Most Reported** selects the value reported most frequently across sources (good for stable attributes). **Last Updated** selects the most recently updated value (good for rapidly changing attributes). "Smallest Value" and "Last Created" are not valid types.

---

### Q6. CMDB 360 Saved Queries

Where can CMDB 360 / Multisource CMDB Saved Queries be viewed and created in CMDB Workspace?

- A. Coverage window on the CMDB 360 tab
- B. Saved queries window on the Insights tab
- C. CMDB Query Builder
- D. Saved queries window on the CMDB 360 tab

**Answer: D**

Saved queries for CMDB 360 are managed on the CMDB 360 tab within the Saved queries window in CMDB Workspace.

---

### Q7. IRE Processing Order

A CMDB Administrator needs to configure identification rules for a custom CI class. What is the processing order of IRE rules?

- A. Identification Rules > Reconciliation Rules > De-duplication Rules
- B. Reconciliation Rules > Identification Rules > De-duplication Rules
- C. De-duplication Rules > Identification Rules > Reconciliation Rules
- D. Identification Rules > De-duplication Rules > Reconciliation Rules

**Answer: A**

The IRE processes: (1) Identification Rules match incoming data to existing CIs, then (2) Reconciliation Rules determine source precedence for attributes, then (3) De-duplication if multiple matches were found.

---

## Domain 2: Ingest (19%) -- Questions 8-15

### Q8. Recommended Import Method Using IRE

To reduce duplicate risk and ensure IRE is not bypassed, what is the recommended method to import external data?

- A. IntegrationHub ETL
- B. Table API (REST/SOAP)
- C. Import Sets and Transform Maps

**Answer: A**

IntegrationHub ETL is natively designed to work with the IRE API, ensuring proper identification, reconciliation, and source tracking out of the box.

---

### Q9. Import Sets IRE Processing Script

When using Import Sets and Transform Maps, which script type ensures processing through the IRE?

- A. onBefore
- B. onComplete
- C. onAfter
- D. onStart

**Answer: C**

The `onAfter` transform script runs after data is mapped and prepared in the staging table, making it ready for IRE processing via the Identification and Reconciliation API.

---

### Q10. Service Graph Connector Categories

Which categories of Service Graph Connectors are available? (Choose Two)

- A. Cloud
- B. Observability
- C. DevOps
- D. Workflow Automation

**Answer: A, B**

**Cloud** connectors integrate with AWS, Azure, GCP. **Observability** connectors integrate with monitoring tools (Datadog, Dynatrace, AppDynamics). SGCs are preferred over custom Import Sets.

---

### Q11. Application Service Mapping in Change Management

An organization is changing data centers. How can Application Service Mapping be used as part of Change Management?

- A. To identify which devices will go offline first
- B. To understand the business impact of CIs
- C. To understand the physical location of CIs

**Answer: B**

Application Service Mapping maps relationships between services and infrastructure CIs, enabling **impact assessments** that show which business services would be affected by changes.

---

### Q12. Application Service Types (Drag & Drop)

Match the application service type to its description:

| Service Type | Description |
|---|---|
| Service Mapping (Top-down) | Mission-critical services discovered using patterns |
| Tag-Based | Cloud-native and container environments using cloud tags |
| Service Mapping (Connection Suggestions) | Custom-built applications using ML-based connection suggestions |
| Dynamic CI Group | Small services defined using filter-based CI grouping |

Each type addresses different scenarios: Top-down for comprehensive critical service discovery, Tag-based for cloud providers, Connection Suggestions for custom apps, Dynamic CI Groups for simple filter-based definitions.

---

### Q13. Asset CI Field Mapping

User endpoints populate "Assigned to" on the Computer CI. The Asset team needs this on the related Asset record. What action achieves this automatically?

- A. Hide the "Assigned to" field on asset and dot-walk to CI
- B. Configure a business rule script on the computer table
- C. Use the Asset CI Field Mapping module to create a new rule

**Answer: C**

The **Asset CI Field Mapping module** is the out-of-box approach for syncing field values between CI records and their related Asset records without custom scripting.

---

### Q14. Preferred Third-Party Integration Method

Which ingest method should be preferred for third-party data sources?

- A. Custom Import Sets with Transform Maps
- B. Direct Table API inserts
- C. Service Graph Connectors
- D. Manual data entry

**Answer: C**

Service Graph Connectors come with **pre-built IRE mappings certified by ServiceNow**, ensuring proper identification, reconciliation, and data source tracking.

---

### Q15. Agent Client Collector (ACC) Function

What is the primary function of ACC in CMDB data ingestion?

- A. Collect CI data from cloud providers
- B. Perform agentless network discovery
- C. Collect detailed software and hardware data from endpoints with an installed agent
- D. Integrate with third-party ITSM tools

**Answer: C**

ACC is **agent-based** discovery that installs a lightweight agent on endpoints. It provides granular data collection without needing stored admin credentials, especially useful for endpoints behind firewalls.

---

## Domain 3: Govern (35%) -- Questions 16-31

### Q16. Duplicate/Orphan/Stale CI Metrics

Which CMDB Health scorecard provides Duplicate CI, Orphan CI, and Stale CI metrics?

- A. Correctness
- B. Compliance
- C. Completeness

**Answer: A**

Duplicates, Orphans, and Stale CIs are sub-metrics of the **Correctness** scorecard. Completeness measures field population, and Compliance measures adherence to desired state audits.

> Note: Some ServiceNow documentation categorizes Stale CIs under Compliance. Be aware that exam questions may test both categorizations. The official CIS-DF blueprint places Duplicates, Orphans, and Stale under Correctness.

---

### Q17. Generating CMDB Health Scores

What needs to happen to generate CMDB health scores?

- A. Scheduled jobs for the CMDB Health Dashboard must be activated
- B. Nothing; scores are calculated by default
- C. The plugin CMDB health calculation needs installation

**Answer: A**

Health scores are generated by **scheduled calculation jobs** that are **disabled by default**. Jobs like "CSDM Get Well Metric Collection" and "CMDB Get Well Metric Collection" must be activated.

---

### Q18. CMDB Data Manager Purpose

Which is a purpose of CMDB Data Manager?

- A. Encrypts archived records for enhanced security
- B. Automates enforcement of relationship rules between CIs
- C. Automates archival and deletion of records based on retention policies

**Answer: C**

Data Manager automates the archival and deletion of records based on lifecycle conditions and retention policies, keeping the CMDB clean.

---

### Q19. Creating Data Manager Policies

Where can a CMDB Data Manager create, publish, and manage lifecycle policies?

- A. CI Class Manager
- B. CMDB Workspace - Management tab
- C. Service Operations Workspace
- D. CMDB Workspace - CMDB 360 tab

**Answer: B**

Lifecycle policies are managed in **CMDB Workspace under the Management tab**, where Data Manager provides a dedicated Policies experience.

---

### Q20. Policy Type That Creates Update Tasks

Which Data Manager policy creates tasks that allow the assigned individual to update fields on the CI record?

- A. Audit
- B. Certification
- C. Attestation
- D. Compliance

**Answer: C**

**Attestation** policies create tasks sent to CI Owners to verify data accuracy and **update fields directly** on CI records.

---

### Q21. Policy for Validating CI Existence

A Configuration Manager needs to automate task creation to validate CI existence. Which policy type?

- A. Certification
- B. Delete
- C. Retire
- D. Attestation

**Answer: A**

**Certification** validates that CIs still exist. **Attestation** validates that CI data is accurate. Key distinction:
- Certification = "Does this CI still exist?"
- Attestation = "Is this data correct?"

---

### Q22. Services Have Owners Playbook

Which remediation plays are used in the "Services Have Owners Identified" playbook? (Choose two)

- A. Govern Data
- B. Analyze Data
- C. Fix Data
- D. Report Data

**Answer: B, C**

**Analyze Data** identifies which CIs lack owner assignments. **Fix Data** performs the actual remediation by populating/correcting owner attributes.

---

### Q23. De-duplication Tasks Location

Where in CMDB Workspace can the team locate de-duplication tasks?

- A. Important actions tile under the Home tab
- B. CMDB feature adoption tile under the Insights tab
- C. Total status under the My Work tab

**Answer: C**

De-duplication tasks are under **My Work tab > Total status**, which consolidates all actionable CMDB work items.

---

### Q24. Preferred Duplicate Cleanup Approach

What is the preferred approach for cleaning up CMDB duplicates?

- A. The de-duplication dashboard on CMDB Workspace
- B. My Tasks in the Application Navigator
- C. The de-duplication task module

**Answer: A**

The **de-duplication dashboard** in CMDB Workspace centralizes duplicate identification, prioritization, and remediation with tools like De-duplication Templates (bulk) and Duplicate CI Remediator (guided).

---

### Q25. Duplicate Management Tools (Matching)

Match each feature with its outcome:

| Feature | Outcome |
|---------|---------|
| CMDB Health Dashboard - Correctness | Surfaces duplicate locations and impact |
| Certification Tasks | Enable governed resolution of duplicates |
| De-duplication Templates | Support bulk remediation of duplicates |
| Duplicate CI Remediator | Guided, record-by-record resolution preserving relationships |

---

### Q26. Missing Serial Numbers Troubleshooting

Many Hardware CIs are missing serial numbers. Which playbooks help troubleshoot this?

- A. CSDM Now Create Playbooks
- B. CMDB Health Dashboard Playbooks
- C. CMDB Data Foundations Dashboard Playbooks
- D. CSDM Data Foundations Dashboard Playbooks

**Answer: C**

**CMDB Data Foundations Dashboard Playbooks** provide structured guidance from dashboard findings to remediation for issues like missing identifiers.

---

### Q27. Dynamic CI Group Synced Groups

Which groups are synced to CIs from Technology Management Service Offerings with Dynamic CI Group relationships? (Choose 2)

- A. Approval Group
- B. Managed by Group
- C. Owned by Group
- D. Support Group

**Answer: B, D**

**Managed by Group** and **Support Group** sync from offerings to CIs, influencing operational ownership and support routing for ITSM processes.

---

### Q28. Partial Identifier Match

Two CIs imported: CI1 matches on name only; CI2 matches on IP address only. Neither matches a complete identifier entry. What happens?

- A. CI1 inserted as new; CI2 updated
- B. CI1 and CI2 both inserted as new records
- C. CI1 updated; CI2 inserted as new
- D. CI1 and CI2 both updated

**Answer: B**

IRE requires **ALL criteria within an identifier entry** to match. Partial matches (name-only or IP-only) don't satisfy any complete rule, so **both are inserted as new CIs**.

---

### Q29. IRE Multiple Match Behavior

What happens when IRE finds two matching CIs for one incoming payload?

- A. Updates both CIs
- B. Creates a de-duplication task and does not update either record
- C. Updates the CI with the most recent timestamp
- D. Rejects the incoming payload

**Answer: B**

IRE halts processing and creates a **De-duplication Task** without updating either record to prevent data corruption. An admin must manually resolve.

---

### Q30. Stale CI Health Metric Category

Which Health Dashboard metric category shows CIs not updated within a defined time period?

- A. Completeness - Required Fields
- B. Correctness - Stale CIs
- C. Correctness - Audit Results
- D. Completeness - Recommended Fields

**Answer: B**

Stale CIs fall under **Correctness** -- they haven't been updated within the configurable threshold, indicating they may no longer be accurate.

---

### Q31. CMDB Health Metrics Matching

Match the metrics to their descriptions:

| Metric | Description |
|--------|-------------|
| Audits | Validate correctness of CI data against rules |
| Duplicate CIs | Redundant records in the CMDB |
| Orphan CIs | CIs lacking required relationships to parent CIs |
| Required/Recommended Fields | Field population supporting diagnostic and governance value |
| Stale CIs | Aging data not refreshed within the threshold period |

---

## Domain 4: Insight (20%) -- Questions 32-37

### Q32. Natural Language CMDB Search

Which feature enables natural language CMDB queries?

- A. CMDB Query Builder
- B. NLQ Search (Natural Language Query)
- C. Unified Map search
- D. Global Text Search

**Answer: B**

**NLQ Search** (part of Intelligent Search) lets users query CMDB using plain English like "show me all Linux servers in the US data center."

---

### Q33. Visual CI Dependency Relationships

Which tool provides visual CI dependency relationship views?

- A. CMDB Query Builder
- B. Unified Map
- C. CMDB Data Foundations Dashboard
- D. CI Class Manager

**Answer: B**

**Unified Map** provides visual dependency views with zoom, expand upstream/downstream, and node filtering capabilities.

---

### Q34. Complex Multi-Class Queries

Which tool is most appropriate for complex queries joining multiple CI classes and relationship types?

- A. List view with filters
- B. CMDB Query Builder
- C. Unified Map
- D. Reporting module

**Answer: B**

**CMDB Query Builder** is purpose-built for complex multi-class queries with a visual interface for traversing the CMDB graph.

---

### Q35. Data Foundations Dashboard Tabs

Which dashboard provides metrics about Hardware CI serial numbers, customization levels, data management quality, and ITSM process CI usage?

- A. CMDB Health Dashboard
- B. CMDB Data Foundations Dashboard
- C. CSDM Dashboard
- D. Performance Analytics Dashboard

**Answer: B**

The **CMDB Data Foundations Dashboard** has four tabs: Hardware CIs, Customization, Data Management, and ITSM Processes.

---

### Q36. Vulnerability Response Playbook

For Vulnerability Response / Security Incident Response risk estimation, which Get Well Playbook helps?

- A. Application Services Playbook
- B. Business Services Playbook
- C. Technology Management Services Playbook
- D. Business Application Playbook

**Answer: D**

The **Business Application Playbook** ensures Business Applications have proper ownership, classification, and relationship data needed for risk estimation.

---

### Q37. Refreshing Dashboard Metrics Off-Schedule

How to populate dashboard metrics outside scheduled run time?

- A. Clear browser cache and reload
- B. Manually execute "CSDM Get Well Metric Collection" and "CMDB Get Well Metric Collection" scheduled jobs
- C. Restart the ServiceNow instance
- D. Re-install the CMDB Health plugin

**Answer: B**

Manually execute the two scheduled jobs to recalculate and refresh the metrics.

---

## Domain 5: CSDM Fundamentals (11%) -- Questions 38-45

### Q38. CSDM Domain for Production Monitoring

A Platform Owner needs to map production line monitoring systems to a CSDM domain. Which one?

- A. Build and Integration
- B. Foundation
- C. Service Consumption
- D. Design and Planning
- E. Service Delivery (Manage Technical)

**Answer: E**

Production monitoring systems operate and support services operationally, aligning with **Service Delivery (Manage Technical)**.

---

### Q39. CSDM Rollout Order

Which is the prescribed CSDM rollout order?

- A. Initial, Developing, Defined, Managed
- B. Architecture, Business, Technical, Governance
- C. Initiate, Plan, Execute, Deliver, Close
- D. Crawl, Walk, Run, Fly

**Answer: D**

**Crawl, Walk, Run, Fly** is the recommended CSDM maturity progression.

---

### Q40. CSDM Walk Stage Benefit

A customer's CMDB is at the Walk stage. What benefit is provided?

- A. Additional stratification of technical teams' support structure
- B. Improved APM Foundation implementation velocity
- C. Enables impact assessments for Incident, Problem, and Change on Business Services

**Answer: C**

At Walk, Technical Services and their relationships to Business Services enable **end-to-end impact analysis** for ITSM processes.

---

### Q41. CSDM Service Types Matching

Match service types to definitions:

| Service Type | Definition |
|---|---|
| Application Service | Models deployed applications including servers and databases |
| Technology Management Service | Shared technical capabilities managed by a technology team |
| Business Service | Published to business users; represents what the business consumes |

---

### Q42. Foundation Domain Content

Which CSDM domain contains core referential data such as locations, groups, and product models?

- A. Foundation
- B. Design and Planning
- C. Build and Integration
- D. Service Delivery

**Answer: A**

**Foundation** contains core referential data (locations, groups, companies, product models) supporting all other domains.

---

### Q43. Lifecycle Stage vs Status Relationship

In CSDM, what is the relationship between Lifecycle Stage and Lifecycle Status?

- A. They are the same field
- B. Lifecycle Stage is the macro phase; Lifecycle Status provides granular detail within a stage
- C. Lifecycle Status is the macro phase; Lifecycle Stage provides detail
- D. They are for different CI classes and never appear together

**Answer: B**

`life_cycle_stage` = macro phase (e.g., Operational). `life_cycle_stage_status` = granular detail within that phase (e.g., In Use, In Maintenance). Status is **dependent on** Stage.

---

### Q44. Independent vs Dependent CIs

What distinguishes an Independent CI from a Dependent CI?

- A. Independent CIs are physical; Dependent CIs are virtual
- B. Independent CIs can exist alone; Dependent CIs cannot exist without a parent
- C. Independent CIs have serial numbers; Dependent CIs do not
- D. Independent CIs are discovered; Dependent CIs are manually entered

**Answer: B**

Independent CIs (e.g., physical server) can exist on their own. Dependent CIs (e.g., software installation) require a parent CI relationship for identification.

---

### Q45. CSDM Domain Owners Matching

Which domain-owner pairings are correct? (Choose all correct)

- A. Foundation - Process/Product Owners
- B. Design and Planning - Enterprise Architects
- C. Build and Integration - Development Teams
- D. Service Delivery - Service Providers
- E. Service Consumption - Business Relationship Managers

**Answer: A, B, C, D, E** (All correct)

Each domain has clear ownership: Foundation (Process/Product Owners), Design (Enterprise Architects), Build (Dev Teams), Service Delivery (Service Providers), Service Consumption (BRMs).

---

## Cross-Domain Questions -- Questions 46-55

### Q46. sys_object_source Table Purpose

What is the purpose of the `sys_object_source` table?

- A. Stores all CI attributes
- B. Maps a Native Key from an external source to a ServiceNow Sys ID
- C. Contains CSDM domain mapping configuration
- D. Logs all API calls to the CMDB

**Answer: B**

`sys_object_source` is the "**Rosetta Stone**" of multisource CMDB -- it maps external Native Keys to ServiceNow Sys IDs, critical for IRE tracking and preventing duplicates.

---

### Q47. Incidents Without CI References

The CMDB Data Foundations Dashboard shows many Incidents without CI references. Which tab surfaces this?

- A. Hardware CIs
- B. Customization
- C. Data Management
- D. ITSM Processes

**Answer: D**

The **ITSM Processes** tab tracks CI usage in Incident and Change Request records, surfacing gaps where incidents aren't associated with CIs.

---

### Q48. Attestation vs Certification

What is the difference between Attestation and Certification policies?

- A. Attestation validates CI existence; Certification validates CI data accuracy
- B. Attestation validates data accuracy by having owners update fields; Certification validates CI existence
- C. They are the same policy type with different names
- D. Attestation is for hardware only; Certification is for software only

**Answer: B**

- **Attestation** = "Is this data correct?" (owners verify and update CI fields)
- **Certification** = "Does this CI still exist?" (validators confirm existence)

---

### Q49. Legacy to Lifecycle Migration

What is the recommended approach for migrating from legacy status fields to CSDM Lifecycle?

- A. Delete all legacy status values immediately
- B. Map legacy attributes to new Lifecycle Stage/Status fields using lifecycle mapping
- C. Create custom fields to replace both
- D. Maintain both systems permanently in parallel

**Answer: B**

ServiceNow provides **lifecycle mapping** functionality to translate legacy `install_status`/`operational_status` values to new Lifecycle Stage/Status fields in a controlled migration.

---

### Q50. CSDM Crawl Stage Focus

What is the primary focus during the Crawl stage?

- A. Implementing Business Services and SLA tracking
- B. Setting up Business Applications with proper ownership
- C. Configuring AI-driven governance and Business Capabilities
- D. Deploying full Service Mapping

**Answer: B**

Crawl focuses on **Business Applications** with correct ownership, classification, and basic relationships -- providing immediate value for APM.

---

### Q51. CI Class Independence Settings

Which tool helps manage and view CI class independence (Independent vs Dependent) settings?

- A. CMDB Query Builder
- B. CI Class Manager
- C. CMDB Data Manager
- D. Service Mapping

**Answer: B**

**CI Class Manager** is where administrators configure whether a class is Independent or Dependent, affecting IRE identification and lifecycle policies.

---

### Q52. AI-Assisted CMDB Quality Recommendations

Which feature provides AI-assisted recommendations for CMDB data quality?

- A. Virtual Agent
- B. Now Assist for CMDB
- C. Predictive Intelligence
- D. Performance Analytics

**Answer: B**

**Now Assist for CMDB** leverages AI to identify data issues, suggest remediation actions, and improve CMDB health.

---

### Q53. The Three Cs of CMDB Health

What are the three Cs of CMDB Health?

- A. Configuration, Compliance, Certification
- B. Completeness, Correctness, Compliance
- C. CMDB, CSDM, Configuration
- D. Crawl, Consolidate, Certify

**Answer: B**

- **Completeness** = Are required/recommended fields populated?
- **Correctness** = Is the data accurate? (duplicates, orphans, stale)
- **Compliance** = Does data meet standards? (desired state audits)

---

### Q54. Reconciliation Rules Purpose

During IRE processing, what do Reconciliation Rules do?

- A. Determine which CI class for incoming data
- B. Determine which data source takes precedence for conflicting attribute values
- C. Determine whether to create or update a CI
- D. Determine the lifecycle stage

**Answer: B**

Reconciliation Rules determine **source-of-truth precedence** when multiple sources provide different values for the same CI attribute.

---

### Q55. CMDB Central Hub

Which workspace serves as the central hub for CMDB configuration, exploration, and governance?

- A. Service Operations Workspace
- B. CMDB Workspace
- C. IT Service Management Workspace
- D. Admin Center

**Answer: B**

**CMDB Workspace** provides access to Health Dashboard, Data Manager, CMDB 360, Unified Map, de-duplication tools, and governance features in one unified interface.

---

## Domain Coverage Summary

| Domain | Weight | Questions | Count |
|--------|--------|-----------|-------|
| Configuration | 15% | Q1-Q7 | 7 |
| Ingest | 19% | Q8-Q15 | 8 |
| Govern | 35% | Q16-Q31 | 16 |
| Insight | 20% | Q32-Q37 | 6 |
| CSDM Fundamentals | 11% | Q38-Q45 | 8 |
| Cross-Domain | -- | Q46-Q55 | 10 |
| **Total** | | | **55** |
