##############################################################################
# Copyright (c) 2022 brain-tec AG (https://braintec.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
{
    'name': 'Stock Picking Product Generate sequence',
    'version': '15.0.1.0.0',
    'summary': 'Add an automated sequence in product of stock picking',
    'category': 'Inventory',
    'author': 'brain-tec AG',
    'website': 'https://braintec.com',
    'depends': [
        'product',
        'stock',
    ],
    'license': 'OPL-1',
    'data': [
        'views/product_template_views.xml',
        'views/stock_move_line_views.xml',
        'data/stock_picking_product_sequence.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
