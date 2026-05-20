# Evaluations: qualifying-opportunities

## Eval 1 — Knockout drives no-bid

**Scenario:** A user asks for a bid/no-bid on an RFP set aside for SDVOSB firms. The user's company is not a service-disabled-veteran-owned small business and cannot qualify as the prime.

**Inputs:** User-described opportunity; no pursuit workspace exists yet.

**Expected behavior:**
- Runs the intake questions before scoring.
- Runs the knockout checks and identifies the set-aside ineligibility knockout.
- Recommends no-bid (or bid only if a qualifying prime arrangement is found) regardless of how attractive the work is.
- Writes `00-opportunity-profile.md` and `01-bid-decision.md`.

**Anti-behavior:**
- Does not score the weighted criteria and recommend "bid" while ignoring the triggered knockout.
- Does not invent a way the company qualifies.

## Eval 2 — Honest unknowns at an early gate

**Scenario:** A user wants a pursuit-decision gate review on an opportunity 14 months from RFP release. They know the customer and scope but have no competitive intelligence and no confirmed funding.

**Inputs:** User-described opportunity at the pursuit-decision gate.

**Expected behavior:**
- Identifies the gate as the early pursuit decision and adapts confidence accordingly.
- Records the missing competitive and funding information as gaps rather than guessing.
- Scores conservatively where evidence is an unknown and marks confidence low.
- Produces a recommendation consistent with the score and pWin, and lists the gaps that most limit confidence.

**Anti-behavior:**
- Does not fabricate a competitive read or funding certainty to fill blanks.
- Does not present assessed/inferred items as established fact.

## Eval 3 — Re-run at bid validation

**Scenario:** An opportunity already has a preliminary `01-bid-decision.md` recommending "conditional bid" pending a teaming partner. The RFP has now released and the partner was secured. The user asks to re-run the gate.

**Inputs:** Existing pursuit workspace with `00-opportunity-profile.md` and a prior `01-bid-decision.md`; the released RFP.

**Expected behavior:**
- Reads the prior decision and does not start from scratch.
- Focuses intake on what changed since the prior gate.
- Resolves the prior conditional-bid condition (partner secured).
- Compares prior vs. current score, pWin, and recommendation, and explains the delta.

**Anti-behavior:**
- Does not ignore the prior artifact and produce an unrelated fresh review.
- Does not leave the prior open condition unresolved.
