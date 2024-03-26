from odoo import http
from odoo.http import request
import json


class SalesOrderController(http.Controller):
    @http.route('/getSalesOrders', type="json", auth="public")
    def allsalesorder(self):
        res = request.env['sale.order'].sudo().search_read(
            fields=['name', 'partner_id', 'state'],
        )
        return res