from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    employee_rate = fields.Float(string="Employee Rate")
    epf_no = fields.Char(string="EPF No")
    etf_no = fields.Char(string="ETF No")
    occupation_code = fields.Char(string="Occupation Code")
    ot_hours = fields.Float(string="OT Hours", readonly=True, store=False)
    ot_hours_month_display = fields.Char(string="New Text")
    ot_month = fields.Float(string="OT Hours (month)", readonly=True)
    ot_month_display = fields.Char(
        string="OT Hours (month) Display", readonly=True, store=False
    )
    ot_rate = fields.Float(string="OT Rate")
    purpose_code = fields.Char(string="Purpose Code")
