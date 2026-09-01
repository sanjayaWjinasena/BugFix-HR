# BugFix-HR — Deferred Items

Items intentionally not ported. Each entry documents WHY the deferral,
what would need to happen to un-defer, and any current-state observations
so a future session can pick up without re-triaging.

---

## Server actions — hr.applicant (9 total, none ported; 4 permanently skipped)

**All shipped as-is on Clear-DB; not yet ported to data/server_actions.xml.**

### PERMANENTLY SKIPPED (v0.0.20 rollback of v0.0.19)
Standard Odoo modules already provide identical Action menu bindings on
hr.applicant. Studio versions were pure code-wrappers calling the same
standard methods -- porting them created duplicate menu items. Skipped
for UX reasons; no functional loss.
- `3017` Digitize document -> hr_recruitment_extract provides identical binding
- `3152` Refuse -> hr_recruitment provides identical binding
- `3019` Request Signature -> hr_recruitment_sign provides identical binding
- `2933` Send Email -> mail / hr_recruitment provides identical binding

### Base automations (usage=base_automation)
- `2579` HR - Applicant
- `2580` HR - Applicant 2
- `2581` HR - Validate Recruiter Marks
- `2582` HR - Validate Line Manager Marks
- `2583` HR - Validate Leadership Marks
- `2584` HR - Validate Assignment Marks
- `1522` HR - Validate Stages

### Cron jobs (usage=ir_cron)
- `3014` Recruitment OCR: Update All Status
- `3016` Recruitment OCR: Validate CV

**Un-defer approach:**
1. RPC-dump each action's `code` + trigger config (base.automation records).
2. Port base_automation triggers with `<field name="action_server_ids"
   eval="[(6, 0, [ref('server_action_NNNN_...')])]"/>` binding.
3. Port cron jobs last (ir.cron records + xmlids).

**Sizing:** 7 base_automation = medium batch. 2 cron = small batch.
Total 2 versions to close out (interactive category permanently skipped
per v0.0.20 rollback).

---

## Server actions — hr.contract (5 total, none ported)

**All shipped as-is on Clear-DB; not yet ported to data/server_actions.xml.**

### Interactive (usage=ir_actions_server)
- `1960` Create Salary Attachment
- `1531` Index contract(s)
- `3090` Signature request

### Cron jobs (usage=ir_cron)
- `2921` Generate Missing Work Entries
- `1264` HR Contract: update state

**Un-defer approach:** same as hr.applicant. Small batch total.

---

## Compute methods — return 0.0 / manual entry

Three x_studio_ Float fields declared with proper Studio-original store
semantics but with placeholder compute logic (no compute method or
plain stored Float). Ship as-is but real values need real compute logic
to work.

### x_studio_total_marks on hr.applicant (v0.0.15)
- Studio: store=True with depends on 4 marks fields.
- Shipped as: plain stored Float. User enters manually or automation
  populates via base_automation trigger.
- **Real compute** likely: weighted or simple sum of the 4 marks.
  Formula unknown — visual builder didn't expose it. To un-defer,
  read the Clear-DB base.automation record that computes this
  (if any), or ask the customer for the weighting.

### x_studio_ot_hours on hr.contract (v0.0.16)
- Studio: store=False with depends=employee_id.
- Shipped as: plain unstored Float returning 0.0.
- **Real compute** likely: sum of hr.attendance x_studio_over_time
  for this contract's employee across the current pay period.
- To un-defer, port the OT calculation logic (probably lives in one
  of the deferred base_automation records above).

### x_studio_paye_tax_amount on hr.contract (v0.0.16)
- Studio: store=False with depends=wage,structure_type_id,employee_id.
- Shipped as: plain unstored Float returning 0.0.
- **Real compute** likely: PAYE (Pay As You Earn) tax calc from
  Sri Lankan salary tax brackets. Requires x_paye_tax + x_paye_tax_tag
  custom models (Clear-DB has these but they're pinned to
  studio_customization, no Python port yet).
- To un-defer, port those 2 custom models first, then add compute.

---

## History of resolved deferrals

- **hr.recruitment.stage x_color field** (v0.0.12) — shipped.
- **hr.attendance 7 fields** (v0.0.14) — shipped.
- **hr.applicant 12 of 15 fields** (v0.0.15) — 12 shipped, 3 CU
  booleans initially deferred with "Studio quirk depends=<self>"
  scope-question. Resolved v0.0.17 with real compute methods
  (env.user matches M2O role field). RPC-verified working.
- **hr.contract 21 fields** (v0.0.16) — all shipped.
- **View 5550 hr.applicant form + view 4930 hr.contract form** —
  deferred through v0.0.15/v0.0.16 pending CU compute methods +
  field ports respectively. Both shipped v0.0.17. v0.0.17 install
  crashed on wage_type xpath anchor (hr_payroll missing from
  depends chain). Hotfixed v0.0.18 by adding hr_payroll dep.
  Saved lesson to [[feedback-cross-repo-field-ref]].

---

## Related memories

- [[feedback-cross-repo-field-ref]] — hr_payroll xpath anchor lesson
  (v0.0.17 crash pattern, same as BugFix-MRP v0.0.18)
- [[feedback-strict-modifier-sentinels]] — Odoo 17 strict-modifier
  validation (used in earlier BugFix-MRP + BugFix-Stock work; hr views
  didn't need sentinels since all modifier refs were declared as fields)
- [[feedback-clear-db-verbatim]] — "always verify pin source" rule
