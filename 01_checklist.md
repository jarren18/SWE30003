# COS30003 Assignment 1 - High Distinction Delta Checklist

Software Requirements Specification: Sarawak Tourism Promotion System

Purpose: exact gap list to move a "Pass"-level SRS to full "High Distinction" marks against `rubric.yaml`.
Reference sample assessed: `C:\Users\Jarren\OneDrive - Swinburne Sarawak\Documents\COS30003\sample_pass.pdf` (HTV Sales Information System - graded Pass).
Method reference: `C:\Users\Jarren\OneDrive - Swinburne Sarawak\Documents\COS30003\TasksSupportAWRE.pdf` (Lauesen, Tasks & Support).

Total available: 100 points.

---

## 1. Project Goals and Assumptions - max 5 points

What the Pass sample did:
- Provided a narrative Project Overview, a 3-bullet Goals list, an Assumptions list, and a Scope paragraph.
- Assumptions were realistic and within constraints (single location, volume/day, staff skill level, staff types).

What the Pass sample omitted / did weakly:
- No explicit statement of Project Type (in-house build vs COTS acquisition vs product development).
- Goals were vague and unmeasurable ("alleviate pain points", "remove redundancies", "tie together key elements").
- No separation of Goals vs Objectives vs Incentives; no measurable objectives; no business case / ROI / funding rationale (Incentives).
- System Context given only as prose - no context diagram, no identified external systems/actors.
- Assumptions not individually justified or traced to a constraint; no dedicated Constraints subsection.

Additions/changes required for full marks:
- [ ] State the Project Type explicitly and justify it (e.g. new public-facing web/mobile product for Sarawak Tourism Board, partly COTS-integrated).
- [ ] Write a distinct Goals subsection: 3-6 outcome statements tied to the identified problem.
- [ ] Write a distinct Objectives subsection: each objective measurable and time-bound (metric + target + deadline), each traceable to a goal.
- [ ] Write a distinct Incentives subsection: business value / expected ROI / tourism-revenue or visitor-number uplift / why the Board is funding this.
- [ ] Add a System Context subsection with a context diagram: system boundary plus every external actor and system (tourists, tour operators, Sarawak Tourism Board marketing staff, content administrators, payment gateway, mapping/geolocation service, email/SMS provider, social media, government tourism data sources).
- [ ] Expand Assumptions: number each, give a one-line justification, and link each to a constraint or scope item; confirm all are realistic and inside project constraints.
- [ ] Add a Constraints subsection (budget, timeline, regulatory - PDPA, technology, hosting location, languages to support, rural-bandwidth reality in Sarawak).
- [ ] Add a Scope subsection with explicit in-scope and out-of-scope lists.

---

## 2. Data / Domain Model - max 5 points

What the Pass sample did:
- Provided an ER-type domain model diagram with named relationships (Supervises, Offers, Accepts, Generates, Receives, Pays, Files, Describes, Details).
- Provided a prose description for each entity.
- Correctly avoided listing attributes / primary keys / data types (penalty avoided).

What the Pass sample omitted / did weakly:
- No cardinality / multiplicity on any relationship.
- Some entities were data-design artefacts rather than domain concepts ("Vehicle Status", "Vehicle Specifications", "Service Type").
- Domain model not cross-checked against tasks / CRUD table (CRUD table later omitted several of these entities).

Additions/changes required for full marks:
- [ ] Produce a single clean ER/domain model for the Sarawak Tourism domain: entities + named relationships + multiplicities on every relationship.
- [ ] Use genuine domain concepts, e.g. Tourist, TourOperator, Attraction, Event, Accommodation, TourPackage, Booking, Itinerary, Payment, Review/Rating, PromotionCampaign, ContentItem, EnquiryTicket.
- [ ] Give each entity a concise business-level description (what it represents and its role in the domain) - not a field list.
- [ ] Ensure every entity appears in at least one user task and in the CRUD validation table, and vice versa.
- [ ] Keep the diagram at conceptual level: entities and relationships only.

MUST AVOID (strict_penalty - up to -3 points):
- [ ] Do NOT include database attributes, columns, primary/foreign keys, data types, or table structures anywhere in the domain model or entity descriptions.
- [ ] Do NOT introduce entities that only exist for data storage/normalisation reasons - keep entities solution-independent.

---

