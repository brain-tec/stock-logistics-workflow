##############################################################################
# Copyright (c) 2022 brain-tec AG (https://braintec.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from re import match as regex_match
from re import split as regex_split


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    serial_lot = fields.Char(
        string='Sequence Product',
        help='Create a sequence for product. Remember sequence contains one character block and one numeric block. '
             'For the numeric part of the sequence, 0 must be used to create the padding. '
             'E.g.: TEST/00000 (padding is 5)'
    )

    @api.onchange('serial_lot')
    def _onchange_serial_lot(self):
        pattern = "(?:^\\D{1,}\\d{1,}$)"
        split_sequence_product = regex_split(r'(\d+)', self.serial_lot)
        global_sequence = self.env.ref("stock_picking_product_generate_sequence.seq_stock_picking_product")
        if split_sequence_product[0] == global_sequence.prefix:
            raise UserError(_("The prefix sequence is the same as for the standard product"))
        if regex_match(pattern, self.serial_lot) is None:
            raise UserError(_("The sequence format is not correct"))

