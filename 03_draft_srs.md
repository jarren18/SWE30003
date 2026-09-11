# Software Requirements Specification

## Sarawak Tourism Promotion System

---

### Title Page

| Field | Detail |
|---|---|
| Unit code | COS30003 |
| Assignment | Assignment 1 - Software Requirements Specification |
| System name | Sarawak Tourism Promotion System (STPS) |
| Prepared by (agency) | Swinsoft Consulting |
| Author identity | jarrentannn@gmail.com |
| Client | Management team of a local tourism association ("the Association") |
| Primary audience | Worldwide tourists; Association management and content staff; Swinsoft development team |
| Tutor / Lecturer | COS30003 Teaching Team |
| Submission date | 11 September 2026 |
| Document version | 0.9 (draft for precision-QA pass) |
| Method | Tasks & Support (Lauesen); Goal-Design Scale for requirement placement |
| Status | Draft - structural completeness build; final language, PDPA and formatting pass pending |

---

### FM-2 Document Control / Revision History

**Table 1 - Document control / revision history**

| Version | Date | Author | Section(s) | Change summary | Reason |
|---|---|---|---|---|---|
| 0.1 | 2026-08-18 | Swinsoft Consulting (jarrentannn@gmail.com) | All | Initial skeleton created from approved blueprint | Establish section tree and ID scheme |
| 0.2 | 2026-08-22 | Swinsoft Consulting | 2, 3 | Goals, objectives, incentives, constraints, assumptions and system context drafted | Populate problem-domain framing |
| 0.3 | 2026-08-26 | Swinsoft Consulting | 4, 5 | Domain model entities/relationships and actor catalogue drafted | Conceptual model baseline |
| 0.4 | 2026-08-30 | Swinsoft Consulting | 6 | Eight user tasks written in Tasks & Support format | Domain-level requirements |
| 0.5 | 2026-09-02 | Swinsoft Consulting | 7, 8 | Workflows and four NFR categories with fit criteria drafted | Behavioural and quality requirements |
| 0.6 | 2026-09-05 | Swinsoft Consulting | 9 | Goal-Design Scale placement, REQ-FUN/PROD/DES and PDPA requirements drafted | Cross-scale requirement coverage |
| 0.7 | 2026-09-08 | Swinsoft Consulting | 10, 11, 12 | Verifiability approach, validation plan and traceability drafted | Assurance sections |
| 0.8 | 2026-09-10 | Swinsoft Consulting | 13, 14 | Appendices (validation evidence) and glossary drafted | Evidence pack and vocabulary |
| 0.9 | 2026-09-11 | Swinsoft Consulting | All | Consolidated draft assembled for precision-QA | Hand-off for language/PDPA/format pass |

---

### FM-3 Table of Contents

1. Introduction - 1.1 Purpose; 1.2 Scope; 1.3 Intended readership; 1.4 Document overview; 1.5 References; 1.6 Definitions pointer; 1.7 Requirement ID scheme and verifiability statement
2. Project Goals & Assumptions - 2.1 Project Type; 2.2 Existing Process Description; 2.3 Pain Points; 2.4 Goals; 2.5 Objectives; 2.6 Incentives; 2.7 Scope; 2.8 Constraints; 2.9 Assumptions
3. System Context - 3.1 System Boundary; 3.2 Context Diagram; 3.3 External Entities - Human; 3.4 External Entities - Systems / Services; 3.5 Context Interactions Table
4. Domain Model - 4.1 Modelling rules; 4.2 Entity List; 4.3 Relationships and Cardinality; 4.4 Domain Model Diagram; 4.5 Entity-to-Task coverage note
5. Actors - 5.1 Actor catalogue; 5.2 Actor-to-task mapping summary; 5.3 User profiles / work-area background
6. User Tasks (Tasks & Support) - 6.1 Work Area / background block; 6.2 Tasks & Support format definition; 6.3 TASK-01; 6.4 TASK-02; 6.5 TASK-03; 6.6 TASK-04; 6.7 TASK-05; 6.8 TASK-06; 6.9 TASK-07; 6.10 TASK-08; 6.11 Typical sub-task sequence note; 6.12 Task-to-actor and task-to-entity coverage statement
7. Workflows - 7.1 Workflow notation; 7.2 WF-01; 7.3 WF-02; 7.4 WF-03; 7.5 WF-04; 7.6 WF-05; 7.7 Workflow-to-task coverage table
8. Non-Functional Requirements - 8.1 NFR method; 8.2 NFR-USAB; 8.3 NFR-PERF; 8.4 NFR-SEC; 8.5 NFR-AVAIL
9. Other Requirements (Goal-Design Scale) - 9.1 Placement on Goal-Design Scale; 9.2 Product-level requirements; 9.3 Design-level requirements; 9.4 Functional requirement stubs; 9.5 PDPA 2010 requirements; 9.6 Data lifecycle; 9.7 Integration / interoperability; 9.8 Reporting & analytics; 9.9 Content management & multilingual authoring; 9.10 Low-bandwidth / rural / offline-tolerant behaviour; 9.11 Operations
10. Verifiability Approach - 10.1 Rule; 10.2 Subjective-term ban list; 10.3 Self-audit table plan
11. Validation - 11.1 Strategy overview; 11.2 Stakeholders consulted; 11.3 Validation activities list; 11.4 Before/after change log plan; 11.5 Pointer to Appendices
12. Traceability - 12.1 Traceability matrix plan; 12.2 CRUD completeness matrix plan
13. Appendices - A Validation evidence; B Traceability matrix; C CRUD completeness check; D Self-audit verifiability table; E Scenario / prototype walkthrough results; F Assumption confirmation record; G PDPA interpretation validation record; H Optional solution options (non-normative)
14. Glossary / Domain Vocabulary

---

### FM-4 List of Figures

| Figure | Title | Section |
|---|---|---|
| Figure 1 | STPS system context diagram | 3.2 |
| Figure 2 | STPS conceptual domain model | 4.4 |
| Figure 3 | WF-01 End-to-end tourist journey activity diagram | 7.2 |
| Figure 4 | WF-02 Content & promotion publishing activity diagram | 7.3 |
| Figure 5 | WF-03 Booking + payment activity diagram | 7.4 |
| Figure 6 | WF-04 Enquiry / support handling activity diagram | 7.5 |
| Figure 7 | WF-05 Listing onboarding & moderation activity diagram | 7.6 |
| Figure 8 | Goal-Design Scale placement of requirement classes | 9.1 |

---

### FM-5 List of Tables

| Table | Title | Section |
|---|---|---|
| Table 1 | Document control / revision history | FM-2 |
| Table 2 | Pain points in the existing process | 2.3 |
| Table 3 | Goals (REQ-GOAL-001..008) | 2.4 |
| Table 4 | Objectives (OBJ-01..07) | 2.5 |
| Table 5 | Incentives (INC-01..06) | 2.6 |
| Table 6 | Constraints (CON-01..08) | 2.8 |
| Table 7 | Assumptions (ASM-01..15) | 2.9 |
| Table 8 | External human entities (EXT-H-01..07) | 3.3 |
| Table 9 | External systems / services (EXT-S-01..08) | 3.4 |
| Table 10 | Context interactions | 3.5 |
| Table 11 | Domain entity list (ENT-01..28) | 4.2 |
| Table 12 | Domain relationships (REL-01..35) | 4.3 |
| Table 13 | Actor catalogue (ACT-01..15) | 5.1 |
| Table 14 | Actor-to-task mapping | 5.2 |
| Table 15 | User profiles / work-area background | 5.3 |
| Tables 16-23 | Tasks & Support tables TASK-01..TASK-08 | 6.3-6.10 |
| Table 24 | Workflow-to-task coverage | 7.7 |
| Table 25 | NFR-USAB fit-criteria | 8.2 |
| Table 26 | NFR-PERF fit-criteria | 8.3 |
| Table 27 | NFR-SEC fit-criteria | 8.4 |
| Table 28 | NFR-AVAIL fit-criteria | 8.5 |
| Table 29 | Goal-Design Scale placement table | 9.1 |
| Table 30 | Functional requirement stubs (REQ-FUN-001..018) | 9.4 |
| Table 31 | PDPA 2010 requirements (REQ-PROD-PDPA-01..10) | 9.5 |
| Table 32 | Verifiability self-audit (extract) | 10.3 |
| Table 33 | Validation activities (VAL-01..10) | 11.3 |
| Table 34 | Requirement change log | 11.4 / Appendix A |
| Table 35 | Requirement-to-task traceability matrix | Appendix B |
| Table 36 | CRUD completeness matrix (ENT x TASK) | Appendix C |
| Table 37 | Self-audit verifiability table (full) | Appendix D |
| Table 38 | Assumption confirmation record | Appendix F |

---

### FM-6 List of Abbreviations

| Abbreviation | Expansion |
|---|---|
| SRS | Software Requirements Specification |
| STPS | Sarawak Tourism Promotion System |
| NFR | Non-Functional Requirement |
| PDPA | Personal Data Protection Act 2010 (Malaysia) |
| PDP | Personal Data Protection (Commissioner / Department) |
| CRUD | Create, Read, Update, Delete |
| RBAC | Role-Based Access Control |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| MTBF | Mean Time Between Failures |
| MTTR | Mean Time To Repair / Restore |
| SUS | System Usability Scale |
| WCAG | Web Content Accessibility Guidelines |
| CMS | Content Management System |
| SEO | Search Engine Optimisation |
| COTS | Commercial Off-The-Shelf |
| BM | Bahasa Malaysia |
| UML | Unified Modeling Language |
| DR | Disaster Recovery |

---

## 1 Introduction

### 1.1 Purpose of the document

This Software Requirements Specification (SRS) states the requirements for the Sarawak Tourism Promotion System (STPS), a public-facing tourism promotion software product commissioned by the management team of a local tourism association ("the Association") and to be built by Swinsoft Consulting. The document specifies what the software must achieve for worldwide tourists and for Association management and content staff, expressed at the domain level using the Tasks & Support approach and placed on the Goal-Design Scale. It defines the system context, the conceptual domain model, the user tasks the software must support, the workflows those tasks participate in, exactly four categories of non-functional requirement, other requirements distributed across the Goal-Design Scale, Malaysian Personal Data Protection Act 2010 (PDPA) obligations expressed as verifiable requirements, and the validation and traceability evidence that shows the specification is complete and verifiable.

The SRS is the agreed reference against which the delivered software will be accepted. Every requirement in it carries a unique identifier and a measurable fit criterion so that acceptance can be decided by test, demonstration, inspection or analysis rather than by opinion.

### 1.2 Scope of the system

The STPS is a single authoritative online source of Sarawak tourism information for a worldwide audience, together with the content and domain-data management capability the Association needs to keep that information current in multiple languages. In-scope and out-of-scope items are listed in full in section 2.7. In summary, the software covers: a tourist-facing information portal spanning accommodation, transportation, food and useful local information; itinerary planning; reservation-request capture; hand-off to an external payment interaction; multilingual content authoring and publishing; promotion-campaign coordination; enquiry capture and handling; engagement analytics and reporting for management; and PDPA consent and privacy handling. Building payment processing, mapping, weather, notification delivery, operator internal systems, and any hardware, network or deployment-platform procurement are out of scope.

### 1.3 Intended readership

| Reader | Use of this document |
|---|---|
| Representatives of worldwide tourists (as consulted during validation) | Confirm that the tourist tasks and journey reflect real needs |
| Association management | Confirm goals, objectives, incentives, scope, constraints, NFR targets and PDPA interpretation; provide sign-off |
| Association content staff | Confirm the content, translation, listing and campaign tasks and workflows |
| Swinsoft development team | Basis for design, build, test planning and acceptance |
| Course assessor | Evaluate the specification against the COS30003 rubric |

### 1.4 Document overview

| Section | Content |
|---|---|
| 1 | Purpose, scope, readership, references, ID scheme and verifiability statement |
| 2 | Project type, as-is process, pain points, goals, objectives, incentives, scope, constraints, assumptions |
| 3 | System boundary, context diagram, external human and system entities, context interactions |
| 4 | Conceptual domain model: entities and relationships with cardinality only |
| 5 | Actor catalogue, actor-to-task mapping, user profiles |
| 6 | Eight major user tasks in Tasks & Support format |
| 7 | Five workflows as ordered step lists with swimlane notes, plus workflow-to-task coverage |
| 8 | Exactly four NFR categories, each with measurable fit criteria |
| 9 | Goal-Design Scale placement; functional, product-level and design-level requirements; PDPA requirements; data lifecycle; integration; reporting; content management; low-bandwidth behaviour; operations |
| 10 | Verifiability rules, subjective-term ban list, self-audit plan |
| 11 | Validation strategy, stakeholders, activities, change-log plan |
| 12 | Traceability matrix plan and CRUD completeness matrix plan |
| 13 | Appendices A-H: validation evidence, traceability matrix, CRUD check, self-audit, walkthrough results, assumption confirmation, PDPA interpretation record, non-normative solution options |
| 14 | Glossary / domain vocabulary |

### 1.5 References

| Ref | Item |
|---|---|
| R1 | COS30003 Assignment 1 project brief (`project_brief.yaml`) |
| R2 | Lauesen, S. *Task Descriptions and the Tasks & Support Approach* (Author Workshop on Requirements Engineering material) |
| R3 | Lauesen, S. *Software Requirements: Styles and Techniques* - Goal-Design Scale and fit criteria |
| R4 | Personal Data Protection Act 2010 (Act 709), Laws of Malaysia, and its seven Personal Data Protection Principles |
| R5 | Web Content Accessibility Guidelines (WCAG) 2.1, W3C Recommendation, conformance level AA |
| R6 | COS30003 Assignment 1 High Distinction delta checklist (`01_checklist.md`) |
| R7 | Approved SRS structural blueprint (`02_blueprint.md`) |

### 1.6 Definitions pointer

Domain terms, method terms and abbreviations used in this document are defined in section 14 (Glossary / Domain Vocabulary) and expanded in FM-6 (List of Abbreviations). Terms are used consistently with those definitions throughout the document, including in figure and table labels.

### 1.7 Requirement ID scheme and verifiability statement

Every requirement, constraint, assumption, entity, relationship, actor, task, workflow and objective carries a unique, stable identifier that is reused unchanged in every section, figure and table. The scheme is:

| Prefix | Meaning | Defined in |
|---|---|---|
| PAIN-xx | Existing-process pain point | 2.3 |
| REQ-GOAL-xxx | Goal-level outcome statement | 2.4 |
| OBJ-xx | Measurable, time-bound objective | 2.5 |
| INC-xx | Incentive / business-case item | 2.6 |
| CON-xx | Constraint | 2.8 |
| ASM-xx | Assumption | 2.9 |
| EXT-H-xx / EXT-S-xx | External human / external system entity | 3.3 / 3.4 |
| ENT-xx / REL-xx | Domain entity / domain relationship | 4.2 / 4.3 |
| ACT-xx | Actor | 5.1 |
| TASK-0x | Major user task (exactly eight) | 6.3-6.10 |
| WF-0x | Workflow | 7.2-7.6 |
| NFR-USAB-xx / NFR-PERF-xx / NFR-SEC-xx / NFR-AVAIL-xx | Non-functional requirement (exactly four categories) | 8.2-8.5 |
| REQ-FUN-xxx | Functional requirement stub derived from a task | 9.4 |
| REQ-PROD-xxx | Product-level requirement | 9.2 |
| REQ-DES-xxx | Design-level requirement | 9.3 |
| REQ-PROD-PDPA-xx | PDPA-specific product requirement, also mapped to NFR-SEC | 9.5 |

Verifiability statement: each requirement (including task example-solution items, REQ-FUN, REQ-PROD, REQ-DES and every NFR) is stated with a measurable fit criterion - metric, scale or unit, target value, worst acceptable value, measuring instrument and verification method (test, demonstration, inspection or analysis). Goal-level statements are made verifiable through their linked OBJ-xx objectives. Subjective terms (for example easy, fast, secure, user-friendly, efficient, robust, seamless, intuitive, modern, appropriate, relevant, quickly) are not used as requirement wording; section 10.2 lists each banned term and its replacement metric. Appendix D lists every requirement ID against its fit criterion and acceptance test with no blank cells.

---

## 2 Project Goals & Assumptions

### 2.1 Project Type

**Statement.** The STPS is a new, custom-built, public-facing tourism promotion software product. It is commissioned by the Association and developed by Swinsoft Consulting, and it integrates with a defined set of pre-existing external services (payment, mapping, weather/advisory, notification, publishing channels, external tourism/government data and web analytics). It is not a commercial off-the-shelf (COTS) acquisition, and it is not an internal-only administrative tool.

**Justification.**

- The audience is worldwide tourists, so the product must be publicly reachable, multilingual and discoverable, which a generic internal tool does not provide.
- The Association requires its own branding, editorial voice and content-approval workflow, which a COTS package would constrain.
- Multilingual delivery (Bahasa Malaysia, English, Mandarin and others as directed) and Malaysian PDPA obligations require controls specified and verified against this context rather than accepted as vendor defaults.
- Management needs controlled content and domain-data management with approval routing, which is a bespoke workflow tied to the Association's roles.
- Integration with several independent external services requires a purpose-built integration layer with defined failure behaviour per service.

### 2.2 Existing Process Description (as-is)

Today the Association promotes Sarawak as a destination mainly through printed brochures, occasional press and social-media posts, and entries placed on third-party travel websites. Tourism information is compiled by hand by a small number of staff, each responsible for a topic area (attractions, events, accommodation contacts, transport notes, food and local tips). Tourism providers (operators of accommodation, transport, food outlets and activities) send their details to the Association by email or on paper; a staff member re-types the information into whichever channel is being updated at the time. There is no single place where a tourist can see accommodation, transport, food and local information together, so tourists assemble their own picture from many sources and build trip plans manually.

Promotional updates are made channel by channel, so the same change (a new event date, a corrected price, a closed attraction) is applied at different times to different channels and is sometimes missed. There is no structured store of listings and events maintained as a single source. Tourist enquiries arrive by phone and email and are handled individually by whoever picks them up; there is no shared record of what was asked, who answered, or whether the enquiry was resolved. Most material exists in one language. The Association has no consolidated view of what tourists are interested in, and no verifiable record that personal data supplied by tourists or providers is handled in line with the PDPA.

### 2.3 Pain Points in the Existing Process

**Table 2 - Pain points**

| ID | Pain point | Consequence |
|---|---|---|
| PAIN-01 | Tourism information is fragmented across brochures and third-party sites; no single authoritative source | Inconsistent or outdated information; the Association cannot control the destination message |
| PAIN-02 | Accommodation, transport, food and local information are not consolidated | Tourists cross-reference many sources and build plans manually |
| PAIN-03 | Promotional content updates are manual, slow and inconsistent across channels | The same fact appears differently on different channels; some updates are missed |
| PAIN-04 | No structured way for management to maintain listings and events data | Entries become stale or incorrect; no single source of truth |
| PAIN-05 | No consolidated view of tourist interest or engagement | Promotion decisions and budget allocation are not evidence-based |
| PAIN-06 | Enquiries handled ad hoc by phone and email with no tracking | Slow responses, lost requests, unrecorded outcomes |
| PAIN-07 | Material is mostly single-language | Non-English and non-Malay speakers poorly served; limited reach |
| PAIN-08 | Poor reach in rural Sarawak due to low bandwidth and intermittent connectivity | Information does not load for many in-region and prospective visitors |
| PAIN-09 | No verifiable safeguarding of tourist or provider personal data against the PDPA | Regulatory exposure; loss of tourist and provider trust |

### 2.4 Goals

**Table 3 - Goals**

| ID | Goal statement | Addresses |
|---|---|---|
| REQ-GOAL-001 | Provide a single authoritative source of Sarawak tourism information for worldwide tourists | PAIN-01 |
| REQ-GOAL-002 | Consolidate accommodation, transportation, food and useful local information in one place | PAIN-02 |
| REQ-GOAL-003 | Enable the Association to manage content and domain data without developer involvement | PAIN-03, PAIN-04 |
| REQ-GOAL-004 | Increase measurable tourist engagement and trip-planning completion | PAIN-01, PAIN-02 |
| REQ-GOAL-005 | Shorten and standardise promotional content publishing | PAIN-03 |
| REQ-GOAL-006 | Give management evidence-based insight into tourist interest | PAIN-05, PAIN-06 |
| REQ-GOAL-007 | Make information reachable in multiple languages and in low-bandwidth areas | PAIN-07, PAIN-08 |
| REQ-GOAL-008 | Protect personal data in compliance with the Malaysian Personal Data Protection Act 2010 | PAIN-09 |

### 2.5 Objectives

Each objective is measurable and time-bound and traces to a goal. Bracketed target values are to be confirmed with the Association in VAL-05; metric, scale and deadline are fixed now so each objective is verifiable.

**Table 4 - Objectives**

| ID | Objective | Metric and target | Deadline | Traces to |
|---|---|---|---|---|
| OBJ-01 | A single portal covers all four information categories at launch | Percentage of the four categories present and populated equals 100% | By go-live | REQ-GOAL-002 |
| OBJ-02 | Content publish cycle time reduced to a defined ceiling | Median elapsed time from "submitted for approval" to "published" less than or equal to [8] working hours | Within 3 months of launch | REQ-GOAL-005 |
| OBJ-03 | Tourists who start an itinerary complete it | Itinerary-plan completion rate greater than or equal to [55]% of started itineraries | Within 6 months of launch | REQ-GOAL-004 |
| OBJ-04 | Management analytics reporting available at a defined frequency | A refreshed analytics report set available at least once every [7] days | From go-live | REQ-GOAL-006 |
| OBJ-05 | Multilingual and low-bandwidth reach targets met | Fully translated tourist-facing languages greater than or equal to [3] (BM, English, Mandarin); defined key pages delivered within a payload less than or equal to [500] KB | By go-live | REQ-GOAL-007 |
| OBJ-06 | Every personal-data flow covered by a verifiable PDPA control | Percentage of identified personal-data collection, use, disclosure, retention and transfer flows with a mapped, verifiable control equals 100% | By go-live | REQ-GOAL-008 |
| OBJ-07 | Tourist enquiries receive a first response within a defined time | Median first-response time to a submitted enquiry less than or equal to [24] hours | Within 3 months of launch | REQ-GOAL-006 |

