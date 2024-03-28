from odoo import models,fields

class ResUsers(models.Model):
    _inherit='res.users'

    payor_transaction_ids = fields.One2many('expense.transaction','payor_id' , readonly=True)
    payee_transaction_ids = fields.One2many('expense.transaction','payee_id' , readonly=True)
    # all_transaction_ids = fields.One2many()
    group_ids = fields.Many2many('expense.group')
    balance = fields.Float('Balance',default=0.00)
    