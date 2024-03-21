# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Expenses',
    'version':'1.0',
    'depends':['mail','web'],
    'data':[
        'security/ir.model.access.csv',
        'views/expense_view.xml',
        'views/expense_transaction_view.xml',
        'views/expense_types_view.xml',
        'views/expense_templete.xml',
        'views/expense_menu.xml',
    ],
    'assets': {
        'splitwise.assets_splitwise': [

            #2 Load frontend variables
            ("include", "web._assets_helpers"),
            ("include", "web._assets_frontend_helpers"),
            ("include", "web._assets_primary_variables"),
            "web/static/src/scss/pre_variables.scss",

            #3 Load Bootstrap and frontend bundles
            "web/static/lib/bootstrap/scss/_functions.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            ("include", "web._assets_bootstrap_frontend"),

            'splitwise/static/src/**/*',
        ],

    },
    'author': "Odoo",
    'sequence':'1',
    'installable': True,
    'application': True,
    'auto_install': True,    
    'license': 'LGPL-3'
}
