# -*- coding: utf-8 -*-
from odoo import fields, models


class HrExpenseApproveDuplicate(models.TransientModel):
    _inherit = 'hr.expense.approve.duplicate'

