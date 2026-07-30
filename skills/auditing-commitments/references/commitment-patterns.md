# Commitment patterns

The recurring ways a federal proposal creates obligations nobody priced. Each
pattern lists what it sounds like in a draft and the defensible form — the
version that keeps the competitive value while bounding the obligation.

The defensible form is almost never "promise less." It is "promise the same thing
with the conditions stated." A bounded commitment is more credible to an
evaluator than an unbounded one, because an unbounded promise signals the offeror
has not thought about performance.

---

## 1. The promise stronger than the requirement

**Sounds like:** the SLA requires 99.5% monthly availability; the draft
guarantees availability and zero unplanned downtime.

**Why it costs:** one ordinary outage becomes a documented failure against the
offeror's own words. The extra half-percent earned no evaluation credit, because
Section M scored compliance with 99.5%, not generosity beyond it.

**Defensible form:** meet the requirement, state the requirement's number, and
put any additional capability in a separate sentence framed as capability rather
than commitment. "Our architecture has sustained 99.98% over the past 24 months
at [reference site]" is a proof point. "We guarantee 99.98%" is a liability.

---

## 2. The absolute

**Sounds like:** `100%`, `zero defects`, `never`, `always`, `at all times`,
`24/7`, `no downtime`, `any and all`, `fully compliant`.

**Why it costs:** absolutes are uninsurable by construction. There is no
performance history that supports "never," and a single counter-example is a
breach. Evaluators discount them anyway; experienced source selection personnel
read an absolute as an offeror who has not performed at scale.

**Defensible form:** a number with a measurement window and stated exclusions.
"99.5% measured monthly, excluding scheduled maintenance windows agreed with the
COR" is stronger, not weaker, than "100% uptime."

---

## 3. The number with nothing behind it

**Sounds like:** a fifteen-minute response commitment, around the clock, in a
proposal whose staffing plan funds one shift.

**Why it costs:** the evaluator may not catch it; the program office will, in
month three. Then it is either an unfunded staffing increase or a performance
failure. This is also the pattern most likely to be caught in a cost-technical
consistency review, where it becomes a weakness before award instead.

**Defensible form:** the number the staffing plan actually funds, with the
coverage window named. If the requirement demands more than the plan funds, that
is a solution problem or a bid problem, not a wording problem — escalate it
rather than writing over it.

---

## 4. Volunteered scope

**Sounds like:** a free public dashboard the RFP never requested. A monthly
report nobody asked for. An extra environment "at no additional cost."

**Why it costs:** recurring cost for the full period of performance, plus any
obligation that rides along — a public dashboard is also a data-exposure and
accessibility obligation. Zero points, because Section M does not evaluate it.

**Defensible form:** offer it as an option priced separately, or describe it as
something the offeror already operates rather than something it will build and
maintain for this customer. If it is a genuine differentiator and the win
strategy says so, keep it and price it deliberately.

---

## 5. Conditions omitted

**Sounds like:** any performance figure that depends on something the offeror
does not control — feed composition, site conditions, weather windows, wave or
solar resource, a customer-supplied input, third-party system availability — and
does not say so.

**Why it costs:** the promise becomes unconditional. When the condition moves,
the shortfall is the offeror's. This is the dominant pattern for technical firms,
because the engineer knows the caveats so well they feel too obvious to write.

**Defensible form:** bind the figure to the conditions under which it was
demonstrated, and name them. "99.97% purity at the feed composition in Table 3,
verified by GC per ASTM D1946." The specificity reads as competence.

---

## 6. Turnaround measured from the wrong event

**Sounds like:** "results delivered within five days."

**Why it costs:** five days from what? Field completion, data receipt, task
order issuance, or contract award? An unanchored clock is read against the
offeror, and it usually starts earlier than intended.

**Defensible form:** anchor to an event the offeror controls or can verify, and
state what pauses the clock. "Within five business days of receipt of complete
field data, excluding periods awaiting government-furnished information."

---

## 7. Filler dressed as confidence

**Sounds like:** "we strive to exceed expectations," "world-class,"
"best-in-class," "seamless," "robust," "state-of-the-art," "industry-leading."

**Why it costs:** no metric, no obligation, no score — and it is consuming page
count in a page-limited volume that needed every paragraph for something
scoreable. It also signals to an evaluator that the offeror had nothing specific
to say at that point.

**Defensible form:** delete it and use the space for a proof point. If the claim
is real, it can be stated as a number with a source.

---

## 8. Promises hidden outside the narrative

**Sounds like:** a commitment in a graphic's action caption, a resume bullet, a
past performance write-up, or a table cell.

**Why it costs:** these are rarely audited, and they carry exactly the same
weight. A resume that says a key person "will be available full time for the life
of the contract" is a staffing commitment with a substitution consequence.

**Defensible form:** audit graphics, captions, tables, resumes and past
performance with the same pass used on body text. The scan script reads whatever
text it is given; give it everything.

---

## The three questions

Every hit reduces to the same test:

1. **Did the solicitation require this?** Find the exact language in the
   compliance matrix. Not a related requirement — the requirement.
2. **Can it be staffed and funded exactly as written?** Ask whoever performs the
   work, not whoever wrote the sentence.
3. **Will an evaluator reward it?** It must appear in the evaluation criteria.

The four verdicts:

| Result | What to do |
|---|---|
| Required but unsupported | Fix the solution, or revisit the bid decision. |
| Not required, but scored, funded and deliberate | Possibly a differentiator. Confirm with the capture lead. |
| Not required and not scored | Being given away. Cut or convert to a priced option. |
| Not measurable or supportable | Cut. It is costing page count and creating exposure. |
