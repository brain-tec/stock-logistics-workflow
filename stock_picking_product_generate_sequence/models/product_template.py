##############################################################################
# Copyright (c) 2022 brain-tec AG (https://braintec.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    serial_lot = fields.Char(
        string='Sequence Product',
        help='Create a sequence for product. Remember sequence contains at least one digit. '
             'For the numeric part of the sequence, 0 must be used to create the padding. '
             'E.g.: TEST/00000 (padding is 5)'
    )
