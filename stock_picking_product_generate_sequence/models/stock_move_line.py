##############################################################################
# Copyright (c) 2022 brain-tec AG (https://braintec.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from re import findall as regex_findall
from re import split as regex_split

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def action_generate_product_serial(self):
        self.ensure_one()
        self.lot_id = self.env['stock.production.lot'].create({
            'product_id': self.product_id.id,
            'company_id': self.company_id.id,
            'name': self._get_next_serial(self.company_id, self.product_id) or
                    self.env['ir.sequence'].next_by_code('stock.picking.product')
        })

    @api.model
    def _get_next_serial(self, company, product):
        sequence = product.product_tmpl_id.serial_lot
        if sequence:
            splitted = regex_split(r'(\d+)', sequence)
            prefix = splitted[0]
            initial_number = int(splitted[1])
            padding = len(splitted[1])
            last_serial = self.env['stock.production.lot'].search(
                [
                    ('company_id', '=', company.id),
                    ('product_id', '=', product.id),
                    ('name', '=ilike', '%s%%' % prefix)
                ],
                limit=1,
                order='id DESC'
            )

            if last_serial:
                last_serial_splitted = regex_split(r'(\d+)', last_serial.name)
                last_serial_prefix = last_serial_splitted[0]
                last_serial_number = int(last_serial_splitted[1])
                return last_serial_prefix + str(last_serial_number + 1).zfill(len(last_serial_splitted[0]))
            return prefix + str(initial_number + 1).zfill(padding)
        return False
