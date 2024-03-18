from odoo import models, fields

class ExpenseType(models.Model):
    _name='expense.type'
    _description='Type of Expenses'

    name=fields.Char(string="Name", required=True)

