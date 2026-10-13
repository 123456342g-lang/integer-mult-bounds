# T37 validation receipts

The strict U8/T37/PR589 replay passed conditional κ = **0.001661960547713947**.
A fresh complete PR589/PR741/PR799 replay took 1835.893 seconds; the T37 driver
then reused that checked ancestry explicitly and ran all 20 mandatory stages
in 660.847 seconds. The separate package audit rejected 47 mutations and
accepted two gzip recompressions. Timings describe this machine, not a
performance claim. See `ENVIRONMENT.json` and `VALIDATION.json`.

The final emitted invoice has prefix779 < charged1024, row17495 < 20161,
router7991 < 30000, literal35287 < 100000 and required C0 exponent200012 <
210000. Both exact moment engines and all 47 outer inequalities passed.
The retained bit/bootstrap512 and local192 allowances are unchanged.

All 18 targets in the base Makefile’s `verify` recipe completed. The prepared
environment run stopped at `verify-positive` because a historical compiler
command ignored BOOST_INCLUDE. After adding CPLUS_INCLUDE_PATH and moving
aside that failed generated directory, the final four targets passed,
including all 87 isolated test modules and patch-application checks. This
is staged complete coverage, not a claim that one uninterrupted `make verify`
command exited successfully. `VERIFY-TARGET-COVERAGE.json` and the compressed
logs preserve the exact commands, target inventory and failure distinction.
No source/checker was modified to fix these environment prerequisites.

`T37-REPLAY-SHA256.json` and `BASELINE-REPLAY-SHA256.json` bind all 165 and 484
output files respectively. Selected exact receipts are retained here; the
complete outputs are recreated by the package’s documented commands.
`VENDOR-GIT-CHECK.json` records all 47 byte-identical source files against
their pinned Git objects. Runtime adapters are reconstructed and compared
byte-for-byte with the exposed literal edits during final binding.

The final main refresh was91a2094f2e022930069e8cfdc810a3ea1b81cd09; its selected
κ remains0.001661634653669567. The PR inventory was checked through922.
PR890 advanced from pinned61b71bcf to4b3bd8cb only to extend its CI timeout;
`PR890-HEAD-DELTA.patch` preserves the exact diff. Its construction and κ are
unchanged, so the T37 gain remains1386533459/500000000000000000.

These are finite conditional validation receipts, not an unconditional
multiplication theorem or authenticated execution history. No independent
human review or hosted CI is claimed. All inherited assumptions remain.
Prepared by Tekalign (@tekuuu) with substantial OpenAI Codex assistance.