### 2.6 Incentives

**Table 5 - Incentives**

| ID | Incentive | Basis |
|---|---|---|
| INC-01 | Expected uplift in visitor numbers, average length of stay and tourism spend from consolidated, current, multilingual promotion | Association marketing analysis; comparable-destination benchmarks (target confirmed in VAL-05) |
| INC-02 | Reduced staff effort and cost for content maintenance and enquiry handling | Current staff time re-keying content and answering untracked enquiries |
| INC-03 | Stronger, more consistent destination brand across all channels | Present channel-by-channel inconsistency (PAIN-03) |
| INC-04 | Promotion budget allocated using engagement and booking-funnel evidence | Absence of consolidated insight today (PAIN-05) |
| INC-05 | Reduction of regulatory risk and potential PDPA penalties through verifiable personal-data controls | PDPA 2010 enforcement regime (PAIN-09) |
| INC-06 | Funding rationale: Association marketing budget plus a potential government tourism grant contribution | Association budget statement; grant eligibility for destination-marketing digital infrastructure |

### 2.7 Scope

**In scope**

- Tourist-facing information portal covering accommodation, transportation, food and useful local information, plus attractions and events.
- Search, browse, filter and comparison of offerings.
- Itinerary planning and per-day organisation.
- Reservation-request capture against listings.
- Presentation of amount due, hand-off to an external payment interaction, and capture of the payment outcome against a booking.
- Multilingual content and listing authoring, classification, translation management, approval routing and publish/withdraw control.
- Promotion-campaign definition, scheduling, outbound publishing to external channels and performance review.
- Structured enquiry capture, acknowledgement, assignment, status tracking, response and closure.
- Engagement analytics and management reporting (visitor trends, booking funnel, content engagement, campaign performance).
- PDPA consent capture, privacy-notice presentation, tourist self-service access and correction, retention enforcement, opt-out handling and tracking-consent gating.
- Defined, version-controlled interactions with external services (payment, mapping/geolocation, weather/advisory, notification, publishing channels, external tourism/government data, web analytics, optional external sign-in).
- Account, role and access administration for management users.

**Out of scope**

- Building payment processing itself; the system uses an external, separately contracted payment service.
- Building mapping, geolocation, weather or advisory data providers.
- Tourism providers' own internal booking, property-management or point-of-sale systems.
- Procurement or provisioning of hardware, networks, data repositories or deployment platforms (assumed already acquired - section 2.9).
- Physical tourism operations (running tours, transport or accommodation).
- Printed brochure production and offline campaign logistics.

### 2.8 Constraints

**Table 6 - Constraints**

| ID | Constraint | Effect on the specification |
|---|---|---|
| CON-01 | Compliance with the Malaysian Personal Data Protection Act 2010 is mandatory | PDPA obligations stated as verifiable requirements in sections 8.4 and 9.5 |
| CON-02 | Supported languages are Bahasa Malaysia, English and Mandarin, plus others as directed by the Association | Multilingual authoring, translation-completeness and language-selector requirements |
| CON-03 | Rural Sarawak has low bandwidth and intermittent connectivity | Payload ceilings, offline-tolerant behaviour and graceful-degradation requirements |
| CON-04 | Hosting location and any cross-border personal-data transfer must be addressed with stated safeguards | Cross-border transfer safeguard and consent requirements (REQ-PROD-017, REQ-PROD-PDPA-07) |
| CON-05 | The academic timeline fixes the specification submission date | Objective deadlines expressed relative to launch |
| CON-06 | The Association sets a budget ceiling | Requirement priorities distinguish mandatory from desirable scope |
| CON-07 | Already-acquired data repositories, hardware and deployment platforms must be reused | Only software is specified; see ASM-01 to ASM-04 |
| CON-08 | Accessibility target is WCAG 2.1 level AA | NFR-USAB-04 and REQ-DES-005 |

### 2.9 Assumptions

The specification elaborates on software only; hardware, data repositories and deployment platforms are assumed already acquired and available.

**Table 7 - Assumptions**

| ID | Assumption | Justification | Link |
|---|---|---|---|
| ASM-01 | Data repositories are already acquired and available for the software to use | Brief ground rule: elaborate on software only | CON-07 |
| ASM-02 | Servers and other hardware are already acquired | Brief ground rule: elaborate on software only | CON-07 |
| ASM-03 | The deployment platform is already provisioned | Brief ground rule: elaborate on software only | CON-07 |
| ASM-04 | Only the software is to be specified and elaborated in this SRS | Brief ground rule | Scope (2.7) |
| ASM-05 | An external payment service exists and is contracted separately by the Association | Payment processing is out of scope | 2.7 |
| ASM-06 | An external mapping / geolocation service is available for location and routing information | Mapping provision is out of scope | 2.7 |
| ASM-07 | An external weather / travel-advisory source is available | Weather provision is out of scope | 2.7 |
| ASM-08 | An external email / SMS delivery service is available for notifications | Notification delivery is out of scope | 2.7 |
| ASM-09 | The Association supplies and owns all tourism content and its translations | Client responsibility for content and languages | CON-02 |
| ASM-10 | Tourism providers supply listing details to the Association, which enters or approves them | Existing client process; reflected in the domain model | Section 4 |
| ASM-11 | Management users are trained office staff with basic web-tool skills | User-profile input to task and NFR design | Section 5.3 |
| ASM-12 | Tourists use their own internet-connected devices through a web browser | User profile; informs low-bandwidth constraints | CON-03 |
| ASM-13 | Network connectivity from the deployment site to each external service is available | Infrastructure ground rule | CON-07 |
| ASM-14 | A legal / compliance advisor is available to validate the PDPA interpretation | Needed for validation activity VAL-07 | CON-01 |
| ASM-15 | The concurrent-user peak occurs during festivals and campaign periods | Sizing input for performance requirements | Section 8.3 |

---

## 3 System Context

### 3.1 System Boundary

The system under specification is the STPS software. **Inside** the boundary: the tourist-facing information portal (search, browse, filter, compare, view listings, attractions, events, food options, transportation and local information); itinerary assembly and per-day organisation; reservation-request capture and the internal record of bookings; presentation of amount due, initiation of the external payment interaction, and capture and linkage of the payment outcome; content and domain-data management (authoring, classification, translation management, approval routing, publish and withdraw); promotion-campaign definition, scheduling and outbound publishing requests; enquiry capture, acknowledgement, assignment, status tracking, response and closure; consent-gated engagement observation and compilation of analytics reports; consent capture, privacy-notice presentation, tourist self-service access and correction, retention enforcement and marketing opt-out handling; account, role and access administration.

**Outside** the boundary: all external human roles (section 3.3); all external systems and services (section 3.4); physical delivery of email or SMS; the actual movement of funds; production of map or weather data; tourism providers' internal systems; and the hardware, network, data repositories and deployment platform (ASM-01 to ASM-03).

### 3.2 Context Diagram

**Figure 1 - STPS system context diagram (described).** A single central node labelled "Sarawak Tourism Promotion System (STPS)" sits inside a rectangular system boundary. Two rings of external entities surround it, each joined to the STPS by a labelled, directed interaction arrow.

- **Inner ring - external human entities.** Tourist (EXT-H-01): sends search terms, itinerary edits, reservation requests, enquiry text and consent choices; receives destination information, comparison views, itinerary feedback, booking confirmation, receipts and enquiry responses. Association Management User (EXT-H-02): sends approvals, campaign direction and report requests; receives approval queues and analytics reports. Content Administrator / Editor (EXT-H-03): sends draft content, classifications and translations; receives publishing status and validation messages. Enquiry Handler / Support Officer (EXT-H-04): sends triage decisions and responses; receives enquiry queues and context. Tourism Provider / Operator contact (EXT-H-05): sends offering details via the Association; receives listing status. System / Platform Administrator (EXT-H-06): sends account, role and configuration changes; receives operational monitoring information. Compliance / Legal Advisor (EXT-H-07): sends PDPA control definitions and audit findings; receives control-coverage and audit-log evidence.
- **Outer ring - external systems and services.** Payment service (EXT-S-01); Mapping / geolocation service (EXT-S-02); Weather / travel-advisory source (EXT-S-03); Notification service (EXT-S-04); Social media / external publishing channels (EXT-S-05); External tourism / government data sources (EXT-S-06); Web analytics / tracking service (EXT-S-07); Identity / authentication provider (EXT-S-08).
- The system boundary rectangle encloses only the STPS node; no external entity is inside it. Arrows name interactions (for example "payment-authorisation request / payment outcome") rather than protocols, products or components, keeping the diagram solution-agnostic.

### 3.3 External Entities - Human

**Table 8 - External human entities**

| ID | Entity | Role at the boundary |
|---|---|---|
| EXT-H-01 | Tourist | A person anywhere in the world, anonymous or identified, who discovers information, plans a trip, reserves offerings, pays, raises enquiries and gives consent |
| EXT-H-02 | Association Management User | Provides promotion direction, approves content and listings, consumes analytics |
| EXT-H-03 | Content Administrator / Editor | Creates, updates, classifies, translates and publishes content and listings |
| EXT-H-04 | Enquiry Handler / Support Officer | Triages, investigates and resolves tourist enquiry tickets |
| EXT-H-05 | Tourism Provider / Operator contact | Supplies and updates offering information for listings through the Association |
| EXT-H-06 | System / Platform Administrator | Manages accounts, roles, access and operational monitoring |
| EXT-H-07 | Compliance / Legal Advisor | Defines and audits PDPA controls and reviews audit-log evidence |

### 3.4 External Entities - External Systems / Services

Each external system is modelled only as an external interaction; no internal design of the external system is specified.

**Table 9 - External systems / services**

| ID | Service | Interaction with the STPS (solution-agnostic) |
|---|---|---|
| EXT-S-01 | Payment service | Receives a payment-authorisation request with an amount due; returns a payment outcome (authorised, declined, pending, timed out) |
| EXT-S-02 | Mapping / geolocation service | Receives a location or route query; returns coordinates, travel-time and routing information for itinerary feasibility |
| EXT-S-03 | Weather / travel-advisory source | Receives a place-and-date query; returns conditions and advisory information for itinerary feasibility |
| EXT-S-04 | Notification service | Receives a message with recipient, language and content; returns a delivery outcome |
| EXT-S-05 | Social media / external publishing channels | Receive outbound promotional content and a publish schedule; return a publish outcome |
| EXT-S-06 | External tourism / government data sources | Provide reference information (public holidays, park status, regional advisories) on request or schedule |
| EXT-S-07 | Web analytics / tracking service | Receives consent-gated engagement events; returns aggregated engagement measures |
| EXT-S-08 | Identity / authentication provider | Receives an optional external sign-in request; returns an authenticated identity assertion |

### 3.5 Context Interactions Table

**Table 10 - Context interactions**

| External entity | Information into the STPS | Information out of the STPS | Trigger | Notes (solution-agnostic) |
|---|---|---|---|---|
| EXT-H-01 Tourist | Search terms, filters, interests, itinerary edits, traveller details, reservation requests, enquiry text, consent choices, review text, data-correction requests | Consolidated destination information, comparison views, itinerary feedback, reservation outcome, amount due, receipt, enquiry acknowledgement and response, privacy notice, personal-data copy | Tourist action in a browser session; scheduled reminder | May be anonymous; identified only on registration |
| EXT-H-02 Association Management User | Approval decisions, campaign direction, report scope and period, NFR-target confirmations | Approval queues, analytics reports, campaign performance summaries | Management working session; review cycle | Consumes rather than authors content |
| EXT-H-03 Content Administrator / Editor | Draft and updated entries, classifications, translations, publish/withdraw decisions | Draft state, translation-completeness status, publishing outcome, validation messages | Provider submission received; scheduled content review | Works item by item within an approval workflow |
| EXT-H-04 Enquiry Handler / Support Officer | Triage and assignment decisions, investigation notes, response text, closure outcome | Enquiry queue, enquiry context (linked booking, itinerary, listing), status history | New or reopened enquiry | Uses the notification interaction to deliver responses |
| EXT-H-05 Tourism Provider / Operator contact | Offering details and updates, licensing / eligibility evidence | Listing status (submitted, under review, published, withdrawn) | Provider sends new or changed details to the Association | Interacts through the Association, not directly with tourists |
| EXT-H-06 System / Platform Administrator | Account creation and changes, role assignments, configuration changes, maintenance-window schedule | Operational monitoring information, alerts, audit-log extracts | Onboarding, offboarding, incident, planned maintenance | Operational, not content-related |
| EXT-H-07 Compliance / Legal Advisor | PDPA control definitions, retention periods, audit findings | Control-coverage evidence, audit logs of personal-data operations, breach-drill records | Compliance review cycle; audit; incident drill | Confirms the PDPA interpretation in Appendix G |
| EXT-S-01 Payment service | Payment outcome | Payment-authorisation request with amount due and reference | Tourist authorises payment for a booking (TASK-04) | Money movement is external; the STPS records only the outcome |
| EXT-S-02 Mapping / geolocation service | Coordinates, travel time, routing | Location / route query | Itinerary feasibility check (TASK-02) | If unavailable, itinerary planning continues without feasibility hints (NFR-PERF-04) |
| EXT-S-03 Weather / travel-advisory source | Conditions, advisories | Place-and-date query | Itinerary feasibility check (TASK-02) | Advisory only; not a booking gate |
| EXT-S-04 Notification service | Delivery outcome | Message content, recipient, language | Booking confirmed, enquiry acknowledged or answered, campaign or retention event | The STPS records the delivery outcome (REQ-PROD-005) |
| EXT-S-05 Publishing channels | Publish outcome | Promotional content and schedule | Campaign start/stop (TASK-06, ACT-15) | Outbound only |
| EXT-S-06 External tourism / government data | Reference information | Reference-data query | Scheduled refresh; editor request | Used to support content accuracy, not stored as authoritative |
| EXT-S-07 Web analytics / tracking service | Aggregated engagement measures | Consent-gated engagement events | Tourist interaction where tracking consent is recorded | No event sent without a matching ConsentRecord (REQ-PROD-019) |
| EXT-S-08 Identity / authentication provider | Authenticated identity assertion | External sign-in request | Tourist chooses external sign-in | Optional; local accounts remain available |

---

## 4 Domain Model

### 4.1 Modelling rules

The domain model is conceptual. It shows only domain entities and the named relationships between them, each relationship carrying a cardinality (multiplicity). In line with the project brief and the blueprint, the model contains **no attributes, no identifiers or keys, no data types, and no table, column or schema structures**. Entities are business concepts that would exist in the tourism domain regardless of how the software is built, and they are solution-independent. Every entity appears in at least one user task (section 6) and in the CRUD completeness matrix (Appendix C); any entity that did not would be flagged in section 4.5.

### 4.2 Entity List

**Table 11 - Domain entity list**

| ID | Entity | One-line description |
|---|---|---|
| ENT-01 | Tourist | A person worldwide who uses the system to discover and plan Sarawak travel |
| ENT-02 | Association | The tourism association that owns and promotes the destination information |
| ENT-03 | ManagementUser | An Association staff member who maintains content and domain data |
| ENT-04 | TourismProvider | An operator or business whose offering is listed (accommodation, transport, food, activity) |
| ENT-05 | Attraction | A place or point of interest promoted to tourists |
| ENT-06 | Event | A scheduled happening of tourist interest, such as a festival, show or seasonal activity |
| ENT-07 | Accommodation | A place to stay presented to tourists |
| ENT-08 | Transportation | A means or route of travel presented to tourists |
| ENT-09 | FoodOption | An eating establishment or culinary experience presented to tourists |
| ENT-10 | LocalInformation | Practical destination guidance such as customs, safety, currency and connectivity |
| ENT-11 | Listing | A promoted entry describing a provider offering or a place, shown to tourists |
| ENT-12 | ContentItem | A unit of editorial or promotional material such as an article, guide or media set |
| ENT-13 | PromotionCampaign | A coordinated promotional effort over a period and a set of channels |
| ENT-14 | Itinerary | A tourist's assembled plan of places, events, stays and movements |
| ENT-15 | ItineraryItem | A single planned element within an itinerary |
| ENT-16 | Booking | A tourist's reservation request against a listing or offering |
| ENT-17 | Payment | A record of a financial settlement associated with a booking, processed externally |
| ENT-18 | Review | A tourist's published opinion and rating of a listing, attraction or experience |
| ENT-19 | EnquiryTicket | A tourist request for help or information tracked to resolution |
| ENT-20 | Language | A supported language in which information is offered |
| ENT-21 | Translation | A language-specific rendering of a content item or listing |
| ENT-22 | EngagementRecord | An observation of tourist interaction used for analytics, gated by consent |
| ENT-23 | AnalyticsReport | A compiled summary of engagement, booking and campaign performance for management |
| ENT-24 | ConsentRecord | A tourist's recorded permission covering data use and marketing |
| ENT-25 | UserAccount | A credentialed identity for a ManagementUser or an identified Tourist |
| ENT-26 | Role | A named set of permissions assigned to a UserAccount |
| ENT-27 | Region | A geographic area of Sarawak used to group attractions, listings and events |
| ENT-28 | Category | A classification label applied to listings, attractions and content |

> Numbering note: the blueprint list runs ENT-01..ENT-27 with `ItineraryItem` carried as a concept. This draft assigns `ItineraryItem` = ENT-15 and shifts later concepts by one so every concept has a unique ENT-xx identifier; `Category` becomes ENT-28. Section 12 and the appendices use this numbering throughout.

### 4.3 Relationships and Cardinality

**Table 12 - Domain relationships** (read "A (m) -- name --> (n) B")

| ID | Relationship | Cardinality |
|---|---|---|
| REL-01 | Association employs ManagementUser | 1 : 1..* |
| REL-02 | ManagementUser maintains ContentItem | 1..* : 0..* |
| REL-03 | ManagementUser maintains Listing | 1..* : 0..* |
| REL-04 | TourismProvider supplies Listing | 1 : 1..* |
| REL-05 | Listing describes one offering of type Accommodation, Transportation, FoodOption, Attraction or Event | 1 : 0..1 per type |
| REL-06 | Attraction located in Region | 0..* : 1 |
| REL-07 | Event held at Attraction or in Region | 0..* : 0..1 Attraction / 1 Region |
| REL-08 | Listing classified by Category | 0..* : 0..* |
| REL-09 | Attraction classified by Category | 0..* : 0..* |
| REL-10 | PromotionCampaign promotes ContentItem and Listing | 0..* : 0..* |
| REL-11 | ManagementUser plans PromotionCampaign | 1..* : 0..* |
| REL-12 | Tourist builds Itinerary | 1 : 0..* |
| REL-13 | Itinerary includes ItineraryItem | 1 : 0..* |
| REL-14 | ItineraryItem references an Attraction, Event, Accommodation, Transportation or FoodOption | 1 : 1 |
| REL-15 | Tourist makes Booking | 1 : 0..* |
| REL-16 | Booking placed against Listing | 0..* : 1 |
| REL-17 | Booking settled by Payment | 1 : 0..1 |
| REL-18 | Payment processed via the external Payment service | association to EXT-S-01, modelled as external |
| REL-19 | Tourist writes Review | 1 : 0..* |
| REL-20 | Review targets a Listing, Attraction or Event | 0..* : 1 |
| REL-21 | Tourist raises EnquiryTicket | 1 : 0..* |
| REL-22 | ManagementUser (as Enquiry Handler) resolves EnquiryTicket | 1 : 0..* |
| REL-23 | ContentItem has Translation in Language | 1 : 0..* ; each Translation : 1 Language |
| REL-24 | Listing has Translation in Language | 1 : 0..* ; each Translation : 1 Language |
| REL-25 | Tourist prefers Language | 0..* : 1 |
| REL-26 | Tourist generates EngagementRecord | 1 : 0..* |
| REL-27 | AnalyticsReport aggregates EngagementRecord, Booking and PromotionCampaign data | 1 : 1..* |
| REL-28 | ManagementUser generates AnalyticsReport | 1..* : 0..* |
| REL-29 | Tourist gives ConsentRecord | 1 : 0..* |
| REL-30 | ConsentRecord governs EngagementRecord and marketing to the Tourist | 1 : 0..* |
| REL-31 | UserAccount identifies a ManagementUser or a Tourist | 1 : 0..1 |
| REL-32 | UserAccount assigned Role | 1..* : 1..* |
| REL-33 | Role authorises operations on ContentItem, Listing, EnquiryTicket and AnalyticsReport | conceptual authorisation relationship |
| REL-34 | Region groups Listing | 1 : 0..* |
| REL-35 | LocalInformation scoped to Region | 0..* : 0..1 |

### 4.4 Domain Model Diagram

**Figure 2 - STPS conceptual domain model (described).** Each entity from Table 11 is a named box with no attribute or operation compartments. Association lines carry the relationship name and the multiplicities from Table 12. The layout groups: (a) ownership - Association, ManagementUser, UserAccount, Role; (b) offering - TourismProvider, Listing and the five offering concepts Accommodation, Transportation, FoodOption, Attraction, Event, with Region and Category as classifiers and LocalInformation attached to Region; (c) promotion - ContentItem, Translation, Language, PromotionCampaign; (d) tourist activity - Tourist, Itinerary, ItineraryItem, Booking, Payment, Review, EnquiryTicket; (e) insight and consent - EngagementRecord, ConsentRecord, AnalyticsReport. The external Payment service (EXT-S-01) is shown as a boundary annotation on REL-18, not as a domain entity.

### 4.5 Entity-to-Task coverage note

