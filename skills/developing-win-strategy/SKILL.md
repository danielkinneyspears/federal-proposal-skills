---
name: developing-win-strategy
description: Develops the win strategy for a US Federal proposal. Use when the user needs win themes, discriminators, a win strategy, a value proposition, key messages, proposal themes, or ghosting language for a federal bid. Validates discriminators against a value-and-rarity test, builds substantiated win themes that connect customer hot buttons to provable strengths, maps each theme to a Section M evaluation factor, and addresses the team's competitive exposures.
---

# Developing Win Strategy

Turn customer knowledge and competitive analysis into a win strategy: the
validated discriminators, the substantiated win themes, the ghosting language,
and the plan for the team's own exposures. This is the difference between a
proposal that is merely compliant and one that is built to win. Compliance
answers every requirement. A win strategy gives the evaluator a reason to pick
*this* offer over the others.

## When to use this skill

Use this skill late in capture, once customer hot buttons, the competitive
field, and the price posture are understood, to set the strategy the proposal
will execute. The win strategy is the bridge from capture to proposal
development: `outlining-proposals`, `drafting-proposal-sections`, and
`writing-executive-summaries` all consume it.

Re-run it when the RFP releases and Section M is known, to map themes to the
actual evaluation factors and re-test discriminators against the real criteria.

## Inputs

**Preferred upstream artifacts:**
- `02-capture-plan.md`: customer hot buttons, biases, and the requirement read.
- `03-competitive-assessment.md`: competitors' likely themes, the ghosting
  opportunities, and the team's exposures.
- `04-price-to-win.md`: the price posture the strategy must be consistent with.
- The solicitation, if released — Section M evaluation factors.

**Without the upstream artifacts**, the skill runs from intake, but a win
strategy built without a competitive assessment cannot validate the *rarity*
half of a discriminator. Flag that limitation clearly and recommend running
`analyzing-competitors` first.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session.

## Intake

Ask these as a numbered list. Skip what upstream artifacts answer.

1. **Customer hot buttons.** What does this customer care about most — the past
   pain, the risks they fear, the mission pressures, the priorities? (See
   `references/customer-hot-buttons.md` for how to surface and validate these.)
2. **Candidate strengths.** What does the team believe it does well for this
   requirement and customer — capabilities, past performance, people, approach,
   relationships?
3. **The competitive field.** Who is competing, and what would each competitor
   claim as *their* discriminators? (This is what tests whether the team's
   strengths are actually rare.)
4. **The team's exposures.** Where is the team weak, and what will competitors
   ghost about the team's likely offer?
5. **Evaluation factors.** If the RFP is out, what are the Section M factors and
   their relative importance? If not, what is the best read of how the customer
   will evaluate?
6. **Price posture.** What pricing posture is the bid taking (from the
   price-to-win analysis), and does the strategy need to defend a premium or win
   on price?

## Workflow

```
Win Strategy Development:
- [ ] Step 1: Read upstream artifacts; complete intake
- [ ] Step 2: Confirm and prioritize customer hot buttons
- [ ] Step 3: Test candidate strengths for discriminator status
- [ ] Step 4: Build substantiated win themes
- [ ] Step 5: Map each theme to a Section M factor
- [ ] Step 6: Build ghosting language and address exposures
- [ ] Step 7: Write the win strategy (05-win-strategy.md) and validate
```

**Step 1: Read and intake.** Read upstream artifacts; run intake for the rest.

**Step 2: Hot buttons.** Confirm and prioritize the customer hot buttons using
`references/customer-hot-buttons.md`. A theme that does not connect to a real hot
button is talking to no one.

**Step 3: Test for discriminators.** Run every candidate strength through the
discriminator test in `references/win-theme-method.md`: it must be **valuable**
to this customer, **true**, **provable**, and **rare** (not readily offered by
the competitors in the assessment). A strength that fails any test is not a
discriminator. A strength that is valuable and true but not rare is *table
stakes* — necessary to state for compliance, but not a theme. Be honest here;
most claimed discriminators are table stakes.

**Step 4: Build win themes.** For each validated discriminator, build a win
theme using the construction in `win-theme-method.md`: connect the discriminator
to the hot button it serves, state the **benefit to the customer** (not the
feature), and attach the **proof** that substantiates it. A theme with no proof
is a slogan.

**Step 5: Map to Section M.** Map each theme to the evaluation factor it
influences. A theme that maps to no factor will not be scored — either find its
factor or drop it. Note which factors have strong theme coverage and which are
thin; thin factors are a strategy gap.

**Step 6: Ghosting and exposures.** Convert the competitive assessment's
ghosting opportunities into specific, legitimately framed ghosting language
(positive statements about the team's strength that let the evaluator draw the
contrast — never a named competitor, never an unsupported claim). Then, for each
of the team's exposures, decide the response: fix it, pre-empt it in the
proposal, or reframe around it. An unaddressed exposure is a planned loss.

**Step 7: Write and validate.** Write `05-win-strategy.md` using
`templates/win-strategy.md`. Run its validation checklist: every theme traces to
a hot button, a validated discriminator, proof, and a Section M factor; table
stakes are separated from discriminators; ghosting is legitimately framed; every
exposure has a response.

## Output

One artifact: `05-win-strategy.md` in the pursuit workspace — the strategy the
proposal-development skills execute.

Present the user with: the validated discriminators, the win themes (each as
hot button → discriminator → benefit → proof → factor), the Section M coverage
map, and the exposures with their responses.

## References

- `references/win-theme-method.md`: the discriminator test, win theme construction, the feature-vs-benefit distinction, substantiation, and legitimate ghosting.
- `references/customer-hot-buttons.md`: surfacing, validating, and prioritizing customer hot buttons.
- `templates/win-strategy.md`: the win strategy artifact template and its validation checklist.

## Guardrails

- **A discriminator must be rare.** A strength every competitor also has is
  table stakes, not a discriminator. Do not let table stakes masquerade as
  themes. This is the most common and most damaging win-strategy error.
- **Benefit, not feature.** A theme states what the customer *gets*, not what
  the team *has*. "We use X" is a feature; "which means the customer gets Y" is
  the theme.
- **No proof, no theme.** Every theme carries substantiation — past performance,
  metrics, named credentials, demonstrable facts. Unprovable claims are cut.
- **Ghost legitimately.** Ghosting names no competitor and makes no unsupported
  negative claim. See the method file.
- **Honesty about exposures.** Every exposure gets a real response. Hoping the
  evaluator misses it is not a strategy.
