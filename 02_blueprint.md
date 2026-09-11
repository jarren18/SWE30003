# SRS Blueprint — Sarawak Tourism Promotion System

> STATUS: Structural skeleton only (Requirements Architect output). No final prose.
> The technical-builder agent expands each bullet below into full SRS prose, diagrams, and tables.
> Bracketed items `[...]` are placeholders requiring stakeholder-sourced facts during drafting/validation.
> Hard constraints enforced in this blueprint: (1) Tasks & Support approach throughout Section 6;
> (2) exactly 4 NFR categories in Section 8; (3) zero database attributes in Section 5; (4) every
> requirement statement must be phrased as an objectively verifiable "the system shall..." condition.

---

## 0. Document Control & ID Legend (Front Matter)

### 0.1 Title Page (fields to populate)
- Project Title: "Software Requirements Specification — Sarawak Tourism Promotion System"
- Client: Management team of a local tourism association
- Preparing Agency: Swinsoft Consulting
- Prepared For / Prepared By: [names, roles]
- Version / Date / Confidentiality Notice
- Document Type: Software Requirements Specification (Tasks & Support / Goal-Design Scale methodology)

### 0.2 Revision History Table
- Columns: Version | Date | Author | Summary of Change | Trigger (e.g., stakeholder feedback ID VAL-xxx)

### 0.3 Table of Contents
- Auto-generated from numbered Sections 1–12 + Appendices A–F. Must be regenerated whenever a section/diagram is added (Coherent Document — Formatting rule).

### 0.4 Requirement / Artifact ID Legend
- `GOAL-xxx` Goal (broad direction)
- `OBJ-xxx` Objective (specific, measurable outcome)
- `INC-xxx` Incentive (business value / ROI)
- `PP-xxx` Pain point (existing process problem)
- `ASSUMP-xxx` Assumption (with rationale/source)
- `ACT-xxx` Actor
- `EXT-xxx` External system/interface
- `DM-ENT-xxx` Domain model entity
- `DM-REL-xxx` Domain model relationship
- `TASK-xxx` Major user task (Tasks & Support)
- `ST-x.y` Subtask of TASK-x
- `REQ-FUN-xxx` Functional requirement (derived from a subtask)
- `REQ-NFR-xxx` Non-functional requirement (exactly 4 categories, numbered 001–004)
- `REQ-DES-xxx` Design-level requirement
- `REQ-PROD-xxx` Product-level requirement
- `REQ-PDPA-xxx` PDPA/regulatory compliance requirement
- `WF-xxx` Workflow diagram (WF-000 = overarching; WF-001…WF-011 = per-task)
- `VAL-xxx` Validation evidence item

### 0.5 Intended Audience Statement (explicit — Coherent Document / audience-fit rule)
- State plainly: this SRS is written for (a) Tourism Association management/decision-makers, (b) Swinsoft development team, (c) QA/test engineers, (d) any PDPA compliance auditor reviewing the system pre-launch.

### 0.6 Project Type Statement (explicit — Goals/Assumptions rule)
- State plainly: greenfield, purpose-built software system; not a replacement of one existing legacy IT system but a consolidation of currently fragmented manual/print/social-media tourism-promotion channels into a single association-operated platform.

---

## 1. Introduction
- 1.1 Purpose of the Document
- 1.2 Scope (software only — hardware, data repositories, deployment platforms assumed already acquired per `project_brief.yaml`)
- 1.3 Intended Audience (reference 0.5)
- 1.4 Project Type (reference 0.6)
- 1.5 Domain Vocabulary / Definitions (pointer to Appendix E)
- 1.6 Document Conventions (ID legend pointer to 0.4; requirement-statement style rule: every normative statement uses "The system shall...")

---

## 2. Project Goals, Objectives, Incentives & Pain Points
Rule: keep Goals / Objectives / Incentives / Pain Points as four **separately labelled** subsections — do not collapse into one "Goals" list.

### 2.1 Goals (broad direction)
- `GOAL-001` Promote Sarawak destinations, accommodation, transportation, and food to worldwide tourists through one authoritative digital channel.
- `GOAL-002` Enable the tourism association's management team to control and maintain promotional content and operational data.
- `GOAL-003` Provide trustworthy, current local information that improves visitor experience and safety.
- `GOAL-004` Operate the platform in demonstrable compliance with the Malaysian PDPA for both tourist and management data.

### 2.2 Objectives (specific, measurable, each traced to a Goal)
- `OBJ-001` (→GOAL-001) Consolidate accommodation, transportation, food, and local-info listings currently spread across independent channels into one searchable catalog before launch.
- `OBJ-002` (→GOAL-002) Reduce the content-update cycle for a new/changed listing to [target, e.g., same business day] from the current manual process.
- `OBJ-003` (→GOAL-001) Enable a tourist to research, assemble, and pay for a multi-component trip package within the platform without leaving it.
- `OBJ-004` (→GOAL-004) Pass a documented PDPA compliance checklist review (Section 10 / Appendix A) prior to go-live.

