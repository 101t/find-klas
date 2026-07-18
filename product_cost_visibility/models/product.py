from odoo import fields, models

COST_GROUP = 'product_cost_visibility.group_product_cost_visibility'


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Field-level security: restrict the Cost field to the "Show Product Cost"
    # group. Redeclaring the field with only ``groups`` set keeps every other
    # attribute (company_dependent, digits, ...) inherited from core. This
    # removes the field from ALL views, exports and read-based reports for
    # users who are not in the group, not just the product form.
    standard_price = fields.Float(groups=COST_GROUP)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    standard_price = fields.Float(groups=COST_GROUP)
