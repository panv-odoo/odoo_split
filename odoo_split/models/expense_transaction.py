from odoo import models, fields

class EstatePropertyType(models.Model):
    _name='expense.transaction'
    _description='Transactions'
    
    expense_id = fields.Many2one('odoo_split.expense')
    from_id = fields.Many2one('res.users', string='From')
    to_id = fields.Many2one('res.users', string='To')
    amount = fields.Float(string='Amount')
    state = fields.Selection(
        string='State',
        selection=[('paid', 'Paid'), ('pending', 'Pending')],
    )
    is_group_expense = fields.Boolean()