## 3. User Tasks - max 40 points (5 points per task; 8 major tasks required for full marks)

What the Pass sample did:
- Documented 9 tasks in tabular Tasks & Support-style tables with Purpose, Trigger/Precondition, Frequency, Critical, Work Area, Subtasks, Example Solution, Variants rows.

What the Pass sample omitted / did weakly:
- No consolidated Work Area / background description block (Lauesen Fig. 1) grouping the tasks (purpose of the work, environment, user profile).
- "Problem" (present-situation problems) column effectively missing from most tasks - only a few ad-hoc "Problem:" lines; this breaks the Tasks & Support format.
- Variants left empty for several tasks (Tasks 1, 5, 6, 8, 9); Critical and Work Area left blank on several tasks.
- Sub-tasks not consistently written in imperative domain-level language; Task 7 sub-tasks were actor narration ("Customer informs Staff"), not domain activities.
- Several tasks are minor, not major (Feedback, Update Customer Information, Stocktake).
- Copy/paste and naming defects: Task 7 titled "Process Payment"; Task 8 name blank; task named differently in Section 5 ("Service Engine").
- Some Example Solution entries prematurely fix the human/computer split and over-specify a solution instead of reading as an example.
- No typical sub-task sequence noted; no high-level (client-journey) task.

Additions/changes required for full marks:
- [ ] Provide at least 8 MAJOR user tasks (high-value core business tasks), each fully in Tasks & Support format. Candidates: Search and discover attractions/experiences; Plan and build an itinerary; Book a tour package / accommodation; Make and confirm payment; Create and publish a tourism promotion/campaign; Register and manage an operator listing; Submit and moderate reviews/ratings; Generate tourism/marketing analytics report; Manage the events calendar; Handle a tourist enquiry / support request.
- [ ] Add a Work Area / background section before the tasks: overall purpose of the work, work environment, user profiles for each actor, grouping of tasks by work area.
- [ ] For every task table include and fill every field: Task ID + name, Purpose, Trigger/Precondition, Frequency (quantified), Critical (quantified worst-case scenario), Users/Work Area, Sub-tasks (imperative, domain-level), Problem (present-situation problems), Example Solution (column clearly headed "Example solution"), Variants (numbered against sub-tasks: 1a, 1b, 2a...).
- [ ] Write every sub-task imperatively so it does not pre-assign work to human or computer.
- [ ] Confirm the 8+ tasks collectively cover every actor and every domain-model entity.
- [ ] Add at least one high-level task from the tourist's journey viewpoint (discover -> plan -> book -> pay -> travel -> review) to surface business needs (Lauesen section 5).
- [ ] Note a typical sub-task sequence for each task while stating sequence is not mandatory.
- [ ] Use identical task names and IDs in Section 4, the Workflow section, the CRUD table, and the traceability matrix.
- [ ] Replace all placeholder Australian/HTV content with Sarawak Tourism domain content.

MUST AVOID (strict_penalty - variable mark deduction):
- [ ] Do NOT deviate from the Tasks & Support style: every task must have the Problem column, the Example Solution column, and populated Variants.
- [ ] Do NOT use feature-style "the system shall..." statements in the sub-task/domain column.
- [ ] Do NOT submit fewer than 8 major tasks - full task marks require 8 (5 points each).
- [ ] Do NOT pad with trivial tasks in place of major tasks.

---

## 4. Workflow - max 5 points

What the Pass sample did:
- Provided one activity diagram per task (start/end nodes, some decision diamonds, some fork/join bars).

What the Pass sample omitted / did weakly:
- Most diagrams are linear restatements of the sub-task list, adding no analytical value.
- No overarching end-to-end workflow linking the tasks.
- No actor swimlanes / partitions; no artefact or data flow.
- Diagram labels contain spelling errors and a duplicated node; diagram titles inconsistent with Section 4 task names.

Additions/changes required for full marks:
- [ ] Provide at least one consolidated end-to-end workflow linking the main user tasks (e.g. tourist journey: discover -> plan itinerary -> book -> pay -> on-trip -> review; plus the operator/marketing publishing workflow).
- [ ] Provide per-task workflows for the more complex tasks (booking+payment, campaign publishing, enquiry handling).
- [ ] Use correct UML activity-diagram notation: swimlanes per actor (tourist, operator, marketing staff, system), decision/merge nodes, fork/join for concurrency, initial/final nodes.
- [ ] Show the Tasks & Support variant paths as decision branches.
- [ ] Ensure every major task in Section 4 is visibly covered by a workflow; cross-reference by task ID.
- [ ] Zero spelling errors; figure captions numbered; titles identical to Section 4 task names.

