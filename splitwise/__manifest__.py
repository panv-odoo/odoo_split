# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Expenses',
    'version':'1.0',
    'depends':['mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/expense_view.xml',
        'views/expense_transaction_view.xml',
        'views/expense_types_view.xml',
        'views/expense_menu.xml',
    ],
    'author': "Odoo",
    'sequence':'1',
    'installable': True,
    'application': True,
    'auto_install': True,    
    'license': 'LGPL-3'
}