### 2.3 Incentives (business value / ROI)
- `INC-001` Increased bookings/revenue channelled to association-endorsed accommodation, transport, and food providers.
- `INC-002` Reduced association staff hours spent on manual/paper-based content coordination and provider liaison.
- `INC-003` Strengthened association brand trust from centralized, verified, moderated information (vs. fragmented/unofficial sources) — supports quality/review loop (TASK-008).
- `INC-004` Data-informed decision-making for the association (which destinations/providers drive engagement) enabled by structured booking/review data.

### 2.4 Pain Points (existing process problems — each must map to ≥1 Goal/Objective and forward into Appendix B traceability)
- `PP-001` Tourist information is scattered across informal/unofficial sites and social media, inconsistent and unverifiable. → OBJ-001
- `PP-002` No single channel lets a tourist discover and book accommodation, transport, and food together. → OBJ-003
- `PP-003` Management currently updates tourism content via manual/offline means (spreadsheets, printed brochures), causing delay and error. → OBJ-002
- `PP-004` Language and currency barriers hinder worldwide tourists using fragmented local-only sites. → GOAL-001/GOAL-003
- `PP-005` No structured feedback channel exists for the association to assess visitor satisfaction or provider quality. → INC-003 / TASK-008
- `PP-006` Absence of a governed data-handling process exposes tourist and management personal data to PDPA compliance risk. → GOAL-004

---

## 3. Assumptions (each requires an explicit rationale/source — Goals/Assumptions rule)
- `ASSUMP-001` Hardware, servers, network, and the data-repository platform are already acquired/provisioned by the client. Source: `project_brief.yaml` → `strict_ground_rules.hardware_assumption`.
- `ASSUMP-002` The tourism association is the sole authoritative content owner; individual accommodation/vehicle/food providers do not receive direct system login — they supply information to association staff off-system. Source: brief's `core_functions.management_facing` wording ("enable content and database management" = staff-only). Flag for stakeholder confirmation (Appendix A).
- `ASSUMP-003` Worldwide tourists are assumed to have access to a modern web browser or smartphone with adequate internet connectivity. Source: `project_brief.yaml` → `target_audience`.
- `ASSUMP-004` Payment processing is delegated to a third-party, PCI-DSS-compliant payment gateway; the system does not store raw payment-card data. Source: software-only scope ground rule + standard practice.
- `ASSUMP-005` The association operates under Malaysian jurisdiction; PDPA is the governing privacy framework even though end users are worldwide; foreign frameworks (e.g., GDPR) are explicitly out of scope unless the client states otherwise. Source: `project_brief.yaml` → `compliance.privacy_framework`. Flag as a risk requiring stakeholder sign-off.
- `ASSUMP-006` One shared platform instance serves all association-endorsed listings; no separate deployment per district. Source: inferred from single-system framing of the brief.
- `ASSUMP-007` English and Bahasa Malaysia are the baseline supported languages; additional languages are budget-dependent stretch scope. Source: target audience + typical practice; requires stakeholder confirmation.
- Cross-check rule: re-scan Sections 8–10 during drafting to ensure no NFR/design requirement silently contradicts an assumption (e.g., a multi-region scalability NFR must not conflict with ASSUMP-006 unless ASSUMP-006 is revised).

---

## 4. System Context & Actors

### 4.1 System Boundary Statement
- In scope: application software — tourist-facing modules, management-facing content/booking/privacy-administration modules, business logic, and API integration logic.
- Out of scope: physical servers/hosting, network provisioning, end-user devices, and the internal implementation of third-party services (treated as external black boxes only), per `strict_ground_rules.hardware_assumption`.

### 4.2 Actors
- `ACT-001` Tourist (Guest / Registered) — primary worldwide end user; standardize this exact term everywhere (never "Visitor"/"Traveler"/"Customer").
- `ACT-002` Management Staff — Content Officer role (tourism association staff curating listings/content).
- `ACT-003` Management Staff — Data/System Administrator role (handles accounts, permissions, PDPA requests); generalizes with ACT-002 under superclass "Management Staff."
- `ACT-004` (External) Payment Gateway Provider.
- `ACT-005` (External) Notification Service (email/SMS gateway).
- `ACT-006` (External) Mapping/Geolocation Service Provider.
- `ACT-007` (External) Translation/Localization Service (if used to support ASSUMP-007 expansion).
- `ACT-008` (Contextual, non-user) PDPA Regulatory Authority — recipient of breach notifications; included in context diagram, not a system operator.
- Terminology rule: actor names above are canonical; audit final document for inconsistent naming before submission (Coherent Document rule).

### 4.3 System Context Diagram (description for technical-builder to render)
- Center node: "Sarawak Tourism Promotion System."
- Inbound/outbound edges to ACT-001 through ACT-008 above, each labeled with the nature of the interaction (e.g., ACT-004 edge = "payment authorization request/response").
- Legend clarifying solid edge = direct system interaction, dashed edge = compliance/regulatory relationship (ACT-008 only).

---

