# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SplitWise',
    'version': '1.0',
    'sequence': 10,
    'description': "RD Task",
    'depends': ['base'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/splitwise_split_views.xml',
        'views/splitwise_groups_views.xml',
        'views/splitwise_menus.xml']
}
