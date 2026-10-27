# 02 Blueprint: STPS Initial Object Design (SWE30003, Group 16, Assignment 2)

Blueprint for the technical writer. Decisions are final; the approved defaults are in Section 2.5 and the remaining open questions in Section 12. "A1 §N" means Assignment 1 SRS section N. Task numbers and titles are the ones in the contract: 1 Discover Local Tourism Information, 2 Reserve Accommodation, 3 Reserve Transportation, 4 Reserve Food & Dining, 5 Book Services, 6 Submit Review & Feedback, 7 Manage Promotional Content & Listing, 8 Manage Bookings Availability, 9 Manage Own Listing Availability, 10 Decide on Own-Listing Bookings.

Revision 2 (team request): guests can book, as A1 says. No class was added or removed; the count stays 36. The changes are AS-01, AS-21, SI-01, D-19, REL-66, rows GST-01 to GST-05, SC-01, and the CRC cards of AccountRegistry, Tourist, ReservationRequest, Booking, ComponentBooking, ReservationCoordinator, NotificationDispatcher, PaymentCoordinator and ReviewCoordinator.

Writer conventions (binding):
- CRC heading `### CRC Card: ClassName`, then `**Superclass:**` (class name or `None`), then `**Description:**`, then a `| Responsibility | Collaborators |` table. Use `—` in an empty collaborator cell.
- Class names appear exactly as in Section 3.
- Sequence-diagram message labels are plain verbs that match the cited responsibility. They carry no parentheses or parameters. Reply arrows (`-->>`) carry results only.
- A message that hits an inherited responsibility is cited "(inherited from X)" in the trace table (approved).
- A1 stale references must NOT be copied (see Section 2.4). A2 includes a short errata note listing them (approved).

---

## 1. Problem analysis (noun/verb extraction)

### 1.1 Nouns
| ID | Candidate | Source | Outcome |
|---|---|---|---|
| N-01 | Tourist | A1 §3.2; Tasks 1–6 | CL-04 |
| N-02 | Guest | A1 §3.2 Actors ("browse as guest"); Task 1 subtask 3; Tasks 4–5 preconditions | Tourist in guest mode (AS-01, D-19) |
| N-03 | Registered profile / tourist account | A1 §3.2 Actors; PR-12 | CL-03 UserAccount, CL-02 AccountRegistry |
| N-04 | Management Staff | A1 §3.2, §6 | CL-06 |
| N-05 | Content Officer, Data/System Admin | A1 §3.2 Actors | Roles held by ManagementStaff (D-03) |
| N-06 | App / Service Management Staff | A1 §6 | D-02 |
| N-07 | User Role and Access | A1 §6 | Merged into UserAccount (D-04) |
| N-08 | Local Service Provider | A1 §3.2; Tasks 9, 10 | CL-05 |
| N-09 | Services (bookable offering) | A1 §6; §7 intro | CL-08 BookableOffering (D-01) |
| N-10 | Accommodation | A1 §6; Task 2 | CL-09 |
| N-11 | Vehicle / Transportation | A1 §6; Task 3 | CL-10 |
| N-12 | Food Establishment | A1 §6; Task 4 | CL-11 |
| N-13 | Destination | A1 §6; Task 1; Task 5 trigger | CL-12 (AS-02) |
| N-14 | Local Article Info | A1 §6; Task 1 subtask 2 | CL-13 |
| N-15 | Listing / promotional content | Task 7 | CL-07 ContentItem |
| N-16 | Package / Service Package / Travel Package | Task 5; PR-09 | CL-14 ServicePackage |
| N-17 | Itinerary | Task 5 trigger | PackageBooking without a ServicePackage (D-08) |
| N-18 | Booking | A1 §6 | CL-18 |
| N-19 | Package Booking, component Booking | Task 5 postcondition; Task 8 subtasks 1–3 | CL-20, CL-19 |
| N-20 | Booking status | PR-15 | Booking responsibility (D-06) |
| N-21 | Availability calendar | Task 8 subtask 4 | CL-22 |
| N-22 | Availability slot / daily capacity | Task 9 subtask 1; A1 §7.4 | CL-23 |
| N-23 | Guest, contact, reservation and journey details | Task 2 subtask 2; Task 3; Task 4 subtask 3; Task 5 subtask 3 | CL-17 ReservationRequest |
| N-24 | Add-on (dietary) | A1 §5 workflow 4 | SI-05 |
| N-25 | Payment | A1 §6; PR-10 | CL-28 |
| N-26 | Refund | Task 8 subtasks 3, 5 | Merged into Payment (D-09) |
| N-27 | Payment Gateway Provider | A1 §2.3, §3.2 | CL-33 |
| N-28 | Notification / Notification Service | A1 §2.3; Task 10 subtask 3 | CL-27, CL-34 |
| N-29 | Mapping / Geolocation Service | A1 §2.3; Task 1 variant 1a | CL-35 |
| N-30 | Translation / Localization Service | A1 §2.3; Task 7 subtask 3 | CL-36 |
| N-31 | SLA window (48 h) | Task 8 trigger; Task 10 subtask 2 | CL-26; ComponentBooking R2 |
| N-32 | Review | A1 §6; Task 6 | CL-31 |
| N-33 | General feedback | Task 6 subtask 1, variant 3a | CL-30 Feedback |
| N-34 | Average rating | Task 6 subtask 6 | BookableOffering R5 |
| N-35 | Bookmark | Task 1 subtask 3 | Tourist R3 (D-11) |
| N-36 | Category | Task 1 subtask 1; PR-03 | ContentItem R1 (value) |
| N-37 | Decline reason | Task 10 subtask 3 | ComponentBooking R4 |
| N-38 | Daily slot-utilisation summary | Task 10 subtask 3 | NotificationDispatcher R4 |
| N-39 | MYR price, indicative conversion | Task 5 subtask 2; A1 §7.3 | BookableOffering R2; CL-36 R2 (D-12) |
| N-40 | PDPA data-subject request, consent | A1 §3.2 Actors; §7.2 | AccountRegistry R5; Tourist R5; ReservationRequest R2 (D-13) |
| N-41 | Data repository | A1 §2.2 | SI-02 (D-14) |
| N-42 | Audit "who and when" | Task 7 subtask 6; A1 §7.2 | ContentItem R4; Payment R3, R4 |

### 1.2 Verbs
| ID | Verb phrase | Source | Owner |
|---|---|---|---|
| V-01 | search by category or location | Task 1 subtask 1, variant 1a | ContentCatalogue R2 |
| V-02 | suggest related categories or alternatives | Task 1 subtask 1; Task 2 variant 1a | ContentCatalogue R3, R5 |
| V-03 | hide expired content | Task 1 subtask 2 | ContentItem R5 |
| V-04 | validate booking and contact details | Task 2 variant 2a; Task 4 subtasks 1, 3; Task 5 subtask 3 | BookableOffering R4, ReservationCoordinator R1 |
| V-05 | check availability, hold capacity | Tasks 2–5; A1 §5 workflows 2–5 | AvailabilityCalendar R2, R3 |
| V-06 | record reservation | Task 2 subtask 2; Task 3 subtask 3 | ReservationCoordinator R3, R4 |
| V-07 | approve / decline with reason | Task 10 subtasks 2–3 | BookingDecisionCoordinator R2, R3 |
| V-08 | escalate after SLA | Task 10 subtask 2; Task 8 trigger | BookingDeadlineMonitor R3 |
| V-09 | override / finalise non-approval | Task 8 variant "Provider decision" | BookingDecisionCoordinator R4 |
| V-10 | pay after approval | Task 4 postcondition; PR-10 | PaymentCoordinator R1–R3 |
| V-11 | refund after capture | Task 8 subtasks 3, 5 | PaymentCoordinator R5 |
| V-12 | set daily capacity, block below Confirmed | Task 9 subtask 1 | AvailabilityCalendar R5 |
| V-13 | publish, schedule, unpublish, archive | Task 7 subtasks 6–7 | ContentPublisher R3, R5, R7 |
| V-14 | validate and preview content | Task 7 subtasks 4–5 | ContentItem R3, R6 |
| V-15 | screen, moderate, publish review | Task 6 subtasks 4–6 | ReviewCoordinator R4–R6 |
| V-16 | notify parties | Task 6 subtask 6; Task 7 subtask 6; Task 10 subtask 3 | NotificationDispatcher |
| V-17 | register, authenticate | PR-12, PR-13 | AccountRegistry R1, R2 |
| V-18 | translate, convert currency | Task 7 subtask 3; Task 5 subtask 2 | LocalizationServiceAdapter |

---

## 2. Assumptions and simplifications

