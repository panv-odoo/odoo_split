from odoo import models, fields, api
from . import expense_transaction
class ExpenseGroupTransaction(models.Model):
    _name='expense.group.transaction'
    _description='Group Transactions'
    
    transaction_date = fields.Date(string='Date of Transaction', copy=False, default=fields.Date.today())
    transaction_ids = fields.One2many('expense.transaction', 'expense_id')
    expense_types = fields.Many2one('expense.type', string="Type of Expense")
    amount = fields.Float(required=True)
    payer = fields.Many2one('res.users', required=True, string='Payer', default=lambda self: self.env.user, readonly=True)
    split_type = fields.Selection([('equally', 'Equally'), ('custom', 'Custom')], default='equally')
    description = fields.Text(string="Description", required=True)
    group_id = fields.Many2one('expense.group', required=True, string='Group')
    payee_ids = fields.Many2many('res.users', string="With you and: ", compute='_compute_payee_ids', store=True)

    @api.depends('group_id')
    def _compute_payee_ids(self):
        for expense in self:
            expense.payee_ids = expense.group_id.member_ids

    @api.model
    def create(self, values):
        expense_group_transaction = super(ExpenseGroupTransaction, self).create(values)
        expense_group_transaction.create_transactions()
        return expense_group_transaction

    def create_transactions(self):
        for expense in self:
            amount_per_user = expense.amount / len(expense.payee_ids)
            for payee in expense.payee_ids:
                self.env['expense.transaction'].create({
                    'payer': expense.payer.id,
                    'payee': payee.id,
                    'amount': amount_per_user,
                    'date': fields.Date.today(),
                    'expense_id': expense.id,
                    'group_id': expense.group_id.id,
                })