---

## 5. Quality Attributes / NFRs - max 20 points (5 points per category)

What the Pass sample did:
- Provided NFR sections with a short rationale for each, and some measurable targets under Reliability and Performance.

What the Pass sample omitted / did weakly:
- Presented 5 categories (Security, Usability, Reliability, Performance, Portability) - rubric scores 5 points x 4 categories = exactly 4 expected.
- Usability deferred entirely to an external design-guidelines document - no metrics.
- Security bullets unmeasurable and cited "Australian Law" (wrong jurisdiction).
- Performance had a missing unit ("< 20"); Reliability targets ambiguous ("10 minutes", "100%").
- No fit criterion structure (metric, scale, target, worst acceptable, measurement method, priority) for any NFR.
- No accessibility, no multilingual/localisation, no scalability for tourist-season peaks.

Additions/changes required for full marks:
- [ ] Provide EXACTLY 4 NFR categories, each the most relevant to a public tourism promotion system. Recommended: (1) Usability (incl. accessibility + multilingual), (2) Performance & Scalability, (3) Security & Privacy (PDPA), (4) Availability & Reliability.
- [ ] For EACH category give: business rationale traced to a specific goal/pain point; one or more quantified fit criteria (metric + scale + target value + worst-acceptable value); the measuring instrument; the verification method; a priority.
- [ ] Usability: SUS >= target; first-time tourist completes a booking in <= N minutes with <= M errors; support >= K languages (Bahasa Malaysia, English, Mandarin, plus stated others); WCAG 2.1 AA conformance.
- [ ] Performance & Scalability: search response time, page load time, transaction time, concurrent-user capacity at campaign/festival peak, throughput, graceful-degradation behaviour.
- [ ] Security & Privacy: PDPA 2010 compliance, encryption in transit and at rest, role-based access control, audit logging, penetration-test pass criterion, consent management, breach-response time.
- [ ] Availability & Reliability: uptime % measured monthly excluding scheduled maintenance, RTO/RPO, MTBF/MTTR targets.
- [ ] Remove all references to "Australian Law"; cite the Malaysian PDPA.
- [ ] Fix all missing units and ambiguous windows.

MUST AVOID:
- [ ] Do NOT list more than 4 or fewer than 4 NFR categories (rubric = exactly 4 categories at 5 points each).
- [ ] Do NOT state any NFR without a measurable fit criterion ("user-friendly", "fast", "secure", "reliable" alone = fail).
- [ ] Do NOT defer an entire NFR to an external document with no metric in the SRS.

---

## 6. Other Requirements - max 5 points

What the Pass sample did:
- Provided short Product-level and Design-level requirement lists (data storage/validation, display, reports, print; algorithms, Terms/Privacy display, logo, design guidelines, images).

What the Pass sample omitted / did weakly:
- Thin and generic; some entries unverifiable ("analyse data using special algorithms").
- No evidence the problem was thought through comprehensively: no data retention/archival, no integration requirements, no reporting detail, no content management, no localisation, no low-bandwidth handling, no operational/support requirements.

Additions/changes required for full marks:
- [ ] Provide in-depth, individually IDed, verifiable product-level and design-level requirements.
- [ ] Cover data lifecycle: retention periods, archival, anonymisation, backup and disaster recovery.
- [ ] Cover legal/regulatory: PDPA 2010, consumer protection, e-commerce/CyberSecurity obligations, accessibility, tourism-operator licensing checks.
- [ ] Cover integration/interoperability: payment gateway, operator booking systems, mapping/geolocation, email/SMS, social media, Sarawak Tourism Board content/CMS, analytics.
- [ ] Cover reporting & analytics: campaign performance, visitor trends, booking funnel, content engagement.
- [ ] Cover content management & multilingual content authoring and publishing workflow.
- [ ] Cover discoverability/SEO, branding/design guidelines, and rural/low-bandwidth and offline-tolerant behaviour for remote Sarawak areas.
- [ ] Cover operations: monitoring, logging, support levels, maintenance windows, training materials, licensing of third-party/open-source components.
- [ ] Trace each requirement to a goal or task and assign a priority.