### 2.1 Assumptions
| ID | Assumption (one testable statement) | Rationale / source | Traces to |
|---|---|---|---|
| AS-01 | A Tourist can book in guest or registered mode. A guest is a temporary, unregistered Tourist object created by AccountRegistry for the visitor's session. Every booking records the contact details and consent from its ReservationRequest, and these are required and validated when the Tourist is a guest. Reviews still require a signed-in registered Tourist (Task 6), and bookmarking still prompts a guest to register without losing context (Task 1 subtask 3). | Task 4 and Task 5 preconditions ("guest or registered mode"); A1 §3.2 Actors. Recording contact details on the booking lets notifications, payment and decisions reach a guest without a stored account. | Tourist R3, R7; ReservationRequest R2; Booking R1, R8; AccountRegistry R1, R6; ReviewCoordinator R1; SC-01 |
| AS-02 | Destination is informational content, not a bookable offering. It can feature in a ServicePackage itinerary but never produces a ComponentBooking. | A1 §7 intro defines Bookable Offering as Accommodation, Vehicle or Food Establishment. The Task 5 postcondition creates component bookings only for those three. This resolves the A1 §6 subtype error. | Destination, ServicePackage |
| AS-03 | Capacity is a whole-number daily value per offering per date, in the offering's own unit: rooms for Accommodation, seats for Vehicle, covers for FoodEstablishment. | Task 9 subtask 1 ("daily capacity"). | AvailabilitySlot |
| AS-04 | Capacity is held from Pending until the booking is Confirmed (converted to confirmed) or Declined/Cancelled (released). Remaining capacity = capacity − held − confirmed. | A1 §5 workflows 2–5 ("hold capacity"); A1 §7.4; Task 4 subtask 2 (capacity held by packages). | AvailabilityCalendar R2–R4 |
| AS-05 | A provider capacity change is refused if it is below that day's Confirmed count (management resolution required) or below Confirmed + held (provider must decide Pending bookings first). Approved default. | Task 9 subtask 1. The extra held rule enforces A1 §7.4 (never overbook). | AvailabilityCalendar R5; SC-04 |
| AS-06 | Approval by the provider (or by a staff override) moves a booking to Pending-Payment and keeps its hold. The booking becomes Confirmed only when payment is captured. | PR-15; Task 4 postcondition. Resolves the Task 10 variant wording "approval confirms". | ComponentBooking R3; SC-01 |
| AS-07 | A Pending-Payment booking that is unpaid 24 hours after approval is Cancelled and its hold released. No refund is due. Approved default, and it applies to guests too. | A1 is silent. Without this rule a hold could last forever. | BookingDeadlineMonitor R5 |
| AS-08 | The 48-hour SLA runs from the creation of each ComponentBooking. Escalation is a flag on a Pending booking, not a status. | Task 8 trigger; Task 10 subtask 2; PR-15 has no "Escalated" state. | ComponentBooking R2; SC-03 |
| AS-09 | Package bookings are all-or-nothing. Every component must be held at creation. If any component is Declined, the PackageBooking is Declined, its other components are Cancelled and all holds are released. The tourist's plan is kept so it can be resubmitted. Approved default. | A1 §5 workflow 5 ("All components approved? No → release held capacity"); Task 5 variant 4a. | PackageBooking R3, R4; SC-02 |
| AS-10 | There is one Payment per payable booking: a standalone ComponentBooking or a whole PackageBooking. | Task 5 trigger ("as one Booking"). | Booking, Payment |
| AS-11 | Management Staff roles (Content Officer, Data/System Admin, booking management) are permission sets held by one ManagementStaff account, and one person may hold several. | A1 §3.2 Actors. Task 8 precondition names a third role, "booking-management permission". Resolves the A1 §6 association drawn instead of a generalisation. | ManagementStaff, UserAccount R2–R3 (D-03) |
| AS-12 | A staff override approval stands in for the provider's approval. After it, the provider cannot decline unilaterally: a provider that cannot honour the booking asks Management Staff to cancel it, with a refund if payment was captured. Approved default. | Task 8 subtask 3 ("Finalize a component Booking that its LSP did not approve … payment already made"); Task 9 "explicit resolution with management". | SC-03 |
| AS-13 | A registered Tourist may write at most one Review per BookableOffering. Tourist 1 — 0..* Review, and each Review is about exactly one BookableOffering. | Task 6 variant 2a. Resolves the A1 §6 table ("Many-to-Many") versus diagram conflict. | Review, Tourist R4 |
| AS-14 | Content statuses are Draft, Scheduled, Published, Unpublished and Archived. An incomplete item can be saved only as Draft. Items unpublish automatically at their end date. | Task 7 subtasks 4–7, variants 4a and 6a. | ContentItem R2–R3; ContentPublisher R7 |
| AS-15 | Prices are held in MYR. The Translation/Localization Service supplies indicative exchange rates, and when it is unreachable prices show in MYR only. | A1 §7.3; Task 5 subtask 2. See OQ-01. | LocalizationServiceAdapter R2 |
| AS-16 | Card details are entered only on the Payment Gateway Provider's own page. STPS keeps only the transaction reference and the payment status. | A1 §2.2; PR-10; Task 5 subtask 3. | PaymentGatewayAdapter R1 |
| AS-17 | A Confirmed booking becomes Completed automatically after its last service day has passed. Approved default. | Task 6 subtask 3 needs a completed booking, and A1 names no trigger. | BookingDeadlineMonitor R6 |
| AS-18 | If an external service is unreachable at start-up, STPS still starts in degraded mode: payments are refused and notifications are queued for retry. | Pay-after-approval means reservations can proceed without the gateway; A1 §7.4 availability. | STPSApplication R2 |
| AS-19 | Each AvailabilityCalendar processes hold requests for its offering one at a time. The locking mechanism is decided in A3. | A1 §7.4 (concurrent requests). | AvailabilityCalendar R3 |
| AS-20 | Withdrawing a listing that has Pending or Confirmed bookings is warned about, not blocked. Management Staff resolve the affected bookings under Task 8. | Task 7 variant 7a. A1 routes this to "(Task 10)", but staff, not providers, resolve it, so the design routes it to Task 8. | ContentPublisher R6 |
| AS-21 | A guest who returns later (to pay, or to view a booking) is identified by the booking reference and the contact address recorded on the booking. If the guest registers, AccountRegistry converts the guest Tourist into a registered one and keeps its bookings. | Pay-after-approval means a guest must come back after the 48-hour decision. Task 1 subtask 3 asks for registration "without losing the current browsing context". | AccountRegistry R1, R2; Booking R8; PaymentCoordinator R1 |

### 2.2 Simplifications
| ID | Simplification | Consequence |
|---|---|---|
| SI-01 | No UI boundary classes. The actor's account object (Tourist in guest or registered mode, LocalServiceProvider, ManagementStaff) acts as the actor's proxy and starts requests. The visitor's session start, which asks AccountRegistry for a guest Tourist, belongs to the deferred UI layer. | Presentation and screen validation move to A3. Sequence diagrams start at the account object. |
| SI-02 | Persistence uses the A1 §2.2 data repository. Re-loading at start-up is modelled as one "re-establishes" responsibility on the owning class. | A3 adds the persistence design. The design has no storage vocabulary. |
| SI-03 | Capacity is daily for every offering type. There are no dining time slots or per-departure seats, and Task 9 recurrence rules and one-day overrides are not modelled. | Finer-grained capacity is deferred. A1 Task 9 itself left this unspecified. |
| SI-04 | A booking modification (Task 8 subtask 5) is a cancellation (with a refund if captured) followed by a new reservation request. | No partial refunds or top-ups. |
| SI-05 | An add-on (A1 §5 workflow 4) is recorded as an unpriced special request on ReservationRequest. | Priced add-ons are deferred. |
| SI-06 | Offline viewing (Task 1 variant 2a) is a client-side concern and is not modelled. | Covered by the A3 client design. |
| SI-07 | Booking transitions are a rule table owned by Booking, not State-pattern classes. | Saves 7 classes. If per-state behaviour grows, State is revisited in A3 (Section 9.1, rejected patterns). |
| SI-08 | Review screening uses one built-in policy inside ReviewCoordinator. | A Strategy for screening rules is deferred. |
| SI-09 | PDPA request handling is limited to recording the request and sending a 14-day reminder. | The full data-subject request workflow is outside A1 Tasks 1–10. |
| SI-10 | There is one currency of record (MYR) and one payment gateway. | No Strategy is needed over gateways. |
| SI-11 | Time-driven classes check at a fixed interval. There is no general scheduler class. | The interval value is set in A3. |
| SI-12 | A guest Tourist is kept only while it holds bookings that are not finished. The retention period after that is decided with the PDPA design in A3. | No guest history is modelled. See OQ-03. |

### 2.3 Resolution of the known A1 gaps
| Gap | Resolution |
|---|---|
| Package, Add-on, availability slot and tourist account are not entities | Package → ServicePackage + PackageBooking. Add-on → SI-05. Slot → AvailabilitySlot «datatype» inside AvailabilityCalendar. Account → UserAccount, Tourist (guest or registered) and AccountRegistry. |
| Management Staff split drawn as an association | AS-11 (roles as permission sets; heuristic H-05). |
| Review–Tourist cardinality conflict | AS-13. |
| Payment and registration have no task | Coverage rows PAY-01 to PAY-05, ACC-01 to ACC-05 and GST-01 to GST-05 (Section 7), owned by PaymentCoordinator and AccountRegistry. |
| Destination drawn as a subtype of bookable Services | AS-02. |

### 2.4 A1 stale references the writer must not repeat (verified)
A2 lists these in a one-paragraph errata note (approved).
- A1 §7.2: "Task 1 (Register & Manage Tourist Account)". Task 1 is Discover Local Tourism Information. Cite PR-12 instead.
- A1 §5 workflows 4 and 5: "Pay after approval (Task 7)". Payment has no task. Cite PR-10.
- A1 §5 workflow 6: "Sign in / register (Task 1)". Cite PR-12.
- A1 §5 workflow 10: "Hand non-approved Booking to … (10)", a self-handoff. The correct target is Task 8.
- A1 §3.3 names Task 8 "Coordinate Bookings Availability", and the §4 heading for Task 9 adds "and Booking Decisions". Use the contract titles.
- A1 §7.3 cites "Section 2.3" for the language assumption, but it is in §2.2.

### 2.5 Approved defaults (team decisions; formerly open questions)
| ID | Decision | Where |
|---|---|---|
| AD-01 | Class model of 36 classes approved without trims | Section 3 |
| AD-02 | Guests can book (A1 Task 4 and Task 5 preconditions) | AS-01, AS-21 |
| AD-03 | 24-hour payment deadline after approval | AS-07 |
| AD-04 | Automatic completion after the last service day | AS-17 |
| AD-05 | All-or-nothing package decline (matches the A1 §5 Task 5 workflow) | AS-09 |
| AD-06 | Capacity reduction blocked below Confirmed + held | AS-05 |
| AD-07 | Staff override stands in for provider approval | AS-12 |
| AD-08 | CRC superclass placeholder is "None"; "—" is used only in collaborator cells | Writer conventions |
| AD-09 | Messages on inherited responsibilities are cited "(inherited from X)" | Writer conventions; Section 11 |
| AD-10 | A2 includes a short A1 errata note | Section 2.4 |

---

## 3. Final classes (36, approved)

Stereotypes: E = entity, C = control, X = external adapter, D = «datatype» (data structure definition), A = abstract (marked «abstract» in the diagram).

