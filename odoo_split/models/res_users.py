from odoo import models,fields

class ResUsers(models.Model):
    _inherit='res.users'

    group_ids = fields.Many2many('expense.group')
    balance = fields.Float('Balance',default=0.00)