# -*- encoding: utf-8 -*-
{
    'name': "Database Expiration Date Updater",
    'summary': """Automated scheduler to update the database expiration date.""",
    'description': """
    This module provides a scheduled task to automatically update the database expiration date from the configured system parameters.
    """,

    'author': "Divyesh Kanzariya",
    'category': 'Tools',
    'version': '17.0.1.0.0',
    'depends': ['base'],

    'data': [
        'data/ir_cron_data.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