| ID | Class | Superclass | Purpose (one line) | Stereo | A1 tasks |
|---|---|---|---|---|---|
| CL-01 | STPSApplication | None | Entry point that creates and wires the long-lived objects at start-up | C | all (start-up) |
| CL-02 | AccountRegistry | None | Creates guest Tourists; registers and authenticates accounts; records role grants and PDPA requests | C | 1–6, PR-12, PR-13 |
| CL-03 | UserAccount | None | Abstract account of any STPS user: contact details, language, roles, authorisation | E, A | all |
| CL-04 | Tourist | UserAccount | Tourist in guest or registered mode; knows its bookings, bookmarks and feedback | E | 1–6 |
| CL-05 | LocalServiceProvider | UserAccount | Provider account; owns offerings and makes booking and capacity decisions | E | 9, 10 |
| CL-06 | ManagementStaff | UserAccount | Staff account holding Content Officer, Data/System Admin or booking-management roles | E | 6, 7, 8 |
| CL-07 | ContentItem | None | Abstract publishable bilingual content with a lifecycle | E, A | 1, 7 |
| CL-08 | BookableOffering | ContentItem | Abstract listing that can be reserved; owns an availability calendar | E, A | 2–5, 7–10 |
| CL-09 | Accommodation | BookableOffering | Lodging; validates stay details | E | 2, 5 |
| CL-10 | Vehicle | BookableOffering | Transport; validates journey details | E | 3, 5 |
| CL-11 | FoodEstablishment | BookableOffering | Dining venue; validates date, time and guest details | E | 4, 5 |
| CL-12 | Destination | ContentItem | Place of interest (park, cultural site, festival); informational only | E | 1, 5 |
| CL-13 | LocalArticleInfo | ContentItem | Culture, safety, weather or event article | E | 1, 7 |
| CL-14 | ServicePackage | ContentItem | Published bundle of offerings and destinations | E | 5, 7 |
| CL-15 | ContentCatalogue | None | Finds and ranks content for tourists and staff | C | 1–5, 7 |
| CL-16 | ContentPublisher | None | Runs the content lifecycle for Content Officers | C | 7 |
| CL-17 | ReservationRequest | None | Data structure holding a requested reservation, including contact details and consent, before it is recorded | D | 2–5 |
| CL-18 | Booking | None | Abstract booking with its recorded contact details (Composite component, Observer subject) | E, A | 2–5, 8, 10 |
| CL-19 | ComponentBooking | Booking | Booking of one offering (Composite leaf) | E | 2–5, 8, 10 |
| CL-20 | PackageBooking | Booking | Parent booking of the components of one trip (Composite) | E | 5, 8 |
| CL-21 | BookingObserver | None | Abstract receiver of booking status changes | C, A | 2–5, 8–10 |
| CL-22 | AvailabilityCalendar | BookingObserver | Daily capacity of one offering; never overbooks | E | 2–5, 8, 9 |
| CL-23 | AvailabilitySlot | None | Data structure for one day's capacity, held and confirmed counts | D | 8, 9 |
| CL-24 | ReservationCoordinator | None | Validates, holds and records single and package reservations | C | 2–5 |
| CL-25 | BookingDecisionCoordinator | None | Records provider and staff decisions, cancellations and modifications | C | 8, 10 |
| CL-26 | BookingDeadlineMonitor | BookingObserver | Watches decision, payment and service-end deadlines | C | 8, 10 |
| CL-27 | NotificationDispatcher | BookingObserver | Decides whom to notify, and at which contact details, and sends messages | C | 2–7, 9, 10 |
| CL-28 | Payment | None | Record of one payment and any refund; holds no card data | E | PR-10, 8 |
| CL-29 | PaymentCoordinator | None | Runs payment capture and refunds for registered and guest Tourists | C | PR-10, 8 |
| CL-30 | Feedback | None | General platform feedback from a registered tourist | E | 6 |
| CL-31 | Review | Feedback | Rated review of a bookable offering, with moderation status | E | 6 |
| CL-32 | ReviewCoordinator | None | Runs eligibility, screening, moderation and publication of reviews | C | 6 |
| CL-33 | PaymentGatewayAdapter | None | Adapter to the Payment Gateway Provider | X | PR-10, 8 |
| CL-34 | NotificationServiceAdapter | None | Adapter to the Notification Service | X | 6, 7, 10 |
| CL-35 | MappingServiceAdapter | None | Adapter to the Mapping/Geolocation Service | X | 1 |
| CL-36 | LocalizationServiceAdapter | None | Adapter to the Translation/Localization Service | X | 5, 7 |

The count (36) is above the 15–25 guide, and the team has approved it. It is driven by 10 tasks plus payment and accounts, by 4 external systems that each need an adapter under the contract, and by 3 A1 offering subtypes. Thin cards: 2 datatypes, 1 abstract observer, 4 adapters and the entry point. Guest booking needed no new class: a guest is a Tourist in guest mode (D-19).

