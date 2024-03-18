{
    'name': 'Odoo Split',
    'summary': 'Split your expenses',
    'depends': [
        'base',
        'website',
    ],
    'category': 'Split/Expense',
    'data' : [
        'security/ir.model.access.csv',
        
        'views/odoo_split_menus.xml',
    ],
    'demo' : [
    ],
    'application': True,
    'installable': True,
}
