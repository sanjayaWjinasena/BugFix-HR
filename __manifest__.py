# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : HR',
    'version': '17.0.0.0.15',
    'summary': 'Studio-to-Python port for BugFix-HR',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
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
    'depends': ['base_setup', 'hr', 'hr_recruitment'],
    'data': [
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'reports/reports.xml',
        'views/hr_recruitment_stage_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}