# Define-Challenge-Build (DCB)

> A planning methodology that separates design (the What) from implementation (the How). Both must pass a mandatory critical review before moving to the next phase.

---

## 1. What it is

Define-Challenge-Build (DCB) is a software project planning methodology. It separates a project's definition (the What) from its implementation plan (the How), and requires each one to pass a critical audit —the Challenge— before advancing to the next phase.

Its core is that Challenge: no artifact, neither the Definition nor the Roadmap, moves into construction without being challenged first.

The Challenge can be carried out in three ways:

* **Human experts only.**
* **AI only.**
* **Human experts + AI**, combined. This is the recommended approach: AI surfaces information, precedents, or risks that an expert doesn't always have top of mind, and the expert provides the judgment to filter how applicable that is to the real project.

```
[Requirements] → [Define: "What"] → [Challenge #1] → [Consolidated Definition]
      → [Define: "How" / Roadmap] → [Challenge #2] → [Build]

```

## 2. What it is not

DCB is not an execution methodology. It doesn't compete with Scrum, Kanban, or Waterfall, and it doesn't dictate how to run sprints or manage a team. It operates before that: it defines how a plan gets validated, not how it gets executed.

It's similar to Spec-Driven Development (SDD): both separate specification from implementation. The difference is that in DCB the Challenge is a mandatory step, not an optional review, and it's applied twice: on the Definition and on the Roadmap.

## 3. Goals

* Prevent a poorly defined or ambiguous plan from reaching construction undetected.
* Reduce the risk of building on unverified assumptions.
* Separate what gets built from how it gets built, so a technical change doesn't force a redefinition of the project's goal.

When an AI generates the content of the Definition or the Roadmap, the Challenge acts as a direct control against its typical failure modes: hallucination, overconfidence, and moving forward on unverified assumptions.

## 4. Core principle: decoupling of components

DCB separates the project's goal from its execution into two independent artifacts:

| Artifact | Answers | Nature |
| --- | --- | --- |
| **Definition file** | The What | Static — goals, business rules, scope, and constraints |
| **Roadmap** | The How | Dynamic and versioned with git — technical implementation path |

If the Roadmap changes, the Definition stays intact.

## 5. The workflow

### 5.1 Define

Requirements are gathered and a first draft of the Definition file is written. Once the Definition is consolidated, this same stage repeats to produce the Roadmap.

### 5.2 Challenge

The artifact that was just produced —Definition or Roadmap— is audited before being accepted, by experts, AI, or both combined (see section 1).

It's applied twice:

1. **On the Definition** — verifies that the "What" is complete and unambiguous.
2. **On the Roadmap** — verifies that the "How" is consistent with the approved Definition and technically feasible.

An artifact is considered consolidated once it passes its corresponding Challenge.

### 5.3 Build

With the Definition locked in and the Roadmap validated, construction begins. If something unexpected comes up that affects the Roadmap, the file is corrected and goes through Challenge again, without touching the Definition. If the unexpected issue reveals that the original "What" was infeasible, it goes back to Define.

## 6. When to use it

* You're using AI to design or plan a system, not just to generate isolated code.
* The project has ambiguous or changing requirements.
* You're working solo and need an external verification mechanism.
* Building on the wrong design would be costly.

## 7. When not to use it

* One-off or narrow tasks: a standalone function, a snippet, a minor fix.
* Rapid prototypes where the goal is to explore, not lock down a design.
* Projects where the "What" is already completely clear.

## 8. Pros and risks

**Pros**

* Reduces the risk of building on hallucinations or unverified assumptions.
* The Roadmap can change without compromising the project's goal.
* Provides traceability: each Roadmap references which part of the Definition it implements.

**Risks**

* If whoever runs the Challenge lacks real authority to block the artifact, it becomes a rubber-stamp step with no real friction.
* An artifact "consolidated after Challenge" can create a false sense of safety during the Build.
* Requires discipline not to skip the Challenge under time pressure.

## 9. Artifacts of the methodology

### 9.1 Definition file (the What)

Master, static document: goals, business rules, scope, and constraints of the system. It isn't modified once consolidated, except in cases of structural infeasibility.

### 9.2 Roadmap (the How)

Dynamic document that lays out the technical implementation path, without depending on references to a specific Definition file.

Each Roadmap lives in a single file, and its name should be descriptive — never generic like `roadmap.md`, since a single feature can end up with several roadmaps. Recommended convention:

* `roadmap-<feature>.md` when the delivery is resolved in a single roadmap.
* `roadmap-<feature>-<slice>.md` when the feature is split into several — by technical layer (`roadmap-auth-backend.md`, `roadmap-auth-frontend.md`) or by sub-delivery.

Change history is tracked with git (commits), not by duplicating the file per version. The exception is when the project doesn't use any version control system: in that case it does make sense to add a v1, v2, v3, etc. suffix to distinguish versions.

*Recommended structure for the Roadmap file:*

Each Roadmap is self-contained and should be internally structured with:

* **Definition:** a short initial description of the specific problem this roadmap solves and which part of the approved Definition it covers, without naming files or anchoring it to an external document.
* **Phases and Atomic Tasks:** a step-by-step breakdown (e.g. Backend, Frontend) organized with checkboxes (`- [ ]`) to track the Build.

### 9.3 Challenge Prompts

Instructions for auditing the Definition and the Roadmap. This repository doesn't include sample prompts: they should be written according to each project's actual risks.

## 10. How to separate the Definition from the Roadmaps