---

## 7. Validation - max 10 points

What the Pass sample did:
- One paragraph asserting the requirements were shown to the CEO and some actors were interviewed.
- Provided a CRUD Check table (Task x Entity).

What the Pass sample omitted / did weakly:
- Validation asserted, not evidenced - no artefacts, notes, sign-off, dates, or before/after changes.
- CRUD table omitted several domain-model entities and did not analyse gaps.
- No traceability matrix; no NFR or goal validation; no walkthrough/inspection record; no prototype/scenario walkthrough.

Additions/changes required for full marks:
- [ ] Provide concrete, dated evidence of validation activities: who was consulted (Sarawak Tourism Board representative, tour operators, sample tourists), what was reviewed, feedback received, and the resulting requirement changes (show before/after).
- [ ] Include a stakeholder review/sign-off record.
- [ ] Include a requirements walkthrough / inspection checklist listing defects found and how each was resolved.
- [ ] Provide a complete CRUD cross-check covering EVERY domain-model entity against EVERY task; explicitly flag and resolve anomalies (entities never Created or never Deleted, tasks that touch no data).
- [ ] Provide a traceability matrix: goals -> objectives -> tasks -> product/design requirements -> NFRs, demonstrating full two-way coverage.
- [ ] Record a task-completeness check with expert users (missing sub-task / missing task findings, Lauesen style).
- [ ] Record a scenario or prototype walkthrough result for the main tasks.
- [ ] Record validation of the NFR fit-criteria targets with stakeholders (are the targets acceptable?).
- [ ] Record that each assumption was confirmed with the client.

---

## 8. Verifiability - max 5 points

What the Pass sample did:
- Some Performance and Reliability items were quantified.

What the Pass sample omitted / did weakly:
- Multiple non-verifiable items: usability deferred to a document; "compliance with Australian Law"; "only give access to those authorized"; "correct information 100% of the time"; "response time < 20" (no unit); "analyse data using special algorithms"; "reduce down time to 10 minutes" (no window); unmeasurable goals.

Additions/changes required for full marks:
- [ ] Give every requirement (task Example-Solution items, product-level, design-level, and every NFR) a fit criterion: measurable quantity + scale + target value + measurement method + verification method (test / demonstration / inspection / analysis).
- [ ] Assign a unique ID to every requirement and state its acceptance test.
- [ ] Remove or replace every subjective term (easy, fast, user-friendly, secure, robust, appropriate, relevant, seamless, quickly) with a metric.
- [ ] Ensure each task is verifiable by "carry out the task and all its variants" - concrete sub-tasks and variants for every task.
- [ ] Include a self-audit table listing each requirement ID against its fit criterion to demonstrate zero non-verifiable requirements.

MUST AVOID (strict_penalty - minus 1 point per non-verifiable requirement):
- [ ] Do NOT leave any requirement without a measurable, testable fit criterion.
- [ ] Do NOT rely on jurisdictionally vague phrases ("comply with the law") - name the statute (PDPA 2010) and the checkable obligation.

---

## 9. Coherent Document - max 5 points

Scoring: structure 1 | clarity & non-contradiction 1 | formatting (title page, TOC, numbered sections/pages) 1 | presentation (English, diagrams) 1 | audience fit 1.

What the Pass sample did:
- Had a TOC with page numbers, numbered top-level sections, page numbers, a domain vocabulary list.

What the Pass sample omitted / did weakly:
- Subsections not numbered ("Task 1:", "Security", "Domain Model" instead of 4.1, 7.1, 6.1).
- Weak title page (no author, student ID, unit code, date, version); no revision history; no list of figures/tables.
- Clarity defects and contradictions: Task 7 mistitled "Process Payment"; Task 8 name blank; workflow task renamed "Service Engine"; "Australian Law" in an otherwise generic document; missing unit on a metric; duplicated workflow node.
- English errors and typos throughout body and diagram labels; low-fidelity, inconsistent diagrams.
- Audience mixed; solution detail leaks into a requirements document; "Possible Solutions" section not required by rubric and reads as scope creep.

Additions/changes required for full marks: see the Formatting & Presentation checklist below.

---