## 5. Domain Model
**Hard rule: entities + one-line conceptual descriptions + relationships/cardinalities only. No attributes, no primary/foreign keys, no normalized sub-entities (e.g., do NOT split Vehicle into "Vehicle Details"/"Vehicle Availability" — keep one Vehicle entity).**

### 5.1 Entity List (`DM-ENT-xxx`) — must reconcile 1:1 with Section 5.2 diagram and Appendix C CRUD matrix
- `DM-ENT-001` Tourist — a worldwide visitor who discovers, plans, and books Sarawak travel experiences via the platform; may act as guest or registered profile.
- `DM-ENT-002` Management Staff — tourism association personnel who curate content, moderate reviews, and administer bookings/data.
- `DM-ENT-003` Destination — a promoted place of interest (cultural site, park, festival, landmark).
- `DM-ENT-004` Accommodation — a lodging listing (hotel, homestay, resort) available for reservation.
- `DM-ENT-005` Vehicle — a transportation option (car, van, boat, bus, etc.) offered/listed for tourist transport or touring. **Single conceptual entity — do not fragment.**
- `DM-ENT-006` Food Establishment — a dining venue listing promoted/reservable through the platform.
- `DM-ENT-007` Local Information Article — general-interest content (culture, safety, weather, events, etiquette) authored by staff.
- `DM-ENT-008` Package (Itinerary) — a curated bundle combining Destinations, Accommodation, Vehicle, and/or Food Establishment selections into one bookable trip plan.
- `DM-ENT-009` Option — a selectable add-on/configuration attached to a Booking or Package (e.g., guided-tour add-on, meal preference, insurance, child seat). **Required entity — do not omit.**
- `DM-ENT-010` Booking — a Tourist's pending or confirmed reservation against an Accommodation, Vehicle, Food Establishment, or Package.
- `DM-ENT-011` Review — a Tourist-submitted rating/comment evaluating an Accommodation, Vehicle, Food Establishment, Destination, or Package.

### 5.2 Relationships (`DM-REL-xxx`, with cardinality — no attributes)
- `DM-REL-001` Tourist (1) —creates→ Booking (0..*)
- `DM-REL-002` Booking (1) —targets→ exactly one of {Accommodation | Vehicle | Food Establishment | Package} (conceptual generalization "Offering"; do not create a new DB-style entity for this — describe in prose only)
- `DM-REL-003` Booking (0..*) —includes→ Option (0..*) [many-to-many]
- `DM-REL-004` Package (0..*) —bundles→ Destination (1..*), Accommodation (0..*), Vehicle (0..*), Food Establishment (0..*) [aggregation, many-to-many]
- `DM-REL-005` Destination (0..*) —near→ Accommodation / Food Establishment (0..*) [informational/spatial, optional]
- `DM-REL-006` Tourist (1) —writes→ Review (0..*)
- `DM-REL-007` Review (0..*) —evaluates→ exactly one of {Accommodation | Vehicle | Food Establishment | Destination | Package}
- `DM-REL-008` Management Staff (1..*) —publishes/maintains→ Local Information Article (0..*)
- `DM-REL-009` Management Staff (1..*) —curates (CRUD)→ Destination, Accommodation, Vehicle, Food Establishment, Package, Option
- `DM-REL-010` Management Staff (1) —processes (approve/adjust/cancel)→ Booking (0..*)

### 5.3 Diagram Instruction
- Render as a simple conceptual class/ER-style diagram: entity boxes contain only the entity name + one-line description; relationship lines carry the verb label + cardinality from 5.2. No attribute compartments.

---

## 6. User Tasks (Tasks & Support Approach) — 40-pt criterion, hard requirement

