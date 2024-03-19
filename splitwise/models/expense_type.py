# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class ExpenseType(models.Model):
    _name='expense.type'
    _description='Type of Expenses'

    name=fields.Char(string="Name", required=True)
