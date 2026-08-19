# -*- coding: utf-8 -*-
{
    'name': 'BugFix - HR',
    'version': '17.0.0.0.11',
    'summary': 'Studio-to-Python port for BugFix-HR',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    'depends': ['base_setup', 'hr', 'hr_contract', 'hr_expense', 'hr_recruitment'],
    'data': [
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'reports/reports.xml',
        'views/hr_contract_studio_ported.xml',
        'views/hr_employee_studio_ported.xml',
        'views/hr_job_studio_ported.xml',
        'views/hr_payslip_studio_ported.xml',
        'views/hr_recruitment_stage_studio_ported.xml',
        'views/hr_attendance_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}