from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_cost_user_ids = fields.Many2many(
        comodel_name='res.users',
        string='Users Allowed to See Product Cost',
        compute='_compute_product_cost_user_ids',
        readonly=False,
        store=False,
        help="Users selected here are allowed to see the Cost field on the "
             "product screen. Anyone not listed will not see it.",
    )

    def _get_cost_group(self):
        return self.env.ref(
            'product_cost_visibility.group_product_cost_visibility',
            raise_if_not_found=False,
        )

    @api.depends('company_id')
    def _compute_product_cost_user_ids(self):
        group = self._get_cost_group()
        for setting in self:
            setting.product_cost_user_ids = group.users if group else False

    def set_values(self):
        super().set_values()
        group = self._get_cost_group()
        if group:
            group.sudo().users = [(6, 0, self.product_cost_user_ids.ids)]