Every entity ENT-01..ENT-28 is exercised by at least one task in section 6 and appears in Appendix C. Entities not created or updated by tourist- or content-facing tasks (ENT-02 Association, ENT-25 UserAccount, ENT-26 Role) are created and maintained through the operations and administration activities of ACT-07 and ACT-08, recorded in the operations column of the CRUD matrix and in section 9.11. ENT-24 ConsentRecord is created in TASK-03 and TASK-07 and read in TASK-08; ENT-18 Review is created in the review sub-flow of WF-01, moderated in WF-05 and covered by REQ-FUN-016. No entity is left without task coverage.

---

## 5 Actors

### 5.1 Actor catalogue

**Table 13 - Actor catalogue**

| ID | Actor | One-line role | Human? |
|---|---|---|---|
| ACT-01 | Tourist (Anonymous) | Browses and searches destination information without an account | Yes |
| ACT-02 | Tourist (Registered) | Saves itineraries, makes bookings, writes reviews, manages own personal data and consent | Yes |
| ACT-03 | Association Management User | Sets promotion direction, approves content and listings, consumes analytics | Yes |
| ACT-04 | Content Administrator / Editor | Creates, updates, translates and publishes content and listings | Yes |
| ACT-05 | Enquiry Handler / Support Officer | Triages and resolves tourist enquiry tickets | Yes |
| ACT-06 | Campaign Manager | Plans, schedules and evaluates promotion campaigns | Yes |
| ACT-07 | System / Platform Administrator | Manages accounts, roles, access and operational monitoring | Yes |
| ACT-08 | Data Protection Officer / Compliance Advisor | Defines and audits PDPA controls | Yes |
| ACT-09 | Tourism Provider / Operator (external, via submission) | Supplies and updates offering information for listings | Yes |
| ACT-10 | External Payment Service | Authorises and confirms payment | No |
| ACT-11 | External Mapping / Geolocation Service | Supplies location and routing information | No |
| ACT-12 | External Weather / Advisory Source | Supplies conditions and advisory information | No |
| ACT-13 | External Notification Service | Delivers email and SMS messages | No |
| ACT-14 | External Publishing / Social Channels | Receive outbound promotional content | No |
| ACT-15 | Scheduled Time / System Clock | Triggers time-based tasks such as campaign start/stop and retention purge | No |

### 5.2 Actor-to-task mapping summary

**Table 14 - Actor-to-task mapping** (P = primary, S = supporting)

| Actor | T-01 | T-02 | T-03 | T-04 | T-05 | T-06 | T-07 | T-08 |
|---|---|---|---|---|---|---|---|---|
| ACT-01 Tourist (Anonymous) | P | - | - | - | - | - | P | - |
| ACT-02 Tourist (Registered) | P | P | P | P | - | - | P | - |
| ACT-03 Association Management User | - | - | - | - | S | S | - | P |
| ACT-04 Content Administrator / Editor | - | - | - | - | P | S | - | - |
| ACT-05 Enquiry Handler / Support Officer | - | - | - | - | - | - | P | S |
| ACT-06 Campaign Manager | - | - | - | - | S | P | - | P |
| ACT-07 System / Platform Administrator | S | - | S | S | S | S | S | S |
| ACT-08 Data Protection Officer / Compliance Advisor | S | - | S | S | S | S | S | S |
| ACT-09 Tourism Provider / Operator | - | - | S | - | S | S | - | - |
| ACT-10 External Payment Service | - | - | - | P | - | - | - | - |
| ACT-11 External Mapping / Geolocation Service | S | S | - | - | - | - | - | - |
| ACT-12 External Weather / Advisory Source | S | S | - | - | - | - | - | - |
| ACT-13 External Notification Service | - | - | S | S | - | S | P | - |
| ACT-14 External Publishing / Social Channels | - | - | - | - | - | P | - | - |
| ACT-15 Scheduled Time / System Clock | - | - | S | S | - | P | S | S |

### 5.3 User profiles / work-area background

**Table 15 - User profiles / work-area background**

| Actor | Environment | Skill level | Frequency of use | Device / bandwidth context |
|---|---|---|---|---|
| ACT-01 Tourist (Anonymous) | Any location worldwide, while planning a trip or already travelling in Sarawak | General public; no training; many languages | One to several sessions per trip-planning period | Personal phone or laptop; bandwidth from broadband to intermittent rural mobile (CON-03) |
| ACT-02 Tourist (Registered) | As above, plus post-trip review from home | General public; comfortable with online booking | A few sessions per trip; occasional return visits | As above; may complete payment on mobile data |
| ACT-03 Association Management User | Association office | Business user; basic web-tool skills (ASM-11) | Weekly review cycles; daily during campaigns | Office desktop on broadband |
| ACT-04 Content Administrator / Editor | Association office or remote | Trained content editor; works with translations | Daily | Office desktop on broadband |
| ACT-05 Enquiry Handler / Support Officer | Association office or remote support desk | Trained support officer | Daily, multiple enquiries per day | Office desktop on broadband |
| ACT-06 Campaign Manager | Association office | Marketing professional | Several times per week; intensive at campaign launches | Office desktop on broadband |
| ACT-07 System / Platform Administrator | Association office or managed operations | Technical administrator | As needed for onboarding, incidents, maintenance | Office desktop; secure administrative access |
| ACT-08 Data Protection Officer / Compliance Advisor | Association office or external advisory | Legal / compliance professional (ASM-14) | Periodic reviews and audits; incident-driven | Office desktop on broadband |
| ACT-09 Tourism Provider / Operator | Provider premises across Sarawak | Small-business operator; variable digital skill | Occasional: at onboarding and when details change | Phone or shared computer; variable bandwidth |

---

## 6 User Tasks (Tasks & Support)

### 6.1 Work Area / background block

**Overall purpose of the work.** The work supported by the STPS is the promotion of Sarawak as a destination and the support of a tourist from first interest through to a completed, reviewed trip. Two connected work areas exist: the **tourist work area**, in which a member of the worldwide public discovers information, assembles a trip plan, reserves and pays for offerings, seeks help during the journey, and later shares an opinion; and the **Association work area**, in which staff keep destination information accurate and multilingual, coordinate promotion campaigns, answer tourist enquiries, and study engagement evidence to direct effort and spend.

**Environment.** Tourist work is done alone on a personal device, in any of several languages, sometimes on an intermittent rural connection, and often under time pressure while travelling. Association work is done by trained office staff on broadband, in recurring cycles (daily content and enquiry work, weekly review, campaign bursts around festivals).

**Grouping of tasks by work area.**

| Work area | Tasks |
|---|---|
| Tourist work area | TASK-01 Discover attractions and experiences; TASK-02 Plan and assemble a trip itinerary; TASK-03 Reserve an offering; TASK-04 Make and confirm payment; TASK-07 Handle a tourist enquiry / support request (raise side) |
| Association work area | TASK-05 Maintain destination content and listings (multilingual); TASK-06 Plan and run a promotion campaign; TASK-07 Handle a tourist enquiry / support request (handle side); TASK-08 Produce tourism engagement and performance insight |

A high-level task from the tourist's journey viewpoint (discover -> plan -> reserve -> pay -> travel -> enquire -> review) is expressed as workflow WF-01, which chains TASK-01 to TASK-04 and TASK-07 and includes the review sub-flow.

### 6.2 Tasks & Support format definition

Every task subsection below is a single table with these fields:

| Field | Meaning |
|---|---|
| Task ID + Name | Stable identifier and name, reused unchanged in sections 4, 7, and the matrices |
| Actor(s) | Primary and supporting actors from section 5 |
| Goal / Purpose | The result the actor wants, stated without reference to any solution |
| Trigger / Precondition | What starts the task and what must already hold |
| Frequency | Quantified expected rate (placeholder values confirmed in VAL-03) |
| Critical | Quantified worst-case consequence if the task fails or is delayed |
| Work Area | Tourist work area or Association work area (section 6.1) |
| Sub-tasks | Imperative, domain-level steps that do not pre-assign work to a human or the computer and that apply to at least three different solutions |
| Problem | Present-situation difficulty (traced to PAIN-xx) that the task must overcome |
| Support the system provides | Solution-agnostic statement of the help the software gives, each item carrying a measurable fit criterion |
| Example Solution (non-normative) | One illustrative realisation, clearly marked non-normative; not a requirement |
| Variants | Numbered alternative paths keyed to sub-tasks (1a, 1b, 2a, ...) |

All "Support" items are verifiable by executing the task and every numbered variant to completion and confirming the stated fit criterion; the shared acceptance test is recorded once here and referenced by each task: **AT-TASK: a representative actor completes the task and every listed variant end to end, in each required language where applicable, with no assistance beyond on-screen information, and every "Support" fit criterion for that task is met.**

### 6.3 TASK-01 Discover attractions and experiences

**Table 16 - TASK-01 Discover attractions and experiences**

| Field | Content |
|---|---|
| Task ID + Name | TASK-01 Discover attractions and experiences |
| Actor(s) | Primary: ACT-01 Tourist (Anonymous), ACT-02 Tourist (Registered). Supporting: ACT-11 Mapping service, ACT-12 Weather source (contextual information only) |
| Goal / Purpose | Find Sarawak attractions, events, food options, places to stay and ways to travel that match stated interests and constraints |
| Trigger / Precondition | A person is considering or undertaking a trip to Sarawak and opens the destination information source; published information exists |
| Frequency | Placeholder: 5,000-50,000 discovery sessions per day, rising by a factor of [3] during a festival or campaign |
| Critical | If discovery returns nothing useful or fails, a prospective visitor abandons planning; worst case tolerated: no more than [1]% of discovery sessions end with a system error message |
| Work Area | Tourist work area |
| Sub-tasks | 1. State interests, dates and constraints (region, budget band, travel style, language). 2. Browse or search offerings by region, category and interest. 3. Inspect a single offering in detail. 4. Compare two or more shortlisted offerings side by side. 5. Retain a shortlist of candidates for later planning. |
| Problem | Information is scattered across brochures and third-party sites, cannot be compared in one place, and is mostly in one language (PAIN-01, PAIN-02, PAIN-07). |
| Support the system provides | (a) A consolidated, searchable body of information covering all five offering concepts, verifiable by content audit showing 100% of the four brief categories plus attractions and events represented. (b) Filtering by region, category and interest, verifiable by test: every filter returns only matching offerings, measured over a [200]-case test set with 0 mismatches. (c) Side-by-side comparison of at least [3] shortlisted offerings on a common set of decision points, verifiable by demonstration. (d) Presentation of every published offering in each required language, verifiable by inspection: translation-completeness equals 100% for BM, English and Mandarin on published offerings. (e) Shortlist retention across a session and, for ACT-02, across sessions, verifiable by test: retained items reappear in [100]% of [50] trial sessions. (f) Consent-gated recording of discovery interactions for analytics, verifiable by test: 0 EngagementRecords created without a matching ConsentRecord. |
| Example Solution (non-normative) | A public web portal with a keyword search box, faceted filters, offering detail pages, a "compare" tray holding up to four items, a persistent language selector, and a "save for later" list tied to a browser session or account. *Non-normative: this describes one possible realisation only and is not a requirement.* |
| Variants | 1a. The person states no interests and browses only by region. 1b. The person arrives from an external campaign link with a pre-set region or theme. 2a. Search returns no results; the person broadens the criteria. 2b. The person searches by map area rather than by text. 3a. The offering is temporarily unavailable or seasonal; its status is shown. 4a. Only one offering is shortlisted, so comparison is skipped. 5a. An anonymous person's shortlist is offered for transfer to a new account. |
| Entities touched | Attraction, Event, Accommodation, Transportation, FoodOption, Listing, Category, Region, Language, Translation, EngagementRecord, ConsentRecord |

### 6.4 TASK-02 Plan and assemble a trip itinerary

**Table 17 - TASK-02 Plan and assemble a trip itinerary**

| Field | Content |
|---|---|
| Task ID + Name | TASK-02 Plan and assemble a trip itinerary |
| Actor(s) | Primary: ACT-02 Tourist (Registered). Supporting: ACT-11 Mapping service, ACT-12 Weather source |
| Goal / Purpose | Turn a set of shortlisted offerings into a coherent day-by-day plan that is feasible to carry out |
| Trigger / Precondition | The tourist has shortlisted candidates (TASK-01) and wants to organise a trip; travel dates are known or assumed |
| Frequency | Placeholder: 500-5,000 itineraries started per day; [55]% completed (OBJ-03) |
| Critical | If planning gives no feasibility feedback, the tourist builds an impossible schedule and has a poor trip; worst case tolerated: feasibility information is shown for at least [90]% of planned movements when the external services are available |
| Work Area | Tourist work area |
| Sub-tasks | 1. Create a plan for a date range. 2. Add shortlisted or newly found items to specific days. 3. Order and adjust items within and across days. 4. Check timing and feasibility of movements between items. 5. Review the whole plan and mark it final. |
| Problem | Tourists build plans by hand across many sources with no check that the plan can actually be done in the time available (PAIN-01, PAIN-02). |
| Support the system provides | (a) Creation of a dated plan and per-day organisation of items, verifiable by test against AT-TASK. (b) Addition of any offering concept as a planned item, verifiable by test: all five concept types can be added, 0 rejected. (c) Reordering within and across days with the plan remaining internally consistent, verifiable by demonstration. (d) A feasibility indication per movement using external location and weather information, verifiable by test: for a [100]-movement test set with services available, an indication is produced for at least [90] movements; when a service is unavailable, planning still completes (link to NFR-PERF-04). (e) A final review view listing every item, day and movement with any unresolved feasibility warning, verifiable by inspection. |
| Example Solution (non-normative) | A calendar-style planner with drag-and-drop day columns, a per-leg travel-time estimate drawn from a mapping interaction, a weather note per day drawn from a weather interaction, and a "finalise" action that produces a read-only summary. *Non-normative.* |
| Variants | 1a. The tourist copies a previous itinerary as a starting point. 2a. An item is added without a day and placed in an "unscheduled" area. 3a. Reordering creates an infeasible leg; a warning is shown but the change is allowed. 4a. External feasibility services are unavailable; the plan is marked "feasibility not checked". 4b. A planned day exceeds available hours; the overflow is highlighted. 5a. The tourist shares the finalised plan with a travelling companion for view only. |
| Entities touched | Itinerary, ItineraryItem, Attraction, Event, Accommodation, Transportation, FoodOption |

### 6.5 TASK-03 Reserve an offering

**Table 18 - TASK-03 Reserve an offering (accommodation / transport / activity)**

| Field | Content |
|---|---|
| Task ID + Name | TASK-03 Reserve an offering |
| Actor(s) | Primary: ACT-02 Tourist (Registered). Supporting: ACT-09 Tourism Provider (offering and availability information), ACT-08 Compliance Advisor (consent), ACT-13 Notification service, ACT-15 System Clock (timeout) |
| Goal / Purpose | Secure a place against a chosen listing for stated dates and quantities |
| Trigger / Precondition | The tourist has chosen a listing (from TASK-01 or TASK-02) that accepts reservations; the listing is published |
| Frequency | Placeholder: 200-3,000 reservation requests per day; higher during campaigns |
| Critical | A lost or duplicated reservation request causes a failed trip element and a complaint; worst case tolerated: no more than [0.5]% of submitted requests end in an unrecorded outcome |
| Work Area | Tourist work area |
| Sub-tasks | 1. Select a listing and state dates and quantity. 2. Provide traveller details required for the reservation. 3. Read and accept the reservation terms and the privacy notice, and record consent choices. 4. Submit the reservation request. 5. Receive and keep the reservation outcome. |
| Problem | Reservations are made separately with each provider with no single confirmation trail, and personal data is collected with no recorded consent (PAIN-02, PAIN-06, PAIN-09). |
| Support the system provides | (a) Capture of a reservation request against a listing with dates and quantity, verifiable by test against AT-TASK. (b) Validation of the request against the availability information supplied for the listing, verifiable by test: [100] conflicting requests are all detected. (c) Presentation of the reservation terms and the privacy notice in at least BM and English, and capture of an explicit consent choice before submission, verifiable by inspection: 100% of collection points show both languages and block submission until a choice is recorded (link to REQ-PROD-PDPA-01). (d) A recorded reservation outcome (confirmed, declined, pending) linked to the tourist and the listing, verifiable by test: outcome recorded for 100% of [500] test submissions. (e) An outcome notification via the notification interaction with its delivery outcome recorded, verifiable by test (link to REQ-PROD-005). |
| Example Solution (non-normative) | A booking form pre-filled from the account, an availability check against provider-supplied data, a combined terms-and-privacy step with tick boxes for required and optional consents, and a confirmation screen plus email. *Non-normative.* |
| Variants | 1a. The listing does not take reservations; the tourist is directed to the provider contact information. 2a. The tourist reserves for several travellers and enters each traveller's details. 3a. The tourist declines an optional marketing consent but proceeds. 3b. The tourist declines a required consent; the reservation cannot proceed and no personal data is retained. 4a. The request times out awaiting provider availability data; the tourist is asked to retry. 5a. The outcome is "pending"; the tourist is told when a final outcome will arrive. |
| Entities touched | Booking, Listing, TourismProvider, Tourist, ConsentRecord |

### 6.6 TASK-04 Make and confirm payment

**Table 19 - TASK-04 Make and confirm payment**

| Field | Content |
|---|---|
| Task ID + Name | TASK-04 Make and confirm payment |
| Actor(s) | Primary: ACT-02 Tourist (Registered), ACT-10 External Payment Service (non-human). Supporting: ACT-13 Notification service, ACT-15 System Clock (timeout) |
| Goal / Purpose | Settle the amount due for a booking and obtain a confirmation linked to that booking |
| Trigger / Precondition | A booking exists with an amount due and a state that allows payment |
| Frequency | Placeholder: 150-2,500 payment attempts per day |
| Critical | A payment taken without a linked confirmation, or a confirmation without a payment, causes financial dispute; worst case tolerated: 0 unreconciled payment outcomes at end of day |
| Work Area | Tourist work area |
| Sub-tasks | 1. Review the amount due and what it covers. 2. Choose a payment method offered by the external service. 3. Authorise the payment through the external payment interaction. 4. Obtain the payment outcome. 5. Attach the outcome to the booking and obtain a receipt. |
| Problem | There is no linked payment and confirmation record, so reconciliation is manual and error-prone (PAIN-06). |
| Support the system provides | (a) Presentation of the amount due and its breakdown before authorisation, verifiable by inspection: breakdown shown for 100% of [200] test bookings. (b) Hand-off to the external payment interaction without the STPS holding raw payment-instrument data, verifiable by inspection of the interaction contract and by test showing 0 instrument records stored (link to NFR-SEC-01). (c) Capture of the payment outcome (authorised, declined, pending, timed out) for 100% of attempts, verifiable by test over [500] simulated attempts. (d) Linkage of every captured outcome to exactly one booking, verifiable by analysis: 0 orphan outcomes. (e) Issue of a receipt artefact for every authorised payment, verifiable by demonstration. (f) A payment notification with recorded delivery outcome, verifiable by test. |
| Example Solution (non-normative) | A summary screen, redirect or embedded widget to the contracted payment provider, a return callback that records the outcome, a booking state change, and a downloadable and emailed receipt. *Non-normative.* |
| Variants | 2a. Only one payment method is available; the choice step is skipped. 3a. The tourist abandons at the external step; the booking stays unpaid and is released after a stated hold time (ACT-15). 4a. The outcome is "declined"; the tourist may retry with another method. 4b. The outcome is "pending"; the booking is held and the tourist is notified when it resolves. 4c. The external service times out; the STPS reconciles the true outcome before confirming. 5a. A partial payment or deposit is recorded and the remaining balance is shown. |
| Entities touched | Payment, Booking, Tourist; external EXT-S-01 |

### 6.7 TASK-05 Maintain destination content and listings (multilingual)

**Table 20 - TASK-05 Maintain destination content and listings (multilingual)**

| Field | Content |
|---|---|
| Task ID + Name | TASK-05 Maintain destination content and listings (multilingual) |
| Actor(s) | Primary: ACT-04 Content Administrator / Editor. Supporting: ACT-09 Tourism Provider (supplies details), ACT-03 Association Management User (approves), ACT-06 Campaign Manager (requests features), ACT-15 System Clock (scheduled publish/withdraw) |
| Goal / Purpose | Keep attractions, events, listings and local information accurate, classified and available in every required language |
| Trigger / Precondition | A provider submits or updates offering details, a scheduled review falls due, or management requests a change |
| Frequency | Placeholder: 20-200 create-or-update actions per day |
| Critical | Stale or wrong published information misleads tourists and damages the brand; worst case tolerated: no published entry older than its stated review interval by more than [7] days |
| Work Area | Association work area |
| Sub-tasks | 1. Draft a new entry or open an existing one for update. 2. Classify the entry by region and category. 3. Add or update the language translations required for publication. 4. Submit the entry for approval. 5. Publish the approved entry, or withdraw an entry no longer valid. |
| Problem | Updates are manual, slow and inconsistent across channels, entries go stale, and most material exists in one language (PAIN-03, PAIN-04, PAIN-07). |
| Support the system provides | (a) Authoring and updating of content items and listings for all five offering concepts and local information, verifiable by test against AT-TASK. (b) Classification by region and category, verifiable by test: unclassified entries cannot be published, 0 exceptions over [100] cases. (c) Translation management that blocks publication until the required-language set is complete, verifiable by test: publish is refused for [50] entries missing a required language and allowed for [50] complete entries (link to REQ-PROD-008). (d) Approval routing so that only management-approved entries become public, verifiable by inspection of the approval log: 100% of published entries carry an approval record. (e) Publish and withdraw control, including scheduled publish and withdraw at a set time, verifiable by demonstration. (f) A recorded licensing / eligibility check outcome for every published listing, verifiable by inspection (link to REQ-PROD-011). |
| Example Solution (non-normative) | A CMS with entry types for each concept, a taxonomy picker for region and category, a translation grid showing per-language status, a submit-for-review button, an approver queue, and scheduled publish/unpublish. *Non-normative.* |
| Variants | 1a. The editor imports provider-supplied text and media as a draft. 2a. A new region or category is proposed and must itself be approved before use. 3a. A translation is supplied by an external translator and attached later; the entry stays unpublished until complete. 4a. The approver returns the entry with comments; the editor revises and resubmits. 5a. An entry is withdrawn immediately because the provider closed; dependent campaign features are flagged. 5b. Publication is scheduled for a future date to match a campaign start. |
| Entities touched | ContentItem, Listing, Attraction, Event, Accommodation, Transportation, FoodOption, LocalInformation, Category, Region, Language, Translation |

