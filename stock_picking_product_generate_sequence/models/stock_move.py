##############################################################################
# Copyright (c) 2022 brain-tec AG (https://braintec.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    show_lots_text = fields.Boolean(compute="_compute_show_lots_text")

    def _compute_show_lots_text(self):
        group_production_lot_enabled = self.user_has_groups('stock.group_production_lot')
        for move in self:
            picking = move.picking_id
            if not picking.move_line_ids and not picking.picking_type_id.use_create_lots:
                move.show_lots_text = False
            elif group_production_lot_enabled and picking.picking_type_id.use_create_lots \
                    and not picking.picking_type_id.use_existing_lots and picking.state != 'done':
                move.show_lots_text = True
            else:
                move.show_lots_text = False
