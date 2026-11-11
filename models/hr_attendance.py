from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    check_in_auto = fields.Boolean(copy=True)
    check_out_auto = fields.Boolean(copy=True)
    accounting_company_id = fields.Many2one("res.company", string="Company")
    ot_approved = fields.Boolean(string="OT Approved", copy=True)
    ot_approved_by = fields.Many2one("res.users", string="OT Approved By", copy=True)
    ot_entry = fields.Boolean(string="OT Entry", copy=True)
    over_time = fields.Float(store=False, readonly=True)
