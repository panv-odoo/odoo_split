from odoo import http
from odoo.http import request

class Expense(http.Controller):
    @http.route(['/split'], type='http', auth="public", website=True, sitemap=False)
    def expense(self):
      return request.render("odoo_split.expense_view")

    # @http.route("/odoo_split", type="http", auth="public", website=True, sitemap=False)
    # def room_room(self):
    #     return request.render("")