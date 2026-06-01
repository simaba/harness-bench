# Public Release Checklist

Use this checklist before changing the repository visibility to public.

## Required before publishing

- [ ] Confirm all benchmark tasks are fictional, synthetic, or public-safe.
- [ ] Confirm no private prompts, system instructions, customer data, employer data, or vendor data are committed.
- [ ] Confirm no internal benchmark outputs or private tool results are included.
- [ ] Confirm no API keys, tokens, credentials, connector details, account identifiers, or private paths are present.
- [ ] Confirm any leaderboard or comparison is labeled as sample, exploratory, or methodology demo unless the methodology is fully documented.
- [ ] Confirm the README does not imply provider endorsement or definitive ranking.
- [ ] Confirm harness versions, model versions, task conditions, and scoring caveats are documented for any published result.
- [ ] Confirm the license, README, and quick-start commands are accurate.

## Recommended before promotion

- [ ] Add multiple benchmark tasks across distinct categories.
- [ ] Add repeated-run support and variance reporting.
- [ ] Add a methodology note on comparability and fairness.
- [ ] Add a sample leaderboard based only on public-safe runs.
- [ ] Run tests locally after a fresh clone.

## Final manual review

Before publishing, search the repo for private prompts, provider-specific secrets, internal acronyms, API keys, tokens, emails, account identifiers, customer names, and unpublished benchmark results.

This checklist is a publication aid, not a security or benchmark-validity guarantee.
