# BugFix-HR — Deferred Items

**Status: EMPTY.** All originally-deferred items either shipped or
permanently skipped as duplicates of standard Odoo bindings.

This file remains as documentation of the arc — see "History of resolved
deferrals" below for the sequence.

---

## Current backlog

None. If new deferrals surface during future work, document them above
this line with the pattern from the resolved section below.

---

## Permanently skipped (v0.0.19-v0.0.22)

Not deferred — actively decided NOT to port because standard Odoo modules
provide identical functionality.

### 4 hr.applicant Action-menu actions (v0.0.20 rollback)
Studio ports were pure code-wrappers calling the same standard methods.
Would have created duplicate menu items. Zero functional loss.
- `3017` Digitize document — hr_recruitment_extract provides binding
- `3152` Refuse — hr_recruitment provides binding
- `3019` Request Signature — hr_recruitment_sign provides binding
- `2933` Send Email — mail / hr_recruitment provides binding

### 3 hr.contract Action-menu actions (skipped without shipping)
Same duplicate-with-standard pattern. Standard bindings already registered
as ir.actions.actions on hr.contract on repair-test-101.
- `1960` Create Salary Attachment — hr_payroll provides binding
- `1531` Index contract(s) — hr_contract/hr_payroll provides binding
- `3090` Signature request — hr_contract_sign provides binding

### 4 hr.applicant + hr.contract cron jobs (skipped without shipping)
Standard-module ir.cron records already exist on repair-test-101 and
invoke the same underlying methods.
- `3014` Recruitment OCR: Update All Status (standard cron 67 exists)
- `3016` Recruitment OCR: Validate CV (standard cron 68 exists)
- `2921` Generate Missing Work Entries (standard cron 51 exists)
- `1264` HR Contract: update state (standard cron 39 exists)

**Lesson learned:** always duplicate-check Studio server actions against
standard-module bindings on target env before shipping. Cost of this
lesson: v0.0.19 push + v0.0.20 rollback for the first 4 hr.applicant
actions before we spotted the pattern.

---

## Followup work on stub compute methods (v0.0.22)

Two of the 3 compute methods ship as stubs returning 0.0 pending
prerequisite ports. Fields work at read/write time (no crashes), but
values are placeholders until real logic lands.

### x_studio_ot_hours on hr.contract (v0.0.22 stub)
- Current: `@api.depends('employee_id')` compute returns 0.0.
- Real formula likely: sum of hr.attendance.x_studio_over_time for the
  contract's employee across the current pay period.
- Un-defer prerequisite: hr.attendance.x_studio_over_time (v0.0.14
  ported as plain unstored Float returning 0) needs its own compute.
  Then adjust _compute_ot_hours to aggregate against attendance records.

### x_studio_paye_tax_amount on hr.contract (v0.0.22 stub)
- Current: `@api.depends('wage', 'structure_type_id', 'employee_id')`
  compute returns 0.0.
- Real formula: Sri Lankan PAYE progressive tax brackets against
  contract.wage.
- Un-defer prerequisite: port x_paye_tax + x_paye_tax_tag Studio-only
  custom models (contain the bracket tables). Then rewrite
  _compute_paye_tax_amount to apply bracket rates.

---

## History of resolved deferrals

- **hr.recruitment.stage x_color field** (v0.0.12) — shipped.
- **Rename + icon** (v0.0.13) — 'Jinasena : Module : HR' branding.
- **hr.attendance 7 fields** (v0.0.14) — shipped.
- **hr.applicant 12 of 15 fields** (v0.0.15) — 12 shipped, 3 CU
  booleans initially deferred. Resolved v0.0.17 with real compute
  methods (env.user matches M2O role field).
- **hr.contract 21 fields** (v0.0.16) — all shipped.
- **View 5550 hr.applicant + View 4930 hr.contract** (v0.0.17) —
  crashed on wage_type xpath anchor (hr_payroll missing from depends).
  Hotfixed v0.0.18. Saved lesson to [[feedback-cross-repo-field-ref]].
- **4 hr.applicant interactive server actions** (v0.0.19 shipped,
  v0.0.20 rolled back) — discovered post-ship they duplicate standard
  bindings. Permanently skipped (see above).
- **7 hr.applicant base_automation records** (v0.0.21) — shipped
  cleanly with proper on_change_field_ids + action_server_ids
  bindings. Includes 6 field-change validators + 1 stage-permission
  guard. RPC-verified.
- **3 compute methods** (v0.0.22) — total_marks REAL compute (sum of
  4 marks); ot_hours + paye_tax_amount STUB computes returning 0.0
  (see "Followup work" above for un-defer prerequisites).

---

## Related memories

- [[feedback-cross-repo-field-ref]] — hr_payroll xpath anchor lesson
  (v0.0.17 crash, same class as BugFix-MRP v0.0.18)
- [[feedback-strict-modifier-sentinels]] — Odoo 17 strict-modifier
  validation
- [[feedback-clear-db-verbatim]] — pin-source verification rule
- Consider a new memory for the "duplicate-with-standard" pattern
  learned from v0.0.19-v0.0.20 rollback (hr.applicant interactive
  actions + hr.contract interactive actions + 4 cron jobs all
  duplicates of standard bindings). Cost: 1 ship + 1 rollback +
  saved 4 other batches from repeating the mistake.