Justification summary (for the writer's 4b section):
- Accommodation, Vehicle and FoodEstablishment stay separate classes because each validates different request details (Tasks 2, 3 and 4). This uses Polymorphism and Template Method.
- ContentCatalogue (finding content) and ContentPublisher (changing content) are split for cohesion (H-09).
- ReservationCoordinator, BookingDecisionCoordinator, BookingDeadlineMonitor and PaymentCoordinator are split by trigger (tourist request, human decision, time, payment) to avoid a BookingManager god class (H-04).

---

## 4. Discarded or merged candidates
| ID | Candidate | Source | Reason |
|---|---|---|---|
| D-01 | Services | A1 §6 | Renamed BookableOffering, and Destination removed from it (AS-02). The A1 §7 intro already equates Services with Bookable Offering. |
| D-02 | App Management Staff, Service Management Staff | A1 §6 | They contradict the A1 §3.2 actor names. Replaced by roles held by ManagementStaff (AS-11). |
| D-03 | ContentOfficer, DataSystemAdmin as subclasses | A1 §3.2 | Roles combine, and Task 8 needs a third role. Subclassing cannot express combined roles, so composition is used instead (H-05). |
| D-04 | UserRoleAndAccess | A1 §6 | Pure data with no behaviour. Merged into UserAccount R2–R3. |
| D-05 | BookingState hierarchy (State pattern) | PR-15 | Would add 7 cards while per-state behaviour is only a permitted-transition table (SI-07). |
| D-06 | BookingStatus class | PR-15 | An enumerated value known by Booking R2, with no behaviour. |
| D-07 | OfferingFactory (Factory Method) | Task 7 subtask 1 | One creation point (ContentPublisher R1) with one choice of kind. GRASP Creator is enough. |
| D-08 | Itinerary / TripPlan | Task 5 trigger | A custom itinerary is a PackageBooking with no ServicePackage. |
| D-09 | Refund | Task 8 subtasks 3, 5 | A refund is a state and record of Payment (Payment R4). |
| D-10 | Notification (message entity) | Task 10 subtask 3 | Messages are transient. Composed by NotificationDispatcher. |
| D-11 | Bookmark | Task 1 subtask 3 | Knowledge held by a registered Tourist, with no behaviour. |
| D-12 | Money / Currency | Task 5 subtask 2 | MYR value on the offering. Conversion is done by LocalizationServiceAdapter. |
| D-13 | PDPARequest, ConsentRecord | A1 §7.2 | Outside Tasks 1–10. Held as records by AccountRegistry R5, Tourist R5 and ReservationRequest R2 (SI-09). |
| D-14 | Database / Repository | A1 §2.2 | Solution-oriented at this stage (SI-02). |
| D-15 | ReviewScreener | Task 6 subtask 4 | A single policy. Merged into ReviewCoordinator R4 (SI-08). |
| D-16 | Scheduler / SLATimer | Task 8, Task 10 | Each time-driven class checks itself at an interval (SI-11). |
| D-17 | TouristPortal, ProviderConsole, StaffConsole | DR-08 | UI boundary classes deferred to A3 (SI-01). |
| D-18 | Main / System / Menu controller | sample critique | A god-class risk and an undefined entry point. STPSApplication only creates objects. |
| D-19 | GuestAccount / GuestBooker | A1 §3.2 Actors; Tasks 4–5 preconditions | No responsibility needs it. A guest is a Tourist in guest mode (Tourist R7). The booking records the guest's contact details (Booking R1), and a returning guest is identified by reference and contact address (AccountRegistry R2, Booking R8). A separate class would duplicate what Tourist already knows about bookings. |

---

## 5. Relationships (one Mermaid classDiagram; names, relationships, multiplicities and labels only)

| ID | Source | Type | Target | Mult (src : tgt) | Label |
|---|---|---|---|---|---|
| REL-01 | Tourist | generalisation | UserAccount | — | — |
| REL-02 | LocalServiceProvider | generalisation | UserAccount | — | — |
| REL-03 | ManagementStaff | generalisation | UserAccount | — | — |
| REL-04 | BookableOffering | generalisation | ContentItem | — | — |
| REL-05 | Destination | generalisation | ContentItem | — | — |
| REL-06 | LocalArticleInfo | generalisation | ContentItem | — | — |
| REL-07 | ServicePackage | generalisation | ContentItem | — | — |
| REL-08 | Accommodation | generalisation | BookableOffering | — | — |
| REL-09 | Vehicle | generalisation | BookableOffering | — | — |
| REL-10 | FoodEstablishment | generalisation | BookableOffering | — | — |
| REL-11 | ComponentBooking | generalisation | Booking | — | — |
| REL-12 | PackageBooking | generalisation | Booking | — | — |
| REL-13 | AvailabilityCalendar | generalisation | BookingObserver | — | — |
| REL-14 | NotificationDispatcher | generalisation | BookingObserver | — | — |
| REL-15 | BookingDeadlineMonitor | generalisation | BookingObserver | — | — |
| REL-16 | Review | generalisation | Feedback | — | — |
| REL-17 | PackageBooking | composition | ComponentBooking | 1 : 1..* | contains |
| REL-18 | BookableOffering | composition | AvailabilityCalendar | 1 : 1 | has |
| REL-19 | AvailabilityCalendar | composition | AvailabilitySlot | 1 : 0..* | records |
| REL-20 | ServicePackage | aggregation | BookableOffering | 0..* : 1..* | bundles |
| REL-21 | ServicePackage | aggregation | Destination | 0..* : 0..* | features |
| REL-22 | ContentCatalogue | aggregation | ContentItem | 1 : 0..* | indexes |
| REL-23 | AccountRegistry | aggregation | UserAccount | 1 : 0..* | registers |
| REL-24 | Tourist | association | Booking | 1 : 0..* | places (guest or registered) |
| REL-25 | ComponentBooking | association | BookableOffering | 0..* : 1 | reserves |
| REL-26 | PackageBooking | association | ServicePackage | 0..* : 0..1 | built from |
| REL-27 | LocalServiceProvider | association | BookableOffering | 1 : 0..* | owns |
| REL-28 | BookableOffering | association | Destination | 0..* : 0..1 | located at |
| REL-29 | LocalArticleInfo | association | Destination | 0..* : 0..1 | relates to |
| REL-30 | Booking | association | Payment | 1 : 0..1 | settled by |
| REL-31 | Booking | association | BookingObserver | 0..* : 0..* | notifies |
| REL-32 | Tourist | association | Feedback | 1 : 0..* | writes (registered only) |
| REL-33 | Review | association | BookableOffering | 0..* : 1 | is about |
| REL-34 | Tourist | association | ContentItem | 0..* : 0..* | bookmarks (registered only) |
| REL-35 | ContentItem | association | ManagementStaff | 0..* : 0..1 | last changed by |
| REL-36 | Review | association | ManagementStaff | 0..* : 0..1 | moderated by |
| REL-37 | AvailabilitySlot | association | ComponentBooking | 0..* : 0..* | counts |
| REL-38 | PaymentCoordinator | association | PaymentGatewayAdapter | 1 : 1 | captures and refunds via |
| REL-39 | NotificationDispatcher | association | NotificationServiceAdapter | 1 : 1 | delivers via |
| REL-40 | ContentCatalogue | association | MappingServiceAdapter | 1 : 1 | locates via |
| REL-41 | ContentCatalogue | association | LocalizationServiceAdapter | 1 : 1 | converts prices via |
| REL-42 | ContentPublisher | association | LocalizationServiceAdapter | 1 : 1 | drafts translations via |
| REL-43 | STPSApplication | dependency | the 13 classes in Section 10, steps 2–15 | — | creates |
| REL-44 | ReservationCoordinator | dependency | ReservationRequest | — | validates |
| REL-45 | ReservationCoordinator | dependency | ComponentBooking | — | creates |
| REL-46 | ReservationCoordinator | dependency | PackageBooking | — | creates |
| REL-47 | ReservationCoordinator | dependency | AvailabilityCalendar | — | holds capacity in |
| REL-48 | ReservationCoordinator | dependency | BookingObserver | — | attaches |
| REL-49 | BookableOffering | dependency | ReservationRequest | — | validates |
| REL-50 | PackageBooking | dependency | ReservationRequest | — | creates components from |
| REL-51 | BookingDecisionCoordinator | dependency | ComponentBooking | — | records decisions on |
| REL-52 | BookingDecisionCoordinator | dependency | PaymentCoordinator | — | requests refunds from |
| REL-53 | BookingDecisionCoordinator | dependency | ReservationCoordinator | — | resubmits modifications to |
| REL-54 | BookingDeadlineMonitor | dependency | NotificationDispatcher | — | alerts via |
| REL-55 | PaymentCoordinator | dependency | Payment | — | creates |
| REL-56 | PaymentCoordinator | dependency | Booking | — | confirms |
| REL-57 | ContentPublisher | dependency | ContentItem | — | creates and publishes |
| REL-58 | ContentPublisher | dependency | ContentCatalogue | — | adds items to |
| REL-59 | ReviewCoordinator | dependency | Review | — | creates |
| REL-60 | ReviewCoordinator | dependency | Feedback | — | creates |
| REL-61 | Destination | dependency | MappingServiceAdapter | — | positions via |
| REL-62 | AccountRegistry, ContentPublisher, PaymentCoordinator, ReviewCoordinator, AvailabilityCalendar | dependency | NotificationDispatcher | — | notifies via |
| REL-63 | Tourist | dependency | ContentCatalogue, ReservationCoordinator, PaymentCoordinator, ReviewCoordinator | — | requests |
| REL-64 | LocalServiceProvider | dependency | BookingDecisionCoordinator, AvailabilityCalendar | — | requests |
| REL-65 | ManagementStaff | dependency | ContentPublisher, BookingDecisionCoordinator, AvailabilityCalendar, ReviewCoordinator, AccountRegistry | — | requests |
| REL-66 | Booking | dependency | ReservationRequest | — | records contact details from |
| REL-67 | AccountRegistry | dependency | Booking | — | identifies returning guests by |

Diagram notes:
- Use `<<abstract>>` on UserAccount, ContentItem, BookableOffering, Booking and BookingObserver.
- Use `<<datatype>>` on ReservationRequest and AvailabilitySlot, and state that these are "data structure definitions".
- Use `<<adapter>>` on CL-33 to CL-36.
- The legend explains generalisation, composition, aggregation, association and dependency.
- Rows that list several classes become one edge per class.
- Guest-mode Tourist objects are created by AccountRegistry, which is already covered by REL-23 (registers); "registered only" in REL-32 and REL-34 is a role note in the label.

---

## 6. CRC skeletons

Collaborators shown as "X (external)" are external systems, each represented by its adapter class.

**CL-01 STPSApplication** (None). Entry point. It creates objects at start-up and has no business behaviour.
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Creates the four external-service adapters before anything that depends on them | PaymentGatewayAdapter, NotificationServiceAdapter, MappingServiceAdapter, LocalizationServiceAdapter |
| R2 | Decides whether start-up continues in degraded mode when an external service is unreachable | PaymentGatewayAdapter, NotificationServiceAdapter |
| R3 | Creates the notification, account and content services and gives each its adapters | NotificationDispatcher, AccountRegistry, ContentCatalogue, ContentPublisher |
| R4 | Creates the payment, deadline, reservation, decision and review coordinators and gives each its collaborators, including the system-wide booking observers | PaymentCoordinator, BookingDeadlineMonitor, ReservationCoordinator, BookingDecisionCoordinator, ReviewCoordinator |
| R5 | Starts the interval-driven checks once every object exists | BookingDeadlineMonitor, ContentPublisher, NotificationDispatcher |
| R6 | Reports that STPS is ready to accept requests | — |

**CL-02 AccountRegistry** (None). Creates guest Tourists, registers and authenticates accounts.
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Records a new Tourist registration with timestamped consent, refusing an already-registered contact address, and converts a guest Tourist into a registered one while keeping its bookings | Tourist |
| R2 | Authenticates an account holder, or identifies a returning guest by booking reference and the contact address recorded on that booking | UserAccount, Booking |
| R3 | Re-establishes registered accounts, and guest Tourists that still hold open bookings, at start-up | UserAccount |
| R4 | Records role grants and revocations made by a staff member holding the Data/System Admin role | ManagementStaff, UserAccount |
| R5 | Records a Tourist's request to access, correct or delete personal data, and alerts the Data/System Admin while it is open after 14 days | Tourist, NotificationDispatcher |
| R6 | Creates a temporary guest Tourist for an unregistered visitor's session | Tourist |

**CL-03 UserAccount** (None, abstract). Any STPS user's account.
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the holder's name, contact details and preferred language (English or Bahasa Malaysia); a guest Tourist may have none stored | — |
| R2 | Knows the roles granted to it | — |
| R3 | Decides whether it is authorised for a requested function | — |
| R4 | Knows whether it is active or suspended | — |

**CL-04 Tourist** (UserAccount). A tourist in guest or registered mode. It also acts as the actor's proxy (SI-01).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the bookings it has placed | Booking |
| R2 | Reports whether it holds a Completed booking for a given offering | Booking |
| R3 | Knows the content items it has bookmarked (registered mode only; a guest is prompted to register) | ContentItem |
| R4 | Knows the feedback and reviews it has written, and reports whether it has already reviewed a given offering | Feedback |
| R5 | Knows its consent records for personal-data processing | — |
| R6 | Initiates searches, reservations, payments and reviews for the person using STPS | ContentCatalogue, ReservationCoordinator, PaymentCoordinator, ReviewCoordinator |
| R7 | Knows whether it is a guest or a registered Tourist | — |

**CL-05 LocalServiceProvider** (UserAccount). A provider account.
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the bookable offerings it owns and decides whether a given offering is one of them | BookableOffering |
| R2 | Initiates decisions on Pending bookings for its offerings | BookingDecisionCoordinator |
| R3 | Initiates daily capacity changes for its offerings | AvailabilityCalendar |

**CL-06 ManagementStaff** (UserAccount). A staff account holding one or more roles (AS-11).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Decides whether it holds the staff role a requested function needs (refines UserAccount R3) | — |
| R2 | Initiates content creation, publication and withdrawal (Content Officer role) | ContentPublisher |
| R3 | Initiates overrides, cancellations and modifications of bookings (booking-management role) | BookingDecisionCoordinator |
| R4 | Initiates availability calendar adjustments (booking-management role) | AvailabilityCalendar |
| R5 | Initiates moderation decisions on flagged reviews | ReviewCoordinator |
| R6 | Initiates role administration and PDPA request handling (Data/System Admin role) | AccountRegistry |

**CL-07 ContentItem** (None, abstract). Publishable bilingual content.
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its English and Bahasa Malaysia text, category, location and images | — |
| R2 | Knows its lifecycle status and its publish and end dates | — |
| R3 | Decides whether it is complete enough to publish: common bilingual fields plus the fields its subtype requires | — |
| R4 | Records each lifecycle change with the staff member, time and reason | ManagementStaff |
| R5 | Decides whether it is visible to tourists now | — |
| R6 | Provides a preview as tourists will see it in a chosen language | — |
| R7 | Decides whether it is outdated or relates to a currently running event | — |

**CL-08 BookableOffering** (ContentItem, abstract). A listing that can be reserved.
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its owning provider | LocalServiceProvider |
| R2 | Knows its price in MYR per capacity unit | — |
| R3 | Creates and knows its AvailabilityCalendar, and reports remaining capacity for the days a request occupies | AvailabilityCalendar |
| R4 | Decides whether a reservation request is complete and valid: common checks (party size, well-formed contact details, future dates) and then the subtype's own checks | ReservationRequest |
| R5 | Knows and updates its average rating from published reviews | Review |
| R6 | Knows the Destination it is located at, if any | Destination |

**CL-09 Accommodation** (BookableOffering).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its lodging type (hotel, homestay, resort) and that its capacity unit is rooms | — |
| R2 | Decides whether a request's stay period and guest count are valid for this property | ReservationRequest |
| R3 | Identifies the nights a stay occupies | ReservationRequest |

**CL-10 Vehicle** (BookableOffering).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its vehicle type (car, van, boat, bus), its route or service area, and that its capacity unit is seats | — |
| R2 | Decides whether a request's origin, destination, journey time and passenger count are valid for this vehicle | ReservationRequest |
| R3 | Identifies the day a journey occupies | ReservationRequest |

**CL-11 FoodEstablishment** (BookableOffering).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its type (restaurant, cafe, food court), opening hours, and that its capacity unit is covers | — |
| R2 | Decides whether a request's date, time and guest count fit its opening hours and table limits | ReservationRequest |
| R3 | Identifies the day a table reservation occupies | ReservationRequest |

**CL-12 Destination** (ContentItem).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its place type (park, cultural site, festival) and its event dates if it is a festival | — |
| R2 | Provides its map position to tourists | MappingServiceAdapter |
| R3 | Knows the bookable offerings located at it | BookableOffering |

**CL-13 LocalArticleInfo** (ContentItem).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its topic (culture, safety, weather, event) | — |
| R2 | Knows the Destination it relates to, if any | Destination |

**CL-14 ServicePackage** (ContentItem).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the bookable offerings it bundles | BookableOffering |
| R2 | Knows the Destinations featured in its itinerary | Destination |
| R3 | Decides whether it is offered for a tourist's travel period | — |
| R4 | Knows its package price in MYR | BookableOffering |

**CL-15 ContentCatalogue** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows every content item and re-establishes them at start-up | ContentItem |
| R2 | Finds content by category, keyword, status, owning provider, travel period or location, showing tourists only visible items | ContentItem, MappingServiceAdapter |
| R3 | Suggests related categories when a search finds nothing | ContentItem |
| R4 | Ranks content about a currently running festival or event first | ContentItem |
| R5 | Finds alternative offerings with remaining capacity for a refused request | BookableOffering |
| R6 | Finds published packages offered for a travel period | ServicePackage |
| R7 | Shows prices in MYR with an indicative conversion into the tourist's chosen currency | LocalizationServiceAdapter |

**CL-16 ContentPublisher** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Creates a new content item of the chosen kind as a Draft and adds it to the catalogue | ContentItem, ContentCatalogue |
| R2 | Records changes to a content item's details and language versions, offering a draft translation for review | ContentItem, LocalizationServiceAdapter |
| R3 | Publishes or schedules a content item for an authorised Content Officer, keeping it as a Draft while it is incomplete | ContentItem, ManagementStaff |
| R4 | Notifies the owning provider when its listing is published | NotificationDispatcher |
| R5 | Unpublishes or archives a content item with a recorded reason | ContentItem |
| R6 | Warns before withdrawing an offering that has Pending or Confirmed bookings and lists those bookings | AvailabilityCalendar |
| R7 | Applies due publish and end dates at each interval | ContentItem |
| R8 | Flags outdated content to Content Officers | ContentItem, NotificationDispatcher |

**CL-17 ReservationRequest** (None, «datatype»).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the target offering and the requested dates or time | BookableOffering |
| R2 | Knows the party size, the lead guest's contact details (required when the Tourist is a guest) and the consent given for their use | — |
| R3 | Knows any special requests, such as a dietary add-on | — |
| R4 | Knows the validation problems found in it | — |

**CL-18 Booking** (None, abstract).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its Tourist, its reference, its creation time, and the contact details and consent recorded from its request | Tourist, ReservationRequest |
| R2 | Knows its current status (Pending, Pending-Payment, Confirmed, Completed, Declined, Cancelled) | — |
| R3 | Decides whether a requested status change is permitted from its current status | — |
| R4 | Knows its total price in MYR | — |
| R5 | Keeps its attached observers and notifies them of each status change, including its initial Pending status | BookingObserver |
| R6 | Records a captured Payment and moves to Confirmed (a package also confirms its components) | Payment |
| R7 | Records cancellation with a reason | — |
| R8 | Decides whether a requester may view or pay for it: its own Tourist, or a guest presenting its reference and recorded contact address | — |

**CL-19 ComponentBooking** (Booking).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the offering, days, party size and special requests it reserves | BookableOffering, ReservationRequest |
| R2 | Knows its 48-hour decision deadline and records its escalation to Management Staff | — |
| R3 | Records approval by its provider or by a staff override, moving to Pending-Payment | — |
| R4 | Records a decline, refusing one without a reason | — |
| R5 | Informs its parent PackageBooking of each status change | PackageBooking |
| R6 | Records completion once its last service day has passed | — |
| R7 | Shows its provider only the contact details needed to decide on it and serve the guest (A1 §7.2) | — |

**CL-20 PackageBooking** (Booking).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Creates one ComponentBooking per validated and held component request | ComponentBooking, ReservationRequest |
| R2 | Knows its components and the ServicePackage it was built from, if any | ComponentBooking, ServicePackage |
| R3 | Derives its status from its components' statuses | ComponentBooking |
| R4 | Cancels its remaining components when one is declined or the package is cancelled | ComponentBooking |
| R5 | Sums its components' prices to give its total | ComponentBooking |

**CL-21 BookingObserver** (None, abstract).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Receives notice of a booking's status change | Booking |

**CL-22 AvailabilityCalendar** (BookingObserver).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the AvailabilitySlot for each day of its offering | AvailabilitySlot |
| R2 | Decides whether each requested day has remaining capacity, reporting a day with none as Full | AvailabilitySlot |
| R3 | Holds capacity for a request on each requested day, one request at a time so capacity is never exceeded, and releases the holds of an abandoned request | AvailabilitySlot, ComponentBooking |
| R4 | Converts a booking's held capacity to confirmed, or releases its held or confirmed capacity, when told of the booking's status change | ComponentBooking, AvailabilitySlot |
| R5 | Records a provider's new daily capacity, refusing an invalid value or one below that day's Confirmed plus held count, and alerting Management Staff to a Confirmed-booking conflict | AvailabilitySlot, LocalServiceProvider, NotificationDispatcher |
| R6 | Records a Management Staff capacity change after warning of any overlapping Confirmed bookings | AvailabilitySlot, ManagementStaff |
| R7 | Lists the bookings holding or confirmed on its future days | ComponentBooking |

**CL-23 AvailabilitySlot** (None, «datatype»).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its date and total capacity | — |
| R2 | Knows its held count and confirmed count | — |
| R3 | Knows which bookings make up those counts | ComponentBooking |

**CL-24 ReservationCoordinator** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Validates a reservation request through the offering it targets, collecting every missing or invalid detail, including the contact details a guest Tourist must supply | BookableOffering, ReservationRequest |
| R2 | Holds capacity on every day a request occupies, holding nothing if any day is Full | AvailabilityCalendar |
| R3 | Creates a Pending ComponentBooking for a validated and held single-offering request, recording the request's contact details and consent | ComponentBooking |
| R4 | Creates a PackageBooking only when every component is valid and held, releasing earlier holds otherwise | PackageBooking, AvailabilityCalendar |
| R5 | Attaches the offering's calendar and the system-wide booking observers to each new booking | BookingObserver |
| R6 | Reports unavailable or invalid components while keeping the rest of the tourist's plan | ReservationRequest |
| R7 | Re-establishes open bookings and re-attaches their observers at start-up | ComponentBooking, PackageBooking |

**CL-25 BookingDecisionCoordinator** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Lists Pending and escalated bookings for the provider or staff member who must decide them | ComponentBooking |
| R2 | Records a provider's approval of a Pending booking for an offering it owns | LocalServiceProvider, ComponentBooking |
| R3 | Records a provider's decline, refusing it without a reason | LocalServiceProvider, ComponentBooking |
| R4 | Records an authorised staff member's override approval or finalised non-approval of an escalated booking | ManagementStaff, ComponentBooking |
| R5 | Records an authorised staff cancellation on the Tourist's behalf and requests a refund if payment was captured | ManagementStaff, Booking, PaymentCoordinator |
| R6 | Applies a staff modification as a cancellation followed by a replacement reservation request | ReservationCoordinator |

**CL-26 BookingDeadlineMonitor** (BookingObserver).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Starts or stops watching a booking's deadlines when told of its status change | Booking |
| R2 | Checks watched deadlines at a fixed interval | — |
| R3 | Records the escalation of Pending component bookings whose 48-hour decision deadline has passed | ComponentBooking |
| R4 | Alerts Management Staff, the provider and the Tourist to each escalation | NotificationDispatcher |
| R5 | Cancels Pending-Payment bookings whose payment deadline has passed | Booking |
| R6 | Records completion of Confirmed component bookings whose last service day has passed | ComponentBooking |

**CL-27 NotificationDispatcher** (BookingObserver).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Decides whom to notify, and with what message, when told of a booking's status change | Booking, NotificationServiceAdapter |
| R2 | Composes each message in the recipient's preferred language, and addresses booking messages to the contact details recorded on the booking so that guests are reached | UserAccount, Booking |
| R3 | Sends alerts requested by other classes (escalations, moderation outcomes, publication notices, capacity conflicts, payment and refund outcomes, PDPA reminders) | NotificationServiceAdapter, UserAccount |
| R4 | Compiles and sends each provider a daily slot-utilisation summary | LocalServiceProvider, AvailabilityCalendar |
| R5 | Keeps undelivered notifications and retries them while the Notification Service is unavailable | NotificationServiceAdapter |

**CL-28 Payment** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the booking it settles, its amount in MYR and the gateway's transaction reference, and never card details | Booking |
| R2 | Knows its status (Initiated, Captured, Failed, Refund-Pending, Refunded) | — |
| R3 | Records capture or failure as reported by the gateway, with the time | — |
| R4 | Records a completed refund, or a refund awaiting retry, with the initiating user and the time | — |
| R5 | Reports whether it has been captured | — |

**CL-29 PaymentCoordinator** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Refuses payment unless the booking is Pending-Payment and the booking accepts the payer (its Tourist, or a guest presenting its reference and contact address) | Booking |
| R2 | Creates a Payment for the booking's total and requests capture through the gateway | Payment, PaymentGatewayAdapter |
| R3 | Records a successful capture on the Payment and the Booking | Payment, Booking |
| R4 | Keeps the booking Pending-Payment and informs the Tourist, at the booking's contact details, when capture fails or the gateway is unavailable | Payment, NotificationDispatcher |
| R5 | Requests a refund for a cancelled booking only if its payment was captured | Payment, PaymentGatewayAdapter |
| R6 | Retries failed refunds and alerts Management Staff, informing the Tourist when the refund completes | Payment, NotificationDispatcher |

**CL-30 Feedback** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows its author, comment and submission time | Tourist |
| R2 | Reports whether it is a review of a given offering (general feedback never is) | — |
| R3 | Knows who may see it (general feedback: Management Staff only) | — |

**CL-31 Review** (Feedback).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Knows the offering it reviews and its star rating | BookableOffering |
| R2 | Knows its moderation status (Submitted, Flagged, Published, Rejected) and any rejection reason | — |
| R3 | Records its screening outcome, its moderation decision with the moderator, and its publication | ManagementStaff |
| R4 | Records its author's edits and returns to screening | — |
| R5 | Shows itself as verified once Published | — |

**CL-32 ReviewCoordinator** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Confirms the Tourist is registered and holds a Completed booking for the offering; a guest is prompted to register first, and a Tourist without a completed booking is offered general feedback | Tourist |
| R2 | Opens the Tourist's existing review of the offering for editing instead of creating a duplicate | Tourist, Review |
| R3 | Creates a Review or general Feedback from the Tourist's submission | Review, Feedback |
| R4 | Screens review text for offensive language, personal data or spam, and flags matches for moderation | Review, NotificationDispatcher |
| R5 | Records an authorised staff member's approval or rejection of a flagged review | ManagementStaff, Review |
| R6 | Publishes an approved or clean review, updates the offering's average rating and notifies the Tourist | Review, BookableOffering, NotificationDispatcher |
| R7 | Summarises feedback and rating trends for Management Staff | Feedback, BookableOffering |

**CL-33 PaymentGatewayAdapter** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Translates a capture request into the gateway's protocol, sending the tourist to the provider's own payment page so that no card data reaches STPS | Payment Gateway Provider (external) |
| R2 | Translates a refund request and returns the provider's outcome | Payment Gateway Provider (external) |
| R3 | Reports whether the Payment Gateway Provider is reachable | Payment Gateway Provider (external) |

**CL-34 NotificationServiceAdapter** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Delivers a composed message to a recipient through the Notification Service | Notification Service (external) |
| R2 | Reports delivery failure | Notification Service (external) |
| R3 | Reports whether the Notification Service is reachable | Notification Service (external) |

**CL-35 MappingServiceAdapter** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Resolves a tourist's current location or a place name into a map position | Mapping/Geolocation Service (external) |
| R2 | Provides the distance between two map positions for location-based ranking | Mapping/Geolocation Service (external) |
| R3 | Reports whether the service is reachable, so that search can fall back to category search | Mapping/Geolocation Service (external) |

**CL-36 LocalizationServiceAdapter** (None).
| R | Responsibility | Collaborators |
|---|---|---|
| R1 | Supplies a draft translation between English and Bahasa Malaysia | Translation/Localization Service (external) |
| R2 | Supplies an indicative exchange rate from MYR into a chosen currency | Translation/Localization Service (external) |
| R3 | Reports whether the service is reachable, so that prices can fall back to MYR only | Translation/Localization Service (external) |

---

## 7. Responsibility coverage matrix (no gaps)
| Row | A1 item | Owner (responsibility) |
|---|---|---|
| T1.1 | Search by category; no results → suggest | ContentCatalogue R2, R3 |
| T1.2 | View article; hide expired or unpublished | ContentItem R5; ContentCatalogue R2 |
| T1.3 | Bookmark; guest prompted to register without losing context | Tourist R3, R7; AccountRegistry R1 |
| T1.v1a | Search by location | ContentCatalogue R2; MappingServiceAdapter R1, R2 |
| T1.v2a | Offline viewing | SI-06 |
| T1.v3a | Festival or event content first | ContentCatalogue R4; ContentItem R7 |
| T2.1 | Find accommodation; show availability | ContentCatalogue R2; BookableOffering R3; AvailabilityCalendar R2 |
| T2.2 | Enter and validate details; record; confirm | ReservationCoordinator R1, R3; Accommodation R2; ReservationRequest R2 |
| T2.v1a | Unavailable → alternatives | ReservationCoordinator R6; ContentCatalogue R5 |
| T2.v2a / v2b | Invalid details; change before recording | ReservationCoordinator R1; ReservationRequest R4 |
| T3.1 | Review transport information | Vehicle R1; ContentCatalogue R2 |
| T3.2 | Check availability (incl. passenger capacity) | Vehicle R2; AvailabilityCalendar R2 |
| T3.3 | Confirm reservation | ReservationCoordinator R3 |
| T3.v2a / 2b / 3a | Unavailable; insufficient capacity; journey changed | ReservationCoordinator R6, R1 |
| T4.pre | Guest or registered mode | Tourist R7; AccountRegistry R6 (AS-01) |
| T4.1 | Specify details; flag invalid | FoodEstablishment R2; ReservationCoordinator R1 |
| T4.2 | Find establishment; capacity incl. package holds | ContentCatalogue R2; AvailabilityCalendar R2, R3 |
| T4.3 | Contact details; recheck on change | ReservationCoordinator R1, R2; BookableOffering R4 |
| T4.post | Pending recorded; provider decides; pay after approval | ReservationCoordinator R3; BookingDecisionCoordinator R2, R3; PaymentCoordinator R1 |
| T5.pre | Guests and registered users | Tourist R7; AccountRegistry R6 (AS-01) |
| T5.1 | Choose a Package; missing service → matching packages | ContentCatalogue R6; ServicePackage R3 |
| T5.2 | Check each component; total in MYR plus estimate | ReservationCoordinator R2, R4; PackageBooking R5; ContentCatalogue R7 |
| T5.3 | Validate contact details and save; status; no card data | ReservationCoordinator R1, R4; PackageBooking R1; Booking R1, R2 |
| T5.v2a / 4a | Missing part; component unavailable → keep plan | ReservationCoordinator R6; ContentCatalogue R5 |
| T6.pre | Signed-in tourist only | ReviewCoordinator R1; Tourist R7 |
| T6.1 | Choose what to review | Tourist R1 |
| T6.2 | Rate and write | ReviewCoordinator R3; Review R1 |
| T6.3 | Check eligibility | ReviewCoordinator R1; Tourist R2 |
| T6.4 | Screen content | ReviewCoordinator R4 |
| T6.5 | Moderate flagged reviews | ReviewCoordinator R5; Review R3 |
| T6.6 | Publish; verified; average rating; notify | ReviewCoordinator R6; Review R5; BookableOffering R5 |
| T6.7 | Feedback trends | ReviewCoordinator R7 |
| T6.v2a / 3a / 5a | Duplicate; no completed booking; rejection | ReviewCoordinator R2, R1, R5; Review R4 |
| T7.1 | Select content | ContentCatalogue R2 |
| T7.2 | Enter or update details | ContentPublisher R2 |
| T7.3 | Both languages | ContentItem R1; ContentPublisher R2; LocalizationServiceAdapter R1 |
| T7.4 | Validate | ContentItem R3 |
| T7.5 | Preview | ContentItem R6 |
| T7.6 | Publish or schedule; log; notify provider | ContentPublisher R3, R4; ContentItem R4 |
| T7.7 | Unpublish or archive with a reason | ContentPublisher R5 |
| T7.8 | Keep content current | ContentPublisher R8; ContentItem R7 |
| T7.v4a / 6a / 7a | Draft only; auto dates; active bookings warning | ContentPublisher R3, R7, R6; AvailabilityCalendar R7 |
| T8.1 | Review pending Package Booking | BookingDecisionCoordinator R1 |
| T8.2 | Approve or reject a pending Package Booking | BookingDecisionCoordinator R4; PackageBooking R3 |
| T8.3 | Finalise a non-approved component; refund if paid | BookingDecisionCoordinator R4, R5; PaymentCoordinator R5 |
| T8.4 | Adjust the calendar; warn on Confirmed overlap | AvailabilityCalendar R6 |
| T8.5 | Modify on the Tourist's behalf; refund after payment | BookingDecisionCoordinator R5, R6; PaymentCoordinator R5 |
| T8.v | Provider decision; cancellation before capture has no refund; zero capacity shown Full | BookingDecisionCoordinator R4; PaymentCoordinator R5; AvailabilityCalendar R2 |
| T9.1 | Set daily slots; block below Confirmed | AvailabilityCalendar R5 |
| T9.2 | Publish updated slots | AvailabilityCalendar R5 (read directly by ContentCatalogue R5 and BookableOffering R3) |
| T9.v | Recurrence; conflicting reduction | SI-03; AvailabilityCalendar R5 |
| T10.1 | Review a pending booking | BookingDecisionCoordinator R1; ComponentBooking R7 |
| T10.2 | Approve or decline; SLA escalation | BookingDecisionCoordinator R2, R3; BookingDeadlineMonitor R3, R4 |
| T10.3 | New-booking alerts; daily summary; decline reason | NotificationDispatcher R1, R4; ComponentBooking R4 |
| T10.v | Approval updates availability; decline reason sent to the Tourist | ComponentBooking R3; AvailabilityCalendar R4; NotificationDispatcher R2 |
| PAY-01 | Initiate payment after approval (PR-10) | PaymentCoordinator R1, R2 |
| PAY-02 | Record payment status; no card data | PaymentCoordinator R3; Payment R1–R3; PaymentGatewayAdapter R1 |
| PAY-03 | Payment failure | PaymentCoordinator R4 |
| PAY-04 | Refund and retry | PaymentCoordinator R5, R6; Payment R4 |
| PAY-05 | Unpaid booking expiry | BookingDeadlineMonitor R5 |
| ACC-01 | Register, with consent | AccountRegistry R1; Tourist R5 |
| ACC-02 | Authenticate | AccountRegistry R2 |
| ACC-03 | Role-based access (PR-13, DR-08) | UserAccount R3; ManagementStaff R1; LocalServiceProvider R1 |
| ACC-04 | Role administration | AccountRegistry R4 |
| ACC-05 | PDPA requests, 14-day alert | AccountRegistry R5 |
| GST-01 | Guest session as a temporary Tourist | AccountRegistry R6; Tourist R7 |
| GST-02 | Guest contact details and consent captured and validated | ReservationRequest R2; ReservationCoordinator R1; BookableOffering R4 |
| GST-03 | Booking records contact details for notifications, payment and decisions | Booking R1; ReservationCoordinator R3; NotificationDispatcher R2; ComponentBooking R7 |
| GST-04 | Returning guest identified to view or pay | AccountRegistry R2; Booking R8; PaymentCoordinator R1 |
| GST-05 | Guest converts to registered account and keeps bookings | AccountRegistry R1 |
| NFR-7.1 | Notify providers within 60 s | NotificationDispatcher R1 |
| NFR-7.2 | Providers see only the Tourist data needed to decide | ComponentBooking R7 |
| NFR-7.4 | Never overbook | AvailabilityCalendar R3; ReservationCoordinator R2, R4 |
| PR-15 | Booking lifecycle; Completed | Booking R2, R3; BookingDeadlineMonitor R6 |

---

## 8. God-class check (responsibilities / distinct collaborators; flag > 8 or > 6)
| Class | R | C | Flag |
|---|---|---|---|
| STPSApplication | 6 | 13 | FLAG (justified) |
| AccountRegistry | 6 | 5 | |
| UserAccount | 4 | 0 | |
| Tourist | 7 | 7 | FLAG (justified) |
| LocalServiceProvider | 3 | 3 | |
| ManagementStaff | 6 | 5 | |
| ContentItem | 7 | 1 | |
| BookableOffering | 6 | 5 | |
| Accommodation / Vehicle / FoodEstablishment | 3 each | 1 each | |
| Destination | 3 | 2 | |
| LocalArticleInfo | 2 | 1 | |
| ServicePackage | 4 | 2 | |
| ContentCatalogue | 7 | 5 | |
| ContentPublisher | 8 | 6 | at limit, not over |
| ReservationRequest | 4 | 1 | |
| Booking | 8 | 4 | at limit, not over |
| ComponentBooking | 7 | 3 | |
| PackageBooking | 5 | 3 | |
| BookingObserver | 1 | 1 | |
| AvailabilityCalendar | 7 | 5 | |
| AvailabilitySlot | 3 | 1 | |
| ReservationCoordinator | 7 | 6 | |
| BookingDecisionCoordinator | 6 | 6 | |
| BookingDeadlineMonitor | 6 | 3 | |
| NotificationDispatcher | 5 | 5 | |
| Payment | 5 | 1 | |
| PaymentCoordinator | 6 | 4 | |
| Feedback | 3 | 1 | |
| Review | 5 | 2 | |
| ReviewCoordinator | 7 | 6 | |
| 4 adapters | 3 each | 1 external each | |

Total is about 175 responsibilities, an average of 4.9 per class. The maximum is 8 (ContentPublisher and Booking, under 5% of the total each).

Justifications for the two flags:
- **STPSApplication.** Its coupling exists only at creation time. Under GRASP Creator it is the only object that lives longer than the services it wires, and it sends no business messages after R6. Spreading creation across the services would create hidden creation chains and break the bootstrap order.
- **Tourist.** As actor proxy (SI-01) it must reach the four Tourist-facing controllers. Its own knowledge is lean. Guest mode added one knowledge responsibility (R7) and no collaborator. Adding boundary classes (OQ-02) would move this coupling away from Tourist.

Guest booking added no collaborator to ReservationCoordinator: guest Tourist creation sits on AccountRegistry R6, which keeps ReservationCoordinator at 6 collaborators.

The before/after split for H-04: a single "BookingManager" would have had about 26 responsibilities and 12 collaborators. It is split into ReservationCoordinator, BookingDecisionCoordinator, BookingDeadlineMonitor and PaymentCoordinator.

---

## 9. Patterns and heuristics

### 9.1 GoF patterns (all mapped to classes in the diagram)
| ID | Pattern (category) | Roles → classes | STPS problem solved |
|---|---|---|---|
| PT-01 | Composite (Structural) | Component = Booking; Leaf = ComponentBooking; Composite = PackageBooking; Clients = PaymentCoordinator, BookingDecisionCoordinator | Task 5 needs one parent booking with one component per offering, yet payment, cancellation and total price must work the same for standalone (Tasks 2–4) and package bookings. |
| PT-02 | Observer (Behavioural) | Subject = Booking; Observer = BookingObserver; Concrete observers = AvailabilityCalendar, NotificationDispatcher, BookingDeadlineMonitor | Six triggers change booking status: provider decision, escalation override, payment capture, cancellation, payment expiry and completion. Each change must update capacity (A1 §7.4), notify the parties (A1 §7.1, 60 s), including guests at their recorded contact details, and update the deadlines. Without Observer, four controllers would repeat this, and a missed release would cause overbooking. |
| PT-03 | Adapter, object form (Structural) | Adapters = PaymentGatewayAdapter, NotificationServiceAdapter, MappingServiceAdapter, LocalizationServiceAdapter; Adaptees = the four external services (outside STPS, A1 §2.3); Clients = PaymentCoordinator, NotificationDispatcher, ContentCatalogue, Destination, ContentPublisher; Target = each adapter's STPS-facing responsibilities | Keeps third-party protocols out of the domain, so a provider can be changed and the no-card-data rule is enforced at one point (AS-16). Outages are reported so that degraded mode works (AS-18). |
| PT-04 | Template Method (Behavioural) | Abstract class = BookableOffering (R4: common checks, then the subtype step) and ContentItem (R3); Concrete classes = Accommodation, Vehicle, FoodEstablishment (R2); Destination, LocalArticleInfo, ServicePackage | Tasks 2, 3 and 4 need different required details (stay, journey, table), while the common checks (party size, contact details, future dates) and the bilingual publish checks (Task 7 subtask 4) must not be duplicated. |

Rejected patterns, with reasons:
- State: SI-07.
- Factory Method: D-07.
- Strategy: there is one gateway and one screening policy (SI-08, SI-10).
- Singleton: STPSApplication passes references explicitly, which avoids global state.
- No creational pattern is claimed.

### 9.2 GRASP and heuristics
| ID | Heuristic (source) | Applied to | Reasoning (before → after) |
|---|---|---|---|
| H-01 | Information Expert (Larman) | AvailabilityCalendar R2–R5; Booking R3, R8; Tourist R2; ContentItem R5; BookableOffering R4 | The class holding the data decides. Before: a coordinator added up slot counts. After: the calendar decides capacity, and the booking, which holds the recorded contact details, decides who may pay for it. |
| H-02 | Creator (Larman) | PackageBooking → ComponentBooking (contains); BookableOffering → AvailabilityCalendar (composes); ReservationCoordinator → bookings (has the validated, held data); PaymentCoordinator → Payment; ReviewCoordinator → Review and Feedback; ContentPublisher → ContentItem; AccountRegistry → Tourist (guest and registered) | Creation follows containment or initialising data. |
| H-03 | Controller (Larman) | ReservationCoordinator (Tasks 2–5), BookingDecisionCoordinator (Tasks 8, 10), PaymentCoordinator, ReviewCoordinator (Task 6), ContentPublisher (Task 7), BookingDeadlineMonitor (time events) | One use-case controller per task group, none of which directs other controllers. Task 9 goes straight to AvailabilityCalendar, because a separate controller would only pass messages through. |
| H-04 | Distribute intelligence uniformly; avoid god classes (Riel) | Booking controllers (Section 8) | BookingManager (about 26 responsibilities) → 4 classes of 6–7 responsibilities each. |
| H-05 | Favour object composition over class inheritance (GoF) | ManagementStaff roles (AS-11); Tourist guest mode (D-19) | ContentOfficer and DataSystemAdmin subclasses → roles held by one account, so roles can be combined. Guest versus registered is a mode of Tourist, not a subclass, so conversion on registration keeps the same object and its bookings. |
| H-06 | Polymorphism (Larman) | BookableOffering subtypes; Feedback R2 overridden by Review | Removes "if type == …" logic from the coordinators. |
| H-07 | Protected Variations (Larman) | Adapters; BookingObserver | Isolates external change and change in the set of observers. |
| H-08 | Pure Fabrication (Larman) | NotificationDispatcher, BookingDeadlineMonitor, ContentCatalogue | Behaviour with no domain owner is given to cohesive invented classes, not loaded onto Booking. |
| H-09 | High Cohesion (Larman); one key abstraction per class (Riel) | ContentCatalogue / ContentPublisher | One "content manager" with 15 responsibilities → find versus change. |
| H-10 | Model external agents only through interfaces (Riel) | The 4 adapters | No class represents a third party's internals (A1 §2.3 scope). |

References for the writer: Gamma et al. 1994; Larman 2004 (*Applying UML and Patterns*, 3rd edn); Riel 1996 (*Object-Oriented Design Heuristics*); Wirfs-Brock & McKean 2003 (*Object Design*); Beck & Cunningham 1989 (CRC cards).

---

## 10. Bootstrap order (start-up only; every participant has a card)
| Step | Actor → action | Responsibility |
|---|---|---|
| 1 | STPSApplication is started by the hosting environment (self-message "start STPS") | STPSApplication R1 |
| 2 | STPSApplication creates LocalizationServiceAdapter | R1 |
| 3 | STPSApplication creates MappingServiceAdapter | R1 |
| 4 | STPSApplication creates NotificationServiceAdapter | R1 |
| 5 | STPSApplication creates PaymentGatewayAdapter | R1 |
| 6 | STPSApplication asks PaymentGatewayAdapter and NotificationServiceAdapter whether they are reachable. **alt** unreachable → record degraded mode (AS-18) | PaymentGatewayAdapter R3; NotificationServiceAdapter R3; STPSApplication R2 |
| 7 | STPSApplication creates NotificationDispatcher (given NotificationServiceAdapter) | R3 |
| 8 | STPSApplication creates AccountRegistry, which re-establishes registered accounts and guest Tourists with open bookings | R3; AccountRegistry R3 |
| 9 | STPSApplication creates ContentCatalogue (given the Mapping and Localization adapters), which re-establishes content items; each BookableOffering re-establishes its AvailabilityCalendar | R3; ContentCatalogue R1; BookableOffering R3 |
| 10 | STPSApplication creates ContentPublisher (given ContentCatalogue, NotificationDispatcher, LocalizationServiceAdapter) | R3 |
| 11 | STPSApplication creates PaymentCoordinator (given PaymentGatewayAdapter, NotificationDispatcher) | R4 |
| 12 | STPSApplication creates BookingDeadlineMonitor (given NotificationDispatcher) | R4 |
| 13 | STPSApplication creates ReservationCoordinator (given the system-wide observers NotificationDispatcher and BookingDeadlineMonitor, and ContentCatalogue), which re-establishes open bookings and re-attaches their observers | R4; ReservationCoordinator R7 |
| 14 | STPSApplication creates BookingDecisionCoordinator (given PaymentCoordinator, ReservationCoordinator) | R4 |
| 15 | STPSApplication creates ReviewCoordinator (given NotificationDispatcher) | R4 |
| 16 | STPSApplication starts the interval checks in BookingDeadlineMonitor, ContentPublisher and NotificationDispatcher | R5; BookingDeadlineMonitor R2; ContentPublisher R7; NotificationDispatcher R4 |
| 17 | STPSApplication reports ready | R6 |

Dependency checks:
- Every class is created after the classes it is given.
- Tourists, including guests with open bookings (step 8), exist before their bookings are re-established (step 13).
- Calendars (step 9) exist before observers are re-attached (step 13).
- BookingDeadlineMonitor (step 12) exists before ReservationCoordinator (step 13).
- PaymentCoordinator and ReservationCoordinator exist before BookingDecisionCoordinator (step 14).

---

## 11. Verification scenarios

Messages cite "Class Rn". A responsibility that the receiver inherits is cited "(inherited from X)" (AD-09). Reply arrows carry results only.

### SC-01 Guest accommodation reservation through approval and payment
- **A1 tasks:** Task 2 Reserve Accommodation; Task 10 Decide on Own-Listing Bookings; PR-10.
- **Preconditions:**
  - A visitor is browsing in guest mode, so AccountRegistry has created a guest Tourist T (AccountRegistry R6, Tourist R7).
  - Accommodation A is published and owned by LocalServiceProvider P, and A's calendar has capacity.
  - The gateway is reachable.
- **Participants (11):** Tourist, ReservationCoordinator, Accommodation, AvailabilityCalendar, ComponentBooking, NotificationDispatcher, LocalServiceProvider, BookingDecisionCoordinator, PaymentCoordinator, Payment, PaymentGatewayAdapter.
- **Flow:**
  1. Tourist → ReservationCoordinator: submit reservation request with guest contact details and consent (RC R1, Tourist R6).
  2. RC → Accommodation: check request complete and valid (Accommodation R2; BookableOffering R4, inherited — common checks include the contact details).
     - **alt** guest contact details missing or invalid (no e-mail or phone, malformed address, consent not given) → reply listing the problems (RC R1, R6). Nothing is recorded and the request is kept for correction.
     - **alt** stay invalid (check-out before check-in) → reply listing the problems (RC R6).
  3. RC → Accommodation: identify nights occupied (R3).
  4. RC → AvailabilityCalendar: hold capacity for each night (AC R3).
     - **alt** Full → reply unavailable, request kept (RC R6).
  5. RC creates ComponentBooking as Pending, recording the request's contact details and consent (RC R3; Booking R1, inherited).
  6. RC → ComponentBooking: attach observers (RC R5; Booking R5, inherited).
  7. ComponentBooking → NotificationDispatcher: status changed to Pending. The provider is alerted, and the guest gets a confirmation with the booking reference at the recorded contact address (ND R1, R2).
  8. LocalServiceProvider → BookingDecisionCoordinator: approve booking (BDC R2), seeing only the needed contact details (CB R7).
  9. BDC → LocalServiceProvider: confirm the offering is owned (LSP R1).
     - **alt** not owner → refused.
  10. **alt** approve: BDC → ComponentBooking: record approval (CB R3). The status moves to Pending-Payment, and ComponentBooking → NotificationDispatcher: status changed, so the guest is asked to pay at the recorded contact address (ND R1, R2).
      **else** decline: BDC → ComponentBooking: record decline (CB R4). A missing reason is refused. Then ComponentBooking → AvailabilityCalendar: status changed, so the hold is released (AC R4), and NotificationDispatcher sends the reason to the guest (ND R2).
  11. Tourist → PaymentCoordinator: pay for booking, presenting booking reference and contact address (PC R1). PC → ComponentBooking: accept payer, and report status and total (Booking R8, R2, R4, inherited).
      - **alt** reference or contact address does not match, or status is not Pending-Payment → refused.
  12. PC creates Payment (PC R2). PC → PaymentGatewayAdapter: request capture (PGA R1).
      - **alt** capture failed or gateway unavailable → PC → Payment: record failure (Payment R3); PC → NotificationDispatcher: inform the guest (ND R3, PC R4). The booking stays Pending-Payment.
      - **else** PC → Payment: record capture (R3); PC → ComponentBooking: record captured payment (Booking R6, inherited), so the status is Confirmed. ComponentBooking → AvailabilityCalendar: convert hold to confirmed (AC R4). ComponentBooking → NotificationDispatcher: confirmation to the guest (ND R1, R2).
- **Result:** the guest's booking is Confirmed and paid, capacity is converted, and the guest is reached at the recorded contact details without an account.
- **Validation shown:** missing or invalid guest contact details, invalid stay, Full calendar, non-owner, missing decline reason, payer mismatch, gateway failure.

### SC-02 Package booking with an unavailable component, then a component decline
- **A1 task:** Task 5 Book Services (with Task 10 for the decline).
- **Preconditions:**
  - T is a registered or guest Tourist; for a guest, contact details travel on each ReservationRequest as in SC-01.
  - ServicePackage SP bundles Accommodation A, Vehicle V and FoodEstablishment F, and features Destination D.
  - V's calendar is Full on day 2, and an alternative vehicle V2 has capacity.
- **Participants (8):** Tourist, ContentCatalogue, ServicePackage, ReservationCoordinator, Vehicle, AvailabilityCalendar, PackageBooking, ComponentBooking.
- **Flow:**
  1. Tourist → ContentCatalogue: find packages for travel period (CC R6). CC → ServicePackage: offered for period? (SP R3).
  2. Tourist → ReservationCoordinator: submit package request with one ReservationRequest per offering; D gets none (RC R4).
  3. **loop** each component: RC → offering: check request valid (Vehicle R2, and likewise for A and F); RC → AvailabilityCalendar: hold capacity (AC R3).
     - **alt** V is Full on day 2 → RC → AvailabilityCalendar: release holds of the abandoned request (AC R3), then reply "Vehicle unavailable, plan kept" (RC R6). Tourist → ContentCatalogue: find alternative offerings (CC R5). Tourist → RC: resubmit with V2, and the loop succeeds.
  4. RC creates PackageBooking (RC R4). PackageBooking creates one ComponentBooking each for A, V2 and F (PB R1). RC attaches observers (RC R5).
  5. **alt** later, F's provider declines (decision recorded as in SC-01): ComponentBooking → PackageBooking: status changed (CB R5). PackageBooking derives Declined (PB R3) and cancels its other components (PB R4). Each calendar releases its hold (AC R4, as an observer).
- **Result:** one PackageBooking with 3 Pending components, all held (A1 §7.4). After a decline, every hold is released (AS-09).
- **Validation shown:** an unavailable component, rollback of earlier holds, and all-or-nothing handling on decline.

### SC-03 SLA expiry escalated to Management Staff, override, then cancellation with refund
- **A1 tasks:** Task 10 Decide on Own-Listing Bookings → Task 8 Manage Bookings Availability (subtasks 3 and 5).
- **Preconditions:** ComponentBooking B (Accommodation, standalone) has been Pending for 48 hours with no provider decision. Staff member M holds the booking-management role.
- **Participants (9):** BookingDeadlineMonitor, ComponentBooking, NotificationDispatcher, ManagementStaff, BookingDecisionCoordinator, AvailabilityCalendar, PaymentCoordinator, Payment, PaymentGatewayAdapter.
- **Flow:**
  1. BookingDeadlineMonitor → self: check watched deadlines (BDM R2).
  2. BDM → ComponentBooking: report decision deadline (CB R2).
     - **alt** deadline passed and still Pending → BDM → ComponentBooking: record escalation (CB R2, BDM R3); BDM → NotificationDispatcher: alert staff, provider and tourist (ND R3, BDM R4).
     - **else** decided in time → no action.
  3. ManagementStaff → BookingDecisionCoordinator: override with approval (BDC R4). BDC → ManagementStaff: confirm booking-management role (MS R1).
     - **alt** not authorised → refused.
  4. BDC → ComponentBooking: record approval by override (CB R3), so the status is Pending-Payment.
  5. Note: the tourist pays as in SC-01, so B is Confirmed and its Payment is Captured.
  6. ManagementStaff → BDC: cancel booking on the tourist's behalf because the provider cannot honour it (BDC R5, AS-12). BDC → ManagementStaff: confirm role (MS R1).
  7. BDC → ComponentBooking: record cancellation with reason (Booking R7, inherited). ComponentBooking → AvailabilityCalendar: release confirmed capacity (AC R4).
  8. BDC → PaymentCoordinator: request refund if captured (PC R5). PC → Payment: report whether captured (Payment R5).
     - **alt** captured → PC → PaymentGatewayAdapter: request refund (PGA R2).
       - **alt** accepted → PC → Payment: record refund (R4); PC → NotificationDispatcher: inform tourist (ND R3, PC R6).
       - **else** gateway failure → PC → Payment: record refund awaiting retry (R4); PC → NotificationDispatcher: alert staff (PC R6).
     - **else** not captured → no refund (Task 8 variant "Staff cancellation or modification").
- **Result:** the escalation is resolved, B is Cancelled, capacity is released and the refund is issued or queued.
- **Validation shown:** the deadline test, the role check, the captured test and gateway failure.

### SC-04 Provider capacity reduction blocked by Confirmed bookings
- **A1 task:** Task 9 Manage Own Listing Availability.
- **Preconditions:** P is signed in and owns FoodEstablishment F. On day D: capacity 40, Confirmed 30, held 5.
- **Participants (5):** LocalServiceProvider, AvailabilityCalendar, AvailabilitySlot, NotificationDispatcher, NotificationServiceAdapter.
- **Flow:**
  1. LocalServiceProvider → AvailabilityCalendar: set capacity for D to N (AC R5).
  2. AC → LocalServiceProvider: confirm the offering is owned (LSP R1).
     - **alt** not owner → refused.
  3. **alt** N is not a whole number ≥ 0 → refused as invalid input (AC R5).
  4. AC → AvailabilitySlot: report Confirmed and held counts (Slot R2).
     - **alt** N < 30 → blocked. AC → NotificationDispatcher: alert Management Staff of the conflict (ND R3). ND → NotificationServiceAdapter: deliver (NSA R1). Reply: "requires resolution with management" (Task 9 subtask 1).
     - **else if** 30 ≤ N < 35 → blocked. Reply listing the Pending bookings to decide first (AC R7, AS-05).
     - **else** AC → AvailabilitySlot: record new capacity (Slot R1). Reply: saved and visible at once.
- **Result:** the reduction is refused and Management Staff are alerted. No booking is silently cancelled.
- **Validation shown:** ownership, input format, Confirmed and held thresholds.

### SC-05 Review submission through screening and moderation
- **A1 task:** Task 6 Submit Review & Feedback.
- **Preconditions:** T is a signed-in registered Tourist, holds a Completed booking for Accommodation A, and has not reviewed A.
- **Participants (6):** Tourist, ReviewCoordinator, Review, ManagementStaff, Accommodation, NotificationDispatcher.
- **Flow:**
  1. Tourist → ReviewCoordinator: submit review of A with 4 stars and a comment (RevC R3).
  2. RevC → Tourist: report whether registered (Tourist R7).
     - **alt** guest → reply "sign in or register to review" (RevC R1).
  3. RevC → Tourist: report a Completed booking for A (Tourist R2).
     - **alt** none → reply "reviews need a completed booking", and offer general feedback (RevC R1).
  4. RevC → Tourist: report an existing review of A (Tourist R4).
     - **alt** exists → open the existing review for editing (RevC R2, Review R4).
  5. RevC creates Review as Submitted (RevC R3).
  6. RevC → self: screen text (RevC R4).
     - **alt** flagged → RevC → Review: record flagged (Review R3); RevC → NotificationDispatcher: alert moderators (ND R3). Then ManagementStaff → RevC: record moderation decision (RevC R5). RevC → ManagementStaff: confirm role (MS R1).
       - **alt** rejected → RevC → Review: record rejection with reason (Review R3); RevC → NotificationDispatcher: tell the tourist why (ND R3). End.
  7. Publish: RevC → Review: record publication (Review R3); RevC → Accommodation: update average rating (BookableOffering R5, inherited); RevC → NotificationDispatcher: notify the tourist (ND R3, RevC R6).
- **Result:** a verified review is published and A's rating is updated, or a flagged review is rejected and the reason is given.
- **Validation shown:** registered-only check, eligibility, duplicate check, screening and moderation.

Design coverage by the five scenarios:
- SC-01: guest reservation, decision and payment.
- SC-02: Composite and package handling.
- SC-03: time trigger, escalation and refund.
- SC-04: provider capacity.
- SC-05: reviews (registered only).
- Every scenario has three or more classes and at least one alt branch.

---

## 12. Open questions for the team
The questions the team decided are recorded in Section 2.5 as approved defaults (AD-01 to AD-10).

| ID | Question | Current decision |
|---|---|---|
| OQ-01 | Source of indicative exchange rates | Translation/Localization Service (AS-15) |
| OQ-02 | Should boundary classes (TouristPortal, ProviderConsole, StaffConsole) be added? This adds 3 cards and removes the Tourist flag. | Deferred (SI-01) |
| OQ-03 | How long is a guest Tourist and its contact details kept after its bookings finish (PDPA retention)? | Decided with the A3 PDPA design (SI-12) |

---

## 13. Files opened
- Assignment2/build/01_checklist.md
- Assignment2/Assignment 2 Object Design2.md
- Assignment2/build/sources/a1/text.md
- Assignment2/build/sources/a1/page_08.png to page_17.png (all ten)
- Assignment2/build/sources/a1/page_18.png to page_21.png (workflows)
- Assignment2/build/sources/a1/page_22.png (domain model)
