# V1 tutorial example

Start with the five reviewed features, including pocket F4, and inspect stock facing from the +Y allowance. This is the simplest example for following a feature from A to the final report.

| Item | Retained example |
| --- | --- |
| Final STEP input | `V1_Part_STEP.stp` |
| Reviewed features | 5 |
| Selected stock, X x Y x Z | 100 x 22 x 70 mm |
| Material | Free machining steel |
| Active operations | 6 |
| Setups | 1 |
| Hosts and routing shares | M-03 (50%), M-04 (50%) |
| Throughput requirement | 2.5 parts/h |
| Recurring cost | EUR 27.1630/part |
| Demonstration simulation | 3 replications of 480 min; variability and downtime enabled |

From the repository root:

```powershell
Expand-Archive -LiteralPath .\examples\V1\project.zip -DestinationPath .\capp_projects\V1_Tutorial
```

Use a new destination, then open **V1 Tutorial Example** in the application.
Steps A-E and a PDF/HTML report are already available. The PDF is stored at
`report/reports/report_20261117T170139540627Z_4b41dbe47549/manufacturing_report.pdf` inside the extracted project.

The raw feature list contains reviewed planner corrections, rather than
uncorrected AAGNet predictions. Geometry enrichment, PMI extraction, stock
selection, operation alternatives, precedence and optimizer inputs were regenerated
with the current code. The accepted five-seed thesis result was reused only after
identical-input verification and independent exact-assignment validation against
the current model. No new optimizer search is claimed.

See the examples guide in the repository for provenance, local regeneration and
the distinction between these demonstration runs and the frozen thesis evidence.
`verification.json` and the accompanying `bundle_manifest.json` record the checks
and file hashes.
