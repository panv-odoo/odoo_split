from odoo import models, fields

class ExpenseTransaction(models.Model):
    _name='expense.transaction'
    _description='Transactions'
    
    expense_id = fields.Many2one('expense.group.transaction')
    from_id = fields.Many2one('res.users', string='From')
    to_id = fields.Many2one('res.users', string='To')
    amount = fields.Float(string='Amount')
    state = fields.Selection(
        string='State',
        selection=[('paid', 'Paid'), ('pending', 'Pending')],
    )
