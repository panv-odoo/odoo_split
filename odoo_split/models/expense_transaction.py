from odoo import models, fields

class ExpenseTransaction(models.Model):
    _name='expense.transaction'
    _description='Transactions'
    

    payer = fields.Many2one('res.users', required=True, string='Payer')
    payee = fields.Many2one('res.users', required=True, string='Payee')
    amount = fields.Float(required=True)
    date = fields.Date(required=True)
    expense_id = fields.Many2one('expense.group.transaction')
    group_id = fields.Many2one('expense.group', string='Group')
    state = fields.Selection(
        string='State',
        selection=[('paid', 'Paid'), ('pending', 'Pending')],
    )