### 6.1 Standard Task Template (apply identically to every task — no field ever left blank)
- Task ID & Name (header must literally read "Task `TASK-xxx`: `<Name>`" — must exactly match the section title, no copy-paste mismatches)
- Actors (which `ACT-xxx` perform/receive the task)
- Trigger
- Precondition
- Postcondition (mandatory — states the resulting system/domain state)
- Frequency
- Priority / Exception-Criticality (mandatory rating + note, never blank)
- Work Area
- Solution-Agnosticism Check: name ≥3 different realizable solutions/channels for this task (per brief's `strict_ground_rules.solution_agnosticism`)
- Subtasks: each subtask must state (a) the normal flow step and (b) at least one realistic Problem/Exception case with the system's handling
- Variants
- Derived Functional Requirements: list of `REQ-FUN-xxx` IDs (verifiable "the system shall..." statements), one or more per subtask

### 6.2 Task Hierarchy / Goal Tree (companion artifact — required)
```
System Goal: Promote Sarawak Tourism & Enable Association Management
├── Tourist Goal: Plan & Experience a Sarawak Trip
│    ├── TASK-001 Register & Manage Tourist Account
│    ├── TASK-002 Discover Local Tourism Information
│    ├── TASK-003 Search & Reserve Accommodation
│    ├── TASK-004 Search & Reserve Transportation (Vehicle)
│    ├── TASK-005 Search & Reserve Food & Dining
│    ├── TASK-006 Build & Book a Travel Package (Itinerary) with Options
│    ├── TASK-007 Complete Payment for a Booking
│    └── TASK-008 Submit Review & Feedback
└── Management Goal: Maintain an Authoritative, Compliant Tourism Platform
     ├── TASK-009 Manage Promotional Content & Listings
     ├── TASK-010 Manage Bookings, Availability & Provider Coordination
     └── TASK-011 Manage Tourist Data Privacy Requests (PDPA)
```

### 6.3 Major Tasks (11 total — exceeds the 8 minimum to demonstrate elicitation depth)

**TASK-001: Register & Manage Tourist Account**
- Actors: ACT-001
- Trigger: Tourist wants to create/update a profile before or during platform use
- Precondition: Platform accessible in guest mode; PDPA notice presented
- Postcondition: Account created/updated with a timestamped consent record; guest browsing still available if consent declined
- Frequency: Low (one-time + occasional updates) | Priority: High — gates personalization & PDPA consent
- Work Area: Tourist account/profile module
- Solution-Agnosticism: (a) self-service web form, (b) native mobile onboarding flow, (c) staff-assisted counter/kiosk registration
- Subtasks:
  - ST-1.1 View & accept/decline Terms of Use and Privacy Policy — Problem: consent declined → system restricts personalization but still allows guest browsing (`REQ-FUN-001`, `REQ-FUN-002`)
  - ST-1.2 Provide profile details (contact, nationality, preferred language/currency) — Problem: invalid/duplicate contact info submitted → system flags for correction before saving (`REQ-FUN-003`)
  - ST-1.3 Update or request deletion of profile/preferences — Problem: tourist requests full data deletion → triggers PDPA data-subject workflow (→TASK-011) (`REQ-FUN-004`)
- Variants: Guest checkout without full registration; social-login-assisted registration (if enabled)

**TASK-002: Discover Local Tourism Information**
- Actors: ACT-001
- Trigger: Tourist wants destination/culture/safety/weather/event information
- Precondition: Platform accessible (guest or registered)
- Postcondition: Tourist has viewed/saved relevant local-information content
- Frequency: High | Priority: Medium-High — core promotional function
- Work Area: Local information/content module
- Solution-Agnosticism: (a) searchable web content hub, (b) mobile app content feed, (c) QR-linked kiosk/brochure backed by the same repository
- Subtasks:
  - ST-2.1 Search/filter information by category (culture, safety, weather, events) — Problem: no matching results → system suggests related/alternative categories (`REQ-FUN-005`)
  - ST-2.2 View a Local Information Article in detail — Problem: article outdated/unpublished → system auto-hides expired content (`REQ-FUN-006`)
  - ST-2.3 Bookmark article for later (registered tourist only) — Problem: guest attempts to bookmark → system prompts registration (→TASK-001) (`REQ-FUN-007`)
- Variants: Location-based auto-suggested info (if geolocation permitted); offline-saved info for low-connectivity areas

**TASK-003: Search & Reserve Accommodation**
- Actors: ACT-001
- Trigger: Tourist needs lodging for planned travel dates
- Precondition: Accommodation listings published with availability
- Postcondition: Booking created in Pending/Confirmed state against an Accommodation
- Frequency: High | Priority: High — core function
- Work Area: Accommodation search & reservation module
- Solution-Agnosticism: (a) web filter + reservation form, (b) mobile booking flow, (c) staff-assisted phone/counter booking recorded in the same system
- Subtasks:
  - ST-3.1 Search/filter Accommodation by location, date, price, type — Problem: zero results for the filter combination → system suggests relaxed filters/nearby dates (`REQ-FUN-008`)
  - ST-3.2 View Accommodation detail & Reviews — Problem: no reviews exist yet → system shows an explicit "no reviews yet" state (`REQ-FUN-009`)
  - ST-3.3 Select Accommodation & submit reservation — Problem: dates become unavailable mid-transaction → system re-validates availability before confirming and notifies tourist if lost (`REQ-FUN-010`)
- Variants: Reservation with Option add-ons; group/multi-room booking

**TASK-004: Search & Reserve Transportation (Vehicle)**
- Actors: ACT-001
- Trigger: Tourist needs transport (car/van/boat/bus) for touring or transfer
- Precondition: Vehicle listings published with an availability calendar
- Postcondition: Booking created in Pending/Confirmed state against a Vehicle
- Frequency: High | Priority: High — core function, explicit Vehicle-entity focus
- Work Area: Transportation search & reservation module
- Solution-Agnosticism: (a) web listing page, (b) mobile app with map-based search, (c) staff-assisted back-office allocation for walk-in tourists
- Subtasks:
  - ST-4.1 Search/filter Vehicle by type, capacity, date, pickup location — Problem: no Vehicle matches requested capacity → system suggests multiple smaller vehicles or nearest alternative (`REQ-FUN-011`)
  - ST-4.2 View Vehicle detail (capacity, coverage area, provider) — Problem: Vehicle temporarily suspended (maintenance) → system excludes it from search results (`REQ-FUN-012`)
  - ST-4.3 Reserve Vehicle with optional add-ons (driver, child seat, via Option) — Problem: selected Option incompatible with the chosen Vehicle → system blocks the combination and explains the conflict (`REQ-FUN-013`)
- Variants: Self-drive rental vs. chauffeured tour vehicle; shared shuttle vs. private vehicle

**TASK-005: Search & Reserve Food & Dining**
- Actors: ACT-001
- Trigger: Tourist wants to find/reserve a dining venue
- Precondition: Food Establishment listings published
- Postcondition: Reservation created, or an informational view logged for walk-in-only venues
- Frequency: High | Priority: Medium — core function
- Work Area: Food & dining discovery/reservation module
- Solution-Agnosticism: (a) web listing + optional reservation form, (b) mobile cuisine-based search, (c) staff-curated recommendation counter using the same backend listings
- Subtasks:
  - ST-5.1 Search/filter by cuisine, location, price, dietary option — Problem: no result for a dietary filter (e.g., halal/vegetarian) → system flags the coverage gap for Management Staff review (`REQ-FUN-014`)
  - ST-5.2 View Food Establishment detail & Reviews — Problem: listing missing required license/registration reference → system withholds publication (links `REQ-PROD-007`) (`REQ-FUN-015`)
  - ST-5.3 Submit table reservation where supported — Problem: venue does not support online reservation → system displays contact-only information instead of a booking form (`REQ-FUN-016`)
- Variants: Walk-in-only venue (informational only); reservable venue with deposit requirement

**TASK-006: Build & Book a Travel Package (Itinerary) with Options**
- Actors: ACT-001
- Trigger: Tourist wants a bundled multi-service/multi-day trip plan
- Precondition: At least one Destination/Accommodation/Vehicle/Food Establishment is published and available
- Postcondition: Package Booking created combining selected components and chosen Options
- Frequency: Medium | Priority: High — ties all domain entities together
- Work Area: Package/itinerary builder module
- Solution-Agnosticism: (a) drag-and-drop web itinerary builder, (b) guided step-by-step mobile wizard, (c) staff-assembled custom quote tool using the same catalog
- Subtasks:
  - ST-6.1 Select Destinations and combine with Accommodation/Vehicle/Food components — Problem: selected components' dates conflict → system flags the scheduling conflict before checkout (`REQ-FUN-017`)
  - ST-6.2 Choose applicable Options for the Package (guided tour, insurance, meal plan) — Problem: chosen Option becomes unavailable → system removes it and notifies the tourist before payment (`REQ-FUN-018`)
  - ST-6.3 Review consolidated Package summary & confirm — Problem: total price changes mid-session due to a component price update → system re-displays the updated total for re-confirmation (`REQ-FUN-019`)
- Variants: Staff-curated "featured package" vs. fully custom tourist-built package

**TASK-007: Complete Payment for a Booking**
- Actors: ACT-001, ACT-004 (external)
- Trigger: Tourist confirms a Booking/Package requiring payment
- Precondition: Booking exists in Pending-Payment state; payment gateway interface available
- Postcondition: Booking transitions to Confirmed (success) or Payment-Failed (failure); tourist notified
- Frequency: High | Priority: High — revenue-critical
- Work Area: Checkout/payment module
- Solution-Agnosticism: (a) redirect to hosted payment page, (b) embedded payment widget/SDK, (c) staff-recorded manual/offline payment reconciled in-system
- Subtasks:
  - ST-7.1 Select payment method & submit payment — Problem: payment declined/gateway timeout → Booking preserved as Pending-Payment for retry within a defined window rather than silently cancelled (`REQ-FUN-020`)
  - ST-7.2 Receive payment & booking confirmation — Problem: gateway confirms payment but system fails to update Booking status → automated reconciliation check alerts Management Staff (`REQ-FUN-021`)
  - ST-7.3 Request refund/cancellation — Problem: cancellation requested after provider's non-refundable cutoff → system displays the applicable policy and auto-limits the refund (`REQ-FUN-022`)
- Variants: Full online payment; partial deposit + balance on arrival (if supported)

**TASK-008: Submit Review & Feedback**
- Actors: ACT-001
- Trigger: Tourist completes a booked experience, or wants to give general feedback
- Precondition: Tourist has a completed Booking (verified review) or a general feedback channel is open
- Postcondition: Review stored and linked to the relevant entity; pending moderation if applicable
- Frequency: Medium | Priority: Medium — supports INC-003 trust goal
- Work Area: Review & feedback module
- Solution-Agnosticism: (a) post-trip web review form, (b) mobile push-prompted review, (c) email/SMS-linked review form after Booking completion
- Subtasks:
  - ST-8.1 Access review form for a completed Booking — Problem: tourist attempts to review a Booking not yet completed → system blocks premature submission (`REQ-FUN-023`)
  - ST-8.2 Submit rating & comment — Problem: content contains prohibited/offensive language → system flags for Management Staff moderation before publishing (`REQ-FUN-024`)
  - ST-8.3 View published Reviews on entity pages — Problem: a Review is removed by moderation → it is not shown publicly and the tourist is notified of the outcome (`REQ-FUN-025`)
- Variants: Verified-booking review vs. general open feedback not tied to a Booking

**TASK-009: Manage Promotional Content & Listings**
- Actors: ACT-002
- Trigger: A Destination/Accommodation/Vehicle/Food Establishment/Local Info Article/Option needs creating, updating, or retiring
- Precondition: Staff authenticated with content-management permission
- Postcondition: Domain entity record created/updated/archived and reflected in tourist-facing views
- Frequency: Medium-High (ongoing) | Priority: High — core management-facing function
- Work Area: Content/listing administration back office
- Solution-Agnosticism: (a) web admin dashboard/CMS, (b) desktop back-office application, (c) bulk spreadsheet-import tool feeding the same repository
- Subtasks:
  - ST-9.1 Create/edit a listing record — Problem: required legal/registration reference missing → system blocks publish until supplied (`REQ-FUN-026`)
  - ST-9.2 Publish/unpublish or archive a listing — Problem: staff attempts to archive an entity with active future Bookings → system warns and requires explicit confirmation/reassignment (`REQ-FUN-027`)
  - ST-9.3 Author/edit a Local Information Article — Problem: article scheduled to publish is missing a required category tag → system prevents publish without categorization (`REQ-FUN-028`)
- Variants: Single-record edit vs. bulk update; optional draft/maker-checker review before publish

**TASK-010: Manage Bookings, Availability & Provider Coordination**
- Actors: ACT-002/ACT-003
- Trigger: A new Booking/Package request is received, or availability/capacity needs adjustment
- Precondition: Staff authenticated with booking-management permission; Booking(s) exist
- Postcondition: Booking approved/adjusted/cancelled; availability calendars updated accordingly
- Frequency: High | Priority: High
- Work Area: Booking & availability administration module
- Solution-Agnosticism: (a) web admin booking queue/calendar, (b) mobile back-office app for on-the-go approvals, (c) call-center/manual-entry tool for phone-based coordination
- Subtasks:
  - ST-10.1 Review & approve/reject a pending Booking — Problem: requested capacity exceeds Vehicle/Accommodation availability → system flags overbooking risk and prevents silent approval (`REQ-FUN-029`)
  - ST-10.2 Adjust an availability calendar — Problem: staff sets a conflicting availability window overlapping confirmed Bookings → system warns of the conflict (`REQ-FUN-030`)
  - ST-10.3 Cancel/modify a Booking on the tourist's or provider's behalf — Problem: cancellation occurs after payment capture → triggers the refund workflow (→TASK-007) (`REQ-FUN-031`)
- Variants: Auto-approval for standard bookings vs. manual review for high-value/group bookings

**TASK-011: Manage Tourist Data Privacy Requests (PDPA)**
- Actors: ACT-003
- Trigger: Tourist submits a data access/correction/deletion request (from ST-1.3 or a dedicated privacy-request channel)
- Precondition: Staff authenticated with data-administration permission; request logged
- Postcondition: Request actioned (exported/corrected/deleted) and requester notified within SLA; action logged for audit
- Frequency: Low | Priority: High — legal/compliance-critical
- Work Area: Privacy/compliance administration module
- Solution-Agnosticism: (a) self-service web privacy-request portal reviewed by staff, (b) staff-managed ticket/case tool, (c) manual email-based request logged into the same backend
- Subtasks:
  - ST-11.1 Verify tourist identity for the request — Problem: identity cannot be confidently verified → system requires an additional verification step before proceeding (`REQ-FUN-032`)
  - ST-11.2 Fulfil the access/correction/deletion request — Problem: deletion requested but data is legally required to be retained (e.g., financial record) → system anonymizes rather than deletes, with justification logged (`REQ-FUN-033`)
  - ST-11.3 Log outcome & notify tourist within SLA — Problem: SLA deadline approaching without resolution → system auto-escalates to responsible staff (`REQ-FUN-034`)
- Variants: Routine access request vs. full account-deletion request (cascades into Booking/Review retention handling)

---

## 7. Workflows

### 7.1 Overarching End-to-End Workflow (required companion to per-task diagrams)
- `WF-000` "Tourist Trip Planning & Booking Lifecycle" — swimlanes: Tourist | System | Management Staff | External (Payment/Notification).
- Sequence to depict: Discover Info (TASK-002) → Browse Accommodation/Vehicle/Food (TASK-003/004/005) → Build Package + Options (TASK-006) → Review Summary → Payment (TASK-007) → Confirmation Notification → Trip Experience → Feedback/Review (TASK-008); parallel Management lane: Manage Content (TASK-009) ↔ Manage Bookings/Availability (TASK-010) feeding back into the tourist-facing catalog; PDPA request lane (TASK-011) branching off TASK-001/any point.
- Must include decision branches for: payment failure/retry, availability conflict at confirmation, PDPA consent declined (guest-mode continuation).

### 7.2 Per-Task Workflow Diagrams
- `WF-001`…`WF-011` — one per TASK-001…TASK-011.
- Rule: each diagram must include swimlanes separating every actor named in that task's Actors field, and must visibly branch for every Problem/Exception case documented in that task's subtasks (no task may be drawn as a straight-line sequence if its table documents a Problem case — this was the exact defect flagged against Tasks 4–9 in the reference sample).

### 7.3 Diagram Legend (mandatory, single shared legend reused across all WF diagrams)
- Notation: UML Activity Diagram.
- Green rounded rectangle = Start; Red rounded rectangle = End/Close; Diamond = Decision; Swimlane column = Actor; Solid arrow = normal flow; Dashed arrow = exception/problem path.

---

## 8. Non-Functional Requirements — exactly 4 categories, each with numeric/testable acceptance criteria

**`REQ-NFR-001` Performance & Scalability**
- Search/browse results (TASK-002…005) return within ≤3 seconds at the 95th percentile for a catalog of up to 10,000 listings, verified by load testing.
- End-to-end Booking submission-to-confirmation (excluding external payment-gateway processing time) completes in ≤5 seconds.
- Platform sustains ≥500 concurrent worldwide users at the above response times, verified by load-test report.

**`REQ-NFR-002` Security & Data Privacy (PDPA Compliance)**
- All personal data (profile, Booking, payment reference) encrypted at rest (e.g., AES-256) and in transit (TLS 1.2+), verified by configuration/pen-test audit.
- 100% of restricted management endpoints reject access from an unauthorized role in role-based access-control test cases.
- 100% of data-processing activities are traceable to a timestamped consent record (TASK-001), verified by consent-log audit.
- Data subject access/correction/deletion requests (TASK-011) are fulfilled within a defined SLA (e.g., ≤21 days), verified by request-tracking log.

**`REQ-NFR-003` Usability & Accessibility**
- A first-time tourist completes a core task (e.g., search + view an Accommodation) within ≤3 minutes with a ≥90% success rate, measured via usability testing on a representative worldwide sample (n≥8).
- Interface ships in a minimum of [N] languages including English and Bahasa Malaysia (ASSUMP-007), with 100% of core-task screens localized, verified by a localization QA checklist.
- Conforms to WCAG 2.1 Level AA, verified by automated accessibility scan (score ≥90) plus manual audit.

**`REQ-NFR-004` Availability & Reliability**
- System availability ≥99.5% measured monthly (excluding pre-announced maintenance windows ≥48 hours notice), verified by uptime-monitoring logs.
- RTO ≤4 hours and RPO ≤24 hours for any unplanned outage, verified by disaster-recovery drill records.
- No single unplanned outage exceeds 2 continuous hours during core booking-service hours, verified by incident-log review.

Rule: no 5th category permitted; any additional quality concern (e.g., portability/localization specifics) is folded into REQ-NFR-003 rather than added as a new category.

---

## 9. Other Design & Product-Level Requirements

### 9.1 Design-Level Requirements (`REQ-DES-xxx`) — each tied back to a Goal/Pain Point
- `REQ-DES-001` (→GOAL-001) Display tourism-association branding/visual identity consistently per the association's brand guideline document.
- `REQ-DES-002` (→GOAL-004/PP-006) Display Terms of Use and PDPA-aligned Privacy Policy with mandatory acknowledgment at first use/registration.
- `REQ-DES-003` (→PP-004) Present pricing in the tourist's selected currency, with a stated exchange-rate source and refresh frequency.
- `REQ-DES-004` (→PP-004) Provide a multi-language toggle accessible from every core screen.

### 9.2 Product-Level Requirements (`REQ-PROD-xxx`)
- `REQ-PROD-001` Data retention: tourist personal data retained no longer than [X years] post last activity unless legally required, then anonymized/purged (PDPA storage-limitation principle).
- `REQ-PROD-002` Audit logging of every create/update/delete performed by Management Staff on a domain entity, retained for [X months] for accountability review.
- `REQ-PROD-003` Interoperability: secure, tokenized API integration with the external Payment Gateway (ACT-004) — no raw card data stored in-system.
- `REQ-PROD-004` Interoperability: integration with an external Mapping/Geolocation service (ACT-006) to display Destination/Accommodation/Vehicle locations.
- `REQ-PROD-005` Interoperability: integration with an external Notification service (ACT-005) for booking confirmations and PDPA-request acknowledgements.
- `REQ-PROD-006` Training/documentation: management-facing modules accompanied by a staff user guide and onboarding walkthrough.
- `REQ-PROD-007` Legal: Accommodation, Vehicle, and Food Establishment listings must record a valid local business registration/license reference before publication (verified in TASK-009 ST-9.1).
- `REQ-PROD-008` Internationalization: currency, date, and unit formatting adapt to the tourist's selected locale.

---

## 10. PDPA & Regulatory Compliance (`REQ-PDPA-xxx`)
- `REQ-PDPA-001` Lawful basis/consent: explicit opt-in consent captured before collecting/processing personal data beyond anonymous browsing (links TASK-001 ST-1.1).
- `REQ-PDPA-002` Purpose limitation: personal data used only for stated purposes (booking fulfillment, service improvement, legally required reporting); no undisclosed secondary use.
- `REQ-PDPA-003` Data minimization: only data necessary for booking/communication is collected.
- `REQ-PDPA-004` Data subject rights: access/correction/deletion mechanism with staff workflow actioned within SLA (links TASK-011, `REQ-NFR-002`).
- `REQ-PDPA-005` Cross-border consideration: explicit statement of where tourist data is hosted/processed and applicable safeguard, given a worldwide user base (links ASSUMP-005).
- `REQ-PDPA-006` Breach handling: documented detection/notification procedure for affected data subjects and the authority (ACT-008).
- `REQ-PDPA-007` Retention & disposal: aligned with `REQ-PROD-001`.

---

## 11. Validation Summary
- State plainly (in-body) that full evidence lives in Appendix A–D, and summarize: number of stakeholders consulted, validation methods used, headline changes made as a result, and confirmation that an IEEE-830-style verifiability audit (Appendix D) was applied to 100% of REQ-* items with zero unresolved non-verifiable statements.

---

## 12. Conclusion & Recommendations
- Summarize how Sections 2–10 jointly satisfy `GOAL-001`…`GOAL-004`.
- State any residual risk/open assumption requiring client sign-off before development begins (pointer back to Section 3 flagged items: ASSUMP-002, ASSUMP-005, ASSUMP-007).
- No new requirements introduced here — recommendation/decision framing only, explicitly tied back to prior sections (avoids the "dangling solutions section" defect).

---

## Appendix A — Stakeholder Validation Evidence
- Table columns: Evidence ID (`VAL-xxx`) | Stakeholder Name & Role (not just "management"/"employees") | Date | Method (interview script / walkthrough / prototype demo / survey) | Specific Feedback | Resulting Document Change (cite section/REQ ID changed).
- Minimum coverage: one entry representing Tourism Association marketing/content role, one representing operations/booking role, one representing IT/compliance role, one representing a sample of worldwide tourists (usability test, n≥8, nationalities noted).

## Appendix B — Requirements Traceability Matrix
- Columns: Goal/Pain Point ID → Objective ID → Task ID → REQ-FUN ID(s) → REQ-NFR/DES/PROD/PDPA ID(s) → Validation Evidence ID (`VAL-xxx`) → Verification Method.
- Rule: every ID minted in Sections 2, 6, 8, 9, 10 must appear as a row; zero orphan requirements (untraced) and zero orphan goals (unaddressed) permitted.

## Appendix C — CRUD Matrix
- Rows: all 11 entities from Section 5.1 (`DM-ENT-001`…`DM-ENT-011`) — must match exactly, no additions/omissions.
- Columns: Tourist | Management Staff | System(automated process), each split into C/R/U/D.
- Rule: every entity has at least one populated C, R, U, and D cell; if an operation is intentionally restricted (e.g., Tourist cannot hard-delete a Review), state the restriction explicitly rather than leaving the cell blank (e.g., "soft-delete/hide only, by Management Staff").

## Appendix D — Verifiability Self-Check (IEEE 830 Quality Audit)
- Table columns: Requirement ID | Statement | Unambiguous (Y/N) | Verifiable (Y/N) | Consistent (Y/N) | Traceable (Y/N) | Notes/Fix Applied.
- Apply to every `REQ-FUN`, `REQ-NFR`, `REQ-DES`, `REQ-PROD`, `REQ-PDPA` item.
- Rule: zero rows may ship with Verifiable = N; any illustrative/example text must be explicitly labeled "Non-Normative" and excluded from the requirement count.

## Appendix E — Domain Vocabulary / Glossary
- One-line definitions for: Tourist, Management Staff, Destination, Accommodation, Vehicle, Food Establishment, Local Information Article, Package, Option, Booking, Review, PDPA, and any acronym used in the document.

## Appendix F — Iteration / Revision Evidence Log
- Format per entry: Draft Requirement (v1) → Feedback Source (`VAL-xxx`) → Revised Requirement (v2) → Rationale.
- Minimum 2–3 worked examples required to demonstrate substantive iteration occurred (not just an assertion of review).

---

## Cross-Cutting Compliance Notes for the Technical-Builder Agent
- Every task in Section 6 must keep identical field order/labels — no per-task template drift (this was the single largest point-loss risk in the reference sample).
- Do not introduce a 5th NFR category anywhere in the document, including Appendix D rows.
- Do not add attribute lists/fields to any Section 5 entity box or description — descriptions stay conceptual/one-line.
- Every "the system shall..." statement must be independently testable; any narrative/illustrative solution text must be visually/typographically separated and marked non-normative.
- Proofread pass required before submission (Coherent Document criterion) — no invented typos to fix, but confirm none are introduced during expansion.
