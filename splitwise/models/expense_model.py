# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models

class ExpensesModel(models.Model):
    _name = "expense.model"
    
    name = fields.Char(string = "Name")
    user_ids = fields.Many2many('res.users', string="Users")