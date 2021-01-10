{
    'name': 'License White List',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
This module creates a module whitelist and doesn't allow users to install modules without updating that list.
This avoids installing modules that the customer hasn't purchased.
    """,
    'depends': ['base'],
    'data': [
    ],
    'demo': [],
    'auto_install': True,
    'post_init_hook': '_post_init',
}
