import json

from odoo import http
from odoo.http import request
from odoo.tools import file_open, ustr

class WebManifest(http.Controller):
    @http.route('/split/manifest.webmanifest', type='http', auth='public', methods=['GET'])
    def webmanifest(self):
        manifest = {
            'name': 'Odoo Split',
            'scope': '/split',
            'start_url': '/split',
            'display': 'standalone',
            'background_color': '#f9fafb',
            'theme_color': '#f9fafb',
            # 'icons': [{
            #     'src': '/room/static/description/pwa-icon.png',
            #     'sizes': '192x192',
            #     'type': 'image/png',
            # }, {
            #     'src': '/room/static/description/icon.svg',
            #     'sizes': '512x512',
            # }]
        }
        body = json.dumps(manifest, default=ustr)
        response = request.make_response(body, [
            ('Content-Type', 'application/manifest+json'),
        ])
        return response

    @http.route('/split/service-worker.js', type='http', auth='public', methods=['GET'], website=True, sitemap=False)
    def service_worker(self):
        # breakpoint()
        with file_open('odoo_split/static/src/service_worker.js') as f:
            body = f.read()
        return request.make_response(
            body,
            [
                ('Content-Type', 'text/javascript'),
                ('Service-Worker-Allowed', '/split'),
            ]
        )