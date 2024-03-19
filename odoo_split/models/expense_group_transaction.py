from odoo import models, fields, api

class ExpenseGroupTransaction(models.Model):
    _name='expense.group.transaction'
    _description='Group Transactions'
    
    group_id = fields.Many2one('expense.group', required=True)
    # payee_group_ids = fields.Many2many('res.users', related='group_id.member_ids')
    payee_ids = fields.Many2many('res.users', string="With you and: ")
    payer = fields.Many2one('res.users', required=True, string='Payer', default=lambda self: self.env.user, readonly=True)
    total_amount = fields.Float(string="Split Amount", required=True)
    description = fields.Text(string="Description", required=True)
    expense_types = fields.Many2one('expense.type', string="Type of Expense")
    transaction_date = fields.Date(string='Date of Transaction', copy=False, default=fields.Date.today())
    status = fields.Selection(
        string='Status',
        selection=[('pending', 'Pending'), ('settled', 'Settled')],
    )

    @api.depends('group_id')
    def _compute_group_name(self):
        for expense in self:
            expense.name = expense.group_id.members.ids

    # @api.depends('group_id')
    # def _compute_payee_ids(self):
    #     for expense in self:
    #         expense.payee_ids = expense.group_id.member_ids
