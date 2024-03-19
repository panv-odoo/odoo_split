{
    'name': 'Odoo Split',
    'summary': 'Split your expenses',
    'depends': [
        'base',
    ],
    'category': 'Split/Expense',
    'data' : [
        'security/ir.model.access.csv',

        'views/expense_types_views.xml',
        'views/expense_transaction_views.xml',
        'views/expense_group_transaction_views.xml',
        'views/expense_group_views.xml',

        'views/odoo_split_menus.xml',
    ],
    'demo' : [
    ],
    'application': True,
    'installable': True,
}
