# Junior Developer Onboarding Guide

**Goal of this document**: Get you productive and confident as quickly as possible on our high-demand platforms.

## First Week Goals

1. **Understand the big picture**
   - Read the current architectural model we use (`architectures/monolith/v1/` or microservices if your team is there).
   - Understand why we made those choices.

2. **Get the local environment working**
   - Clone the main application(s) you will work on.
   - Run the app locally and hit a few endpoints.
   - Make a trivial change (e.g. add a log line) and see it reload.

3. **Make your first meaningful contribution**
   - A small bug fix or a very small feature.
   - Follow the patterns in the Spring Boot 4 handbook and API best practices.

## Key Concepts You Must Understand Early

- **Bounded contexts** and why we care about them (even in a monolith)
- **Dependency inversion** / ports & adapters (makes testing and future extraction easier)
- **API contracts** are more important than implementation details
- Observability: logs + traces + metrics (we use them every day)
- How configuration and secrets work in our environment

## Where to Find Things (This Repo)

- **How we build systems**: `architectures/`
- **Spring Boot 4 patterns**: `spring-boot/4/`
- **How we design and version APIs**: `api-design/` and `spring-boot/4/api/`
- **General best practices**: Scattered under language and framework sections (search for "best-practices")
- **"Why do we do it this way?"**: Usually at the top of the architecture model READMEs

## Recommended Reading Order (First 2 Weeks)

1. `architectures/monolith/v1/overview.md`
2. `spring-boot/4/getting-started.md`
3. `spring-boot/4/api/rest-controller-best-practices.md`
4. Your team's main application README
5. `spring-boot/4/best-practices/testing.md` (once you start writing tests)

## Common Anti-Patterns for Juniors (Learn to Spot Them)

- Fat controllers with business logic
- Shared database across services "because it's easier"
- Ignoring error handling / returning raw exceptions
- Hardcoding values instead of using configuration
- Not writing tests because "the code is simple"

## How to Ask Good Questions

Instead of: "How do I do X?"

Try: "I'm trying to implement feature Y following the patterns in `spring-boot/4/api/`. The requirement is Z. I see two possible approaches — here's what I think the trade-offs are. Which direction should I go?"

This handbook exists precisely so you have context before asking.

---

Welcome aboard. The faster you internalize the models in this repo, the faster you'll stop feeling lost. Update pages when you discover something that would have helped you on day one.