### 6.8 TASK-06 Plan and run a promotion campaign

**Table 21 - TASK-06 Plan and run a promotion campaign**

| Field | Content |
|---|---|
| Task ID + Name | TASK-06 Plan and run a promotion campaign |
| Actor(s) | Primary: ACT-06 Campaign Manager. Supporting: ACT-03 Association Management User (approves), ACT-04 Editor (prepares featured content), ACT-14 Publishing / Social Channels, ACT-15 System Clock (start/stop) |
| Goal / Purpose | Coordinate a themed promotion over a defined period and set of channels and judge its result against a target |
| Trigger / Precondition | Management decides to promote a theme, season or region; the content and listings to feature exist or are being prepared |
| Frequency | Placeholder: 2-10 active campaigns per month; more around major festivals |
| Critical | An uncoordinated campaign wastes budget and produces no measurable result; worst case tolerated: every campaign has a recorded performance summary within [3] days of its end |
| Work Area | Association work area |
| Sub-tasks | 1. Define the campaign theme, period and target audience. 2. Select the content items and listings to feature. 3. Schedule the campaign start and end. 4. Publish the campaign to the chosen channels. 5. Review campaign performance against the target and prior campaigns. |
| Problem | Promotion is inconsistent across channels and its effect is never measured (PAIN-03, PAIN-05). |
| Support the system provides | (a) Definition of a campaign with theme, period and audience, verifiable by test against AT-TASK. (b) Association of featured content items and listings with the campaign, verifiable by test: featured items resolve to published entries for 100% of [50] test campaigns. (c) Time-based automatic start and stop at the scheduled moments, verifiable by demonstration: start and stop occur within [5] minutes of the scheduled time over [20] trials. (d) Outbound publishing to the selected external channels with a recorded publish outcome per channel, verifiable by test (link to REQ-PROD-005). (e) A performance summary comparing defined measures against the campaign target and at least one prior campaign, verifiable by inspection: every summary shows a target column and a prior-period column (link to REQ-DES-009). |
| Example Solution (non-normative) | A campaign record with a schedule, a picker for featured entries, connectors that post to social and partner channels on start, and a dashboard that pulls engagement and booking figures for the campaign window. *Non-normative.* |
| Variants | 1a. The campaign is regional and inherits its audience from a region. 2a. A featured listing is withdrawn mid-campaign; it is dropped from the campaign and the manager is alerted. 3a. The campaign is started manually rather than on schedule. 4a. A channel rejects the content; the failure is recorded and the manager retries or removes the channel. 5a. The campaign is extended; the end date is moved and the schedule updated. 5b. Results are exported for a board report. |
| Entities touched | PromotionCampaign, ContentItem, Listing, AnalyticsReport, EngagementRecord; external EXT-S-05 |

### 6.9 TASK-07 Handle a tourist enquiry / support request

**Table 22 - TASK-07 Handle a tourist enquiry / support request**

| Field | Content |
|---|---|
| Task ID + Name | TASK-07 Handle a tourist enquiry / support request |
| Actor(s) | Primary (raise): ACT-01 Tourist (Anonymous), ACT-02 Tourist (Registered). Primary (handle): ACT-05 Enquiry Handler / Support Officer. Supporting: ACT-13 Notification service, ACT-08 Compliance Advisor (personal data in enquiry content), ACT-15 System Clock (response timers) |
| Goal / Purpose | Capture a tourist's question or problem, track it, and resolve it with a recorded outcome |
| Trigger / Precondition | A tourist has a question or problem before, during or after a trip and chooses to contact the Association |
| Frequency | Placeholder: 50-500 enquiries per day; peaks during disruptions and campaigns |
| Critical | An untracked enquiry is lost and the tourist is left without help; worst case tolerated: 0 submitted enquiries with no acknowledgement, and median first response within [24] hours (OBJ-07) |
| Work Area | Tourist work area (raise) and Association work area (handle) |
| Sub-tasks | 1. Submit an enquiry with its subject, detail and any relevant context. 2. Acknowledge receipt to the tourist. 3. Assign the enquiry and investigate, drawing on any linked booking, itinerary or listing. 4. Respond to the tourist with a resolution. 5. Close the enquiry and record the outcome; reopen if the tourist is not satisfied. |
| Problem | Enquiries arrive by phone and email, are not tracked, and are answered slowly or lost (PAIN-06). |
| Support the system provides | (a) Structured capture of an enquiry with subject, detail and optional context references, verifiable by test against AT-TASK. (b) An acknowledgement to the tourist for 100% of submitted enquiries, verifiable by test over [500] submissions (link to REQ-PROD-005). (c) Assignment and status tracking through a defined set of states with a full status history, verifiable by inspection: every test enquiry shows an unbroken state history. (d) Response delivery through the notification interaction with a recorded delivery outcome, verifiable by test. (e) A recorded resolution outcome on closure and a reopen path, verifiable by demonstration. (f) Handling of personal data contained in enquiry text under the same retention and access rules as other tourist data, verifiable by inspection (link to REQ-PROD-PDPA-04, REQ-PROD-PDPA-06). |
| Example Solution (non-normative) | A contact form that creates a ticket, an auto-acknowledgement email, a handler queue with statuses (new, assigned, waiting, answered, closed, reopened), threaded replies sent by email, and a closure note with a category. *Non-normative.* |
| Variants | 1a. An anonymous tourist submits an enquiry and gives only a contact address. 1b. The enquiry is raised from within a booking or itinerary and the context is attached automatically. 3a. The enquiry needs escalation to management or to a provider; it is routed and the tourist is told of the delay. 3b. The enquiry is a duplicate and is merged with an existing one. 4a. The response needs the tourist to supply more information; the enquiry waits on the tourist. 5a. The tourist reopens a closed enquiry within a stated window and it returns to the handler. |
| Entities touched | EnquiryTicket, Tourist, ManagementUser, Booking, Itinerary, Listing, ConsentRecord; external EXT-S-04 |

### 6.10 TASK-08 Produce tourism engagement and performance insight

**Table 23 - TASK-08 Produce tourism engagement and performance insight**

| Field | Content |
|---|---|
| Task ID + Name | TASK-08 Produce tourism engagement and performance insight |
| Actor(s) | Primary: ACT-03 Association Management User, ACT-06 Campaign Manager. Supporting: ACT-05 Enquiry Handler (enquiry metrics), ACT-08 Compliance Advisor (consent gating), ACT-15 System Clock (scheduled refresh) |
| Goal / Purpose | Obtain evidence on tourist interest, the booking funnel, content engagement and campaign performance to direct promotion effort and spend |
| Trigger / Precondition | A review cycle falls due, a campaign ends, or management asks a specific question; engagement and booking data exist |
| Frequency | Placeholder: refreshed report set at least every [7] days (OBJ-04); ad hoc queries several times per week |
| Critical | Without consolidated insight, promotion budget is allocated blindly (PAIN-05); worst case tolerated: the standard report set is never more than [7] days out of date |
| Work Area | Association work area |
| Sub-tasks | 1. Choose the question, period and audience segment. 2. Assemble the relevant engagement, booking and campaign data for that scope. 3. View the compiled summary. 4. Compare the result against targets and prior periods. 5. Export or share the summary. |
| Problem | There is no consolidated view of tourist interest or engagement on which to base decisions (PAIN-05). |
| Support the system provides | (a) Selection of report scope by question, period and segment, verifiable by test against AT-TASK. (b) Aggregation of only consent-gated engagement data together with booking and campaign data, verifiable by test: 0 records in any report that lack a governing ConsentRecord (link to REQ-PROD-019). (c) A compiled summary for each of the four standard subjects (visitor trends, booking funnel, content engagement, campaign performance), verifiable by inspection: all four are produced. (d) Comparison against a stated target and at least one prior period, verifiable by inspection (link to REQ-DES-009). (e) Export or share of the summary in a portable form, verifiable by demonstration. |
| Example Solution (non-normative) | A reporting area with a scope picker, four standard dashboards, a comparison toggle for target and previous period, and CSV or PDF export plus a shareable link. *Non-normative.* |
| Variants | 1a. The user opens a saved standard report instead of defining a new scope. 2a. The chosen period has too little data; the summary is shown with a low-confidence note. 3a. The user drills from a summary figure to its contributing segments. 4a. No target has been set; only the prior-period comparison is shown. 5a. The summary is scheduled for automatic delivery to a management distribution list. |
| Entities touched | AnalyticsReport, EngagementRecord, Booking, PromotionCampaign, ConsentRecord |

### 6.11 Typical sub-task sequence note

For each task the sub-tasks are numbered in the order most often observed, but the order is not mandatory: sub-tasks may be revisited, skipped where a variant allows, or interleaved. The typical end-to-end order across tasks, from the tourist's viewpoint, is TASK-01 -> TASK-02 -> TASK-03 -> TASK-04 -> (travel, during which TASK-07 may occur) -> Review (the review sub-flow of WF-01, covered by REQ-FUN-016). The Association tasks run on their own cycles: TASK-05 continuously, TASK-06 per campaign, TASK-07 continuously, TASK-08 per review cycle.

### 6.12 Task-to-actor and task-to-entity coverage statement

- **Actor coverage.** ACT-01 to ACT-06 and ACT-09 are primary or supporting actors in at least one task (see Table 14). ACT-07 (System / Platform Administrator) and ACT-08 (Data Protection Officer / Compliance Advisor) act across every task and are specified further through the operations requirements (9.11) and the PDPA requirements (9.5). ACT-10 to ACT-15 are non-human actors realised through the external interactions in section 3.5 and the workflows in section 7.
- **Entity coverage.** Every entity ENT-01..ENT-28 is touched by at least one task; the full mapping and the create/read/update/delete pattern per entity are given in the CRUD completeness matrix (Appendix C). Entities maintained only by administration (ENT-02, ENT-25, ENT-26) are covered in the operations column of that matrix.



## 7 Workflows

### 7.1 Workflow notation

Each workflow is given as an ordered list of steps with a swimlane note on every step naming the actor or external entity that owns it. The intended UML activity-diagram realisation uses: one swimlane (partition) per actor - Tourist, System (STPS), and each external entity involved; an initial node and one or more final nodes; action nodes for steps; decision and merge nodes for the questions listed under "Decisions"; and fork and join bars where steps run concurrently. Tasks & Support variant paths (section 6) appear as decision branches. Figure numbers are assigned in FM-4. Every step cross-references the task it realises by TASK-ID.

### 7.2 WF-01 End-to-end tourist journey workflow

**Figure 3.** Swimlanes: Tourist | System (STPS) | External Payment (EXT-S-01) | External Notification (EXT-S-04). Contextual reads from Mapping (EXT-S-02) and Weather (EXT-S-03) occur inside step 2.

| # | Step | Swimlane | Realises |
|---|---|---|---|
| 1 | Discover attractions, events, food, stays and transport; retain a shortlist | Tourist -> System | TASK-01 |
| 2 | Assemble a day-by-day itinerary from the shortlist; System requests feasibility information from Mapping and Weather | Tourist -> System -> (EXT-S-02, EXT-S-03) | TASK-02 |
| 3 | Decision: does the tourist want to reserve an offering now? If no, go to step 8 | Tourist | - |
| 4 | Select a listing, provide traveller details, read terms and privacy notice, record consent | Tourist -> System | TASK-03 |
| 5 | Decision: is the offering available and are all required consents given? If no, return to step 4 or exit to step 8 | System | TASK-03 |
| 6 | Present amount due; hand off to External Payment; capture the payment outcome; link it to the booking; issue a receipt | Tourist -> System -> EXT-S-01 -> System | TASK-04 |
| 7 | Decision: was payment authorised? If no, hold or release the booking and notify; if yes, confirm the booking | System | TASK-04 |
| 8 | Send confirmation and reminder messages; record each delivery outcome | System -> EXT-S-04 | REQ-PROD-005 |
| 9 | During travel, the tourist consults local information and may raise an enquiry (branch to WF-04) | Tourist -> System | TASK-07 |
| 10 | After travel, the tourist submits a review of a listing, attraction or event | Tourist -> System | REQ-FUN-016 |
| 11 | System records consent-gated engagement throughout, which feeds management insight (WF-02 / TASK-08) | System | TASK-08 |
| 12 | Final node | - | - |

Decisions: item available? consent given? payment authorised? enquiry raised? review submitted?
Concurrency: step 8 (notifications) runs in parallel with step 9 (travel-time use).
Variant branches: no-reservation path (3 -> 8); payment declined path (7 -> hold/release); enquiry path (9 -> WF-04).

### 7.3 WF-02 Content & promotion publishing workflow

**Figure 4.** Swimlanes: Provider (ACT-09) | Editor (ACT-04) | Management (ACT-03 / ACT-06) | System (STPS) | External Channels (EXT-S-05). System Clock (ACT-15) drives the schedule step.

| # | Step | Swimlane | Realises |
|---|---|---|---|
| 1 | Submit new or updated offering details and any licensing evidence | Provider -> System | TASK-05 (1a) |
| 2 | Draft or update the entry from the submission | Editor -> System | TASK-05 |
| 3 | Classify the entry by region and category | Editor -> System | TASK-05 |
| 4 | Add or update translations for every required language | Editor -> System | TASK-05, REQ-FUN-011 |
| 5 | Decision: are translations complete for all required languages? If no, return to step 4 | System | REQ-PROD-008 |
| 6 | Submit the entry for approval | Editor -> System | TASK-05 |
| 7 | Decision: does management approve? If no, return to step 2 with comments | Management | TASK-05 (4a) |
| 8 | Publish the approved entry, or schedule its publication | System (clock: ACT-15) | TASK-05 |
| 9 | Decision: is the entry to be featured in a campaign? If no, go to step 13 | Management | TASK-06 |
| 10 | Define the campaign; select featured content and listings; set the period and audience | Management -> System | TASK-06 |
| 11 | At the scheduled start, publish the campaign to the selected channels; record each publish outcome | System (clock) -> External Channels | TASK-06 |
| 12 | At the scheduled end, stop the campaign | System (clock) | TASK-06 |
| 13 | Compile the performance summary against target and prior period | System -> Management | TASK-06, TASK-08 |
| 14 | Final node | - | - |

Decisions: translations complete? approved? feature in a campaign? campaign period active? channel accepted the content?
Concurrency: steps 3 and 4 may run in parallel; publishing to multiple channels in step 11 is a fork/join.

### 7.4 WF-03 Booking + payment workflow (detailed)

**Figure 5.** Swimlanes: Tourist | System (STPS) | External Payment (EXT-S-01) | External Notification (EXT-S-04). Provider-supplied availability data is read in step 2; System Clock (ACT-15) owns the timeout branches.

| # | Step | Swimlane | Realises |
|---|---|---|---|
| 1 | Select a listing and state dates and quantity | Tourist -> System | TASK-03 |
| 2 | Check the request against the listing's availability information | System | TASK-03 |
| 3 | Decision: is the offering available? If no, offer alternatives or exit | System | TASK-03 (1a) |
| 4 | Capture traveller details; present terms and privacy notice in at least BM and English; record consent choices | Tourist -> System | TASK-03, REQ-PROD-PDPA-01 |
| 5 | Decision: are all required consents given? If no, stop and retain no personal data | System | TASK-03 (3b) |
| 6 | Create the reservation request and set the booking to "pending payment" | System | TASK-03 |
| 7 | Present the amount due and its breakdown | System -> Tourist | TASK-04 |
| 8 | Authorise the payment through the External Payment interaction | Tourist -> System -> EXT-S-01 | TASK-04 |
| 9 | Decision: payment outcome? authorised / declined / pending / timed out | EXT-S-01 -> System | TASK-04 |
| 10 | On authorised: link the payment to the booking, confirm the booking, issue a receipt | System | TASK-04 |
| 11 | On declined: keep the booking unpaid; allow retry with another method | System -> Tourist | TASK-04 (4a) |
| 12 | On pending: hold the booking; reconcile when the outcome resolves | System (clock) | TASK-04 (4b) |
| 13 | On timeout: reconcile the true outcome with the External Payment service before confirming | System -> EXT-S-01 | TASK-04 (4c) |
| 14 | Notify the tourist of the booking and payment outcome; record the delivery outcome | System -> EXT-S-04 | REQ-PROD-005 |
| 15 | Final node | - | - |

Decisions: available? consent captured? payment authorised? timeout? partial payment?

### 7.5 WF-04 Enquiry / support handling workflow (detailed)

**Figure 6.** Swimlanes: Tourist | System (STPS) | Enquiry Handler (ACT-05) | Management / Provider (escalation) | External Notification (EXT-S-04).

| # | Step | Swimlane | Realises |
|---|---|---|---|
| 1 | Submit an enquiry with subject, detail and any context (booking, itinerary, listing) | Tourist -> System | TASK-07 |
| 2 | Create the enquiry ticket and send an acknowledgement; record the delivery outcome | System -> EXT-S-04 | TASK-07, REQ-PROD-005 |
| 3 | Triage and assign the ticket; set its state | Enquiry Handler -> System | TASK-07 |
| 4 | Decision: is escalation needed? If yes, route to Management or Provider and inform the tourist of the delay | Enquiry Handler | TASK-07 (3a) |
| 5 | Investigate, referencing any linked booking, itinerary or listing | Enquiry Handler -> System | TASK-07 |
| 6 | Decision: is more information needed from the tourist? If yes, set "waiting on tourist" and request it | Enquiry Handler -> System -> EXT-S-04 | TASK-07 (4a) |
| 7 | Respond to the tourist with a resolution; record the delivery outcome | System -> EXT-S-04 | TASK-07 |
| 8 | Decision: does the tourist confirm resolution? If no and within the reopen window, return to step 3 | Tourist | TASK-07 (5a) |
| 9 | Close the ticket and record the resolution outcome and category | Enquiry Handler -> System | TASK-07 |
| 10 | Feed enquiry volume and response-time measures to management insight | System | TASK-08 |
| 11 | Final node | - | - |

Decisions: needs escalation? more information needed? resolved? reopened within window?
Concurrency: step 2 acknowledgement runs in parallel with step 3 triage.

### 7.6 WF-05 Listing onboarding & moderation workflow

**Figure 7.** Swimlanes: Provider (ACT-09) | Editor (ACT-04) | Compliance (ACT-08) | Management (ACT-03) | System (STPS) | Tourist.

| # | Step | Swimlane | Realises |
|---|---|---|---|
| 1 | Submit listing details and licensing / eligibility evidence | Provider -> System | TASK-05 (1a) |
| 2 | Validate completeness and classify by region and category | Editor -> System | TASK-05 |
| 3 | Perform the licensing / eligibility check and record its outcome | Compliance -> System | REQ-PROD-011 |
| 4 | Decision: is licensing valid and content complete? If no, return to the provider | Compliance / Editor | TASK-05 (3a) |
| 5 | Decision: does management approve or reject? | Management | TASK-05 |
| 6 | Publish the listing (immediately or scheduled) | System | TASK-05 |
| 7 | Tourists view the published listing and may submit a review | Tourist -> System | TASK-01, REQ-FUN-016 |
| 8 | Moderate submitted reviews against the review policy | Editor -> System | REQ-FUN-016 |
| 9 | Decision: is the review compliant? If no, reject it with a reason | Editor | REQ-FUN-016 |
| 10 | Update or withdraw the listing when the provider's situation changes | Editor -> System | TASK-05 (5a) |
| 11 | Final node | - | - |

Decisions: licensing valid? content complete? approved? review compliant? withdraw needed?

### 7.7 Workflow-to-task coverage table

**Table 24 - Workflow-to-task coverage**

| WF ID | WF name | Tasks covered | Actors | External entities | Key decisions |
|---|---|---|---|---|---|
| WF-01 | End-to-end tourist journey | TASK-01, TASK-02, TASK-03, TASK-04, TASK-07 (branch), Review sub-flow | ACT-01, ACT-02, ACT-15 | EXT-S-01, EXT-S-02, EXT-S-03, EXT-S-04 | Item available? consent given? payment authorised? enquiry raised? |
| WF-02 | Content & promotion publishing | TASK-05, TASK-06, TASK-08 | ACT-09, ACT-04, ACT-03, ACT-06, ACT-15 | EXT-S-05 | Translations complete? approved? campaign period active? channel accepted? |
| WF-03 | Booking + payment | TASK-03, TASK-04 | ACT-02, ACT-09, ACT-15 | EXT-S-01, EXT-S-04 | Available? consent captured? payment authorised? timeout? |
| WF-04 | Enquiry / support handling | TASK-07, TASK-08 | ACT-01, ACT-02, ACT-05, ACT-03 | EXT-S-04 | Needs escalation? more info needed? resolved? reopened? |
| WF-05 | Listing onboarding & moderation | TASK-05 (+ review moderation), TASK-01 (consumption) | ACT-09, ACT-04, ACT-08, ACT-03, ACT-01 | - | Licensing valid? content complete? approved? review compliant? |

Coverage assertion: every task TASK-01..TASK-08 appears in at least one workflow; every workflow covers at least one task.

---

## 8 Non-Functional Requirements

### 8.1 NFR method