## Formatting & Presentation Checklist (Section 9 points)

- [ ] Title page: unit code (COS30003), assignment title, system name (Sarawak Tourism Promotion System), author name(s) + student ID(s), tutor/lecturer name, submission date, document version.
- [ ] Document control page: revision history table (version, date, author, change).
- [ ] Table of contents: auto-generated, accurate, with correct page numbers.
- [ ] List of figures and list of tables.
- [ ] Every section AND subsection hierarchically numbered (1, 1.1, 1.1.1).
- [ ] Every page numbered (e.g. "Page X of Y") with consistent header/footer.
- [ ] Every figure and table numbered, captioned, referenced from the text, legible, high-resolution, and using consistent UML notation.
- [ ] Consistent heading styles, fonts, spacing, and layout throughout; professional appearance.
- [ ] Full proofread: formal, correct English; no typos; terminology identical to the glossary everywhere (including diagram labels).
- [ ] No contradictions: task names and IDs identical across Section 4, Workflow, CRUD, and traceability matrix; all cross-references correct.
- [ ] Glossary / domain vocabulary section plus a list of abbreviations.
- [ ] Introduction states purpose, scope, intended readership, references, and a document overview.
- [ ] Audience fit: written for the client (Sarawak Tourism Board) and the development team; consistent level of abstraction; no premature human/computer work split; solution ideas confined to the "Example solution" column or a clearly labelled options appendix.
- [ ] Any non-required content (e.g. "Possible Solutions") is either removed or clearly delineated as an optional appendix so it is not read as requirements.
- [ ] Data/Domain model placed logically (near the problem domain, before or alongside the tasks that use it).

---

## PDPA Compliance Checklist (Malaysian Personal Data Protection Act 2010)

- [ ] Replace all "Australian Law" / generic compliance wording with explicit reference to the Malaysian Personal Data Protection Act 2010 (PDPA).
- [ ] Identify all personal data processed:
  - Tourist data: name, contact details, passport/IC number, nationality, payment details, itinerary/location history, booking history, reviews, enquiry content.
  - Management/operator data: operator staff accounts and credentials, business registration details, banking/payout details, marketing-staff accounts.
- [ ] State each PDPA obligation as a verifiable requirement with a fit criterion and verification method:
  - [ ] Notice & Choice: consent captured before collection; purpose-limitation notice presented in Bahasa Malaysia and English.
  - [ ] Disclosure: personal data disclosed only to named third parties (payment gateway, specific tour operators) and only with consent.
  - [ ] Security: encryption in transit and at rest, role-based access control, audit logging, defined breach-response procedure and notification time.
  - [ ] Retention: defined retention period per data category; automatic deletion or anonymisation of tourist data after the stated period.
  - [ ] Data Integrity: tourists can review and correct their personal data.
  - [ ] Access: self-service data-access and correction requests, fulfilled within the stated time.
  - [ ] Cross-border transfer: cloud hosting outside Malaysia addressed with stated safeguards/consent.
  - [ ] Direct marketing: email/SMS campaign opt-out honoured and testable.
  - [ ] Cookies/tracking consent for marketing analytics on the promotion site.
  - [ ] Data-user responsibilities identified; registration with the PDP Commissioner addressed if the system falls within a registration class.
- [ ] Validate the PDPA interpretation with a legal/compliance stakeholder and record it in the Validation section.
- [ ] Ensure every PDPA requirement has a measurable fit criterion so it does not trigger the verifiability penalty.

---

## Consolidated MUST AVOID (all strict_penalty triggers)

- [ ] Domain model: NO database attributes, keys, data types, or table structures (up to -3 points).
- [ ] User tasks: MUST adhere to Tasks & Support style - Problem column, Example Solution column, populated Variants, imperative domain-level sub-tasks, no "system shall" feature statements in the domain column (variable deduction).
- [ ] User tasks: MUST provide 8 major user tasks for full marks (5 points each).
- [ ] NFRs: MUST have exactly 4 NFR categories (5 points each = 20).
- [ ] Verifiability: EVERY requirement MUST be verifiable with a measurable fit criterion (-1 per non-verifiable requirement).
- [ ] Document: NO internal contradictions or inconsistent task naming across sections.
- [ ] Compliance: name the Malaysian PDPA 2010, not a vague or foreign legal reference.
