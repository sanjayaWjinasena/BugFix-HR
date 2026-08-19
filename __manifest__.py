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
    'depends': ['base_setup', 'hr'],
    'data': [
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'reports/reports.xml',
        'views/hr_expense_approve_duplicate_studio_ported.xml',
        'views/hr_expense_studio_ported.xml',
        'views/hr_expense_refuse_wizard_studio_ported.xml',
        'views/hr_expense_sheet_studio_ported.xml',
        'views/hr_applicant_studio_ported.xml',
        'views/hr_contract_studio_ported.xml',
        'views/hr_employee_studio_ported.xml',
        'views/hr_job_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}