from odoo import fields, models


class X_update_ot_line_7eea7(models.Model):
    _name = "update_ot_line_7eea7"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Update Ot  Lines"

    name = fields.Char(string="Description", required=True)
    approve_ot = fields.Boolean(string="Approve OT")
    attendance_id = fields.Many2one(
        comodel_name="hr.attendance", string="Attendance Id"
    )
    check_in = fields.Datetime()
    check_out = fields.Datetime()
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee ID")
    sequence = fields.Integer()
    update_ot_id = fields.Many2one(comodel_name="update_ot")


class XUpdateOtLine7eea7Gap(models.Model):
    _inherit = "update_ot_line_7eea7"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Description", required=True)
    update_ot_id = fields.Many2one(comodel_name="update_ot")
