# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Spiltwise',
    'version':'1.0',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/expense_view.xml',
        'views/expense_menu.xml',
    ],
    'author': "Odoo",
    'sequence':'1',
    'installable': True,
    'application': True,
    'auto_install': True,    
    'license': 'LGPL-3'
}
