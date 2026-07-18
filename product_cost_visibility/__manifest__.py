{
    'name': 'Product Cost Visibility',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Control which users can see the product Cost field from Settings',
    'description': """
Product Cost Visibility
=======================

Adds a configurable permission that controls whether a user can see the
**Cost** field (``standard_price``) on the product screen.

Features
--------
* A security group **"Show Product Cost"**.
* Field-level security on ``standard_price`` restricts the Cost to that group,
  so it is removed from every view, export and read-based report for users who
  are not members - not just the product form.
* The Cost label is also hidden on the product form so no empty row is left.
* A setting under **Settings** where an administrator can pick exactly which
  users are allowed to see the product cost. Saving the setting syncs the
  selected users into the security group.
""",
    'author': 'Mohamed Hassan',
    'maintainer': 'Mohamed Hassan',
    'license': 'LGPL-3',
    'depends': ['product', 'base_setup'],
    'data': [
        'security/product_cost_security.xml',
        'views/product_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
}
