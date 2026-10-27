---
name: ood
description: Assignment 2 object-design pipeline for the Sarawak Tourism project (rubric → blueprint → draft → QA → checks → grade). Run only when the user types /ood.
argument-hint: "[from:0-6] [fresh] [auto]"
disable-model-invocation: true
allowed-tools: Agent, AskUserQuestion, Read, Write, Glob, Grep, Bash(python .claude/skills/ood/scripts/*), Bash(cp Assignment2/build/*)
---

# /ood: Assignment 2 Object Design orchestrator

You run a staged pipeline that turns the team's Assignment 1 SRS into the Assignment 2 Object Design Document (ODD) for the Sarawak Tourism Promotion System (STPS). Subagents write the content. You own the inputs, the gates between stages and the final report. Do not write document content yourself.

Arguments: `$ARGUMENTS`
- `from:N`: start at step N (default 0). Outputs of earlier steps must already exist.
- `fresh`: regenerate a step's output even if the file exists. Without it, a step whose output exists is skipped and reported as reused.
- `auto`: skip the human checkpoint after step 2.

## Files

All paths are relative to the repository root (`COS30003/`).

| Role | Path |
|---|---|
| Marking rubric (authoritative for scoring) | `Assignment2/marking_rubric.md` |
| Assignment brief | `Assignment2/Assignment 2 Object Design2.md` |
| Sample submission (a reference, not a model answer) | `Assignment2/build/sources/sample/` (`text.md`, `index.md`, `page_NN.png`) |
| Assignment 1 SRS (the case study) | `Assignment2/build/sources/a1/` (same layout) |
| Assignment 1 result and rubric | `Assignment2/Assignment1_details/Assignemnt_1_mark.md`, `Assignment2/Assignment1_details/rubric.yaml` |
| Stage outputs | `Assignment2/build/01_checklist.md`, `02_blueprint.md`, `03_draft_ood.md`, `FINAL_OOD.md`, `04_check_report.txt`, `05_grade_report.md` |

Subagents have no shell and cannot open PDFs. They read `text.md` for wording and the PNGs listed in `index.md` for diagrams.

## Operating rules

1. Run the steps in order. Before each delegation, confirm its inputs exist. After it, confirm the output file exists and is non-empty (Glob, then Read its first 40 lines). If a check fails, stop and report. Never fill a gap yourself or report a step as done when it did not run.
2. Subagents do not see this conversation. Each delegation prompt must contain the step's brief from this file, the **Design contract** where the step lists it, the **Domain carry-forward** where listed, and any reviewer or user feedback.
3. Each agent's definition already holds its role, standards and output contract (write to the given path, reply in at most 10 lines). The delegation supplies only the task: input paths, output path, brief, contract and feedback. Never ask an agent to paste the document back.
4. A PostToolUse hook (`.claude/settings.json`) re-runs `check_ood.py` on every write to `FINAL_OOD.md` and feeds errors back to the editing agent. Step 5 still runs the check explicitly to produce the report file.
5. Use the `rubric-analyst`, `requirements-architect`, `technical-builder` and `precision-qa` agents exactly as named. Do not substitute general-purpose agents.

## Design contract

Steps 2, 3 and 4 must follow this contract. `.claude/skills/ood/scripts/check_ood.py` enforces it mechanically.

- **Names.** Class names are PascalCase and identical everywhere: the candidate list, the class diagram, the CRC headings, the bootstrap diagram and the scenario diagrams.
- **Class diagram.** One Mermaid `classDiagram`. It shows class names, relationships (association, aggregation, composition, generalisation, dependency), multiplicities and relationship labels only. It has **no attributes, methods or signatures**, because the rubric deducts up to 5 marks for them. Data-holder classes carry a `<<datatype>>` stereotype and are described as data-structure definitions. A legend below the diagram explains the notation.
- **CRC cards.** Each card has the heading `### CRC Card: ClassName`, then `**Superclass:** <name or —>`, then `**Description:** <one or two sentences>`, then a table `| Responsibility | Collaborators |`. Each row holds one responsibility with its own collaborators, and `—` when there is none. Responsibilities are phrases such as "Knows …", "Decides …" or "Records …", never method names.
- **Bootstrap.** A Mermaid `sequenceDiagram` plus a numbered list give the creation order from a named entry-point class (for example `STPSApplication`). Every participant is a class with a CRC card. There is no undefined "Main" or "System".
- **Verification.** At least 4 non-trivial scenarios, with 5 as the target. Each scenario names the Assignment 1 task it exercises, its preconditions, and a Mermaid `sequenceDiagram` (people as `actor`), followed by a walkthrough. Each one includes at least one `alt` branch showing how invalid input or a failure is detected and handled. Messages use plain verbs, not parameter lists.
- **Patterns and heuristics.** Every claimed pattern or heuristic names the classes that play each role and the concrete problem it solves in STPS. Leave out any pattern you cannot map to classes.
- **Cross-references.** Every "Section N", "Figure N", "Table N" and "Task N" points to something that exists. Assignment 1 lost marks for stale task numbers.

## Domain carry-forward

These are starting facts from the Assignment 1 SRS. Steps 2 and 3 verify each one against `a1/text.md` and cite the section.

- Actors: Tourist (guest or registered); Management Staff, specialised as Content Officer and Data/System Admin; Local Service Provider. External systems: Payment Gateway Provider, Notification Service, Mapping/Geolocation Service, Translation/Localization Service.
- Bookable offerings are Accommodation, Vehicle and Food Establishment. Destination and Local Article Info are informational. The A1 ER diagram made Destination a subtype of the bookable "Services"; resolve this and record the decision.
- Booking lifecycle (PR-15): Pending → Pending-Payment → Confirmed → Completed, plus Declined and Cancelled. The provider decides within a 48-hour SLA, otherwise the booking escalates to Management Staff (Tasks 8 and 10). The Tourist pays only after approval. Cancelling after payment capture triggers a refund.
- A Package Booking is one parent booking with one component booking per offering (Task 5). Capacity is held while a booking is Pending and released on decline.
- Availability is a daily capacity per offering. A provider cannot set it below that day's Confirmed bookings (Task 9). The system never overbooks, including under concurrent requests and capacity held by packages (NFR 7.4).
- Reviews need a completed booking, pass screening and moderation, and are limited to one per tourist per item (Task 6).
- Content lifecycle: draft → published or scheduled → unpublished or archived. Content is bilingual (EN/BM), auto-unpublishes at its end date, and withdrawing a listing with active bookings raises a warning (Task 7).
- Prices are in MYR with an indicative conversion. STPS never stores card data.
- Known A1 gaps for the design to resolve and record as assumptions or simplifications:
  - Package, Add-on, availability slot and tourist account are used but are not domain entities.
  - The Management Staff split is drawn as an association, not a generalisation.
  - Review–Tourist cardinality conflicts between the table and the diagram.
  - Payment and registration have no task of their own.
  - Do not copy A1's stale task numbers.

## Step 0: Prepare sources (you)

Skip this step if `Assignment2/build/sources/a1/index.md` and `sample/index.md` exist and `fresh` is not set. Otherwise run `python .claude/skills/ood/scripts/extract_sources.py`. If it fails because `pymupdf` is missing, stop and tell the user to run `! python -m pip install pymupdf`.

## Step 1: `rubric-analyst` → `01_checklist.md`

Brief: read `marking_rubric.md`, the assignment brief, the A1 result and rubric, and the sample (`sample/text.md`, plus `page_09.png` for its class diagram and `page_19.png`–`page_22.png` for its sequence diagrams). Write `Assignment2/build/01_checklist.md` with:
1. A per-criterion table: criterion, maximum marks, what full marks requires stated as observable properties of the document, and every penalty trigger as a hard gate with its deduction.
2. A critique of the sample: where it would lose marks under this rubric. Confirm or reject each of these candidate issues and add others you find:
   - the `Menu` class "controls what other classes do" (god class);
   - the bootstrap section describes a sales scenario rather than system start-up;
   - MVC is labelled a structural pattern;
   - the Factory Method claim maps to no factory class;
   - `Database` "executes arbitrary SQL", which is solution-oriented;
   - several CRC responsibilities have no collaborators;
   - heuristics are listed but never applied to specific classes.
3. Lessons from Assignment 1 (71.5/100): for each criterion that lost marks, the equivalent risk in Assignment 2. This covers coherence, consistency, stale cross-references and inconsistent templates.
4. A Definition of Done: a flat list of yes/no checks that a reviewer can tick against the final document.

Do not design classes.

## Step 2: `requirements-architect` → `02_blueprint.md`

Inputs: `01_checklist.md`; `a1/text.md` (Sections 2–6 and 8); the A1 domain model (`a1/page_22.png`) and workflow pages (`a1/page_18.png`–`page_21.png`); the assignment brief; the **Design contract**; the **Domain carry-forward**.

Brief: write `Assignment2/build/02_blueprint.md` as structured bullets and tables with IDs, not prose:
1. **Problem analysis:** a noun/verb analysis of the A1 tasks and entities. List each candidate with its source (A1 task, subtask or entity).
2. **Assumptions (AS-xx) and simplifications (SI-xx):** realistic and within the brief's constraints, each with a rationale. Include how each A1 gap above is resolved.
3. **Final classes (CL-xx):** name, superclass, purpose in one line, stereotype (entity, control, boundary, datatype or external adapter), and the A1 tasks it serves.
4. **Discarded or merged candidates:** at least 5, each with a reason.
5. **Relationships:** source, relationship type, target, multiplicity and label.
6. **A CRC skeleton per class:** responsibility → collaborators.
7. **Responsibility coverage matrix:** every subtask of A1 Tasks 1–10, plus payment and account handling, mapped to the class that owns it. There must be no gaps.
8. **God-class check:** the responsibility and collaborator count per class. Flag any class with more than 8 responsibilities or more than 6 collaborators, then split it or justify it.
9. **Patterns and heuristics:** the name, the role of each class and the STPS problem solved. Candidates worth testing, used only where a responsibility needs them: State (booking lifecycle), Observer (notifications), Adapter or Strategy (payment and other external services), Composite (package bookings), Factory (offering creation), and GRASP Controller, Creator and Information Expert.
10. **Bootstrap order:** which class creates which, in order, starting from the entry-point class.
11. **Verification scenarios (SC-xx), 5 in total:** each with its A1 task, the participating classes and the validation or failure branch it will show. Cover at least: an accommodation reservation through approval and payment; a package booking where one component is unavailable or declined; SLA expiry escalated to Management Staff with a refund after payment; a provider capacity reduction blocked by Confirmed bookings; and review submission through moderation.
12. **Open questions for the team.**

## Checkpoint (you; skipped with `auto`)

Show the user the class table (name, superclass, purpose), the discarded list, the pattern mapping and the scenario list from `02_blueprint.md`. Ask with AskUserQuestion: "Approve" or "Revise". If they choose Revise, re-run step 2 with their feedback, at most twice. This class model becomes the Assignment 3 baseline, so the team must agree with it.

## Step 3: `technical-builder` → `03_draft_ood.md`

Inputs: `02_blueprint.md`, `01_checklist.md`, `a1/text.md` (cover page for authorship), the **Design contract** and the **Domain carry-forward**.

Brief: expand the blueprint into the complete ODD at `Assignment2/build/03_draft_ood.md`. Use numbered sections in this order:
- A title block: document title, unit SWE30003, Group 16, and the members with their IDs as listed on the A1 cover.
- Document control, then the table of contents.
- 1 Executive Summary
- 2 Introduction: purpose, scope, audience, outlook of the solution, and definitions.
- 3 Assumptions
- 4 Problem Analysis: approach, analysis, and simplifications.
- 5 Candidate Classes: the list, the class diagram with its legend, the justification of chosen classes, and the discarded classes.
- 6 CRC Cards: one card per class, in the same order as the list.
- 7 Design Quality: responsibility coverage, design heuristics and design patterns.
- 8 Bootstrap Process
- 9 Verification
- 10 References: Harvard style, consistent with A1.
- Appendix A: a statement that the Assignment 1 SRS is attached as a separate PDF.
- Appendix B: the A1 task → class traceability table.

Write for a technical reader on the client's side. Every diagram has a numbered caption.

## Step 4: `precision-qa` → `FINAL_OOD.md`

First run `cp Assignment2/build/03_draft_ood.md Assignment2/build/FINAL_OOD.md` yourself. `precision-qa` has only Read and Edit and cannot create files.

Brief: edit `Assignment2/build/FINAL_OOD.md` in place against the **Design contract** and the Definition of Done in `01_checklist.md`. Fix the following:
- class names that differ between the list, the diagram, the CRC cards and the sequence diagrams;
- any attribute or method that has crept into the class diagram;
- CRC rows without collaborators;
- responsibilities that are vague or duplicated across classes;
- cross-references that point nowhere.

Use plain English, the active voice and the British/Australian spelling used in A1. Apply PDPA wording only where the document handles personal data.

## Step 5: Mechanical checks (you)

Run `python .claude/skills/ood/scripts/check_ood.py Assignment2/build/FINAL_OOD.md > Assignment2/build/04_check_report.txt`, then read the report.
- If the exit code is 0, continue. Pass any warnings on to step 6.
- If there are errors, delegate to `precision-qa` with the full report and ask it to fix every error in `FINAL_OOD.md`, then re-run the check. Allow at most 2 fix rounds. If errors remain, stop and report them without grading.

## Step 6: `rubric-analyst` → `05_grade_report.md`

The grader deliberately runs on a different model from the authoring agents.

**Calibration.** In a blind run on the Assignment 1 SRS (`Assignment2/build/calibration/a1_blind_grade.md`), this grader predicted 78.5 against a real mark of 71.5.
- Almost all of the +7 came from the two heaviest criteria: user tasks (+5 of 40) and quality attributes (+4 of 20).
- Small criteria were within ±1 mark.
- It viewed only 3 of the page images it was pointed to and misread one diagram as a result.

Treat its total as a ceiling, and its fix ranking as the useful output.

Brief: grade `Assignment2/build/FINAL_OOD.md` against `marking_rubric.md` as a strict marker. Use `04_check_report.txt` as evidence for the mechanical penalties.

Include this in the brief: "A blind calibration on Assignment 1 showed you over-marking the heaviest criteria by 10–20% of their weight. For Candidate Classes, CRC Cards and Verification (20 marks each), list the specific defects you found before you assign a mark. Where you are unsure between two marks, give the lower one."

Write `Assignment2/build/05_grade_report.md` with:
- a per-criterion table of maximum marks, predicted marks, evidence (section or figure references) and confidence (high, medium or low);
- the penalties applied;
- the predicted total, labelled as an upper estimate;
- the top fixes, ranked by marks recovered per unit of effort;
- a "Sources viewed" list naming every file the grader actually opened.

Do not edit `FINAL_OOD.md`.

## Final report (you)

Reply to the user in under 25 lines with:
- each step's status (ran, reused or failed);
- the class count and class names;
- the checker result;
- the predicted total, stated as an upper estimate (the grader ran about 7 marks high on A1), and the top 5 fixes;
- the remaining manual work: render the Mermaid diagrams for the PDF (for example `npx @mermaid-js/mermaid-cli`); add the signed cover sheet and contribution worksheet; attach the A1 PDF as an appendix.
