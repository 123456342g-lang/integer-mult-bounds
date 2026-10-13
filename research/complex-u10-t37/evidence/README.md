# Retained arithmetic evidence

`ALL-T-BOUND.json` is the U10 all-replica bound (independent/all_t_bound.py). `u10/` holds the
U10 construction receipts (audit_local, 14 controls, 95 end controls, native chain). The strict
U10/T37 assembly receipt will be added after the cold replay completes.

They are review snapshots, not verifier inputs. Run the package verifier to
rebuild ancestry, U8, ownership, the emitted controller, invoice and binding
receipts. The verifier does not substitute these snapshots for computation.
Generated artifact hashes can vary with compression and runtime paths; compare
proof-relevant profiles, exact rational endpoints and inequalities, not unrelated
container metadata. Committed source files retain exact byte pins.

The default CI rebuilds the complete chain on Python 3.11 and 3.14. Local replay
success does not imply a hosted CI result or an unconditional theorem proof.
