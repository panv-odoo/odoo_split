from traitlets import default
from odoo import models, fields, api

class ExpenseGroupTransaction(models.Model):
    _name='expense.group.transaction'
    _description='Group Transactions'

    group_id = fields.Many2one('expense.group', required=True)
    payee_ids = fields.Many2many('res.users', string="With you and: " ,compute='_compute_payee_ids',store=True,)
    payer = fields.Many2one('res.users', required=True, string='Payer', default=lambda self: self.env.user)
    total_amount = fields.Float(string="Amount", required=True,default=0.00)
    description = fields.Text(string="Description", required=True)
    expense_types = fields.Many2one('expense.type', string="Type of Expense")
    transaction_date = fields.Date(string='Date of Transaction', copy=False, default=fields.Date.today())
    status = fields.Selection(
        string='Status',
        selection=[('pending', 'Pending'), ('settled', 'Settled')],
    )
    amount_per_head = fields.Float('Split Share',compute='_compute_amount_per_head')

    @api.depends('group_id')
    def _compute_payee_ids(self):
      for expense in self:
        expense.payee_ids = expense.group_id.member_ids
        
    @api.depends('total_amount','description','payee_ids','group_id')
    def _compute_display_name(self):
      if self.total_amount:
        for record in self:
          if (len(record.description) > 25):
            description = record.description[:25]+'...'
          else:
            description = record.description
          record.display_name = '₹ '+ str(record.total_amount) + ' : ' + description
          
          
      else:
        self.display_name = ''
        
    def _compute_amount_per_head(self):
      for record in self:
        if record.total_amount:
          record.amount_per_head = record.total_amount / len(record.payee_ids)