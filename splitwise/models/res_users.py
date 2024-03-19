#  -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.Many2many(
        comodel_name="expence.groups", string="Properties")
