# -*- coding: utf-8 -*-
#    Author: Leonardo Pistone
#    Copyright 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import models, api, fields


class Quant(models.Model):
    _inherit = 'stock.quant'

    @api.model
    def create(self, vals):
        """Set the owner based on the location.

        This is not a default method because we need to know the location.

        Quants are always created as superuser and can't be manually created
        (enforced by ACL). Therefore, we can't use the company of the current
        user as default owner.
        """
        if not vals.get('owner_id'):
            Company = self.env['res.company']
            location = self.env['stock.location'].browse(vals['location_id'])

            vals['owner_id'] = (
                location.partner_id.id or
                location.company_id.partner_id.id or
                Company.browse(
                    self.env.context.get('company_id')
                ).partner_id.id
            )

        return super(Quant, self).create(vals)

    owner_id = fields.Many2one('res.partner', 'Owner',
                               help="This is the owner of the quant",
                               readonly=True,
                               select=True,
                               required=True)

    @api.model
    def _quant_create(self, qty, move, lot_id=False, owner_id=False,
                      src_package_id=False, dest_package_id=False,
                      force_location_from=False, force_location_to=False,
                      context=None):
        # _quant_create call the create method with SUPERUSER_ID. Therefore,
        # If the quant is for a location without an associated company_id,
        # or partner the quant will be created without owner.
        # Put the company id into the context to work around this bug in the
        # odoo core (quant created as superuser).
        # The create method will take care of the company_id into the context
        # to determine the owner of the quant.
        company_id = self.env.user.company_id.id
        this = self.with_context(
            company_id=company_id)
        return super(Quant, this)._quant_create(
            qty, move, lot_id=lot_id, owner_id=owner_id,
            src_package_id=src_package_id, dest_package_id=dest_package_id,
            force_location_from=force_location_from,
            force_location_to=force_location_to,
            context=context)

    @api.model
    def quants_get_prefered_domain(self, location, product, qty, domain=None,
                                   prefered_domain_list=None,
                                   restrict_lot_id=False,
                                   restrict_partner_id=False):
        """Enforce the requested owner on quant reservation.

        If no restriction is imposed, enforce the location partner (or the
        company partner) as owner.

        On the other hand, the core stock module uses the requested owner as
        first choice, but then reserves anything else. Also, no restriction
        means we can reserve anything, while we want to reserve only own stock.

        """
        if domain is None:
            domain = []
        if prefered_domain_list is None:
            prefered_domain_list = []

        if not restrict_partner_id:
            restrict_partner_id = (location.partner_id.id or
                                   location.company_id.partner_id.id)
        if not restrict_partner_id:
            # location can be customer, so use partner from user company
            restrict_partner_id = self.env.user.company_id.partner_id.id

        domain += [
            ('owner_id', '=', restrict_partner_id),
        ]

        return super(Quant, self).quants_get_prefered_domain(
            location, product, qty, domain, prefered_domain_list,
            restrict_lot_id, restrict_partner_id)
