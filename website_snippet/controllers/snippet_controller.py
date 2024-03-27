from odoo import http
from odoo.http import request
import json


class SalesOrderController(http.Controller):
    @http.route('/getSalesOrders', type="json", auth="public")
    def allsalesorder(self, show_all=False, *args):
      domain = []
      if show_all:
        domain.append(('state','=','sale'))
      res = request.env['sale.order'].sudo().search_read(
        domain,
        fields=['name', 'partner_id', 'state'],
      )
      return res
