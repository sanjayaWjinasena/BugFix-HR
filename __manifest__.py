# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : HR',
    'version': '17.0.0.0.34',
    'summary': 'Studio-to-Python port for BugFix-HR',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.24: 3 remaining Studio views (the audit gap).
    #   * views/hr_employee_studio_ported.xml: view 4929 (form, 721b).
    #     Adds 8 x_studio_ fields to hr.employee form. All fields
    #     pre-existing in models/hr_employee.py.
    #   * views/hr_expense_studio_ported.xml: view 4949 (form, 1185b).
    #     Attribute-only overrides on 5 base hr.expense fields. Zero
    #     field ports. NEW DEP: hr_expense.
    #   * views/hr_payslip_studio_ported.xml: view 9511 (tree, 552b).
    #     Reorders 2 x_dest_* columns via xpath position='move'. Zero
    #     field ports (all x_dest_* fields owned by bank-data module).
    #     NEW DEP: bank-data.
    # Closes the last audit gap. All 9 Studio priority-99 views on hr.*
    # models now landed (6 as BugFix-HR ports + 2 by standard hr_job +
    # 1 by earlier v0.0.12 port). HR migration substantively complete.
    # v0.0.23: hotfix for v0.0.21 server-action names.
    # Comprehensive HR migration audit discovered that the 7 server
    # actions shipped in v0.0.21 all had their `name` field overwritten
    # to 'Execute Code' by Odoo internal logic (likely _onchange_state
    # or base.automation side-effect at action_server_ids binding time).
    # Records were functional (base.automations triggered correct code)
    # but harder to identify in the backend server-actions list.
    # Fix: 7 <function> tags at end of data/automations.xml force-write
    # the intended names AFTER all base.automation records are created.
    # Idempotent on upgrade.
    # v0.0.22: compute methods for 3 unstored Float fields.
    #   * x_studio_total_marks on hr.applicant: REAL compute -- simple sum
    #     of the 4 mark percentages (matches Studio's depends declaration).
    #     Was plain stored Float in v0.0.15; now computed+stored so it
    #     auto-recalculates on marks-field changes. View 5550 displays it
    #     with widget='progressbar' (max useful = 400).
    #   * x_studio_ot_hours on hr.contract: STUB compute returning 0.0.
    #     Real logic depends on hr.attendance.x_studio_over_time having
    #     its own compute (currently also 0). Depends on employee_id.
    #   * x_studio_paye_tax_amount on hr.contract: STUB compute returning
    #     0.0. Real logic needs Sri Lankan PAYE tax brackets via
    #     x_paye_tax + x_paye_tax_tag custom models (Studio-only, not
    #     ported). Depends on wage/structure_type_id/employee_id.
    # Both stubs are documented in-code and in DEFERRED.md with the
    # prerequisite chain to un-defer.
    # v0.0.21: 7 hr.applicant base_automation records + backing server actions.
    # These fire on field-change (6) or create-or-write (1) triggers and
    # implement custom validation/workflow logic that is NOT provided by
    # standard modules (unlike v0.0.19's interactive actions which were
    # rolled back as duplicates).
    #   * 262 HR - Applicant             on_change x_studio_priority
    #                                     -> if 'No', set stage_id=1
    #   * 263 HR - Applicant 2           on_change x_studio_2nd_selection
    #                                     -> if 'Yes', set stage_id=0 (Studio bug preserved)
    #   * 264 Validate Recruiter Marks   on_change x_studio_interview_marks_3
    #                                     -> raise if >100
    #   * 265 Validate Line Manager Marks on_change x_studio_interview_marks_1
    #                                     -> raise if >100
    #   * 266 Validate Leadership Marks  on_change x_studio_interview_marks_2
    #                                     -> raise if >100
    #   * 267 Validate Assignment Marks  on_change x_studio_marks_1
    #                                     -> raise if >100
    #   * 93  Validate Stages            on_create_or_write
    #                                     -> check env.user has x_studio_recr_stages
    #                                        permission for the stage being set
    # Uses ref='BugFix-HR.field_hr_applicant__X' to bind on_change_field_ids
    # cleanly (xmlids from v0.0.15 field port).
    # Action 93 references res.users.x_studio_recr_stages (M2M pinned to
    # studio_usermodel_migration on target env) -- runtime-safe due to
    # state=code lazy eval.
    # v0.0.20: ROLLBACK of v0.0.19's 4 hr.applicant Action-menu server
    # actions (Digitize, Refuse, Request Signature, Send Email).
    # Discovered post-ship that standard Odoo modules already provide
    # identical Action menu bindings on hr.applicant:
    #   * Digitize -> hr_recruitment_extract
    #   * Refuse -> hr_recruitment
    #   * Request Signature -> hr_recruitment_sign
    #   * Send Email -> mail / hr_recruitment
    # Studio versions were pure code-wrappers calling the same standard
    # methods. Landing them created duplicate menu items (2 of each).
    # data/server_actions.xml reverted to empty stub. DEFERRED.md updated
    # to remove these 4 from the deferred list -- they are permanently
    # skipped, not deferred.
    # v0.0.19: 4 interactive hr.applicant server actions (usage=ir_actions_server,
    # binding_model_id=hr.applicant, binding_type=action - appear in Action menu):
    #   * 3017 Digitize document -> records.action_send_batch_for_digitization()
    #   * 3152 Refuse            -> records.archive_applicant()
    #   * 3019 Request Signature -> records._send_applicant_sign_request()
    #   * 2933 Send Email        -> records.action_send_email()
    # All 4 install-safe (state=code lazy eval). Runtime failures possible
    # if underlying methods unavailable (hr_recruitment_extract for OCR,
    # hr_recruitment_sign for signature). Documented in server_actions.xml
    # header comment.
    # v0.0.18: hotfix for v0.0.17 install failure.
    # ParseError: Element '<xpath expr="//field[@name='wage_type']">' cannot
    # be located in parent view. views/hr_contract_studio_ported.xml line 17.
    # Root cause: wage_type field on hr.contract is owned by hr_payroll,
    # not the base hr_contract module. Same class of failure as MRP v0.0.18
    # (see memory feedback-cross-repo-field-ref). hr_payroll IS installed
    # on repair-test-101 but wasn't in our depends chain, so at install-
    # time arch composition the wage_type xpath anchor was absent.
    # Fix: add hr_payroll to depends. yearly_benefits group also comes
    # from hr_payroll (both anchors used in view 4930).
    # v0.0.17: 2 Studio views + 3 CU boolean compute methods.
    #   * models/hr_applicant.py: 3 new store=False computed booleans
    #     (x_studio_cu_line_manager, x_studio_cu_leadership, x_studio_cu_recruiter)
    #     each with @api.depends on the corresponding M2O role field.
    #     Compute logic: rec.cu_X = (rec.x_studio_X_name == env.user).
    #     Re-evaluates per user session (env.user changes).
    #   * views/hr_contract_studio_ported.xml: view 4930 (form extension,
    #     785b). 12 fields into 3 groups (identity/payroll/benefits).
    #     Zero missing refs, zero sentinels needed.
    #   * views/hr_applicant_studio_ported.xml: view 5550 (form extension,
    #     ~1718b). Recruitment scoring UI with CU-gated readonly. Uses
    #     xpath position="move" to reposition user_id + attribute overrides.
    # NEW DEPS added for proper fresh-install load order:
    #   * hr_contract (view 4930 inherits hr_contract.hr_contract_view_form)
    #   * hr_attendance (v0.0.14 shipped hr.attendance fields without this
    #     dep - retroactively added for fresh-install correctness).
    # v0.0.16: hr.contract port - all 21 x_studio_ fields, no view/actions.
    # See models/hr_contract.py. Fields split:
    #   * 3 Char identity: x_studio_initial, x_studio_surname, x_studio_occupation_grade
    #   * 7 Monetary compensation: x_studio_ex_gratia, x_studio_gbud_a,
    #     x_studio_gbud_l2, x_studio_government_budget_a (duplicate label
    #     with gbud_a - Studio quirk preserved), x_studio_standing_order_1,
    #     x_studio_std_ord2, x_studio_travelling_allowance
    #   * 1 Float stored: x_studio_ot_rate
    #   * 2 Float unstored (Studio compute w/o method - ship as plain
    #     unstored Float returning 0.0): x_studio_ot_hours (depends=employee_id),
    #     x_studio_paye_tax_amount (depends=wage,structure_type_id,employee_id).
    #     Real compute logic (OT from attendance, PAYE from wage/structure)
    #     needs follow-up.
    #   * 8 "New Related Field" placeholders (x_studio_related_field_XXXXX):
    #     Studio artifacts with no `related=` configured. Shipped verbatim
    #     as plain Char/M2O/Integer for data-copy fidelity.
    # NOT shipped this version:
    #   * View 4930 (form extension, 785b - uses 5 of the 21 fields).
    #   * 5 server actions: Create Salary Attachment (interactive),
    #     Index contract(s) (interactive), Signature request (interactive),
    #     Generate Missing Work Entries (cron), HR Contract update state (cron).
    # v0.0.15: hr.applicant port - 12 of 15 x_studio_ fields.
    # See models/hr_applicant.py. Fields shipped:
    #   * 3 selections: x_studio_priority (Line Manager),
    #     x_studio_2nd_selection (Leadership), x_studio_appreciation
    #   * 4 integer mark percentages: x_studio_marks_1,
    #     x_studio_interview_marks_1/2/3
    #   * 1 float x_studio_total_marks (Studio declared computed/stored
    #     but no visible compute method - shipped as plain stored Float)
    #   * 4 M2O approver roles: x_studio_recruiter (res.users),
    #     x_studio_line_manager_name, x_studio_leadership_name,
    #     x_studio_hr_responsible (hr.employee)
    # DEFERRED: 3 x_studio_cu_* current-user permission booleans and
    # view 5550 (uses those booleans as readonly gates). Need to write
    # a proper compute method matching current user against the M2O
    # role fields. Documented inline in models/hr_applicant.py.
    # Also NOT shipped this version: 13 server actions on hr.applicant
    # (mix of automations + interactive + cron - Digitize document, OCR
    # validation, Refuse, Request Signature, Send Email, plus 6
    # base_automation validators). Port in follow-up versions.
    # v0.0.14: hr.attendance port - 7 x_studio_ fields, 0 views.
    # See models/hr_attendance.py. All fields declared from Clear-DB scout:
    #   * x_studio_check_in_auto     (Boolean, copy=True)
    #   * x_studio_check_out_auto    (Boolean, copy=True)
    #   * x_studio_company_id        (M2O -> res.company)
    #   * x_studio_ot_approved       (Boolean, copy=True)
    #   * x_studio_ot_approved_by    (M2O -> res.users, copy=True)
    #   * x_studio_ot_entry          (Boolean, copy=True)
    #   * x_studio_over_time         (Float, store=False, readonly=True)
    # Zero Studio views on hr.attendance -- the empty stub file
    # views/hr_attendance_studio_ported.xml is intentionally left as-is.
    # No new deps (hr_attendance already in dep chain).
    # v0.0.13: rename 'BugFix - HR' -> 'Jinasena : Module : HR' + add
    # module icon (static/description/icon.png). Matches the branding
    # pattern used by BugFix-MRP + other Jinasena_* modules.
    # v0.0.12: hr.recruitment.stage port (1 field + 1 view). First
    # substantive add after the v0.0.9-v0.0.11 CRITICAL strip cycle.
    #   * NEW DEP hr_recruitment (was stripped in v0.0.11 CRITICAL).
    #     Required for hr.recruitment.stage model + the base view
    #     we inherit (hr_recruitment.hr_recruitment_stage_tree).
    #   * models/hr_recruitment_stage.py: x_color Integer field.
    #     Clear-DB pin: hr_recruitment.field_hr_recruitment_stage__x_color
    #     (studio_customization is the secondary pin). state=manual on
    #     Clear-DB, will be state=base after our port.
    #   * views/hr_recruitment_stage_studio_ported.xml: Studio view 5549
    #     (tree inherit, 90b). Adds `id` column after `hired_stage`.
    #     Independent of the x_color field port -- the view doesn't
    #     reference x_color at all.
    # Smallest hr.* port in the audit -- used to kick off a rebuild
    # of BugFix-HR after the strip cycle.
    'depends': ['base_setup', 'hr', 'hr_attendance', 'hr_contract', 'hr_expense', 'hr_payroll', 'hr_recruitment', 'bank-data', 'base_automation'],
    'data': [
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'reports/reports.xml',
        'views/hr_recruitment_stage_studio_ported.xml',
        'views/hr_contract_studio_ported.xml',
        'views/hr_applicant_studio_ported.xml',
        'views/hr_employee_studio_ported.xml',
        'views/hr_expense_studio_ported.xml',
        'views/hr_payslip_studio_ported.xml',
        'data/record_rules.xml',
        'data/server_actions_backlog.xml',
        'data/automations_backlog.xml',
        'data/window_actions_backlog.xml',
        'data/menus_from_routing.xml',
        'data/gap_automations.xml',
        'data/record_rules_gap.xml',
        'data/server_actions_gap.xml',
        'data/window_actions_gap.xml',
        'data/ir_defaults_gap.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}