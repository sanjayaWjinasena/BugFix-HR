# -*- coding: utf-8 -*-
from odoo import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    # === Identity / naming (3 Char) ===
    x_studio_initial = fields.Char(string='Initial', copy=True)
    x_studio_surname = fields.Char(string='Surname', copy=True)
    x_studio_occupation_grade = fields.Char(string='Occupation Grade', copy=True)

    # === Monetary compensation fields (7) ===
    x_studio_ex_gratia = fields.Monetary(string='Ex-gratia', copy=True)
    x_studio_gbud_a = fields.Monetary(string='Government Budget A', copy=True)
    x_studio_gbud_l2 = fields.Monetary(string='Government Budget L2', copy=True)
    x_studio_government_budget_a = fields.Monetary(string='Government Budget A', copy=True)  # duplicate label - Studio quirk
    x_studio_standing_order_1 = fields.Monetary(string='Standing Order 1', copy=True)
    x_studio_std_ord2 = fields.Monetary(string='Standing Order 2', copy=True)
    x_studio_travelling_allowance = fields.Monetary(string='Travelling Allowance', copy=True)

    # === OT + Payroll computed/stored (3 Float) ===
    x_studio_ot_rate = fields.Float(string='OT Rate', copy=True)
    # Studio declared these as store=False with depends but no compute method.
    # Shipped as plain unstored Float (returns 0.0). Real compute logic
    # (OT hours from attendance, PAYE tax from wage/structure) needs
    # follow-up implementation.
    x_studio_ot_hours = fields.Float(string='OT Hours', store=False, readonly=True)
    x_studio_paye_tax_amount = fields.Float(string='Paye Tax Amount', store=False, readonly=True)

    # === "New Related Field" placeholders (8) ===
    # Studio created these via the "New Related Field" widget but the
    # user never configured a related= target. Shipped verbatim as
    # plain Char/M2O/Integer without related= -- accept manual input
    # for stored variants, always empty for unstored. Preserved for
    # data-copy fidelity from Clear-DB.
    x_studio_related_field_Dj7xv = fields.Many2one('account.journal', string='New Related Field', store=False, ondelete='set null')
    x_studio_related_field_Q8TCb = fields.Char(string='New Related Field')
    x_studio_related_field_SFy8j = fields.Integer(string='New Related Field')
    x_studio_related_field_a17Kz = fields.Char(string='New Related Field')
    x_studio_related_field_hYOxU = fields.Char(string='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    x_studio_related_field_l45bF = fields.Char(string='New Related Field', store=False, readonly=True)
    x_studio_related_field_rE5UU = fields.Char(string='New Related Field', store=False, readonly=True)
    x_studio_related_field_w5zlV = fields.Char(string='New Related Field', store=False, readonly=True)
