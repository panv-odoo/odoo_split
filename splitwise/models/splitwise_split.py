#  -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class SplitwiseSplit(models.Model):
    _name = "splitwise.split"
    _description = "RD Task"

    name = fields.Char(string="Transaction")
    
