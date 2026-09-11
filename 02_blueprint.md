# SRS STRUCTURAL BLUEPRINT - Sarawak Tourism Promotion System

- Document: Software Requirements Specification (SRS) skeleton / blueprint only
- Unit: COS30003 Assignment 1
- Agency: Swinsoft Consulting
- Client: Management team of a local tourism association (referred to as "the Association")
- Audience: worldwide tourists + Association management/content staff + Swinsoft development team
- Method: Tasks & Support approach (Lauesen); Goal-Design Scale for requirement placement
- Status: blueprint = bullets + logic structures + IDs; NO final prose

---

## A. DOCUMENT SECTION TREE (numbered)

- FRONT MATTER
  - FM-1 Title Page
    - unit code COS30003; assignment title; system name; author name + student ID (jarrentannn@gmail.com as author identity); tutor/lecturer; submission date; document version
  - FM-2 Document Control / Revision History
    - table columns: Version | Date | Author | Section(s) | Change summary | Reason
  - FM-3 Table of Contents
    - auto-generated; section + subsection numbers; page numbers
  - FM-4 List of Figures
    - Fig entries: context diagram, domain model, each workflow activity diagram
  - FM-5 List of Tables
    - Table entries: assumptions, actors, each task table, NFR fit-criteria tables, CRUD matrix, traceability matrix, validation logs
  - FM-6 List of Abbreviations
    - SRS, NFR, PDPA, CRUD, RBAC, RTO, RPO, MTBF, MTTR, SUS, WCAG, CMS, SEO, COTS

