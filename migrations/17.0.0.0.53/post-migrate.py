from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["hr.payroll.structure"]._bugfix_hr_setup_workers_payroll()
