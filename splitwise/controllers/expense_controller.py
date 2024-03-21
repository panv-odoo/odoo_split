# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request

class Splitwise(http.Controller):
    @http.route(['/expenses'], type='http', auth="public", website=True, sitemap=False)
    def splitwise(self):
        return request.render("splitwise.expense_view")

    @http.route(["/expenses/json"], type='json', auth="public")
    def get_existing_expenses(self):
        res = request.env["res.users"].sudo().search_read([])
        return res
