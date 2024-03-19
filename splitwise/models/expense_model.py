# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _,api,fields,models

class ExpenseModel(models.Model):
    _name = "expense.model"
    _rec_name = "description"
    _inherit = "mail.thread"
    
    amount = fields.Float(string = "Amount", tracking=True)
    description = fields.Char(string = "Description", tracking=True)
    paid_user_ids = fields.Many2one('res.users', string="Paid By")
    involve_users_ids = fields.Many2many('res.users', string="Involved Person")
    isSettle = fields.Boolean(default=False)
    types_ids = fields.Many2one('expense.type', string="Types")

    @api.model
    def create(self, val):
        res = super().create(val)
        body = "This payment has been created from : " + str(self.env['res.users'].browse(val['paid_user_ids']).name) + " of amount" + str(val['amount'])
        res.message_post(body=body)
        return res
