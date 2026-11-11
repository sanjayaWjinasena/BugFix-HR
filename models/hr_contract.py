from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    # === Identity / naming (3 Char) ===
    initial = fields.Char(copy=True)
    surname = fields.Char(copy=True)
    occupation_grade = fields.Char(copy=True)

    # === Monetary compensation fields (7) ===
    ex_gratia = fields.Monetary(string="Ex-gratia", copy=True)
    gbud_a = fields.Monetary(string="Government Budget A", copy=True)
    gbud_l2 = fields.Monetary(string="Government Budget L2", copy=True)
    government_budget_a = fields.Monetary(copy=True)  # duplicate label - Studio quirk
    standing_order_1 = fields.Monetary(copy=True)
    std_ord2 = fields.Monetary(string="Standing Order 2", copy=True)
    travelling_allowance = fields.Monetary(copy=True)
    special_allowance = fields.Monetary(copy=True)
    production_incentive = fields.Monetary(copy=True)
    asian_alliance_insurance = fields.Monetary(copy=True)
    union_insurance = fields.Monetary(copy=True)

    # === OT + Payroll computed/stored (3 Float) ===
    ot_rate = fields.Float(string="OT Rate", copy=True)

    # STUB COMPUTE: returns 0.0. Real logic needs hr.attendance
    # over_time to have a compute of its own (currently also
    # returns 0 - unstored placeholder). Shape of the real compute is
    # likely: sum(hr.attendance.over_time) for the contract's
    # employee across the current pay period. See docs/DEFERRED.md.
    ot_hours = fields.Float(string="OT Hours", store=False, compute="_compute_ot_hours")

    # v0.0.49: Clear-DB Studio compute ported (bug sheet 16/Oct, Chandika: PAYE always 0).
    # gross = wage + the contract's default salary structure's non-code Allowance (ALW)
    # rules; the PAYE amount is the paye_tax slab whose from/to range contains gross.
    # Needs the paye_tax slab records (data) to return anything but 0.
    paye_tax_amount = fields.Float(store=False, compute="_compute_paye_tax_amount")

    @api.depends("employee_id")
    def _compute_ot_hours(self):
        for rec in self:
            rec.ot_hours = 0.0

    @api.depends("wage", "structure_type_id", "employee_id")
    def _compute_paye_tax_amount(self):
        PayeTax = self.env["paye_tax"]
        for rec in self:
            tot_rule = 0.0
            paye_tax = 0.0
            salary_structure = rec.structure_type_id.default_struct_id
            if salary_structure:
                # Clear-DB filters category_id = 2, which is Allowance (code ALW) on both databases.
                rules = self.env["hr.salary.rule"].search(
                    [
                        ("struct_id", "=", salary_structure.id),
                        ("category_id.code", "=", "ALW"),
                        ("amount_select", "!=", "code"),
                    ]
                )
                if rules:
                    localdict = dict(employee=rec.employee_id, contract=rec)
                    for rule in rules:
                        localdict["result"] = None
                        localdict["result_qty"] = 1.0
                        localdict["result_rate"] = 100
                        if rule._satisfy_condition(localdict):
                            amount, qty, rate = rule._compute_rule(localdict)
                            tot_rule += amount * qty * rate / 100.0
            gross = rec.wage + tot_rule
            slab = PayeTax.search(
                [
                    ("from_value", "<=", gross),
                    ("to_value", ">=", gross),
                ],
                limit=1,
            )
            if slab:
                paye_tax = slab.tax_amount
            rec.paye_tax_amount = paye_tax

    # === "New Related Field" placeholders (8) ===
    # Studio created these via the "New Related Field" widget but the
    # user never configured a related= target. Shipped verbatim as
    # plain Char/M2O/Integer without related= -- accept manual input
    # for stored variants, always empty for unstored. Preserved for
    # data-copy fidelity from Clear-DB.
    related_field_Dj7xv = fields.Many2one(
        "account.journal", string="New Related Field", store=False, ondelete="set null"
    )
    related_field_Q8TCb = fields.Char(string="New Related Field")
    related_field_SFy8j = fields.Integer(string="New Related Field")
    related_field_a17Kz = fields.Char(string="New Related Field")
    related_field_hYOxU = fields.Char(
        string="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    related_field_l45bF = fields.Char(
        string="New Related Field", store=False, readonly=True
    )
    related_field_rE5UU = fields.Char(
        string="New Related Field", store=False, readonly=True
    )
    related_field_w5zlV = fields.Char(
        string="New Related Field", store=False, readonly=True
    )
