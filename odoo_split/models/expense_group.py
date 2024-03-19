from odoo import models, fields

class ExpenseGroup(models.Model):
    _name='expense.group'
    _description='Group'

    name=fields.Char(string="Group Name", required=True)
    member_ids = fields.Many2many('res.users', string="Members")
    group_transaction_ids = fields.One2many('expense.group.transaction', 'group_id')
