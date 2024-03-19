from odoo import models,fields

class InheritedModelUsers(models.Model):
    _inherit='res.users'

    group_ids = fields.Many2many('expense.group')
