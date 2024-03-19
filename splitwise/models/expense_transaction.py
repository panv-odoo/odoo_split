# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class ExpenseTransaction(models.Model):
    _name='expense.transaction'
    _description='Transactions'

    expense_id = fields.Many2one('expense.model')
    from_id = fields.Many2one('res.users', string='From')
    to_id = fields.Many2one('res.users', string='To')
    amount = fields.Float(string='Amount')
    state = fields.Selection(
        string='State',
        selection=[('paid', 'Paid'), ('pending', 'Pending')],
    )
    is_group_expense = fields.Boolean()
