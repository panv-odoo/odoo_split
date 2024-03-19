#  -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class SplitwiseGroups(models.Model):
    _name = "splitwise.groups"
    _description = "RD Task"

    name = fields.Char(string="Group Title", required=True)

    member_ids = fields.Many2many(comodel_name='res.users', string="Members", domain="[('groups_id','in',[1])]")