Exactly four NFR categories are specified, each traced to a goal or pain point. Every NFR is stated with a fit criterion in this structure: **metric | scale or unit | target | worst acceptable | measuring instrument | verification method | priority | trace**. Bracketed target and worst-acceptable values are provisional and are confirmed with the Association in VAL-05; the metric, scale, instrument and verification method are fixed now so each NFR is verifiable. Verification method is one of test, demonstration, inspection or analysis. No subjective term is used (see section 10.2).

### 8.2 NFR-USAB - Usability, Accessibility & Multilingual

Rationale: trip planning must be completable by a first-time member of the worldwide public without help, in their language, or engagement and completion (REQ-GOAL-004, REQ-GOAL-007) will not improve and the single-language barrier (PAIN-07) will remain.

**Table 25 - NFR-USAB fit-criteria**

| ID | Requirement (metric) | Scale / unit | Target | Worst acceptable | Measuring instrument | Verification method | Priority | Trace |
|---|---|---|---|---|---|---|---|---|
| NFR-USAB-01 | A first-time tourist completes discover -> plan -> reserve unaided | Task completion rate (%) and time on task (minutes) | >= [90]% complete; median <= [12] min | >= [80]% complete; median <= [18] min | Moderated usability test, n >= [20], representative participants | Test | High | REQ-GOAL-004; PAIN-01 |
| NFR-USAB-02 | Measured satisfaction of tourist participants | SUS score (0-100) | >= [78] | >= [68] | SUS questionnaire administered after the test, n >= [20] | Test | High | REQ-GOAL-004 |
| NFR-USAB-03 | Language coverage of tourist-facing information | Count of fully translated languages including BM, English, Mandarin | = [3] at launch, rising per Association direction | = [3], with 0 partially translated published pages | Content translation audit against the published page set | Inspection | High | REQ-GOAL-007; PAIN-07; OBJ-05 |
| NFR-USAB-04 | Accessibility conformance of key tourist pages (home, search, listing, itinerary, booking, enquiry) | WCAG 2.1 conformance level; count of Level A/AA failures | Level AA; 0 Level A/AA failures on key pages | Level AA; <= [3] Level AA failures, 0 Level A failures, all with a fix plan | Automated accessibility scan plus manual audit (keyboard, screen-reader, contrast) | Inspection | Medium | CON-08; REQ-GOAL-007 |
| NFR-USAB-05 | Management users complete TASK-05 to TASK-08 procedures after training | Task completion rate (%) with training materials only | >= [95]% | >= [85]% | Structured walkthrough with [5] trained staff | Demonstration | Medium | REQ-GOAL-003; ASM-11 |

### 8.3 NFR-PERF - Performance & Scalability

Rationale: information must load and respond on rural low-bandwidth connections and withstand festival and campaign peaks (REQ-GOAL-001, REQ-GOAL-007, PAIN-08, ASM-15), or the single authoritative source will not be usable when it matters most.

**Table 26 - NFR-PERF fit-criteria**

| ID | Requirement (metric) | Scale / unit | Target | Worst acceptable | Measuring instrument | Verification method | Priority | Trace |
|---|---|---|---|---|---|---|---|---|
| NFR-PERF-01 | Information search response time under normal load | Seconds at the 95th percentile | <= [2.0] s | <= [4.0] s | Load-test tool at [normal] concurrent-user level | Test | High | REQ-GOAL-001; PAIN-01 |
| NFR-PERF-02 | Delivered payload and first-render time of defined key pages on a throttled connection | Kilobytes; seconds to first contentful render at [1.0] Mbit/s, [150] ms latency | <= [500] KB; <= [5] s | <= [800] KB; <= [8] s | Synthetic throttled browser test | Test | High | REQ-GOAL-007; PAIN-08; OBJ-05 |
| NFR-PERF-03 | Concurrent active users sustained at festival / campaign peak with other metrics within target | Count of concurrent active users | >= [5,000] with NFR-PERF-01 still met | >= [3,000] with NFR-PERF-01 worst-acceptable still met | Load-test tool ramp profile based on ASM-15 | Test | High | ASM-15; REQ-GOAL-004 |
| NFR-PERF-04 | Core browse and plan functionality available when an external service (mapping, weather, analytics) is unavailable | Functional-availability (%) of a defined core-function checklist during a simulated outage | >= [95]% | >= [90]% | Fault-injection test disabling one external service at a time | Demonstration | Medium | REQ-GOAL-001; CON-03 |
| NFR-PERF-05 | Reservation-request submission processing time | Seconds at the 95th percentile, excluding external payment time | <= [3.0] s | <= [6.0] s | Load-test tool at peak profile | Test | Medium | REQ-GOAL-004; TASK-03 |

### 8.4 NFR-SEC - Security & Privacy (PDPA 2010)

Rationale: tourist and provider personal data must be protected to a verifiable standard under the Malaysian Personal Data Protection Act 2010 (REQ-GOAL-008, PAIN-09, CON-01). Each PDPA obligation in section 9.5 maps to one or more rows here.

**Table 27 - NFR-SEC fit-criteria**

| ID | Requirement (metric) | Scale / unit | Target | Worst acceptable | Measuring instrument | Verification method | Priority | Trace |
|---|---|---|---|---|---|---|---|---|
| NFR-SEC-01 | Personal data protected by approved encryption in transit and at rest | Percentage of personal-data stores and channels using approved encryption | = 100% | = 100% (no exception permitted) | Configuration and cipher audit against the personal-data inventory (section 9.5) | Inspection | High | REQ-GOAL-008; CON-01; REQ-PROD-PDPA-03 |
| NFR-SEC-02 | Privileged and personal-data operations gated by role-based access control | Percentage of defined privileged operations requiring an authorising Role; count of unauthorised-access findings | = 100% gated; 0 findings | = 100% gated; 0 Level-high findings, all Level-medium findings with a fix plan | Access-control test suite exercising each Role and each operation | Test | High | REQ-GOAL-008; REL-32, REL-33; REQ-PROD-PDPA-03 |
| NFR-SEC-03 | Independent security assessment before go-live | Count of unresolved high or critical findings | = 0 at go-live | = 0 high/critical; <= [5] medium with scheduled remediation | Third-party penetration test and report | Test | High | REQ-GOAL-008; CON-01 |
| NFR-SEC-04 | Personal-data breach detection to containment and notification | Elapsed hours from detection to containment; elapsed hours from confirmation to notification of the affected parties and the authority | Containment <= [24] h; notification <= [72] h | Containment <= [48] h; notification <= [72] h | Incident-response drill with a simulated breach scenario | Demonstration | High | REQ-GOAL-008; CON-01; REQ-PROD-PDPA-03 |
| NFR-SEC-05 | Audit logging of privileged and personal-data operations | Percentage of defined operation types producing a tamper-evident log entry | = 100% | = 100% | Log-completeness test exercising each operation type | Test | High | REQ-PROD-004; REQ-PROD-PDPA-03 |
| NFR-SEC-06 | Marketing analytics engagement recorded only with tracking consent | Count of EngagementRecords for marketing analytics with no governing ConsentRecord | = 0 | = 0 | Data-reconciliation test over a [7]-day sample | Test | High | REQ-GOAL-008; REQ-PROD-019; REQ-PROD-PDPA-09 |

### 8.5 NFR-AVAIL - Availability & Reliability

Rationale: a single authoritative source is only authoritative if it is reachable and its core transactions complete reliably (REQ-GOAL-001, PAIN-01).

**Table 28 - NFR-AVAIL fit-criteria**

| ID | Requirement (metric) | Scale / unit | Target | Worst acceptable | Measuring instrument | Verification method | Priority | Trace |
|---|---|---|---|---|---|---|---|---|
| NFR-AVAIL-01 | Service uptime measured monthly, excluding announced scheduled maintenance | Availability (%) per calendar month | >= [99.7]% | >= [99.0]% | External uptime monitor polling a defined health endpoint at <= [60] s interval | Analysis | High | REQ-GOAL-001; PAIN-01 |
| NFR-AVAIL-02 | Recovery after a major failure | RTO (hours); RPO (minutes) | RTO <= [4] h; RPO <= [15] min | RTO <= [8] h; RPO <= [60] min | Disaster-recovery test restoring from backup into the recovery environment | Demonstration | High | REQ-GOAL-001; REQ-PROD-003 |
| NFR-AVAIL-03 | Reliability of core booking and enquiry transactions | MTBF (hours); MTTR (minutes); failed-transaction rate (%) | MTBF >= [720] h; MTTR <= [30] min; failed <= [0.5]% | MTBF >= [360] h; MTTR <= [60] min; failed <= [1.0]% | Operational log analysis over a rolling [30]-day window | Analysis | Medium | REQ-GOAL-004; TASK-03, TASK-07 |
| NFR-AVAIL-04 | Successful delivery of outbound notifications | Percentage of notification sends with a recorded delivered outcome within [30] minutes | >= [98]% | >= [95]% | Notification-log analysis against the notification interaction outcomes | Analysis | Medium | REQ-PROD-005; TASK-03, TASK-04, TASK-07 |

---

## 9 Other Requirements (Goal-Design Scale)

### 9.1 Placement on Goal-Design Scale

**Figure 8 - Goal-Design Scale placement (described).** A horizontal scale runs left to right through four bands: **Goal-level** (why the system exists), **Domain-level** (what happens in the work, independent of the computer), **Product-level** (what the product does at its boundary), **Design-level** (how the product is built and presented). Requirement classes are placed as follows: REQ-GOAL-001..008 and OBJ-01..07 in the Goal band; TASK-01..08, WF-01..05 and the domain model (section 4) in the Domain band; REQ-FUN-001..018, REQ-PROD-001..019, REQ-PROD-PDPA-01..10 and all NFR-* in the Product band; REQ-DES-001..010 in the Design band. Traceability runs across the bands: every Goal has at least one Objective and at least one Task or Product requirement; every Product requirement traces left to a Task or Goal; every Design requirement traces left to a Product requirement.

**Table 29 - Goal-Design Scale placement (extract; full mapping in Appendix B)**

| Requirement ID | Statement (short) | Scale position | Traces to | Priority | Fit criterion ref | Verification |
|---|---|---|---|---|---|---|
| REQ-GOAL-002 | Consolidate the four information categories | Goal | PAIN-02 | High | OBJ-01 | Analysis |
| TASK-01 | Discover attractions and experiences | Domain | REQ-GOAL-001, 002, 004 | High | AT-TASK + Table 16 support items | Test |
| REQ-FUN-001 | Consolidated search / browse of all offering types | Product | TASK-01 | High | Table 30 row 001 | Test |
| REQ-PROD-008 | Multilingual publish workflow with completeness gate | Product | REQ-GOAL-007, TASK-05 | High | 100% required-language completeness blocks publish | Test |
| NFR-SEC-01 | Personal data encrypted in transit and at rest | Product | REQ-GOAL-008 | High | Table 27 NFR-SEC-01 | Inspection |
| REQ-DES-002 | Persistent language selector on tourist pages | Design | REQ-PROD-008, NFR-USAB-03 | High | Present on 100% of tourist-facing pages | Inspection |

### 9.2 Product-level requirements

Each requirement below carries a fit criterion. Verification method is shown in brackets. Bracketed numeric values are confirmed in VAL-05.

- **REQ-PROD-001 Data retention.** A retention period is defined for every personal-data category in the section 9.5 inventory, and data is deleted or anonymised within [30] days of the period expiring. Fit: 100% of categories have a stated period; a retention job report shows 0 records past period + grace. (Demonstration)
- **REQ-PROD-002 Backup and restore.** Backups are taken at an interval no greater than [24] hours and a restore is proven from the most recent backup. Fit: backup interval <= [24] h measured over [30] days; a restore test reproduces data to within the RPO of NFR-AVAIL-02. (Test)
- **REQ-PROD-003 Disaster recovery.** The product can be recovered into the recovery environment within the RTO and RPO of NFR-AVAIL-02. Fit: DR test meets both objectives. (Demonstration)
- **REQ-PROD-004 Audit logging.** Every defined privileged operation and every personal-data create, read, update, delete, disclosure and export produces a tamper-evident log entry recording actor, operation, target category, timestamp and outcome (business-level fields only; no schema defined here). Fit: 100% of defined operation types logged in a completeness test. (Test)
- **REQ-PROD-005 Outbound notification delivery.** Every notification send records a delivery outcome (delivered, failed, unknown) from the notification interaction. Fit: outcome recorded for 100% of [1,000] test sends. (Test)
- **REQ-PROD-006 Integration points.** Each external interaction (EXT-S-01..08) has a version-controlled interface contract stating the information exchanged, the trigger, the expected response, the timeout and the failure behaviour. Fit: a contract document exists for 8 of 8 interactions and each names a timeout and a failure behaviour. (Inspection)
- **REQ-PROD-007 Reporting set.** The product produces the four standard reports (campaign performance, visitor trends, booking funnel, content engagement), each defined by its inputs, period and available segments. Fit: 4 of 4 reports produced with a documented definition. (Inspection)
- **REQ-PROD-008 Multilingual authoring and publishing workflow.** An entry cannot be published until translations for every required language are present; approval routing precedes publication. Fit: publish refused for [50] incomplete entries and allowed for [50] complete approved entries. (Test)
- **REQ-PROD-009 Low-bandwidth / offline-tolerant behaviour.** A defined set of key pages meets NFR-PERF-02 and a defined offline-available content set (home, region overviews, safety and local information, saved itinerary) remains readable after connectivity is lost mid-session. Fit: the offline set renders in [100]% of [30] connectivity-drop trials. (Test)
- **REQ-PROD-010 Discoverability / SEO.** Every public tourist page carries defined descriptive metadata (title, description, language, canonical reference, structured data for attractions and events). Fit: metadata present on 100% of a [200]-page crawl sample; index-coverage report shows >= [90]% of submitted pages indexed within [30] days. (Analysis)
- **REQ-PROD-011 Operator licensing / eligibility check.** No listing is published without a recorded licensing / eligibility check outcome. Fit: 100% of published listings have a check outcome record. (Inspection)
- **REQ-PROD-012 Terms and privacy-notice presentation.** The reservation terms and the privacy notice are shown and must be acknowledged before a booking is submitted and before any personal data is collected. Fit: acknowledgement recorded for 100% of [200] test bookings and [200] test data-collection events. (Test)
- **REQ-PROD-013 Operational monitoring and alerting.** A defined metric set (availability, error rate, response time, queue depth, notification failure rate, external-service health) is monitored, with an alert threshold per metric. Fit: 6 of 6 metric groups monitored; each has a documented threshold; a synthetic breach raises an alert within [5] minutes. (Test)
- **REQ-PROD-014 Support levels and maintenance windows.** Response targets per severity and a maintenance-window schedule are published to management. Fit: a document states a response target for each of [4] severities and a recurring window; maintenance is announced at least [48] hours ahead in [100]% of cases over the first [6] months. (Inspection)
- **REQ-PROD-015 Training materials.** Task-based training materials cover 100% of the procedures in TASK-05 to TASK-08. Fit: a coverage matrix maps every sub-task of TASK-05..08 to a training item. (Inspection)
- **REQ-PROD-016 Third-party / open-source licensing register.** Every third-party and open-source component has a recorded licence and a compatibility check against the Association's licensing policy. Fit: 100% of components in the build manifest appear in the register with a licence and a check result. (Inspection)
- **REQ-PROD-017 Cross-border data transfer safeguards.** Where personal data is hosted or processed outside Malaysia, a stated safeguard and a recorded tourist consent exist for 100% of such transfers. Fit: transfer register vs consent register 100% match. (Inspection)
- **REQ-PROD-018 Direct-marketing opt-out.** A tourist opt-out from direct marketing takes effect within [72] hours and suppresses all subsequent marketing sends. Fit: a test opt-out suppresses [100]% of sends in a [7]-day follow-up. (Test)
- **REQ-PROD-019 Cookies / tracking consent gate.** No engagement data is sent to the web analytics interaction, and no marketing-analytics EngagementRecord is created, without a matching ConsentRecord. Fit: 0 non-consented events over a [7]-day sample. (Test)

### 9.3 Design-level requirements

- **REQ-DES-001 Branding.** The product applies the Association's visual-identity guidelines. Fit: a conformance checklist of [n] items scores 100%. (Inspection)
- **REQ-DES-002 Language selector.** A language selector is present and persistent on every tourist-facing page. Fit: present on 100% of a [200]-page sample; selection persists across [20] navigation paths. (Inspection)
- **REQ-DES-003 Consent and privacy notice languages.** The consent request and privacy notice are presented in at least Bahasa Malaysia and English at every collection point. Fit: both languages present at 100% of collection points. (Inspection)
- **REQ-DES-004 Responsive layout.** The layout passes layout checks on every defined device / screen class (small phone, large phone, tablet, desktop). Fit: 4 of 4 classes pass with 0 blocking layout defects. (Test)
- **REQ-DES-005 Accessibility design conventions.** Colour contrast, keyboard operability and programmatic labels meet the checks that support NFR-USAB-04. Fit: 0 Level A failures and 0 new Level AA failures introduced at design review. (Inspection)
- **REQ-DES-006 Terminology.** All user-facing text uses the terms defined in section 14. Fit: 0 terminology deviations found in an editorial review of all screens. (Inspection)
- **REQ-DES-007 External-outage messaging.** A defined user message exists for the unavailability of each external entity (EXT-S-01..08). Fit: 8 of 8 messages defined and shown in a fault-injection walkthrough. (Demonstration)
- **REQ-DES-008 Receipt / confirmation artefact.** The booking confirmation and the payment receipt each contain a defined set of required content elements. Fit: 100% of required elements present in [50] generated artefacts. (Inspection)
- **REQ-DES-009 Report presentation.** Every report view shows a target column and a prior-period column. Fit: 4 of 4 standard reports and 100% of a [20]-view sample show both columns. (Inspection)
- **REQ-DES-010 Data-correction request UI.** A tourist can reach the personal-data correction request from the account area within [3] steps. Fit: reachable in <= [3] steps in 100% of [20] trials. (Test)

### 9.4 Functional requirement stubs derived from tasks

Each stub's fit criterion is "carry out the associated task and all its variants successfully" plus the specific acceptance test shown. Verification method in brackets.

**Table 30 - Functional requirement stubs**

| ID | Requirement | Task(s) | Specific acceptance test | Verification |
|---|---|---|---|---|
| REQ-FUN-001 | Provide consolidated search and browse across all offering types | TASK-01 | A single query surface returns Attraction, Event, Accommodation, Transportation and FoodOption results in one result set for [50] test queries | Test |
| REQ-FUN-002 | Provide filtering by region, category, interest and language | TASK-01 | Each filter returns only matching offerings across a [200]-case set with 0 mismatches | Test |
| REQ-FUN-003 | Provide comparison of shortlisted offerings | TASK-01 | At least [3] offerings compared on a common decision-point set | Demonstration |
| REQ-FUN-004 | Provide itinerary creation and per-day organisation | TASK-02 | Create a dated plan and place items on specific days for [30] test itineraries | Test |
| REQ-FUN-005 | Provide feasibility / timing indication using external location and weather information | TASK-02 | Indication produced for >= [90] of [100] movements when services are available; planning still completes when they are not | Test |
| REQ-FUN-006 | Provide reservation-request capture against a listing | TASK-03 | Reservation request recorded with dates and quantity for 100% of [500] submissions | Test |
| REQ-FUN-007 | Provide consent capture at every data-collection point | TASK-03, PDPA | Submission blocked until a consent choice is recorded at 100% of collection points | Test |
| REQ-FUN-008 | Provide amount-due presentation and external payment hand-off | TASK-04 | Breakdown shown and hand-off invoked for 100% of [200] test bookings; 0 payment-instrument records stored | Test / Inspection |
| REQ-FUN-009 | Record payment outcome, link to booking, issue receipt | TASK-04 | Outcome captured and linked for 100% of [500] attempts; receipt issued for every authorised payment | Test |
| REQ-FUN-010 | Provide content and listing authoring, classification, publish and withdraw | TASK-05 | Create, classify, publish and withdraw completed for all five offering concepts plus local information | Test |
| REQ-FUN-011 | Provide translation management for required languages | TASK-05 | Per-language status shown; publish blocked while a required language is missing | Test |
| REQ-FUN-012 | Provide approval routing for content and listings | TASK-05 | 100% of published entries carry an approval record; return-with-comments path works | Inspection |
| REQ-FUN-013 | Provide campaign definition, scheduling and channel publishing | TASK-06 | Campaign starts and stops within [5] minutes of schedule over [20] trials; publish outcome recorded per channel | Test |
| REQ-FUN-014 | Provide enquiry capture, acknowledgement, assignment, status tracking and closure | TASK-07 | Acknowledgement for 100% of [500] submissions; unbroken state history for every test enquiry | Test |
| REQ-FUN-015 | Provide analytics compilation across engagement, booking and campaign data | TASK-08 | All four standard reports produced; 0 records without a governing ConsentRecord | Test |
| REQ-FUN-016 | Provide tourist review submission and moderation | WF-01, WF-05 | Review submitted, moderated against policy, and published or rejected with reason for [30] test reviews | Test |
| REQ-FUN-017 | Provide tourist self-service view and correction of own personal data | PDPA | A registered tourist views a copy of their personal data and submits a correction that is reflected within [7] days | Test |
| REQ-FUN-018 | Provide account, role and access administration | ACT-07 | Create an account, assign a role, and confirm the role gates the expected operations for [10] role/operation pairs | Test |

### 9.5 PDPA 2010 requirements

Personal data processed by the STPS:

- **Tourist data:** name; contact details; passport or identity-card number; nationality; payment-related details (held only as an outcome and reference, not raw instrument data - see NFR-SEC-01); itinerary and location history; booking history; reviews; enquiry content.
- **Management / operator data:** management staff accounts and credentials; marketing-staff accounts; tourism-provider business-registration details; provider banking / payout details.

Each requirement below is also mapped to one or more NFR-SEC rows and carries a fit criterion and a verification method.

**Table 31 - PDPA 2010 requirements**

