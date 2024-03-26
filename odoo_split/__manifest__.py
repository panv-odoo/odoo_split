{
    'name': 'Odoo Split',
    'version': '1.0',
    'summary': 'Split your expenses',
    'depends': ['base', 'web', 'room'],
    'category': 'Split/Expense',
    'data' : [
        'security/ir.model.access.csv',

        'views/expense_templates.xml',
        'views/expense_types_views.xml',
        'views/expense_transaction_views.xml',
        'views/expense_group_transaction_views.xml',
        'views/expense_group_views.xml',
        'views/odoo_split_menus.xml',
    ],
    'demo' : [
        'data/expense.type.csv'
    ],'assets' : {
        'web.assets_frontend': [

            #2 Load variables, Bootstrap and UI icons bundles
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),
            "web/static/src/libs/fontawesome/css/font-awesome.css",
            "web/static/lib/odoo_ui_icons/*",
            'web/static/src/legacy/scss/ui.scss',
            'web/static/src/scss/base_frontend.scss',
            'web/static/src/core/utils/transitions.scss',
            'web/static/src/core/notifications/notification.scss',
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
            'odoo_split/static/src/js/**/*',

        ],
    },
    'author': "panv-odoo",
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