- 1 Introduction
  - 1.1 Purpose of the document
  - 1.2 Scope of the system (in-scope / out-of-scope pointers -> section 2.7)
  - 1.3 Intended readership (tourists' representatives, Association management, content staff, developers, assessor)
  - 1.4 Document overview (section-by-section map)
  - 1.5 References (project brief; Lauesen Tasks & Support; PDPA 2010; WCAG 2.1; rubric)
  - 1.6 Definitions pointer -> Glossary (section 14)
  - 1.7 Requirement ID scheme and verifiability statement (see section D)

- 2 Project Goals & Assumptions
  - 2.1 Project Type (statement + justification)
  - 2.2 Existing Process Description (as-is)
  - 2.3 Pain Points in the Existing Process (IDed: PAIN-01..)
  - 2.4 Goals (goal-level, outcome statements: REQ-GOAL-001..)
  - 2.5 Objectives (measurable + time-bound; each traced to a goal: OBJ-01..)
  - 2.6 Incentives (business case / funding rationale / expected uplift: INC-01..)
  - 2.7 Scope (in-scope list / out-of-scope list)
  - 2.8 Constraints (CON-01..: regulatory/PDPA, languages, rural bandwidth, hosting, budget, timeline, technology)
  - 2.9 Assumptions (numbered ASM-01..; one-line justification; link to a constraint/scope item; software-only elaboration; hardware/data repositories/deployment platforms already acquired)

- 3 System Context
  - 3.1 System Boundary (what is inside the system under specification)
  - 3.2 Context Diagram (Fig) - system + all external entities, solution-agnostic
  - 3.3 External Entities - human (EXT-H-01..)
  - 3.4 External Entities - external systems/services (EXT-S-01..), described as external interactions only
  - 3.5 Context Interactions Table (entity <-> system, information exchanged, direction)

- 4 Domain Model
  - 4.1 Modelling rules (conceptual only; NO attributes / keys / data types / tables)
  - 4.2 Entity List with one-line descriptions (ENT-01..)
  - 4.3 Relationships + cardinality/multiplicity (REL-01..)
  - 4.4 Domain Model Diagram (Fig)
  - 4.5 Entity-to-Task coverage note (forward reference to CRUD matrix)

- 5 Actors
  - 5.1 Actor catalogue (ACT-01..; one-line role)
  - 5.2 Actor-to-task mapping summary
  - 5.3 User profiles / work-area background (per actor: environment, skill level, frequency, device/bandwidth context)

- 6 User Tasks (Tasks & Support)
  - 6.1 Work Area / background block (overall purpose of the work; environment; grouping of tasks by work area)
  - 6.2 Tasks & Support format definition (fields used in every task table)
  - 6.3 TASK-01 .. 6.10 TASK-08 (one subsection per task; identical IDs/names reused everywhere)
  - 6.11 Typical sub-task sequence note (sequence not mandatory)
  - 6.12 Task-to-actor and task-to-entity coverage statement

- 7 Workflows
  - 7.1 Workflow notation (UML activity: swimlanes per actor, decision/merge, fork/join, initial/final)
  - 7.2 WF-01 End-to-end tourist journey workflow
  - 7.3 WF-02 Content & promotion publishing workflow
  - 7.4 WF-03 Booking + payment workflow (external payment interaction)
  - 7.5 WF-04 Enquiry / support handling workflow
  - 7.6 WF-05 Listing onboarding & moderation workflow
  - 7.7 Workflow-to-task coverage table (WF -> TASK IDs)

- 8 Non-Functional Requirements
  - 8.1 NFR method (fit-criterion structure: metric | scale | target | worst acceptable | measuring instrument | verification method | priority)
  - 8.2 NFR-USAB Usability, Accessibility & Multilingual
  - 8.3 NFR-PERF Performance & Scalability
  - 8.4 NFR-SEC Security & Privacy (PDPA 2010)
  - 8.5 NFR-AVAIL Availability & Reliability
  - (exactly 4 categories; no more, no fewer)

- 9 Other Requirements (Goal-Design Scale)
  - 9.1 Placement on Goal-Design Scale (diagram/table: Goal -> Domain -> Product -> Design)
  - 9.2 Product-level requirements (REQ-PROD-001..)
  - 9.3 Design-level requirements (REQ-DES-001..)
  - 9.4 Functional requirement stubs derived from tasks (REQ-FUN-001..)
  - 9.5 PDPA 2010 requirements (verifiable; cross-listed with NFR-SEC) (REQ-PROD-PDPA-01.. / mapped to NFR-SEC)
  - 9.6 Data lifecycle requirements (retention, archival, anonymisation, backup, DR)
  - 9.7 Integration/interoperability requirements (external interactions, solution-agnostic)
  - 9.8 Reporting & analytics requirements
  - 9.9 Content management & multilingual authoring requirements
  - 9.10 Low-bandwidth / rural / offline-tolerant behaviour requirements
  - 9.11 Operations requirements (monitoring, logging, support levels, maintenance windows, training materials, third-party/open-source licensing)

- 10 Verifiability Approach
  - 10.1 Rule: every requirement has a unique ID + measurable fit criterion + verification method (test | demonstration | inspection | analysis)
  - 10.2 Subjective-term ban list + replacement metrics
  - 10.3 Self-audit table plan (Requirement ID | fit criterion present? | verification method | acceptance test)

- 11 Validation
  - 11.1 Validation strategy overview
  - 11.2 Stakeholders consulted (roles, dates placeholder)
  - 11.3 Validation activities list (walkthroughs, sign-off, task-completeness check, scenario/prototype walkthrough, NFR target validation, assumption confirmation)
  - 11.4 Before/after requirement change log plan
  - 11.5 Pointer to Appendices for evidence

- 12 Traceability
  - 12.1 Traceability matrix plan (see section H)
  - 12.2 CRUD completeness matrix plan (Task x Entity)

- 13 Appendices
  - Appendix A Validation evidence (review walkthrough notes, inspection checklist + defects log, stakeholder sign-off record)
  - Appendix B Requirement-to-task traceability matrix (full)
  - Appendix C CRUD completeness check (full, every entity x every task, anomalies flagged)
  - Appendix D Self-audit verifiability table
  - Appendix E Scenario / prototype walkthrough results
  - Appendix F Assumption confirmation record
  - Appendix G PDPA interpretation validation record
  - Appendix H Optional solution options (clearly non-normative; not requirements)

- 14 Glossary / Domain Vocabulary

---

## B. SECTION 2 CONTENT SKELETON

- 2.1 Project Type
  - TYPE: new custom-built public-facing tourism promotion software product commissioned by the Association, developed by Swinsoft, integrating with pre-existing external services
  - NOT: COTS-only acquisition; NOT internal-only tool
  - justification bullets: public worldwide audience; Association-specific branding + content workflow; multilingual + PDPA obligations; need for controlled content/database management

- 2.3 Pain Points (existing process)
  - PAIN-01 tourism information fragmented across brochures/third-party sites; no single authoritative source
  - PAIN-02 accommodation/transport/food/local info not consolidated; tourists cross-reference many sources
  - PAIN-03 promotional content updates are manual, slow, and inconsistent across channels
  - PAIN-04 no structured way for management to maintain listings/events data -> stale/incorrect entries
  - PAIN-05 no consolidated view of tourist interest/engagement to guide promotion decisions
  - PAIN-06 enquiries handled ad hoc (email/phone); no tracking, slow response, lost requests
  - PAIN-07 language barrier; existing material mostly single-language
  - PAIN-08 poor reach in rural Sarawak due to bandwidth and offline conditions
  - PAIN-09 no verifiable safeguarding of tourist personal data against PDPA 2010

- 2.4 Goals (REQ-GOAL-001..)
  - REQ-GOAL-001 provide a single authoritative source of Sarawak tourism information for worldwide tourists
  - REQ-GOAL-002 consolidate accommodation, transportation, food, and local information in one place
  - REQ-GOAL-003 enable the Association to manage content and domain data without developer involvement
  - REQ-GOAL-004 increase measurable tourist engagement and trip planning completion
  - REQ-GOAL-005 shorten and standardise promotional content publishing
  - REQ-GOAL-006 give management evidence-based insight into tourist interest
  - REQ-GOAL-007 make information reachable in multiple languages and in low-bandwidth areas
  - REQ-GOAL-008 protect personal data in compliance with PDPA 2010

- 2.5 Objectives (OBJ-01..; metric + target + deadline; each -> a goal)
  - OBJ-01 [-> GOAL-002] single portal covering all 4 information categories at launch (100% categories, by go-live)
  - OBJ-02 [-> GOAL-005] content publish cycle time <= X hours within 3 months of launch
  - OBJ-03 [-> GOAL-004] itinerary-plan completion rate >= X% within 6 months
  - OBJ-04 [-> GOAL-006] management analytics report available at frequency X from go-live
  - OBJ-05 [-> GOAL-007] >= K languages supported at launch; key pages usable at <= Y KB payload
  - OBJ-06 [-> GOAL-008] 100% of personal-data flows covered by a verifiable PDPA control by go-live
  - OBJ-07 [-> GOAL-006] enquiry first-response time <= X hours within 3 months

- 2.6 Incentives (INC-01..)
  - INC-01 expected uplift in visitor numbers / length of stay / tourism spend (target placeholder)
  - INC-02 reduced staff effort/cost for content maintenance and enquiry handling
  - INC-03 stronger destination brand and channel consistency
  - INC-04 data-driven promotion budget allocation
  - INC-05 regulatory risk reduction (PDPA 2010 penalties avoided)
  - INC-06 funding rationale: Association marketing budget + potential government tourism grant

- 2.7 Scope
  - IN-SCOPE: information portal for tourists; content/data management for management; multilingual delivery; enquiry capture and handling; analytics/reporting; PDPA controls; defined external interactions
  - OUT-OF-SCOPE: building payment processing itself; building mapping/weather/data providers; operator internal systems; hardware/network/deployment platform procurement; physical tourism operations

- 2.8 Constraints (CON-01..)
  - CON-01 PDPA 2010 compliance mandatory
  - CON-02 languages: Bahasa Malaysia + English + Mandarin + others as directed by Association
  - CON-03 rural Sarawak low-bandwidth / intermittent connectivity reality
  - CON-04 hosting location and any cross-border data transfer must be addressed with safeguards
  - CON-05 fixed academic timeline / assignment submission date
  - CON-06 budget ceiling set by Association
  - CON-07 must reuse already-acquired data repositories, hardware, and deployment platforms
  - CON-08 accessibility target WCAG 2.1 AA

- 2.9 Assumptions (ASM-01..; each: statement | justification | linked CON/scope)
  - ASM-01 data repositories already acquired and available | brief ground rule | CON-07
  - ASM-02 hardware/servers already acquired | brief ground rule | CON-07
  - ASM-03 deployment platform already provisioned | brief ground rule | CON-07
  - ASM-04 only software is to be specified/elaborated | brief ground rule | scope
  - ASM-05 external payment service exists and is contracted separately | out-of-scope item | 2.7
  - ASM-06 external mapping/geolocation service available | out-of-scope item | 2.7
  - ASM-07 external weather/advisory source available | out-of-scope item | 2.7
  - ASM-08 external email/SMS delivery service available | out-of-scope item | 2.7
  - ASM-09 Association will supply and own tourism content and translations | client responsibility | CON-02
  - ASM-10 tourism operators/providers supply listing details to the Association | client process | domain
  - ASM-11 management users are trained office staff with basic web-tool skills | user profile | 5.3
  - ASM-12 tourists use personal internet-connected devices, browser-based | user profile | CON-03
  - ASM-13 network connectivity to external services is available at the deployment site | infra | CON-07
  - ASM-14 legal/compliance advisor available to validate PDPA interpretation | validation | CON-01
  - ASM-15 expected concurrent-user peak occurs during festivals/campaigns | sizing | NFR-PERF

---

## C. SECTION 3 SYSTEM CONTEXT SKELETON

- 3.1 System Boundary
  - INSIDE: tourist-facing information portal; content & domain-data management function; enquiry capture/handling; analytics/reporting; multilingual delivery; consent/privacy handling
  - OUTSIDE: all external human roles + all external services listed below

- 3.3 External human entities (EXT-H)
  - EXT-H-01 Tourist (worldwide, anonymous or identified)
  - EXT-H-02 Association Management User (oversight, approvals, analytics consumer)
  - EXT-H-03 Content Administrator / Editor (maintains content and domain data)
  - EXT-H-04 Enquiry Handler / Support Officer
  - EXT-H-05 Tourism Provider / Operator contact (supplies listing information via the Association)
  - EXT-H-06 System/Platform Administrator (accounts, access, operations)
  - EXT-H-07 Compliance/Legal Advisor (PDPA oversight)

- 3.4 External systems/services (EXT-S) - modelled as external interactions only, solution-agnostic
  - EXT-S-01 Payment service (payment authorisation/confirmation interaction)
  - EXT-S-02 Mapping / geolocation service (location and routing information)
  - EXT-S-03 Weather / travel-advisory source (conditions information)
  - EXT-S-04 Notification service (email / SMS delivery)
  - EXT-S-05 Social media / external publishing channels (outbound promotion)
  - EXT-S-06 External tourism / government data sources (reference information)
  - EXT-S-07 Web analytics / tracking service (engagement data, consent-gated)
  - EXT-S-08 Identity / authentication provider (optional external sign-in interaction)

- 3.5 Context Interactions Table columns
  - External Entity | Information INTO system | Information OUT OF system | Trigger | Notes (solution-agnostic)

---

## D. REQUIREMENT ID SCHEME (global)

- REQ-GOAL-xxx  : goal-level outcome statements (section 2.4)
- OBJ-xx        : measurable objectives (section 2.5)
- INC-xx        : incentives / business case (section 2.6)
- PAIN-xx       : existing-process pain points (section 2.3)
- CON-xx        : constraints (section 2.8)
- ASM-xx        : assumptions (section 2.9)
- ENT-xx / REL-xx : domain entities / relationships (section 4)
- ACT-xx        : actors (section 5)
- TASK-0x       : major user tasks in Tasks & Support format (section 6) - exactly 8
- WF-0x         : workflows (section 7)
- REQ-FUN-xxx   : functional requirement stubs derived from tasks (section 9.4)
- NFR-USAB-xx / NFR-PERF-xx / NFR-SEC-xx / NFR-AVAIL-xx : non-functional (section 8) - exactly 4 categories
- REQ-PROD-xxx  : product-level requirements (section 9.2)
- REQ-DES-xxx   : design-level requirements (section 9.3)
- REQ-PROD-PDPA-xx : PDPA-specific product requirements (section 9.5), each also mapped to NFR-SEC
- RULES:
  - every ID unique and stable across all sections, diagrams, tables
  - every requirement (TASK example-solution items, REQ-FUN, REQ-PROD, REQ-DES, all NFR) MUST carry a measurable fit criterion + a verification method (test | demonstration | inspection | analysis)
  - no subjective terms (easy, fast, user-friendly, secure, robust, seamless, appropriate, relevant, quickly)
  - task names + IDs identical in sections 4, 6, 7, CRUD matrix, traceability matrix

---

## E. SECTION 4 DOMAIN MODEL SKELETON (entities + relationships ONLY - NO attributes/keys/types/tables)

- 4.2 Entity list (ENT-xx | one-line description)
  - ENT-01 Tourist - a person worldwide who uses the system to discover and plan Sarawak travel
  - ENT-02 Association - the tourism association that owns and promotes the destination information
  - ENT-03 ManagementUser - an Association staff member who maintains content and domain data
  - ENT-04 TourismProvider - an operator/business whose offering is listed (accommodation, transport, food, activity)
  - ENT-05 Attraction - a place or point of interest promoted to tourists
  - ENT-06 Event - a scheduled happening of tourist interest (festival, show, seasonal activity)
  - ENT-07 Accommodation - a place to stay presented to tourists
  - ENT-08 Transportation - a means/route of travel presented to tourists
  - ENT-09 FoodOption - an eating establishment or culinary experience presented to tourists
  - ENT-10 LocalInformation - practical destination guidance (customs, safety, currency, connectivity)
  - ENT-11 Listing - a promoted entry describing a provider offering or place, shown to tourists
  - ENT-12 ContentItem - a unit of editorial/promotional material (article, guide, media set)
  - ENT-13 PromotionCampaign - a coordinated promotional effort over a period and channels
  - ENT-14 Itinerary - a tourist's assembled plan of places, events, stays, and movements
  - ItineraryItem - a single planned element within an itinerary (kept as concept, not a data row)
  - ENT-15 Booking - a tourist's reservation request against a listing/offering
  - ENT-16 Payment - a record of a financial settlement associated with a booking (external processing)
  - ENT-17 Review - a tourist's published opinion and rating of a listing/attraction/experience
  - ENT-18 EnquiryTicket - a tourist request for help/information tracked to resolution
  - ENT-19 Language - a supported language in which information is offered
  - ENT-20 Translation - a language-specific rendering of a content item or listing
  - ENT-21 EngagementRecord - an observation of tourist interaction used for analytics (consent-gated)
  - ENT-22 AnalyticsReport - a compiled summary of engagement/booking/campaign performance for management
  - ENT-23 ConsentRecord - a tourist's recorded permission covering data use and marketing
  - ENT-24 UserAccount - a credentialed identity for a ManagementUser or identified Tourist
  - ENT-25 Role - a named set of permissions assigned to a UserAccount
  - ENT-26 Region - a geographic area of Sarawak used to group attractions/listings/events
  - ENT-27 Category - a classification label applied to listings/attractions/content

- 4.3 Relationships (REL-xx | entities | cardinality | named)
  - REL-01 Association employs ManagementUser (1 .. 1..*)
  - REL-02 ManagementUser maintains ContentItem (1..* .. 0..*)
  - REL-03 ManagementUser maintains Listing (1..* .. 0..*)
  - REL-04 TourismProvider supplies Listing (1 .. 1..*)
  - REL-05 Listing describes one of {Accommodation | Transportation | FoodOption | Attraction | Event} (1 .. 0..1 per type)
  - REL-06 Attraction located in Region (0..* .. 1)
  - REL-07 Event held at Attraction / in Region (0..* .. 0..1 / 1)
  - REL-08 Listing classified by Category (0..* .. 0..*)
  - REL-09 Attraction classified by Category (0..* .. 0..*)
  - REL-10 PromotionCampaign promotes ContentItem / Listing (0..* .. 0..*)
  - REL-11 ManagementUser plans PromotionCampaign (1..* .. 0..*)
  - REL-12 Tourist builds Itinerary (1 .. 0..*)
  - REL-13 Itinerary includes ItineraryItem (1 .. 0..*)
  - REL-14 ItineraryItem references {Attraction | Event | Accommodation | Transportation | FoodOption} (1 .. 1)
  - REL-15 Tourist makes Booking (1 .. 0..*)
  - REL-16 Booking placed against Listing (0..* .. 1)
  - REL-17 Booking settled by Payment (1 .. 0..1)
  - REL-18 Payment processed via external Payment service (association to EXT-S-01, modelled as external)
  - REL-19 Tourist writes Review (1 .. 0..*)
  - REL-20 Review targets {Listing | Attraction | Event} (0..* .. 1)
  - REL-21 Tourist raises EnquiryTicket (1 .. 0..*)
  - REL-22 EnquiryHandler (ManagementUser) resolves EnquiryTicket (1 .. 0..*)
  - REL-23 ContentItem has Translation in Language (1 .. 0..*)
  - REL-24 Listing has Translation in Language (1 .. 0..*)
  - REL-25 Tourist prefers Language (0..* .. 1)
  - REL-26 Tourist generates EngagementRecord (1 .. 0..*)
  - REL-27 AnalyticsReport aggregates EngagementRecord / Booking / PromotionCampaign (1 .. 1..*)
  - REL-28 ManagementUser generates AnalyticsReport (1..* .. 0..*)
  - REL-29 Tourist gives ConsentRecord (1 .. 0..*)
  - REL-30 ConsentRecord governs EngagementRecord and marketing to Tourist (1 .. 0..*)
  - REL-31 UserAccount identifies {ManagementUser | Tourist} (1 .. 0..1)
  - REL-32 UserAccount assigned Role (1..* .. 1..*)
  - REL-33 Role authorises access to {ContentItem | Listing | EnquiryTicket | AnalyticsReport} operations (conceptual)
  - REL-34 Region groups Listing (1 .. 0..*)
  - REL-35 LocalInformation scoped to Region (0..* .. 0..1)

- 4.5 note: every ENT-xx must appear in >= 1 TASK and in the CRUD matrix; flag any that do not

---

## F. SECTION 5 ACTORS SKELETON (ACT-xx | one-line role)

- ACT-01 Tourist (Anonymous) - browses and searches destination information without an account
- ACT-02 Tourist (Registered) - saves itineraries, makes bookings, writes reviews, manages own personal data and consent
- ACT-03 Association Management User - sets promotion direction, approves content, consumes analytics
- ACT-04 Content Administrator / Editor - creates, updates, translates, publishes content and listings
- ACT-05 Enquiry Handler / Support Officer - triages and resolves tourist enquiry tickets
- ACT-06 Campaign Manager - plans, schedules, and evaluates promotion campaigns
- ACT-07 System / Platform Administrator - manages accounts, roles, access, operational monitoring
- ACT-08 Data Protection Officer / Compliance Advisor - defines and audits PDPA controls
- ACT-09 Tourism Provider / Operator (external, via submission) - supplies and updates offering information for listings
- ACT-10 External Payment Service - authorises and confirms payment (non-human actor)
- ACT-11 External Mapping / Geolocation Service - supplies location and routing information (non-human actor)
- ACT-12 External Weather / Advisory Source - supplies conditions and advisory information (non-human actor)
- ACT-13 External Notification Service - delivers email/SMS messages (non-human actor)
- ACT-14 External Publishing / Social Channels - receive outbound promotional content (non-human actor)
- ACT-15 Scheduled Time / System Clock - triggers time-based tasks (campaign start/stop, retention purge) (non-human actor)

---

## G. SECTION 6 USER TASKS - EXACTLY 8 (Tasks & Support style)

- Every task table fields: Task ID + Name | Actor(s) | Goal/Purpose | Trigger/Precondition | Frequency (quantified placeholder) | Critical (quantified worst case) | Work Area | Sub-tasks (imperative, domain-level) | Problem (present-situation) | Support the system provides (solution-agnostic) | Example Solution (clearly non-normative) | Variants (numbered 1a,1b,2a...)
- Rule: each task description applicable to >= 3 different solutions; no "system shall"; no human/computer split in sub-tasks

- TASK-01 Discover attractions and experiences
  - Actor: ACT-01, ACT-02
  - Goal: find relevant Sarawak attractions, events, food, stays, transport matching interests/constraints
  - Sub-tasks: state interests/constraints; browse by region/category; inspect a listing; compare options; save candidates
  - Problem (PAIN-01, PAIN-02, PAIN-07): information scattered; no comparison; language barrier
  - Support: consolidated searchable information; filtering by region/category/interest; side-by-side comparison; multilingual presentation; shortlist retention
  - Entities: Attraction, Event, Accommodation, Transportation, FoodOption, Listing, Category, Region, Language, Translation, EngagementRecord

- TASK-02 Plan and assemble a trip itinerary
  - Actor: ACT-02
  - Goal: turn shortlisted items into a coherent day-by-day plan
  - Sub-tasks: create a plan; add items to days; order/adjust items; check timing/feasibility; review and finalise plan
  - Problem (PAIN-02, PAIN-01): tourists build plans manually across sources; no feasibility feedback
  - Support: itinerary assembly; per-day organisation; feasibility/timing indication using external location/weather information; plan review
  - Entities: Itinerary, ItineraryItem, Attraction, Event, Accommodation, Transportation, FoodOption

- TASK-03 Reserve an offering (accommodation/transport/activity)
  - Actor: ACT-02
  - Goal: secure a place against a chosen listing
  - Sub-tasks: select a listing and dates/quantity; provide traveller details; confirm terms and consent; submit reservation request; receive reservation outcome
  - Problem (PAIN-02, PAIN-06): fragmented booking across providers; no single confirmation trail
  - Support: capture of reservation request; validation of availability details; consent capture; confirmation and record of outcome
  - Entities: Booking, Listing, TourismProvider, Tourist, ConsentRecord

- TASK-04 Make and confirm payment
  - Actor: ACT-02, ACT-10
  - Goal: settle the amount due for a booking and obtain confirmation
  - Sub-tasks: review amount due; choose payment method; authorise payment via external service; obtain payment outcome; attach outcome to booking
  - Problem (PAIN-06): no linked payment/confirmation record; manual reconciliation
  - Support: presentation of amount due; hand-off to an external payment interaction; capture of payment outcome; linkage of payment to booking; receipt issue
  - Entities: Payment, Booking, Tourist; external EXT-S-01

- TASK-05 Maintain destination content and listings (multilingual)
  - Actor: ACT-04, ACT-09 (as supplier), ACT-03 (approver)
  - Goal: keep attractions/events/listings/local information accurate and available in supported languages
  - Sub-tasks: draft or update an entry; classify by region/category; add language translations; submit for approval; publish or withdraw
  - Problem (PAIN-03, PAIN-04, PAIN-07): manual, slow, inconsistent updates; stale data; single language
  - Support: authoring of content/listings; classification; translation management; approval routing; publish/withdraw control
  - Entities: ContentItem, Listing, Attraction, Event, Accommodation, Transportation, FoodOption, LocalInformation, Category, Region, Language, Translation

- TASK-06 Plan and run a promotion campaign
  - Actor: ACT-06, ACT-03
  - Goal: coordinate a themed promotion over a period and channels and evaluate its result
  - Sub-tasks: define campaign theme/period/audience; select content/listings to feature; schedule start and end; publish to channels; review campaign performance
  - Problem (PAIN-03, PAIN-05): channel inconsistency; no measurement of promotion effect
  - Support: campaign definition; association of featured items; scheduling by time; outbound publishing to external channels; performance summary
  - Entities: PromotionCampaign, ContentItem, Listing, AnalyticsReport, EngagementRecord; external EXT-S-05; ACT-15 trigger

- TASK-07 Handle a tourist enquiry / support request
  - Actor: ACT-01/ACT-02 (raiser), ACT-05 (handler)
  - Goal: capture, track, and resolve a tourist's question or problem
  - Sub-tasks: submit an enquiry with context; acknowledge receipt; assign and investigate; respond with resolution; close and record outcome
  - Problem (PAIN-06): enquiries via phone/email untracked; slow, lost requests
  - Support: structured enquiry capture; acknowledgement; assignment and status tracking; response delivery via notification interaction; resolution record
  - Entities: EnquiryTicket, Tourist, ManagementUser; external EXT-S-04

- TASK-08 Produce tourism engagement and performance insight
  - Actor: ACT-03, ACT-06
  - Goal: obtain evidence on tourist interest, booking funnel, content engagement, and campaign performance
  - Sub-tasks: choose the question/period/segment; assemble relevant engagement and booking data; view the compiled summary; compare against targets/prior periods; export or share the summary
  - Problem (PAIN-05): no consolidated insight to direct promotion spend
  - Support: selection of scope; aggregation of consent-gated engagement, booking, and campaign data; compiled summary presentation; comparison; export/share
  - Entities: AnalyticsReport, EngagementRecord, Booking, PromotionCampaign, ConsentRecord

- 6.11 coverage checks
  - actors covered: ACT-01..ACT-06, ACT-09, ACT-10 direct; ACT-07/ACT-08 via section 9 operations/PDPA; ACT-11..ACT-15 via external interactions
  - high-level journey task: TASK-01 -> TASK-02 -> TASK-03 -> TASK-04 -> (travel) -> TASK-07 (support) -> Review (see REQ-FUN + WF-01); note Review captured as sub-flow of WF-01
  - confirm every ENT-xx touched by >= 1 task (map in CRUD matrix; Review + ConsentRecord + UserAccount + Role coverage noted in section 9 + WF)

---

## H. SECTION 7 WORKFLOWS SKELETON

- WF-01 End-to-end tourist journey
  - steps: discover [TASK-01] -> plan itinerary [TASK-02] -> reserve offering [TASK-03] -> pay and confirm [TASK-04] -> receive notifications [EXT-S-04] -> travel/on-trip use of local info -> submit review (REQ-FUN review) -> engagement recorded [feeds TASK-08]
  - swimlanes: Tourist | System | External Payment | External Notification
  - decisions: item available? payment authorised? consent given?
  - covers: TASK-01, TASK-02, TASK-03, TASK-04, TASK-07 (optional branch)

- WF-02 Content & promotion publishing
  - steps: provider submits offering [ACT-09] -> editor drafts/updates entry [TASK-05] -> classify + translate [TASK-05] -> management approval [ACT-03] -> publish [TASK-05] -> feature in campaign [TASK-06] -> schedule start/stop [ACT-15] -> publish to channels [EXT-S-05] -> review performance [TASK-06/TASK-08]
  - swimlanes: Provider | Editor | Management | System | External Channels
  - decisions: approved? translations complete for required languages? campaign period active?
  - covers: TASK-05, TASK-06, TASK-08

- WF-03 Booking + payment (detailed)
  - steps: select listing [TASK-03] -> check availability details -> capture traveller details + consent [TASK-03] -> create reservation request -> present amount due [TASK-04] -> authorise via external payment [EXT-S-01] -> capture outcome -> confirm/decline booking -> notify tourist [EXT-S-04]
  - decisions: available? consent captured? payment authorised? timeout?
  - covers: TASK-03, TASK-04

- WF-04 Enquiry / support handling (detailed)
  - steps: tourist submits enquiry [TASK-07] -> auto-acknowledge [EXT-S-04] -> triage/assign [ACT-05] -> investigate (may reference booking/itinerary/listing) -> respond [EXT-S-04] -> tourist confirms or reopens -> close + record [TASK-07] -> feed volume/response metrics [TASK-08]
  - decisions: needs escalation? resolved? reopened?
  - covers: TASK-07, TASK-08

- WF-05 Listing onboarding & moderation
  - steps: provider submits details [ACT-09] -> editor validates/classifies [TASK-05] -> compliance/licensing check [ACT-08] -> approve/reject [ACT-03] -> publish listing [TASK-05] -> tourists review published listing (Review) -> editor moderates reviews -> update or withdraw listing [TASK-05]
  - decisions: licensing valid? content complete? review compliant?
  - covers: TASK-05 (+ Review moderation), TASK-01 (consumption)

- 7.7 Workflow-to-task coverage table columns: WF ID | WF name | TASK IDs covered | Actors | External entities | Key decisions

---

## I. SECTION 8 NON-FUNCTIONAL REQUIREMENTS - EXACTLY 4 CATEGORIES

- fit-criterion template per stub: METRIC | SCALE/UNIT | TARGET (placeholder) | WORST ACCEPTABLE (placeholder) | MEASURING INSTRUMENT | VERIFICATION METHOD | PRIORITY | TRACE (goal/pain)

- 8.2 NFR-USAB - Usability, Accessibility & Multilingual  (trace: REQ-GOAL-004, GOAL-007; PAIN-07)
  - NFR-USAB-01 first-time tourist completes discover->plan->reserve without assistance | task completion rate % + time in minutes | target/worst placeholders | moderated usability test | test | high
  - NFR-USAB-02 measured satisfaction score | SUS score 0-100 | target >= placeholder | SUS questionnaire, n>=placeholder | test | high
  - NFR-USAB-03 language coverage of tourist-facing information | count of fully translated languages incl. Bahasa Malaysia, English, Mandarin | target = K | content audit | inspection | high
  - NFR-USAB-04 accessibility conformance | WCAG 2.1 level | target = AA, 0 level-A/AA violations on key pages | automated + manual audit | inspection | medium

- 8.3 NFR-PERF - Performance & Scalability  (trace: REQ-GOAL-001, GOAL-007; PAIN-08; ASM-15)
  - NFR-PERF-01 information search response time | seconds at 95th percentile | target <= placeholder s | load-test tool | test | high
  - NFR-PERF-02 key page delivered payload / first render on low bandwidth | KB and seconds at defined bandwidth | target <= placeholder | synthetic throttled test | test | high
  - NFR-PERF-03 concurrent active users sustained at festival/campaign peak with metrics within target | concurrent user count | target >= placeholder with no target breach | load-test tool | test | high
  - NFR-PERF-04 graceful degradation when external service unavailable | measured functional-availability % of core browse/plan | target >= placeholder | fault-injection test | demonstration | medium

- 8.4 NFR-SEC - Security & Privacy (PDPA 2010)  (trace: REQ-GOAL-008; PAIN-09; CON-01)
  - NFR-SEC-01 personal data encrypted in transit and at rest | % of personal-data stores/channels using approved encryption | target = 100% | configuration audit | inspection | high
  - NFR-SEC-02 access enforced by role-based access control | % of privileged operations gated by Role | target = 100%, 0 unauthorised-access findings | access-control test | test | high
  - NFR-SEC-03 security assessment / penetration test | count of unresolved high/critical findings | target = 0 before go-live | third-party pen test | test | high
  - NFR-SEC-04 personal-data breach response and notification | elapsed time from detection to containment + notification | target <= placeholder hours | incident drill | demonstration | high
  - (PDPA obligation stubs enumerated in section 9.5; each mapped here)

- 8.5 NFR-AVAIL - Availability & Reliability  (trace: REQ-GOAL-001; PAIN-01)
  - NFR-AVAIL-01 service uptime measured monthly excluding scheduled maintenance | availability % | target >= placeholder %, worst >= placeholder % | uptime monitor | analysis | high
  - NFR-AVAIL-02 recovery objectives after major failure | RTO hours / RPO minutes | targets = placeholders | DR test | demonstration | high
  - NFR-AVAIL-03 reliability of core booking/enquiry transactions | MTBF hours / MTTR minutes / failed-transaction % | targets = placeholders | operational log analysis | analysis | medium

---

## J. SECTION 9 OTHER REQUIREMENTS - STUBS ACROSS GOAL-DESIGN SCALE

- 9.1 Goal-Design Scale placement table columns: Requirement ID | Statement (short) | Scale position (Goal / Domain / Product / Design) | Traces to | Priority | Fit criterion ref | Verification method

- 9.4 Functional stubs from tasks (REQ-FUN-xxx) - one or more per task
  - REQ-FUN-001 provide consolidated search/browse of all offering types [TASK-01]
  - REQ-FUN-002 provide filtering by region, category, interest, language [TASK-01]
  - REQ-FUN-003 provide comparison of shortlisted offerings [TASK-01]
  - REQ-FUN-004 provide itinerary creation and per-day organisation [TASK-02]
  - REQ-FUN-005 provide feasibility/timing indication using external location/weather info [TASK-02]
  - REQ-FUN-006 provide reservation-request capture against a listing [TASK-03]
  - REQ-FUN-007 provide consent capture at data collection points [TASK-03, PDPA]
  - REQ-FUN-008 provide amount-due presentation and external payment hand-off [TASK-04]
  - REQ-FUN-009 record payment outcome and link to booking; issue receipt [TASK-04]
  - REQ-FUN-010 provide content/listing authoring, classification, publish/withdraw [TASK-05]
  - REQ-FUN-011 provide translation management for required languages [TASK-05]
  - REQ-FUN-012 provide approval routing for content/listings [TASK-05]
  - REQ-FUN-013 provide campaign definition, scheduling, channel publishing [TASK-06]
  - REQ-FUN-014 provide enquiry capture, acknowledgement, assignment, status tracking, closure [TASK-07]
  - REQ-FUN-015 provide analytics compilation across engagement/booking/campaign data [TASK-08]
  - REQ-FUN-016 provide tourist review submission and moderation [WF-01, WF-05]
  - REQ-FUN-017 provide tourist self-service view/correction of own personal data [PDPA]
  - REQ-FUN-018 provide account, role, and access administration [ACT-07]
  - each REQ-FUN gets: fit criterion = "carry out the task and all its variants successfully" + specific measurable acceptance test + verification method

- 9.2 Product-level requirements (REQ-PROD-xxx)
  - REQ-PROD-001 data retention period defined per data category; enforced deletion/anonymisation after period | fit: 100% categories have a stated period; purge job verifiable
  - REQ-PROD-002 backup frequency and restore capability | fit: backup interval <= placeholder; successful restore test
  - REQ-PROD-003 disaster recovery capability | fit: meets NFR-AVAIL-02 RTO/RPO
  - REQ-PROD-004 audit logging of privileged and personal-data operations | fit: 100% of defined operation types logged; log fields defined at business level (no schema)
  - REQ-PROD-005 outbound notification delivery via external service | fit: delivery outcome recorded for 100% of sends
  - REQ-PROD-006 integration points enumerated and version-controlled (payment, mapping, weather, notification, channels, analytics, external data) | fit: each has a defined interface contract + failure behaviour
  - REQ-PROD-007 reporting set: campaign performance, visitor trends, booking funnel, content engagement | fit: each report defined with inputs, period, segments
  - REQ-PROD-008 multilingual content authoring + publishing workflow | fit: required-language completeness check blocks publish
  - REQ-PROD-009 low-bandwidth / offline-tolerant behaviour for defined key pages | fit: meets NFR-PERF-02; defined offline-available content set
  - REQ-PROD-010 discoverability / SEO for public tourist pages | fit: defined metadata present on 100% of public pages; measurable index coverage
  - REQ-PROD-011 tourism-operator licensing/eligibility check before listing publish | fit: 100% published listings have a recorded check outcome
  - REQ-PROD-012 consumer-protection / terms + privacy notice presentation | fit: shown and acknowledged before booking and before data collection
  - REQ-PROD-013 operational monitoring + alerting | fit: defined metric set monitored; alert threshold per metric
  - REQ-PROD-014 support levels + maintenance windows published | fit: response targets per severity; maintenance window schedule stated
  - REQ-PROD-015 training materials for management users | fit: coverage of 100% of TASK-05..TASK-08 procedures
  - REQ-PROD-016 third-party / open-source component licensing register | fit: 100% components have a recorded licence + compatibility check
  - REQ-PROD-017 cross-border data transfer safeguards for hosting outside Malaysia | fit: safeguard + consent recorded for 100% of such transfers
  - REQ-PROD-018 direct-marketing opt-out honoured | fit: opt-out effective within placeholder time; testable suppression
  - REQ-PROD-019 cookies/tracking consent gate for analytics | fit: no EngagementRecord for marketing analytics without ConsentRecord

- 9.3 Design-level requirements (REQ-DES-xxx)
  - REQ-DES-001 apply Association branding/visual identity guidelines | fit: conformance checklist 100%
  - REQ-DES-002 language selector present and persistent on tourist-facing pages | fit: present on 100% of such pages
  - REQ-DES-003 consent and privacy-notice presented in Bahasa Malaysia and English at minimum | fit: both languages present at every collection point
  - REQ-DES-004 responsive layout for defined device/screen classes | fit: passes layout checks on 100% of defined classes
  - REQ-DES-005 accessibility design conventions (contrast, keyboard, labels) | fit: supports NFR-USAB-04
  - REQ-DES-006 consistent domain terminology matching Glossary in all UI text | fit: 0 terminology deviations in review
  - REQ-DES-007 error and unavailable-service messaging pattern for external outages | fit: defined message per external entity
  - REQ-DES-008 receipt/confirmation artefact layout for bookings and payments | fit: defined required content elements present
  - REQ-DES-009 report presentation format (comparison to target/prior period) | fit: each report shows target + prior-period columns
  - REQ-DES-010 data-correction request UI for tourists | fit: reachable within placeholder number of steps from account area

- 9.5 PDPA 2010 requirements (REQ-PROD-PDPA-xx; each also mapped to NFR-SEC and given a fit criterion + verification method)
  - REQ-PROD-PDPA-01 Notice & Choice: consent captured before collection; purpose notice in BM + English | fit: 100% collection points; inspection + test
  - REQ-PROD-PDPA-02 Disclosure: personal data disclosed only to named third parties with consent | fit: disclosure register vs consent 100% match; inspection
  - REQ-PROD-PDPA-03 Security Principle: encryption, RBAC, audit logging, breach procedure | fit: maps to NFR-SEC-01/02/04; test
  - REQ-PROD-PDPA-04 Retention: per-category retention + automatic deletion/anonymisation | fit: maps to REQ-PROD-001; demonstration
  - REQ-PROD-PDPA-05 Data Integrity: tourist can review and correct personal data | fit: correction reflected within placeholder time; test
  - REQ-PROD-PDPA-06 Access: self-service access/correction request fulfilled within stated time | fit: <= placeholder days; demonstration
  - REQ-PROD-PDPA-07 Cross-border transfer safeguards | fit: maps to REQ-PROD-017; inspection
  - REQ-PROD-PDPA-08 Direct marketing opt-out | fit: maps to REQ-PROD-018; test
  - REQ-PROD-PDPA-09 Cookies/tracking consent | fit: maps to REQ-PROD-019; test
  - REQ-PROD-PDPA-10 Data-user responsibilities + PDP Commissioner registration if in a registration class | fit: documented determination + evidence; inspection
  - data covered - tourist: name, contact, passport/IC, nationality, payment details, itinerary/location history, booking history, reviews, enquiry content
  - data covered - management/operator: staff accounts + credentials, business registration details, banking/payout details, marketing-staff accounts

---

## K. SECTION 10 VERIFIABILITY APPROACH

- every requirement ID -> row in self-audit table (Appendix D): ID | statement | metric | scale/unit | target | measurement instrument | verification method (test/demonstration/inspection/analysis) | acceptance test | priority
- subjective-term ban list: easy, fast, user-friendly, secure, robust, appropriate, relevant, seamless, quickly, efficient, intuitive, modern
- each TASK verifiable by "execute the task and every numbered variant to completion"
- each NFR verifiable by its fit criterion + named instrument
- goal-level statements made verifiable via their linked OBJ-xx measurable objectives
- target: zero requirements without a fit criterion (demonstrated by Appendix D having no blank cells)

---

## L. SECTION 11 VALIDATION PLAN (evidence -> Appendices)

- validation activities (each dated, with participants, artefacts, outcomes, before/after changes):
  - VAL-01 requirements walkthrough / inspection with Swinsoft team - defect log + resolution (Appendix A)
  - VAL-02 stakeholder review with Association management - feedback + sign-off record (Appendix A)
  - VAL-03 task-completeness check with expert/representative users - missing task/sub-task findings, Lauesen style (Appendix E)
  - VAL-04 scenario / prototype walkthrough for TASK-01..TASK-08 - results (Appendix E)
  - VAL-05 NFR fit-criteria target validation with stakeholders - are targets acceptable? (Appendix A)
  - VAL-06 assumption confirmation with client - each ASM-xx confirmed/adjusted (Appendix F)
  - VAL-07 PDPA interpretation validation with legal/compliance advisor (Appendix G)
  - VAL-08 requirement-to-task traceability review - two-way coverage confirmed (Appendix B)
  - VAL-09 CRUD completeness check - every ENT x every TASK; anomalies (never Created / never Deleted / task touches no data) flagged and resolved (Appendix C)
  - VAL-10 verifiability self-audit review - Appendix D confirmed complete
- change log plan: table columns: Change ID | Source activity (VAL-xx) | Requirement(s) affected | Before | After | Rationale | Date

---

## M. SECTION 12 TRACEABILITY

- 12.1 Traceability matrix (Appendix B) columns:
  - Requirement ID | Type (GOAL/OBJ/FUN/PROD/DES/NFR) | Statement (short) | Traces up to (Goal/Pain) | Task(s) (TASK-0x) | Workflow(s) (WF-0x) | Domain entities touched | Validation method (VAL-xx) | Verification method (test/demo/inspection/analysis) | Fit criterion ref | Priority
  - two-way coverage assertions: every GOAL -> >=1 OBJ -> >=1 TASK/REQ; every TASK -> >=1 WF; every REQ-FUN -> >=1 TASK; every NFR -> >=1 GOAL/PAIN; every ENT -> >=1 TASK

- 12.2 CRUD completeness matrix (Appendix C):
  - rows = ENT-01..ENT-27; columns = TASK-01..TASK-08 (+ operations/admin column for ACT-07/ACT-08 activities)
  - cell values: C / R / U / D combination
  - anomaly checks: entity never Created; entity never Deleted (justify via retention/PDPA); entity never Read; task with no data effect
  - resolution notes column

---

## N. SECTION 14 GLOSSARY / DOMAIN VOCABULARY (term list to define - no definitions here)

- Association, Tourist, Tourism Provider, Listing, Attraction, Event, Accommodation, Transportation, Food Option, Local Information, Content Item, Promotion Campaign, Itinerary, Itinerary Item, Booking, Payment, Review, Enquiry Ticket, Engagement Record, Analytics Report, Consent Record, Role, Region, Category, Language, Translation, Tasks & Support, Goal-Design Scale, Fit Criterion, PDPA 2010, WCAG 2.1 AA, RBAC, RTO, RPO, MTBF, MTTR, SUS

---

## O. BLUEPRINT SELF-CHECK AGAINST CHECKLIST

- [x] Project Type stated + justified (2.1)
- [x] Goals / Objectives / Incentives separated (2.4/2.5/2.6); pain points IDed (2.3)
- [x] System Context with boundary + external entities + context diagram slot (3)
- [x] Assumptions numbered + justified + linked; Constraints + Scope subsections (2.7/2.8/2.9)
- [x] Software-only elaboration; hardware/data repositories/deployment assumed acquired (ASM-01..04)
- [x] Domain model: entities + relationships + cardinality ONLY; NO attributes/keys/types/tables (4, rule 4.1)
- [x] Exactly 8 major user tasks in Tasks & Support format with Problem + Example Solution + Variants (6)
- [x] Sub-tasks imperative, domain-level, solution-agnostic (>=3 solutions) (6.2 rule)
- [x] Work Area / background block (6.1); high-level journey task via WF-01 + TASK chain
- [x] Consolidated end-to-end workflow + per-task workflows; swimlanes; variant branches (7)
- [x] Exactly 4 NFR categories, each with quantified fit criteria + instrument + verification + priority (8)
- [x] Other requirements across Goal-Design Scale: REQ-FUN / REQ-PROD / REQ-DES with fit criteria (9)
- [x] PDPA 2010 named explicitly; obligations as verifiable requirements; tourist + management data (9.5, 8.4)
- [x] Every requirement verifiable; self-audit table planned (10, Appendix D)
- [x] Validation evidence in Appendices: walkthroughs, sign-off, traceability, CRUD completeness (11, 13)
- [x] Traceability matrix columns defined: Requirement ID -> Task -> Workflow -> Validation method (12.1)
- [x] Front matter: title page, revision history, TOC, list of figures/tables, abbreviations (FM-1..FM-6)
- [x] Consistent task IDs/names reused across sections 4, 6, 7, CRUD, traceability (rule in D)
- [x] No final prose in this blueprint