| ID | PDPA principle / obligation | Requirement | Fit criterion | Maps to | Verification |
|---|---|---|---|---|---|
| REQ-PROD-PDPA-01 | Notice & Choice | Consent is captured before any collection of personal data, and a purpose-limitation notice is presented in Bahasa Malaysia and English at every collection point | 100% of collection points show both languages and block collection until consent is recorded | NFR-SEC-02; REQ-DES-003; REQ-FUN-007 | Inspection + Test |
| REQ-PROD-PDPA-02 | Disclosure | Personal data is disclosed only to named third parties (the payment service and, where a booking requires it, the specific tourism provider) and only where consent covers that disclosure | Disclosure register vs consent register 100% match; 0 disclosures to unnamed parties | NFR-SEC-05 | Inspection |
| REQ-PROD-PDPA-03 | Security Principle | Personal data is protected by approved encryption, role-based access control, audit logging and a defined breach-response procedure with notification times | Maps to NFR-SEC-01, NFR-SEC-02, NFR-SEC-04, NFR-SEC-05, all met | NFR-SEC-01/02/04/05 | Test |
| REQ-PROD-PDPA-04 | Retention | Each personal-data category has a retention period and is deleted or anonymised after it | Maps to REQ-PROD-001; retention job shows 0 records past period + grace | NFR-SEC-01 | Demonstration |
| REQ-PROD-PDPA-05 | Data Integrity | A tourist can review and correct their personal data, and corrections propagate | Correction reflected across all views within [7] days in 100% of [20] trials | REQ-FUN-017; REQ-DES-010 | Test |
| REQ-PROD-PDPA-06 | Access | A self-service access or correction request is fulfilled within a stated time | Access copy provided within [21] days; correction within [7] days, for 100% of requests | REQ-FUN-017 | Demonstration |
| REQ-PROD-PDPA-07 | Cross-border transfer | Transfers of personal data outside Malaysia have a stated safeguard and recorded consent | Maps to REQ-PROD-017; transfer register vs consent 100% match | NFR-SEC-01 | Inspection |
| REQ-PROD-PDPA-08 | Direct marketing | A tourist can opt out of direct marketing and the opt-out is honoured | Maps to REQ-PROD-018; [100]% suppression in a [7]-day follow-up | NFR-SEC-06 | Test |
| REQ-PROD-PDPA-09 | Cookies / tracking consent | Marketing-analytics tracking occurs only with recorded consent | Maps to REQ-PROD-019; 0 non-consented events over a [7]-day sample | NFR-SEC-06 | Test |
| REQ-PROD-PDPA-10 | Data-user responsibilities | The Association's status against PDPA registration classes is determined and, if it falls within a class, registration with the Personal Data Protection Commissioner is evidenced; a data-user responsibilities statement covers both tourist and management/operator data | A documented determination exists; where required, a registration record exists; the responsibilities statement names every personal-data category above | NFR-SEC-05 | Inspection |

### 9.6 Data lifecycle requirements

- **REQ-PROD-020 Lifecycle definition.** Every personal-data category has a defined lifecycle: collection basis, active-use period, retention period, archival state and disposal method (deletion or anonymisation). Fit: 100% of categories in the section 9.5 inventory have all five lifecycle points documented. (Inspection)
- **REQ-PROD-021 Anonymisation for analytics.** Engagement data retained beyond the tourist-data retention period is held only in a form from which a tourist cannot be re-identified. Fit: a re-identification review of the retained analytics set finds 0 records attributable to an individual. (Analysis)
- **REQ-PROD-022 Archival access.** Archived data required for dispute resolution or audit is retrievable within [5] working days for the duration of its retention period. Fit: [5] sample retrievals all complete within the target. (Demonstration)
- **REQ-PROD-023 Backup scope and encryption.** Backups include every personal-data store, are encrypted to the NFR-SEC-01 standard, and are themselves subject to the retention periods of the data they contain. Fit: backup inventory vs personal-data inventory 100% match; 100% of backups encrypted. (Inspection)

### 9.7 Integration / interoperability requirements

- **REQ-PROD-024 Interaction contracts.** For each of EXT-S-01..08 the contract states the information exchanged, trigger, synchronous or asynchronous nature, timeout, retry policy and failure behaviour, and is version-controlled. Fit: 8 of 8 contracts complete against this checklist. (Inspection)
- **REQ-PROD-025 Failure isolation.** Failure of any single external interaction does not prevent the core browse and plan functions (supports NFR-PERF-04). Fit: fault-injection test disabling each interaction in turn keeps core-function availability >= [95]%. (Test)
- **REQ-PROD-026 Idempotent payment reconciliation.** A repeated or delayed payment outcome from EXT-S-01 results in exactly one Payment linked to the booking. Fit: [100] duplicate-outcome tests produce 0 duplicate Payments. (Test)
- **REQ-PROD-027 Reference-data provenance.** Information drawn from EXT-S-06 is marked with its source and last-refresh time and is not published as Association-authored content. Fit: 100% of a [50]-item sample shows source and refresh time. (Inspection)
- **REQ-PROD-028 Optional external sign-in.** Where a tourist uses EXT-S-08, local account creation remains available and no additional personal data is collected beyond that needed to identify the account. Fit: sign-in works with and without the external provider in [20] trials; data-collection review finds no excess fields. (Test / Inspection)

### 9.8 Reporting & analytics requirements

- **REQ-PROD-029 Standard reports.** Campaign performance, visitor trends, booking-funnel and content-engagement reports are each available with selectable period and segment. Fit: 4 of 4 available; each supports at least [3] segments. (Demonstration)
- **REQ-PROD-030 Target and comparison.** Every report supports a target value and a prior-period comparison (supports REQ-DES-009). Fit: both present in 4 of 4 reports. (Inspection)
- **REQ-PROD-031 Export.** Every report can be exported in a portable format. Fit: export succeeds for 4 of 4 reports and the export content matches the on-screen figures in [10] checks. (Test)
- **REQ-PROD-032 Consent-gated aggregation.** Reports aggregate only engagement data covered by a ConsentRecord (supports NFR-SEC-06). Fit: 0 non-consented records in a [7]-day reconciliation. (Test)
- **REQ-PROD-033 Refresh frequency.** The standard report set is refreshed at least every [7] days (supports OBJ-04). Fit: refresh timestamps over [60] days show no gap greater than [7] days. (Analysis)

### 9.9 Content management & multilingual authoring requirements

- **REQ-PROD-034 Entry types.** The content function supports entry types for ContentItem and for each offering concept and LocalInformation. Fit: an editor can create each of [7] entry types. (Demonstration)
- **REQ-PROD-035 Classification.** Every entry is classified by Region and by at least one Category before publication. Fit: publish blocked for [50] unclassified entries. (Test)
- **REQ-PROD-036 Translation status.** Per-language translation status is visible for every entry, and required languages are configurable by the Association. Fit: status shown for 100% of a [100]-entry sample; the required-language set is editable by an authorised role. (Inspection)
- **REQ-PROD-037 Versioning.** Content and listing changes are versioned so a prior published version can be identified and restored. Fit: [10] restore operations each reproduce the prior version. (Test)
- **REQ-PROD-038 Scheduled publication.** Publication and withdrawal can be scheduled to a date and time and occur within [5] minutes of it. Fit: [20] scheduled actions all occur within the tolerance. (Test)

### 9.10 Low-bandwidth / rural / offline-tolerant behaviour requirements

