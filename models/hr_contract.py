# -*- coding: utf-8 -*-
from odoo import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    x_studio_ex_gratia = fields.Float(string='Ex-gratia')  # was Monetary (no currency_field)
    x_studio_gbud_a = fields.Float(string='Government Budget A')  # was Monetary (no currency_field)
    x_studio_gbud_l2 = fields.Float(string='Government Budget L2')  # was Monetary (no currency_field)
    x_studio_government_budget_a = fields.Float(string='Government Budget A')  # was Monetary (no currency_field)
    x_studio_initial = fields.Char(string='Initial')
    x_studio_occupation_grade = fields.Char(string='Occupation Grade')
    x_studio_ot_hours = fields.Float(string='OT Hours', readonly=True, store=False)
    x_studio_ot_rate = fields.Float(string='OT Rate')
    x_studio_paye_tax_amount = fields.Float(string='Paye Tax Amount', readonly=True, store=False)
    x_studio_related_field_Dj7xv = fields.Many2one('account.journal', string='New Related Field', readonly=True, store=False)
    x_studio_related_field_Q8TCb = fields.Char(string='New Related Field', readonly=True)
    x_studio_related_field_SFy8j = fields.Integer(string='New Related Field', readonly=True)
    x_studio_related_field_a17Kz = fields.Char(string='New Related Field', readonly=True)
    x_studio_related_field_hYOxU = fields.Char(string='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', readonly=True)
    x_studio_related_field_l45bF = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_rE5UU = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_w5zlV = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_standing_order_1 = fields.Float(string='Standing Order 1')  # was Monetary (no currency_field)
    x_studio_std_ord2 = fields.Float(string='Standing Order 2')  # was Monetary (no currency_field)
    x_studio_surname = fields.Char(string='Surname')
    x_studio_travelling_allowance = fields.Float(string='Travelling Allowance')  # was Monetary (no currency_field)