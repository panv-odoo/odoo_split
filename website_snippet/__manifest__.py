# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Website Snippet',
    'version':'1.0',
    'depends':['web','website','sale_management','web_editor'],
    'data':[
        'views/snippets/snippets.xml',
        'views/snippets/s_sales_order_snippet.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            #2 Load frontend variables
            "website_snippet/static/src/js/000.xml",
            "website_snippet/static/src/js/000.js",
            
        ],

    },
    'author': "panv-odoo",
    'sequence':'1',
    'installable': True,
    'application': True,
    'auto_install': True,    
    'license': 'LGPL-3'
}