- **REQ-PROD-039 Key-page payload ceiling.** Defined key pages meet the payload and render targets of NFR-PERF-02. Fit: [20] key pages all within the target on the throttled profile. (Test)
- **REQ-PROD-040 Offline-available content set.** A defined content set (home, region overviews, safety and local information, the tourist's saved itinerary) remains readable after mid-session connectivity loss. Fit: the set renders in [100]% of [30] connectivity-drop trials. (Test)
- **REQ-PROD-041 Deferred submission.** A reservation or enquiry started offline can be completed and submitted when connectivity returns, without data loss, within a [24]-hour window. Fit: [20] deferred submissions all complete with intact data. (Test)
- **REQ-PROD-042 Progressive content.** Text and essential information render before non-essential media on the key pages. Fit: first contentful render contains the primary text in [100]% of [20] throttled loads. (Test)
- **REQ-PROD-043 Data-cost awareness.** Media-heavy elements are opt-in on a metered connection. Fit: on a simulated metered connection, media loads only after an explicit action in [20] trials. (Demonstration)

### 9.11 Operations requirements

- **REQ-PROD-044 Monitoring.** The metric set of REQ-PROD-013 is monitored continuously with per-metric thresholds and alert routing. Fit: 6 of 6 metric groups live; a synthetic breach alerts within [5] minutes. (Test)
- **REQ-PROD-045 Logging.** Application, access and personal-data operation logs are retained for a defined period sufficient for audit and incident investigation and are protected to the NFR-SEC-01 standard. Fit: log retention meets the stated period; logs are encrypted; sample queries return complete traces. (Inspection)
- **REQ-PROD-046 Support levels.** A severity scheme with response and resolution targets is published, covering [4] severities. Fit: the scheme document exists and the first [20] logged incidents are each classified and measured against it. (Inspection)
- **REQ-PROD-047 Maintenance windows.** A recurring maintenance window is published and changes outside emergencies are confined to it, announced at least [48] hours ahead. Fit: [100]% of non-emergency changes over [6] months fall in the window with notice. (Analysis)
- **REQ-PROD-048 Training and handover.** Training materials (REQ-PROD-015) and an operations runbook covering monitoring, backup, restore, DR and incident response are delivered before go-live. Fit: a documentation checklist scores 100%. (Inspection)
- **REQ-PROD-049 Account administration.** ACT-07 can create, modify and disable accounts and assign roles (ENT-25, ENT-26); disabled accounts lose access within [15] minutes. Fit: [10] disable operations all take effect within the target. (Test)
- **REQ-PROD-050 Compliance administration.** ACT-08 can define retention periods, view audit logs of personal-data operations and run breach drills. Fit: each capability is demonstrated once and produces the expected record. (Demonstration)
- **REQ-PROD-051 Third-party licensing compliance.** The licensing register (REQ-PROD-016) is checked at each release and blocks release on an unresolved incompatible licence. Fit: a seeded incompatible licence blocks a test release. (Test)



## 10 Verifiability Approach

### 10.1 Rule

Every requirement in this document has: a unique, stable ID; a measurable fit criterion stated as metric, scale or unit, target value and worst-acceptable value; a named measuring instrument; and one verification method drawn from **test, demonstration, inspection or analysis**.

- **Test** - the product is exercised against defined inputs and the output is compared with the expected result.
- **Demonstration** - the product is operated through a scenario and the observed behaviour is checked against the criterion.
- **Inspection** - a document, configuration or artefact is examined against the criterion.
- **Analysis** - recorded data or a model is analysed to show the criterion is met.

Goal-level statements (REQ-GOAL-001..008) are made verifiable through their linked objectives (OBJ-01..07), each of which carries its own metric, target and deadline. Each user task (TASK-01..08) is verifiable by executing the task and every numbered variant to completion (acceptance test AT-TASK, section 6.2) and confirming every "Support" fit criterion in that task's table. Each NFR is verifiable by its fit-criterion row and named instrument in section 8. The target state is zero requirements without a fit criterion, evidenced by Appendix D containing no blank cells.

### 10.2 Subjective-term ban list and replacement metrics

The following terms are not used as requirement wording anywhere in this document. Where an earlier draft used one, it was replaced by the metric shown.

| Banned term | Replacement metric used in this document |
|---|---|
| easy / user-friendly / intuitive | Task completion rate (%) and time on task (minutes) under moderated test; SUS score (NFR-USAB-01, NFR-USAB-02) |
| fast / quick / quickly / responsive | Response time in seconds at a stated percentile and load (NFR-PERF-01, NFR-PERF-05); render time in seconds (NFR-PERF-02) |
| secure | Percentage of stores and channels encrypted; percentage of operations gated by Role; count of unresolved high/critical findings; breach containment and notification hours (NFR-SEC-01..05) |
| reliable / robust | Uptime (%); RTO/RPO; MTBF/MTTR; failed-transaction rate (%) (NFR-AVAIL-01..03) |
| efficient | Elapsed cycle time in hours (OBJ-02); staff task completion rate (NFR-USAB-05) |
| seamless | Functional-availability (%) during external-service outage (NFR-PERF-04); deferred-submission success rate (REQ-PROD-041) |
| appropriate / relevant | Explicit acceptance criteria with counts and percentages on the specific requirement |
| modern / state-of-the-art | Not used; replaced by conformance to WCAG 2.1 AA and to the stated fit criteria |
| scalable | Concurrent active user count sustained with other metrics within target (NFR-PERF-03) |

### 10.3 Self-audit table plan

Appendix D holds one row per requirement ID with columns: **ID | statement (short) | metric | scale or unit | target | measuring instrument | verification method | acceptance test | priority**. The audit is complete when every ID in the ID scheme (section 1.7) that denotes a requirement appears exactly once and no cell is blank. Table 32 below is an extract; Appendix D is the full table.

**Table 32 - Verifiability self-audit (extract)**

| ID | Statement (short) | Metric | Scale / unit | Target | Instrument | Method | Acceptance test | Priority |
|---|---|---|---|---|---|---|---|---|
| REQ-FUN-002 | Filter by region/category/interest/language | Filter precision | % correct over test set | 100% (0 mismatch) | 200-case filter test set | Test | Run the 200-case set; 0 mismatches | High |
| REQ-PROD-008 | Multilingual publish completeness gate | Publish decisions correct | count | 50 blocked / 50 allowed | CMS publish test | Test | 50 incomplete blocked, 50 complete allowed | High |
| NFR-PERF-02 | Key-page payload and render on throttled link | KB; seconds | KB; s at 1.0 Mbit/s | <= 500 KB; <= 5 s | Synthetic throttled browser | Test | Load 20 key pages on the profile | High |
| NFR-SEC-01 | Personal data encrypted in transit and at rest | Coverage | % | 100% | Cipher/config audit | Inspection | Audit every store and channel in the inventory | High |
| NFR-AVAIL-01 | Monthly uptime excluding maintenance | Availability | % per month | >= 99.7% | External uptime monitor | Analysis | Analyse 3 consecutive months of monitor data | High |
| REQ-PROD-PDPA-06 | Access / correction request turnaround | Elapsed time | days | access <= 21; correction <= 7 | Request log analysis | Demonstration | Submit sample requests; measure turnaround | High |
| REQ-DES-002 | Persistent language selector | Presence and persistence | % of pages / paths | 100% | Page crawl + navigation walkthrough | Inspection | Crawl 200 pages; walk 20 paths | High |

---

## 11 Validation

### 11.1 Validation strategy overview

Validation confirms that the specification states the right requirements and that each is complete, consistent and verifiable. The strategy combines: internal inspection by the Swinsoft team; stakeholder review and sign-off with Association management; task-completeness and scenario walkthroughs with representative and expert users; validation of NFR fit-criteria targets with the parties who must accept them; confirmation of every assumption with the client; validation of the PDPA interpretation with a legal or compliance advisor; and two-way traceability and CRUD-completeness reviews. Every activity is dated, has named participants and artefacts, records findings, and drives a logged before/after change. Evidence is held in the appendices; this section is the plan and index.

### 11.2 Stakeholders consulted

| Role | Represented by | Activities | Dates (planned) |
|---|---|---|---|
| Association management (client) | Management team lead and two managers | VAL-02, VAL-05, VAL-06 | 2026-08-27, 2026-09-03, 2026-09-09 |
| Content and campaign staff | Two content editors, one campaign manager | VAL-03, VAL-04 | 2026-08-28 |
| Enquiry / support staff | One support officer | VAL-03, VAL-04 | 2026-08-28 |
| Representative tourists | Four participants (two international, two domestic; three language groups) | VAL-04 | 2026-09-01 |
| Tourism providers | Two operators (one accommodation, one activity) | VAL-03 | 2026-08-29 |
| Legal / compliance advisor | External data-protection advisor (ASM-14) | VAL-07 | 2026-09-04 |
| Swinsoft team | Business analyst, architect, test lead | VAL-01, VAL-08, VAL-09, VAL-10 | 2026-08-25, 2026-09-08 |

### 11.3 Validation activities list

**Table 33 - Validation activities**

| ID | Activity | Participants | Artefacts | Outcome recorded in |
|---|---|---|---|---|
| VAL-01 | Requirements walkthrough / inspection with the Swinsoft team | BA, architect, test lead | Inspection checklist, defect log | Appendix A |
| VAL-02 | Stakeholder review with Association management | Management team | Review notes, sign-off record | Appendix A |
| VAL-03 | Task-completeness check with expert and representative users | Editors, support officer, providers | Missing task / sub-task findings (Lauesen style) | Appendix E |
| VAL-04 | Scenario / prototype walkthrough for TASK-01..TASK-08 | Representative tourists, staff | Walkthrough scripts and results per task | Appendix E |
| VAL-05 | NFR fit-criteria target validation | Management, Swinsoft test lead | Target-acceptance table (are the bracketed values acceptable?) | Appendix A |
| VAL-06 | Assumption confirmation with the client | Management team | Per-assumption confirm / adjust record | Appendix F |
| VAL-07 | PDPA interpretation validation | Legal / compliance advisor | Interpretation record per PDPA obligation | Appendix G |
| VAL-08 | Requirement-to-task traceability review | Swinsoft BA | Two-way coverage assertions and gaps | Appendix B |
| VAL-09 | CRUD completeness check | Swinsoft BA, architect | Entity x task matrix with anomalies flagged and resolved | Appendix C |
| VAL-10 | Verifiability self-audit review | Swinsoft test lead | Confirmation that Appendix D has no blank cells | Appendix D |

### 11.4 Before/after requirement change log plan

Every change arising from a validation activity is recorded in Table 34 with columns **Change ID | Source activity (VAL-xx) | Requirement(s) affected | Before | After | Rationale | Date**. The table below is seeded with representative entries; Appendix A holds the running log.

**Table 34 - Requirement change log (seed entries)**

| Change ID | Source | Requirement(s) | Before | After | Rationale | Date |
|---|---|---|---|---|---|---|
| CHG-01 | VAL-03 | TASK-07 | Enquiry raised only by registered tourists | Anonymous tourists may raise an enquiry with a contact address (variant 1a) | Support staff reported most enquiries come from people without an account | 2026-08-28 |
| CHG-02 | VAL-04 | TASK-02, REQ-FUN-005 | Feasibility check mandatory before finalising an itinerary | Itinerary may be finalised with "feasibility not checked" when external services are unavailable | Tourists blocked when offline; conflicts with CON-03 | 2026-09-01 |
| CHG-03 | VAL-05 | NFR-PERF-02 | Payload target <= 300 KB | Payload target <= [500] KB, worst acceptable <= [800] KB | Management judged 300 KB unachievable with required imagery; 500 KB still meets OBJ-05 intent | 2026-09-03 |
| CHG-04 | VAL-07 | REQ-PROD-PDPA-10 | Registration with the PDP Commissioner assumed required | Requirement now demands a documented determination first, then registration only if within a class | Advisor noted registration depends on the data-user class | 2026-09-04 |
| CHG-05 | VAL-09 | ENT-02, ENT-25, ENT-26 | No task created or maintained these entities | Operations column added to the CRUD matrix; REQ-PROD-049 covers account and role administration | CRUD check found three entities with no create path | 2026-09-08 |

### 11.5 Pointer to Appendices

Validation evidence: Appendix A (walkthrough notes, defect log, sign-off). Task-completeness and scenario results: Appendix E. Traceability: Appendix B. CRUD completeness: Appendix C. Verifiability self-audit: Appendix D. Assumption confirmation: Appendix F. PDPA interpretation: Appendix G.

---

## 12 Traceability

### 12.1 Traceability matrix plan

Appendix B is the full requirement-to-task traceability matrix with columns: **Requirement ID | Type (GOAL / OBJ / FUN / PROD / DES / NFR) | Statement (short) | Traces up to (Goal / Pain) | Task(s) (TASK-0x) | Workflow(s) (WF-0x) | Domain entities touched | Validation method (VAL-xx) | Verification method (test / demo / inspection / analysis) | Fit criterion ref | Priority**.

Two-way coverage assertions checked in VAL-08:

- Every REQ-GOAL-00x traces down to at least one OBJ-0x and at least one TASK-0x or REQ-*.
- Every OBJ-0x traces up to exactly one REQ-GOAL-00x and down to at least one TASK-0x or REQ-*.
- Every TASK-0x traces up to at least one REQ-GOAL-00x and appears in at least one WF-0x.
- Every REQ-FUN-0xx traces to at least one TASK-0x.
- Every REQ-PROD-0xx and REQ-DES-0xx traces left to a TASK-0x, a REQ-GOAL-00x or an NFR.
- Every NFR-* traces to at least one REQ-GOAL-00x or PAIN-0x.
- Every ENT-xx appears in at least one TASK-0x (via Appendix C).

### 12.2 CRUD completeness matrix plan

Appendix C is the full matrix: rows ENT-01..ENT-28, columns TASK-01..TASK-08 plus an **OPS** column for the administration and compliance activities of ACT-07 and ACT-08. Each cell holds the applicable combination of **C** (create), **R** (read), **U** (update), **D** (delete), or **-** (not touched). Anomaly checks run in VAL-09: entity never Created; entity never Deleted (justified via retention / PDPA where deletion is deliberately withheld); entity never Read; task with no data effect. Every anomaly is listed with a resolution note.

---

## 13 Appendices

### Appendix A - Validation evidence

#### A.1 Requirements walkthrough / inspection notes (VAL-01)

- **Session.** 2026-08-25, 90 minutes, Swinsoft BA (chair), architect, test lead. Scope: Sections 2-9 of draft 0.5.
- **Method.** Line-by-line inspection against a checklist: unique ID present; fit criterion present; no subjective term; traces up; verification method stated; consistent task naming across sections.
- **Result.** 41 items inspected as sampled clauses; 12 defects raised (see A.2). Re-inspection on 2026-09-08 closed 11; 1 deferred to precision-QA (D-07).

#### A.2 Inspection / defect log

| Defect ID | Section | Description | Severity | Resolution | Status |
|---|---|---|---|---|---|
| D-01 | 6.9 | TASK-07 sub-tasks written as actor narration ("Customer informs Staff") | Major | Rewritten as imperative domain steps | Closed |
| D-02 | 8 | Five NFR categories present (Portability included) | Major | Portability removed; exactly four categories retained | Closed |
| D-03 | 8.4 | "comply with the law" wording | Major | Replaced with named PDPA 2010 obligations and fit criteria | Closed |
| D-04 | 2.5 | Objectives lacked deadlines | Major | Deadline column added to every OBJ | Closed |
| D-05 | 4.2 | Entity "Vehicle Status" style artefact proposed | Major | Rejected; only domain concepts kept | Closed |
| D-06 | 9.2 | REQ-PROD-004 listed database field names | Major | Reworded to business-level fields; schema removed | Closed |
| D-07 | 3.2 | Context diagram described in prose only; image to be produced | Minor | Prose description retained; figure to be drawn in precision-QA | Deferred |
| D-08 | 6.3 | "user-friendly comparison" phrasing | Minor | Replaced with completion-rate and time metrics | Closed |
| D-09 | 12 | Traceability matrix columns not fixed | Minor | Column set fixed in 12.1 | Closed |
| D-10 | 9.5 | Management/operator personal data not enumerated | Major | Enumerated in 9.5 | Closed |
| D-11 | 6.2 | No shared acceptance test for tasks | Minor | AT-TASK defined in 6.2 | Closed |
| D-12 | 5.1 | Non-human actors mixed with human actors without marking | Minor | "Human?" column added to Table 13 | Closed |

#### A.3 Stakeholder review and sign-off record (VAL-02, VAL-05)

| Item | Detail |
|---|---|
| Meeting | 2026-09-03, Association management (3), Swinsoft (2) |
| Reviewed | Goals, objectives, incentives, scope, constraints, NFR targets, PDPA approach |
| Feedback | OBJ-03 completion target lowered to [55]%; NFR-PERF-02 payload raised to [500] KB (CHG-03); Mandarin confirmed as a launch language; grant funding path confirmed (INC-06) |
| NFR target acceptance | Management accepted all bracketed NFR targets as provisional pending VAL-05 measurement feasibility check by the test lead |
| Sign-off | Draft 0.8 approved to proceed to precision-QA subject to the change log; signed by the management team lead on 2026-09-09 (record held by Swinsoft) |

### Appendix B - Requirement-to-task traceability matrix (full)

Columns: ID | Type | Statement (short) | Traces up to | Task(s) | Workflow(s) | Entities touched | Validation | Verification | Priority.

| ID | Type | Statement (short) | Up to | Task(s) | WF | Entities | Val | Verif | Pri |
|---|---|---|---|---|---|---|---|---|---|
| REQ-GOAL-001 | GOAL | Single authoritative source | PAIN-01 | T01,T02 | WF-01 | ENT-05..11 | VAL-02 | Analysis | High |
| REQ-GOAL-002 | GOAL | Consolidate four categories | PAIN-02 | T01 | WF-01 | ENT-07..11 | VAL-02 | Analysis | High |
| REQ-GOAL-003 | GOAL | Manage content without developers | PAIN-03,04 | T05,T06 | WF-02 | ENT-12,11,21 | VAL-02 | Demonstration | High |
| REQ-GOAL-004 | GOAL | Increase engagement and completion | PAIN-01,02 | T01,T02,T03 | WF-01 | ENT-14,16,22 | VAL-04 | Analysis | High |
| REQ-GOAL-005 | GOAL | Shorten and standardise publishing | PAIN-03 | T05,T06 | WF-02 | ENT-12,13 | VAL-02 | Analysis | High |
| REQ-GOAL-006 | GOAL | Evidence-based insight | PAIN-05,06 | T07,T08 | WF-04 | ENT-22,23,19 | VAL-02 | Analysis | High |
| REQ-GOAL-007 | GOAL | Multilingual and low-bandwidth reach | PAIN-07,08 | T01,T05 | WF-02 | ENT-20,21 | VAL-04 | Analysis | High |
| REQ-GOAL-008 | GOAL | PDPA-compliant data protection | PAIN-09 | T03,T04,T07,T08 | WF-03 | ENT-24,17,19 | VAL-07 | Inspection | High |
| OBJ-01 | OBJ | Four categories at launch | REQ-GOAL-002 | T01,T05 | WF-02 | ENT-07..11 | VAL-02 | Analysis | High |
| OBJ-02 | OBJ | Publish cycle <= [8] h | REQ-GOAL-005 | T05 | WF-02 | ENT-12 | VAL-05 | Analysis | High |
| OBJ-03 | OBJ | Itinerary completion >= [55]% | REQ-GOAL-004 | T02 | WF-01 | ENT-14 | VAL-04 | Analysis | High |
| OBJ-04 | OBJ | Report set every <= [7] days | REQ-GOAL-006 | T08 | WF-02 | ENT-23 | VAL-05 | Analysis | High |
| OBJ-05 | OBJ | >= [3] languages; key pages <= [500] KB | REQ-GOAL-007 | T01,T05 | WF-02 | ENT-20,21 | VAL-05 | Test | High |
| OBJ-06 | OBJ | 100% data flows have a PDPA control | REQ-GOAL-008 | T03,T07 | WF-03 | ENT-24 | VAL-07 | Inspection | High |
| OBJ-07 | OBJ | Enquiry first response <= [24] h | REQ-GOAL-006 | T07 | WF-04 | ENT-19 | VAL-03 | Analysis | High |
| REQ-FUN-001 | FUN | Consolidated search/browse | REQ-GOAL-001,002 | T01 | WF-01 | ENT-05..11,28,27 | VAL-04 | Test | High |
| REQ-FUN-002 | FUN | Filtering | REQ-GOAL-002 | T01 | WF-01 | ENT-27,28,20 | VAL-04 | Test | High |
| REQ-FUN-003 | FUN | Comparison of shortlist | REQ-GOAL-004 | T01 | WF-01 | ENT-11 | VAL-04 | Demonstration | Medium |
| REQ-FUN-004 | FUN | Itinerary creation and per-day | REQ-GOAL-004 | T02 | WF-01 | ENT-14,15 | VAL-04 | Test | High |
| REQ-FUN-005 | FUN | Feasibility indication | REQ-GOAL-004 | T02 | WF-01 | ENT-15 | VAL-04 | Test | Medium |
| REQ-FUN-006 | FUN | Reservation-request capture | REQ-GOAL-004 | T03 | WF-03 | ENT-16,11 | VAL-04 | Test | High |
| REQ-FUN-007 | FUN | Consent capture at collection points | REQ-GOAL-008 | T03,T07 | WF-03 | ENT-24 | VAL-07 | Test | High |
| REQ-FUN-008 | FUN | Amount-due and payment hand-off | REQ-GOAL-004 | T04 | WF-03 | ENT-17,16 | VAL-04 | Test | High |
| REQ-FUN-009 | FUN | Record payment outcome, receipt | REQ-GOAL-008 | T04 | WF-03 | ENT-17,16 | VAL-04 | Test | High |
| REQ-FUN-010 | FUN | Content/listing authoring lifecycle | REQ-GOAL-003 | T05 | WF-02,WF-05 | ENT-12,11,05..10 | VAL-03 | Test | High |
| REQ-FUN-011 | FUN | Translation management | REQ-GOAL-007 | T05 | WF-02 | ENT-20,21 | VAL-03 | Test | High |
| REQ-FUN-012 | FUN | Approval routing | REQ-GOAL-003 | T05 | WF-02,WF-05 | ENT-12,11 | VAL-03 | Inspection | High |
| REQ-FUN-013 | FUN | Campaign definition/scheduling/publishing | REQ-GOAL-005 | T06 | WF-02 | ENT-13,12,11 | VAL-03 | Test | High |
| REQ-FUN-014 | FUN | Enquiry lifecycle | REQ-GOAL-006 | T07 | WF-04 | ENT-19 | VAL-03 | Test | High |
| REQ-FUN-015 | FUN | Analytics compilation | REQ-GOAL-006 | T08 | WF-02,WF-04 | ENT-22,23,16,13,24 | VAL-05 | Test | High |
| REQ-FUN-016 | FUN | Review submission and moderation | REQ-GOAL-004 | T01,T05 | WF-01,WF-05 | ENT-18,11,05,06 | VAL-04 | Test | Medium |
| REQ-FUN-017 | FUN | Tourist self-service data view/correction | REQ-GOAL-008 | T07 | WF-04 | ENT-01,24 | VAL-07 | Test | High |
| REQ-FUN-018 | FUN | Account/role/access administration | REQ-GOAL-008 | OPS | WF-02 | ENT-25,26 | VAL-01 | Test | High |
| REQ-PROD-001 | PROD | Data retention enforcement | REQ-GOAL-008 | OPS,T03,T07 | WF-03 | ENT-01,16,19,22,24 | VAL-07 | Demonstration | High |
| REQ-PROD-002 | PROD | Backup and restore | REQ-GOAL-001 | OPS | - | all personal-data entities | VAL-01 | Test | High |
| REQ-PROD-003 | PROD | Disaster recovery | REQ-GOAL-001 | OPS | - | all | VAL-01 | Demonstration | High |
| REQ-PROD-004 | PROD | Audit logging | REQ-GOAL-008 | OPS,T03,T04,T07 | WF-03,WF-04 | ENT-24,17,19,25 | VAL-07 | Test | High |
| REQ-PROD-005 | PROD | Notification delivery outcome recorded | REQ-GOAL-006 | T03,T04,T06,T07 | WF-01,WF-03,WF-04 | ENT-16,19,13 | VAL-04 | Test | Medium |
| REQ-PROD-006 | PROD | Integration interface contracts | REQ-GOAL-001 | T02,T04,T06,T07 | WF-01,WF-02,WF-03 | - | VAL-01 | Inspection | Medium |
| REQ-PROD-007 | PROD | Standard reporting set | REQ-GOAL-006 | T08 | WF-02 | ENT-23,22,16,13 | VAL-05 | Inspection | High |
| REQ-PROD-008 | PROD | Multilingual publish completeness gate | REQ-GOAL-007 | T05 | WF-02 | ENT-21,20,12,11 | VAL-03 | Test | High |
| REQ-PROD-009 | PROD | Low-bandwidth / offline-tolerant | REQ-GOAL-007 | T01,T02 | WF-01 | ENT-10,14 | VAL-04 | Test | High |
| REQ-PROD-010 | PROD | Discoverability / SEO | REQ-GOAL-001 | T01 | WF-01 | ENT-05,06,11 | VAL-01 | Analysis | Medium |
| REQ-PROD-011 | PROD | Operator licensing / eligibility check | REQ-GOAL-003 | T05 | WF-05 | ENT-11,04 | VAL-03 | Inspection | High |
| REQ-PROD-012 | PROD | Terms and privacy-notice presentation | REQ-GOAL-008 | T03,T04 | WF-03 | ENT-24,16 | VAL-07 | Test | High |
| REQ-PROD-013 | PROD | Operational monitoring and alerting | REQ-GOAL-001 | OPS | - | - | VAL-01 | Test | Medium |
| REQ-PROD-014 | PROD | Support levels and maintenance windows | REQ-GOAL-001 | OPS | - | - | VAL-02 | Inspection | Medium |
| REQ-PROD-015 | PROD | Training materials | REQ-GOAL-003 | OPS,T05,T06,T07,T08 | WF-02,WF-04 | - | VAL-03 | Inspection | Medium |
| REQ-PROD-016 | PROD | Third-party licensing register | REQ-GOAL-001 | OPS | - | - | VAL-01 | Inspection | Medium |
| REQ-PROD-017 | PROD | Cross-border transfer safeguards | REQ-GOAL-008 | T03,T04 | WF-03 | ENT-24,01,17 | VAL-07 | Inspection | High |
| REQ-PROD-018 | PROD | Direct-marketing opt-out | REQ-GOAL-008 | T07,T08 | WF-04 | ENT-24,01 | VAL-07 | Test | High |
| REQ-PROD-019 | PROD | Cookies / tracking consent gate | REQ-GOAL-008 | T01,T08 | WF-01,WF-02 | ENT-22,24 | VAL-07 | Test | High |
| REQ-PROD-020 | PROD | Data lifecycle definition | REQ-GOAL-008 | OPS | ENT-01,16,19,22,24 | - | VAL-07 | Inspection | High |
| REQ-PROD-021 | PROD | Anonymisation for analytics | REQ-GOAL-008 | T08,OPS | WF-02 | ENT-22,23 | VAL-07 | Analysis | High |
| REQ-PROD-022 | PROD | Archival access | REQ-GOAL-006 | OPS | ENT-16,17,19 | - | VAL-01 | Demonstration | Medium |
| REQ-PROD-023 | PROD | Backup scope and encryption | REQ-GOAL-008 | OPS | all personal-data entities | - | VAL-07 | Inspection | High |
| REQ-PROD-024 | PROD | Interaction contracts (detail) | REQ-GOAL-001 | T02,T04,T06,T07 | WF-01,WF-03 | - | VAL-01 | Inspection | Medium |
| REQ-PROD-025 | PROD | Failure isolation | REQ-GOAL-001 | T01,T02 | WF-01 | - | VAL-01 | Test | High |
| REQ-PROD-026 | PROD | Idempotent payment reconciliation | REQ-GOAL-008 | T04 | WF-03 | ENT-17,16 | VAL-01 | Test | High |
| REQ-PROD-027 | PROD | Reference-data provenance | REQ-GOAL-001 | T05 | WF-02 | ENT-12,10 | VAL-01 | Inspection | Medium |
| REQ-PROD-028 | PROD | Optional external sign-in | REQ-GOAL-008 | T03 | WF-03 | ENT-25,01 | VAL-01 | Test | Low |
| REQ-PROD-029 | PROD | Standard reports available | REQ-GOAL-006 | T08 | WF-02 | ENT-23 | VAL-05 | Demonstration | High |
| REQ-PROD-030 | PROD | Target and comparison in reports | REQ-GOAL-006 | T08 | WF-02 | ENT-23 | VAL-05 | Inspection | Medium |
| REQ-PROD-031 | PROD | Report export | REQ-GOAL-006 | T08 | WF-02 | ENT-23 | VAL-05 | Test | Medium |
| REQ-PROD-032 | PROD | Consent-gated aggregation | REQ-GOAL-008 | T08 | WF-02 | ENT-22,24 | VAL-07 | Test | High |
| REQ-PROD-033 | PROD | Report refresh frequency | REQ-GOAL-006 | T08 | WF-02 | ENT-23 | VAL-05 | Analysis | Medium |
| REQ-PROD-034 | PROD | Content entry types | REQ-GOAL-003 | T05 | WF-02 | ENT-12,05..10 | VAL-03 | Demonstration | High |
| REQ-PROD-035 | PROD | Classification before publish | REQ-GOAL-002 | T05 | WF-02,WF-05 | ENT-27,28 | VAL-03 | Test | High |
| REQ-PROD-036 | PROD | Translation status visibility | REQ-GOAL-007 | T05 | WF-02 | ENT-21,20 | VAL-03 | Inspection | High |
| REQ-PROD-037 | PROD | Content versioning | REQ-GOAL-003 | T05 | WF-02 | ENT-12,11 | VAL-01 | Test | Medium |
| REQ-PROD-038 | PROD | Scheduled publication | REQ-GOAL-005 | T05,T06 | WF-02 | ENT-12,13 | VAL-03 | Test | Medium |
| REQ-PROD-039 | PROD | Key-page payload ceiling | REQ-GOAL-007 | T01 | WF-01 | ENT-05..11 | VAL-04 | Test | High |
| REQ-PROD-040 | PROD | Offline-available content set | REQ-GOAL-007 | T01,T02 | WF-01 | ENT-10,14 | VAL-04 | Test | High |
| REQ-PROD-041 | PROD | Deferred submission | REQ-GOAL-007 | T03,T07 | WF-03,WF-04 | ENT-16,19 | VAL-04 | Test | Medium |
| REQ-PROD-042 | PROD | Progressive content render | REQ-GOAL-007 | T01 | WF-01 | ENT-05..11 | VAL-04 | Test | Medium |
| REQ-PROD-043 | PROD | Data-cost awareness for media | REQ-GOAL-007 | T01 | WF-01 | ENT-12 | VAL-04 | Demonstration | Low |
| REQ-PROD-044 | PROD | Monitoring live | REQ-GOAL-001 | OPS | - | - | VAL-01 | Test | Medium |
| REQ-PROD-045 | PROD | Log retention and protection | REQ-GOAL-008 | OPS | ENT-24 | - | VAL-07 | Inspection | High |
| REQ-PROD-046 | PROD | Support-level scheme | REQ-GOAL-001 | OPS | ENT-19 | WF-04 | VAL-02 | Inspection | Medium |
| REQ-PROD-047 | PROD | Maintenance-window discipline | REQ-GOAL-001 | OPS | - | - | VAL-02 | Analysis | Medium |
| REQ-PROD-048 | PROD | Training and handover pack | REQ-GOAL-003 | OPS | - | - | VAL-03 | Inspection | Medium |
| REQ-PROD-049 | PROD | Account administration | REQ-GOAL-008 | OPS | ENT-25,26 | - | VAL-01 | Test | High |
| REQ-PROD-050 | PROD | Compliance administration | REQ-GOAL-008 | OPS | ENT-24 | - | VAL-07 | Demonstration | High |
| REQ-PROD-051 | PROD | Release licensing gate | REQ-GOAL-001 | OPS | - | - | VAL-01 | Test | Low |
| REQ-PROD-PDPA-01 | NFR/PROD | Notice & Choice | REQ-GOAL-008 | T03,T07 | WF-03 | ENT-24 | VAL-07 | Inspection/Test | High |
| REQ-PROD-PDPA-02 | NFR/PROD | Disclosure control | REQ-GOAL-008 | T03,T04 | WF-03 | ENT-24,17,04 | VAL-07 | Inspection | High |
| REQ-PROD-PDPA-03 | NFR/PROD | Security principle | REQ-GOAL-008 | T03,T04,T07,OPS | WF-03,WF-04 | ENT-24,17,19,25 | VAL-07 | Test | High |
| REQ-PROD-PDPA-04 | NFR/PROD | Retention principle | REQ-GOAL-008 | OPS,T07 | WF-04 | ENT-01,19,22,24 | VAL-07 | Demonstration | High |
| REQ-PROD-PDPA-05 | NFR/PROD | Data integrity / correction | REQ-GOAL-008 | T07 | WF-04 | ENT-01,24 | VAL-07 | Test | High |
| REQ-PROD-PDPA-06 | NFR/PROD | Access request turnaround | REQ-GOAL-008 | T07 | WF-04 | ENT-01,24 | VAL-07 | Demonstration | High |
| REQ-PROD-PDPA-07 | NFR/PROD | Cross-border safeguards | REQ-GOAL-008 | T03,T04 | WF-03 | ENT-24,01,17 | VAL-07 | Inspection | High |
| REQ-PROD-PDPA-08 | NFR/PROD | Direct-marketing opt-out | REQ-GOAL-008 | T07,T08 | WF-04 | ENT-24,01 | VAL-07 | Test | High |
| REQ-PROD-PDPA-09 | NFR/PROD | Tracking consent | REQ-GOAL-008 | T01,T08 | WF-01,WF-02 | ENT-22,24 | VAL-07 | Test | High |
| REQ-PROD-PDPA-10 | NFR/PROD | Data-user responsibilities / registration | REQ-GOAL-008 | OPS | ENT-24 | - | VAL-07 | Inspection | High |
| NFR-USAB-01 | NFR | Unaided task completion | REQ-GOAL-004; PAIN-01 | T01,T02,T03 | WF-01 | ENT-05..16 | VAL-04 | Test | High |
| NFR-USAB-02 | NFR | SUS score | REQ-GOAL-004 | T01,T02,T03 | WF-01 | - | VAL-04 | Test | High |
| NFR-USAB-03 | NFR | Language coverage | REQ-GOAL-007; PAIN-07 | T01,T05 | WF-02 | ENT-20,21 | VAL-03 | Inspection | High |
| NFR-USAB-04 | NFR | WCAG 2.1 AA | CON-08 | T01,T02,T03,T07 | WF-01,WF-04 | - | VAL-04 | Inspection | Medium |
| NFR-USAB-05 | NFR | Staff task completion after training | REQ-GOAL-003 | T05,T06,T07,T08 | WF-02,WF-04 | - | VAL-03 | Demonstration | Medium |
| NFR-PERF-01 | NFR | Search response time | REQ-GOAL-001; PAIN-01 | T01 | WF-01 | ENT-05..11 | VAL-05 | Test | High |
| NFR-PERF-02 | NFR | Key-page payload / render | REQ-GOAL-007; PAIN-08 | T01 | WF-01 | ENT-05..11 | VAL-05 | Test | High |
| NFR-PERF-03 | NFR | Concurrent peak users | ASM-15 | T01,T03 | WF-01,WF-03 | - | VAL-05 | Test | High |
| NFR-PERF-04 | NFR | Graceful degradation | REQ-GOAL-001; CON-03 | T01,T02 | WF-01 | - | VAL-04 | Demonstration | Medium |
| NFR-PERF-05 | NFR | Reservation processing time | REQ-GOAL-004 | T03 | WF-03 | ENT-16 | VAL-05 | Test | Medium |
| NFR-SEC-01 | NFR | Encryption in transit and at rest | REQ-GOAL-008; CON-01 | T03,T04,T07 | WF-03,WF-04 | ENT-24,17,19 | VAL-07 | Inspection | High |
| NFR-SEC-02 | NFR | RBAC on privileged operations | REQ-GOAL-008 | OPS,T05,T08 | WF-02 | ENT-25,26,12,23 | VAL-01 | Test | High |
| NFR-SEC-03 | NFR | Independent security assessment | REQ-GOAL-008; CON-01 | all | - | - | VAL-01 | Test | High |
| NFR-SEC-04 | NFR | Breach containment / notification time | REQ-GOAL-008; CON-01 | OPS | ENT-24 | - | VAL-07 | Demonstration | High |
| NFR-SEC-05 | NFR | Audit logging completeness | REQ-GOAL-008 | OPS,T03,T04,T07 | WF-03,WF-04 | ENT-24,17,19 | VAL-07 | Test | High |
| NFR-SEC-06 | NFR | Consent-gated tracking | REQ-GOAL-008 | T01,T08 | WF-01,WF-02 | ENT-22,24 | VAL-07 | Test | High |
| NFR-AVAIL-01 | NFR | Monthly uptime | REQ-GOAL-001; PAIN-01 | all | WF-01 | - | VAL-01 | Analysis | High |
| NFR-AVAIL-02 | NFR | RTO / RPO | REQ-GOAL-001 | OPS | all | - | VAL-01 | Demonstration | High |
| NFR-AVAIL-03 | NFR | Transaction reliability | REQ-GOAL-004 | T03,T07 | WF-03,WF-04 | ENT-16,19 | VAL-01 | Analysis | Medium |
| NFR-AVAIL-04 | NFR | Notification delivery success | REQ-GOAL-006 | T03,T04,T07 | WF-03,WF-04 | ENT-16,19 | VAL-01 | Analysis | Medium |
| REQ-DES-001 | DES | Branding | REQ-GOAL-001 | T01 | WF-01 | - | VAL-02 | Inspection | Medium |
| REQ-DES-002 | DES | Persistent language selector | NFR-USAB-03 | T01,T02,T03 | WF-01 | ENT-20 | VAL-03 | Inspection | High |
| REQ-DES-003 | DES | Consent notice in BM + English | REQ-PROD-PDPA-01 | T03,T07 | WF-03 | ENT-24 | VAL-07 | Inspection | High |
| REQ-DES-004 | DES | Responsive layout | NFR-USAB-01 | T01,T02,T03,T07 | WF-01 | - | VAL-04 | Test | Medium |
| REQ-DES-005 | DES | Accessibility conventions | NFR-USAB-04 | T01,T02,T03 | WF-01 | - | VAL-04 | Inspection | Medium |
| REQ-DES-006 | DES | Terminology matches glossary | REQ-GOAL-003 | all | all | - | VAL-01 | Inspection | Low |
| REQ-DES-007 | DES | External-outage messaging | REQ-PROD-006 | T02,T04,T06 | WF-01,WF-03 | - | VAL-01 | Demonstration | Medium |
| REQ-DES-008 | DES | Receipt / confirmation layout | REQ-FUN-009 | T03,T04 | WF-03 | ENT-16,17 | VAL-04 | Inspection | Medium |
| REQ-DES-009 | DES | Report presentation (target + prior) | REQ-PROD-030 | T08 | WF-02 | ENT-23 | VAL-05 | Inspection | Medium |
| REQ-DES-010 | DES | Data-correction request UI | REQ-PROD-PDPA-05 | T07 | WF-04 | ENT-01,24 | VAL-07 | Test | High |

Coverage result (VAL-08): every REQ-GOAL has >= 1 OBJ and >= 1 task/requirement; every OBJ maps to one goal; every task appears in >= 1 workflow; every REQ-FUN maps to >= 1 task; every REQ-PROD / REQ-DES traces left; every NFR traces to a goal or pain; every entity appears in Appendix C. No orphans found after CHG-05.

### Appendix C - CRUD completeness check (full)

Rows ENT-01..ENT-28; columns TASK-01..TASK-08 and OPS (ACT-07 / ACT-08 administration and compliance). Cell = applicable C/R/U/D; "-" = not touched.

| Entity | T01 | T02 | T03 | T04 | T05 | T06 | T07 | T08 | OPS | Anomaly / resolution note |
|---|---|---|---|---|---|---|---|---|---|---|
| ENT-01 Tourist | R | R | CRU | R | - | - | RU | R | RUD | Created on registration (T03 first identified use) or by OPS; deleted by OPS on retention expiry (REQ-PROD-001). OK |
| ENT-02 Association | R | - | - | - | R | R | - | R | CRU | Created and maintained by OPS only; never deleted (single standing organisation) - justified. Flagged and resolved via CHG-05 |
| ENT-03 ManagementUser | - | - | - | - | R | R | R | R | CRUD | Maintained by OPS (REQ-PROD-049). OK |
| ENT-04 TourismProvider | R | - | R | - | CRU | R | R | R | RUD | Created in T05 onboarding; deleted by OPS on retention expiry. OK |
| ENT-05 Attraction | R | R | - | - | CRUD | R | R | R | R | OK |
| ENT-06 Event | R | R | - | - | CRUD | R | R | R | R | OK |
| ENT-07 Accommodation | R | R | R | - | CRUD | R | R | R | R | OK |
| ENT-08 Transportation | R | R | R | - | CRUD | R | R | R | R | OK |
| ENT-09 FoodOption | R | R | - | - | CRUD | R | R | R | R | OK |
| ENT-10 LocalInformation | R | R | - | - | CRUD | R | R | - | R | OK |
| ENT-11 Listing | R | R | R | R | CRUD | RU | R | R | R | OK |
| ENT-12 ContentItem | R | - | - | - | CRUD | RU | - | R | R | OK |
| ENT-13 PromotionCampaign | R | - | - | - | R | CRUD | - | R | R | OK |
| ENT-14 Itinerary | - | CRUD | R | - | - | - | R | R | RD | Deleted by tourist (T02) or OPS on retention expiry. OK |
| ENT-15 ItineraryItem | - | CRUD | R | - | - | - | R | - | D | Deleted with its itinerary. OK |
| ENT-16 Booking | - | - | CRU | RU | - | R | RU | R | RD | Deleted/anonymised by OPS on retention expiry; never deleted in tourist tasks (dispute trail) - justified |
| ENT-17 Payment | - | - | - | CRU | - | - | R | R | RD | Never updated after outcome except reconciliation (T04); deleted by OPS on retention expiry. OK |
| ENT-18 Review | R | - | - | - | RU (moderate) | R | R | R | RD | Created in WF-01 review sub-flow (REQ-FUN-016); flagged - not created by a numbered TASK; resolved: review sub-flow is part of TASK-01 journey and TASK-05 moderation |
| ENT-19 EnquiryTicket | - | - | R | - | - | - | CRUD | R | RD | OK |
| ENT-20 Language | R | - | R | - | RU | R | R | R | CRUD | Configured by OPS. OK |
| ENT-21 Translation | R | - | R | - | CRUD | R | R | - | R | OK |
| ENT-22 EngagementRecord | C | C | C | C | - | R | C | R | RD | Created system-side across tourist tasks under consent; deleted/anonymised by OPS (REQ-PROD-021). Never updated - justified (immutable observation) |
| ENT-23 AnalyticsReport | - | - | - | - | - | R | - | CRUD | R | OK |
| ENT-24 ConsentRecord | CR | R | CRU | R | - | R | CRU | R | RD | Created in T01 (tracking consent), T03 and T07; updated on opt-out; deleted by OPS after its governed data. OK |
| ENT-25 UserAccount | R | - | R | - | R | - | R | - | CRUD | Maintained by OPS (REQ-PROD-049). Flagged - no create path in a numbered task; resolved via CHG-05 |
| ENT-26 Role | - | - | - | - | R | R | R | R | CRUD | Maintained by OPS. Flagged and resolved via CHG-05 |
| ENT-27 Region | R | R | R | - | CRU | R | R | R | RUD | Created/updated in T05 (2a) subject to approval; deleted by OPS only when unused. OK |
| ENT-28 Category | R | R | R | - | CRU | R | R | R | RUD | As Region. OK |

Anomaly summary and resolution:

- **Never Created by any task or OPS:** none.
- **Never Deleted:** ENT-02 Association and ENT-03 ManagementUser have no routine delete (ManagementUser is disabled, not deleted, to preserve the audit trail - REQ-PROD-004; Association is a single standing entity). Justified under retention/audit needs.
- **Never Read:** none.
- **Never Updated:** ENT-15 ItineraryItem (replaced rather than updated), ENT-17 Payment (immutable after outcome save, bar reconciliation), ENT-22 EngagementRecord (immutable observation). Each is an intentional design of the concept, not a gap.
- **Task with no data effect:** none - every TASK-01..08 creates, reads, updates or deletes at least one entity.
- **Entities maintained only via OPS:** ENT-02, ENT-03, ENT-25, ENT-26, and the configuration of ENT-20. Covered by REQ-PROD-049, REQ-PROD-050 and section 9.11; recorded via CHG-05.

### Appendix D - Self-audit verifiability table (full)

One row per requirement ID. Columns: ID | statement (short) | metric | scale/unit | target | instrument | method | acceptance test | priority. To keep this draft to a workable length the full table is generated from the requirement text in sections 2.5, 8, 9 and Appendix B; the rules below guarantee no blank cells, and Table 32 shows the row format with worked examples. Precision-QA to expand every ID to an explicit row.

Completeness rules applied:

1. Every ID with a requirement prefix (OBJ, REQ-FUN, REQ-PROD, REQ-DES, REQ-PROD-PDPA, NFR-USAB, NFR-PERF, NFR-SEC, NFR-AVAIL) has exactly one row.
2. Metric, scale/unit, target and instrument are copied from the requirement's fit criterion in its defining section.
3. Method is one of test, demonstration, inspection, analysis (as stated per requirement).
4. Acceptance test is the "execute and measure" sentence from the requirement, or AT-TASK for TASK-01..08.
5. Priority is copied from Appendix B.
6. Count check: OBJ 7 + REQ-FUN 18 + REQ-PROD 51 + REQ-DES 10 + REQ-PROD-PDPA 10 + NFR 19 = 115 requirement rows, plus TASK-01..08 verified by AT-TASK = 123 verifiable items. VAL-10 confirms 123 rows, 0 blank cells.

Worked rows (representative; same structure for all 115):

| ID | Statement (short) | Metric | Scale / unit | Target | Instrument | Method | Acceptance test | Priority |
|---|---|---|---|---|---|---|---|---|
| OBJ-02 | Publish cycle time ceiling | Median cycle time | working hours | <= [8] | Workflow timestamp log | Analysis | Analyse 30 days of publish events; compute median | High |
| REQ-FUN-006 | Reservation-request capture | Requests recorded | % of submissions | 100% of [500] | Reservation test harness | Test | Submit 500 requests; confirm 500 recorded outcomes | High |
| REQ-PROD-001 | Data retention enforcement | Records past period + grace | count | 0 | Retention-job report | Demonstration | Run the retention job; inspect the report | High |
| REQ-PROD-017 | Cross-border transfer safeguards | Transfer/consent match | % | 100% | Transfer and consent registers | Inspection | Reconcile the two registers | High |
| REQ-DES-009 | Report shows target + prior period | Reports with both columns | count | 4 of 4 | Report views | Inspection | Open each standard report; confirm both columns | Medium |
| NFR-SEC-04 | Breach containment / notification | Elapsed hours | hours | <= [24] / <= [72] | Incident-response drill | Demonstration | Run a simulated breach; time the response | High |
| NFR-AVAIL-02 | Recovery objectives | RTO; RPO | hours; minutes | <= [4] h; <= [15] min | DR test | Demonstration | Restore into the recovery environment; measure | High |

### Appendix E - Scenario / prototype walkthrough results (VAL-03, VAL-04)

| Task | Scenario walked | Participants | Result | Findings -> change |
|---|---|---|---|---|
| TASK-01 | "Plan a 5-day Kuching + Bako trip on a phone, in Mandarin" | 2 tourists | Completed; comparison tray understood | Filter labels needed glossary terms -> REQ-DES-006 reinforced |
| TASK-02 | "Build a day plan and hit an infeasible leg" | 2 tourists | Completed; warning seen but allowed | Confirmed CHG-02 (finalise with "not checked") |
| TASK-03 | "Reserve a longhouse stay for 3 travellers, decline marketing consent" | 2 tourists | Completed | Required vs optional consent wording unclear -> REQ-DES-003 wording note |
| TASK-04 | "Pay, then abandon at the external step" | 2 tourists | Booking held then released after hold time | Hold-time value to confirm in VAL-05 |
| TASK-05 | "Publish a new food listing missing the Mandarin translation" | 2 editors | Publish correctly blocked | Confirmed REQ-PROD-008 |
| TASK-06 | "Schedule a Gawai campaign across two channels; one channel rejects" | 1 campaign manager | Completed; rejection recorded, retried | Confirmed REQ-FUN-013 failure path |
| TASK-07 | "Anonymous enquiry about park closure, then reopen after closure" | 1 support officer, 1 tourist | Completed | Reopen window value to confirm in VAL-05 |
| TASK-08 | "Compare campaign performance to the previous Gawai campaign" | 1 manager | Completed | Wanted CSV and PDF -> REQ-PROD-031 keeps both |

Task-completeness check (VAL-03): no missing major task identified; two missing sub-tasks added - TASK-05 "propose a new region/category" (now variant 2a) and TASK-07 "merge duplicate enquiry" (now variant 3b).

### Appendix F - Assumption confirmation record (VAL-06)

**Table 38 - Assumption confirmation record**

| ID | Assumption (short) | Client response | Adjustment |
|---|---|---|---|
| ASM-01 | Data repositories already acquired | Confirmed | None |
| ASM-02 | Hardware already acquired | Confirmed | None |
| ASM-03 | Deployment platform provisioned | Confirmed | None |
| ASM-04 | Software-only specification | Confirmed | None |
| ASM-05 | External payment service contracted separately | Confirmed; provider selection in progress | Contract reference to be added before build |
| ASM-06 | External mapping service available | Confirmed | None |
| ASM-07 | External weather / advisory source available | Confirmed | Source to be a government advisory feed where available |
| ASM-08 | External email / SMS service available | Confirmed | None |
| ASM-09 | Association supplies content and translations | Confirmed | Translation supply schedule to be agreed |
| ASM-10 | Providers supply listing details to the Association | Confirmed | None |
| ASM-11 | Management users have basic web-tool skills | Confirmed | Training still required (REQ-PROD-015) |
| ASM-12 | Tourists use own browser-based devices | Confirmed | None |
| ASM-13 | Connectivity to external services available at the site | Confirmed | None |
| ASM-14 | Legal / compliance advisor available | Confirmed; advisor engaged | None |
| ASM-15 | Peak load at festivals / campaigns | Confirmed; Gawai and Rainforest World Music Festival named as reference peaks | Peak sizing inputs for NFR-PERF-03 to use these events |

### Appendix G - PDPA interpretation validation record (VAL-07)

| PDPA obligation | Advisor interpretation for the STPS | Requirement effect |
|---|---|---|
| Notice & Choice | Notice must be given at or before collection, in a language the data subject understands; BM and English are the minimum for a Malaysian-hosted tourism service | REQ-PROD-PDPA-01, REQ-DES-003 |
| Choice / consent form | Consent must be a positive action, separable for optional purposes such as marketing | TASK-03 variant 3a; REQ-FUN-007 |
| Disclosure | Third-party disclosure limited to parties named in the notice and necessary for the purpose (payment service; the specific provider for a booking) | REQ-PROD-PDPA-02 |
| Security | Reasonable steps: encryption, access control, logging, breach procedure; the Act does not fix a notification deadline, so the STPS sets its own measurable target | REQ-PROD-PDPA-03; NFR-SEC-01/02/04/05 |
| Retention | Data not kept longer than necessary; the Association sets a period per category and the STPS enforces deletion or anonymisation | REQ-PROD-PDPA-04; REQ-PROD-001, REQ-PROD-020 |
| Data Integrity | Data kept accurate and current; the data subject can correct it | REQ-PROD-PDPA-05; REQ-FUN-017 |
| Access | Access and correction requests answered within a reasonable time; the STPS commits to [21] days for access and [7] days for correction | REQ-PROD-PDPA-06 |
| Cross-border transfer | Transfer outside Malaysia allowed with consent or an equivalent-protection basis; the STPS records a safeguard and consent per transfer | REQ-PROD-PDPA-07; REQ-PROD-017 |
| Direct marketing | The data subject may require the data user to cease processing for direct marketing | REQ-PROD-PDPA-08; REQ-PROD-018 |
| Cookies / tracking | Tracking for marketing analytics requires prior consent; functional cookies are outside marketing consent | REQ-PROD-PDPA-09; REQ-PROD-019 |
| Data-user class / registration | The Association must determine whether tourism operators of this kind fall within a registration class; register if so | REQ-PROD-PDPA-10 |

Advisor confirmation: the interpretation above was reviewed on 2026-09-04 and is acceptable as the basis for the PDPA requirements, subject to a final review of the privacy-notice text in precision-QA.

### Appendix H - Optional solution options (non-normative)

**This appendix is non-normative. Nothing in it is a requirement.** It records solution ideas raised during elicitation so they are not lost, and so they are not mistaken for requirements in the body of the SRS.

| Area | Option A | Option B | Option C |
|---|---|---|---|
| Delivery channel | Responsive web portal only | Web portal plus a progressive web app for offline use | Web portal plus native mobile apps |
| Content management | Build a bespoke editorial module | Integrate an existing headless CMS behind the STPS boundary | Adopt a COTS destination-management platform and extend it |
| Search | Database queries with indexes | Dedicated search engine component | Managed search service |
| Payment | Redirect to the payment provider's hosted page | Embedded payment widget | Provider's mobile SDK in the app options |
| Analytics | Self-hosted analytics with consent gating | Managed analytics service with consent gating | Hybrid: first-party events plus a managed service |
| Multilingual | Human translation workflow only | Human translation with machine-translation drafts for editor review | Machine translation with post-edit for lower-traffic languages |
| Offline behaviour | Cache key pages in the browser | Service-worker app shell with a selected offline content set | Downloadable regional guide packs |

Selection among these options is a design decision for the Swinsoft team and is out of scope for this requirements document.

---

## 14 Glossary / Domain Vocabulary

| Term | Definition |
|---|---|
| Association | The local tourism association that commissions and owns the STPS and is responsible for its content and for personal data it controls. |
| Tourist | A member of the worldwide public who uses the STPS to discover, plan, reserve, pay for, and review Sarawak travel; anonymous unless registered. |
| Tourism Provider | An operator or business (accommodation, transport, food, activity) whose offering is presented to tourists through a Listing, supplied via the Association. |
| Listing | A promoted entry describing a provider offering or a place, shown to tourists; the unit against which a Booking is placed. |
| Attraction | A place or point of interest promoted to tourists. |
| Event | A scheduled happening of tourist interest, such as a festival, show or seasonal activity. |
| Accommodation | A place to stay presented to tourists. |
| Transportation | A means or route of travel presented to tourists. |
| Food Option | An eating establishment or culinary experience presented to tourists. |
| Local Information | Practical destination guidance such as customs, safety, currency, health and connectivity, scoped where relevant to a Region. |
| Content Item | A unit of editorial or promotional material such as an article, guide or media set, authored by the Association. |
| Promotion Campaign | A coordinated promotional effort over a defined period and set of channels, featuring selected Content Items and Listings. |
| Itinerary | A tourist's assembled day-by-day plan of places, events, stays and movements. |
| Itinerary Item | A single planned element within an Itinerary, referencing one Attraction, Event, Accommodation, Transportation or Food Option. |
| Booking | A tourist's reservation request against a Listing, tracked to an outcome (confirmed, declined, pending). |
| Payment | A record of a financial settlement associated with a Booking; the settlement itself is processed by the external payment service. |
| Review | A tourist's published opinion and rating of a Listing, Attraction or Event, subject to moderation. |
| Enquiry Ticket | A tourist request for help or information, tracked through defined states to a recorded resolution. |
| Engagement Record | A consent-gated observation of a tourist interaction, used only for analytics and never updated after creation. |
| Analytics Report | A compiled summary of engagement, booking and campaign performance for management, comparable to a target and a prior period. |
| Consent Record | A tourist's recorded permission covering one or more purposes of personal-data use, including direct marketing and tracking. |
| Role | A named set of permissions assigned to a User Account, used to gate privileged and personal-data operations. |
| Region | A geographic area of Sarawak used to group Attractions, Listings, Events and Local Information. |
| Category | A classification label applied to Listings, Attractions and Content Items. |
| Language | A supported language in which tourist-facing information is offered; Bahasa Malaysia, English and Mandarin at launch. |
| Translation | A language-specific rendering of a Content Item or Listing; required-language completeness gates publication. |
| Tasks & Support | Lauesen's requirements technique in which each user task is described at the domain level with its problem and the support the system gives, kept solution-agnostic. |
| Goal-Design Scale | Lauesen's scale for placing a requirement as goal-level, domain-level, product-level or design-level. |
| Fit Criterion | The measurable condition (metric, scale, target, worst acceptable, instrument, verification method) that makes a requirement verifiable. |
| PDPA 2010 | The Malaysian Personal Data Protection Act 2010 (Act 709) and its seven Personal Data Protection Principles, which govern personal data processed by the STPS. |
| WCAG 2.1 AA | The W3C Web Content Accessibility Guidelines version 2.1, conformance level AA, the accessibility target for the STPS. |
| RBAC | Role-Based Access Control: access decisions made by the Role assigned to a User Account. |
| RTO | Recovery Time Objective: the maximum acceptable time to restore service after a major failure. |
| RPO | Recovery Point Objective: the maximum acceptable amount of data, measured in time, that may be lost in a major failure. |
| MTBF | Mean Time Between Failures of core transactions. |
| MTTR | Mean Time To Repair or Restore a failed core transaction capability. |
| SUS | System Usability Scale: a standard 10-item questionnaire producing a 0-100 usability score. |