* **A single Definition file per project**, at the root of the repository. It isn't fragmented by module or by sprint.
* **One or more Roadmaps per unit of delivery** (module, feature, technical milestone). A feature can be resolved with a single vertical roadmap, or split into several — by technical layer (backend, frontend) or by sub-delivery — as needed; what never happens is a monolithic roadmap covering the whole system.
* **Each Roadmap is self-contained** and describes the delivery it implements without depending on references to other artifacts.
* **File naming is descriptive.** Each roadmap is named following the convention in section 9.2 (`roadmap-<feature>.md` or `roadmap-<feature>-<slice>.md`), never generically.
* **The Definition doesn't carry implementation details** — stack, libraries, endpoints, database schemas.
* **The Roadmap doesn't redefine business goals.** If building it out reveals that the Definition is ambiguous or infeasible, it goes back to Define.
* **Versioned with git.** The Definition and Roadmaps are single files; every change is recorded as a commit, and that history is what shows the artifact's evolution. Only when a project doesn't use git or another version control system does it make sense to name files v1, v2, v3.

## 11. Recommended project structure

```
my-project/
├── definition.md                  # The What — single, static, source of truth
├── CHALLENGE_LOG.md               # History of Challenges on the Definition
│
├── roadmaps/
│   ├── roadmap-auth/
│   │   ├── roadmap-auth-backend.md
│   │   ├── roadmap-auth-frontend.md
│   │   └── challenge-log.md
│   ├── roadmap-payments/
│   │   ├── roadmap-payments.md
│   │   └── challenge-log.md
│   └── roadmap-notifications/
│       ├── roadmap-notifications.md
│       └── challenge-log.md
│
├── prompts/
│   └── challenge/
│       └── ...                    # Prompts written by the team (see section 9.3)
│
└── src/                            # Code built from the consolidated roadmaps

```

The Definition sits isolated at the root, so it can be reviewed without going through code or roadmaps. Each folder under `roadmaps/` is self-contained: it groups the roadmaps for a single feature —one or several, depending on whether it makes sense to split it— along with a shared Challenge log. Changes to each roadmap file over time are tracked with git, not with duplicated files. The `challenge-log.md` records who challenged which roadmap and how it was resolved.

## 12. Roadmaps as hyper-specific Spec-Driven Development

A Roadmap within DCB has already gone through Define, has already been challenged, and is already tied to an approved Definition. By the time it reaches Build, there's no remaining business or design ambiguity — only execution.

For teams using coding agents (Claude Code or others), this means a consolidated Roadmap can be handed directly to the agent as a work spec:

* Architecture and scope decisions were already locked in during Define + Challenge, not made during the Build.
* The agent doesn't infer business intent — that intent lives in the referenced Definition.
* Each step of the Roadmap is an atomic, verifiable task.
* If the agent finds an inconsistency, the protocol already exists: correct the Roadmap (logging it in git), or go back to Define if the problem is fundamental.

## 13. DCB and Vertical Slice Architecture

DCB pairs well with Vertical Slice Architecture (VSA): organizing the system by end-to-end feature instead of by horizontal technical layer.

A VSA feature translates into one or more DCB Roadmaps, all referencing the same central Definition. Splitting a feature into several roadmaps —for example, separating backend and frontend within the same folder— doesn't break the VSA principle: the feature is still the unit of delivery and of Challenge, it's just that its How is split into smaller pieces that are easier to audit separately.

Applying DCB per feature brings:

* **A narrower Challenge.** Auditing a single feature is faster than auditing the whole system at once.
* **Real parallelization.** Different features can be at different stages of DCB at the same time.
* **Contained changes.** Fixing one feature's Roadmap doesn't affect the rest.
* **Feature-by-feature traceability.**

## 14. Example

Project: a sports court booking platform for a club.

**Step 1 — Define (Definition).**
The client's requirements are gathered (booking rules, user roles, cancellations, legal constraints) and a first version of the Definition is drafted.

**Step 2 — Challenge on the Definition.**
The team (experts + AI) audits the draft and finds gaps:

* It doesn't specify what happens when two users book the same court at the same instant.
* It doesn't define how rain cancellations are handled for outdoor courts.

This gets logged in `CHALLENGE_LOG.md`, fixed, and repeated until there are no open objections left. The Definition is consolidated.

**Step 3 — Define (Roadmap with definition and tasks).**
`roadmaps/roadmap-bookings/roadmap-bookings.md` is created:

```markdown
# Roadmap: Court Bookings
## 1. Definition
- **What it solves:** Implements the locking and slot-registration logic referencing the Definition, section 3.
- **Scope:** Excludes online payments for now; internal booking operations only.

## 2. Phases and Tasks
### Phase 1: Backend (.NET)
- [ ] Create the booking endpoint with concurrency locking.
### Phase 2: Frontend (Next.js)
- [ ] Build the calendar view and confirmation button.

```

> Roadmaps must always be deterministic: no "to be confirmed" items, no pretending something will be added later — that's what the Challenge is for. They also can't reference other roadmaps or the Definition. Later changes to the same file are strictly for corrections, not for adding new content; that history lives in git. If a feature from an already-completed roadmap needs to be extended, a separate roadmap is created instead.
>
> The roadmap is for design decisions and system contracts, not a log of every small adjustment made along the way.

**Step 4 — Challenge on the Roadmap.**
It's flagged that the proposed locking mechanism won't scale well with multiple concurrent courts. `roadmap-bookings.md` is corrected and re-audited; the change is documented in `challenge-log.md` and recorded as a commit in git.

**Step 5 — Build.**
The consolidated Roadmap is handed directly to a coding agent as an execution spec. During the Build, something unexpected comes up (the chosen library doesn't support the client's database engine): `roadmap-bookings.md` is corrected, the reason is documented in `challenge-log.md`, and the change is versioned in git, without touching the Definition.