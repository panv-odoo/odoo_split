from odoo import http
from odoo.http import request

class Expense(http.Controller):
    @http.route(['/expenses'], type='http', auth="public")
    def expense(self):
      return request.render("odoo_split.expense_view")