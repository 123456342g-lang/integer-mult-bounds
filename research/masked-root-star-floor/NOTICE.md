# Notice and attribution

Prepared by **Navinor** with help from opencode (research, proof development,
implementation, verification and documentation). Apache-2.0; new contributions are under
the repository's license.

Model and question: PR717 (DreamingOfClouds), `research/format-limits-2/` at head
`4a97676294f9fa413b65986e9984fddeda71e4cc` (B14 decoder model, D1(a) masked reduction,
D1 mixed-beta open problem, D1(e) sampled covering bound; read for definitions only, not
vendored or executed). Prior decoder floors: PR620 (Joel Pulikkan / GamingPuzzled),
PR968 and PR1077 (woklerx and the seed44/seed48 packages; both defer masked E-graph
identities), PR845 (Mihir Srivastava; fixed-reader ninth total). The E8 line enumeration
is adapted from `research/complex-frame-pair-decoders/verify.py` (Apache-2.0, same
repository) with attribution; no predecessor file is modified or imported at runtime.

The selected construction chain (see `certificates/selected-result.json`) is read only:
Jonathan Capalbo, Chafik Boukhalfa, Jeremy Kothe, Hao Yan, DreamingOfClouds, eumemic and
the other credited authors of the T37/PR589 chain. No selected-frontier change is proposed.

Third-party code: none. Standard library only. Retained source attribution and licenses of
all predecessor packages apply to their own files.
