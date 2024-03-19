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
    'assets' : {
        'splitwise.assets_expense': [
            # bootstrap
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),

            # required for fa icons
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            
            # include base files from framework
            ('include', 'web._assets_core'),

            'web/static/src/core/utils/functions.js',
            'web/static/src/core/browser/browser.js',
            'web/static/src/core/registry.js',
            'web/static/src/core/assets.js',
            'splitwise/static/src/js/**/*',
        ],
    },
    'author': "Odoo",
    'sequence':'1',
    'installable': True,
    'application': True,
    'auto_install': True,    
    'license': 'LGPL-3'
}
