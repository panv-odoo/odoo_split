
from odoo import models, fields

class ExpenseTransaction(models.Model):
    _name='expense.transaction'
    _description='Expense'
    
    # expense_id = fields.Many2one('expense.group.transaction')
    payor_id = fields.Many2one('res.users', string='Payor', required=True)
    payee_id = fields.Many2one('res.users', string='Payee', required=True)
    amount = fields.Float(string='Amount', required=True)
    state = fields.Selection(
        string='State',
        selection=[('paid', 'Paid'), ('pending', 'Pending')],
        default="pending"
    )
    is_group_expense = fields.Boolean()
