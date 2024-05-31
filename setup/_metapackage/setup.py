import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-workflow",
    description="Meta package for oca-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-delivery_procurement_group_carrier>=16.0dev,<16.1dev',
        'odoo-addon-delivery_total_weight_from_packaging>=16.0dev,<16.1dev',
        'odoo-addon-purchase_stock_picking_invoice_link>=16.0dev,<16.1dev',
        'odoo-addon-sale_line_returned_qty>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_global_stock_route>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_restocking_fee_invoicing>=16.0dev,<16.1dev',
        'odoo-addon-stock_account_product_run_fifo_hook>=16.0dev,<16.1dev',
        'odoo-addon-stock_auto_move>=16.0dev,<16.1dev',
        'odoo-addon-stock_customer_deposit>=16.0dev,<16.1dev',
        'odoo-addon-stock_customer_deposit_elaboration>=16.0dev,<16.1dev',
        'odoo-addon-stock_customer_deposit_sale_margin>=16.0dev,<16.1dev',
        'odoo-addon-stock_delivery_note>=16.0dev,<16.1dev',
        'odoo-addon-stock_grn>=16.0dev,<16.1dev',
        'odoo-addon-stock_landed_costs_currency>=16.0dev,<16.1dev',
        'odoo-addon-stock_landed_costs_delivery>=16.0dev,<16.1dev',
        'odoo-addon-stock_landed_costs_purchase_auto>=16.0dev,<16.1dev',
        'odoo-addon-stock_landed_costs_security>=16.0dev,<16.1dev',
        'odoo-addon-stock_lot_production_date>=16.0dev,<16.1dev',
        'odoo-addon-stock_lot_scrap>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_free_reservation_reassign>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_line_auto_fill>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_line_change_lot>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_line_expiration_date_required>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_line_reserved_quant>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_line_serial_unique>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_manage_priority>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_priority_picking_assign>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_propagate_first_move>=16.0dev,<16.1dev',
        'odoo-addon-stock_no_negative>=16.0dev,<16.1dev',
        'odoo-addon-stock_override_procurement>=16.0dev,<16.1dev',
        'odoo-addon-stock_owner_restriction>=16.0dev,<16.1dev',
        'odoo-addon-stock_partner_delivery_window>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_auto_create_lot>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_back2draft>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_extended>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_extended_account>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_extended_account_sale_type>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_invoice_frequency>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_print_invoices>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_print_pickings>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_validate_confirm>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_customer_ref>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_filter_lot>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_grn_mandatory>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_group_by_base>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_group_by_max_weight>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_group_by_partner_by_carrier>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_group_by_partner_by_carrier_by_date>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_import_serial_number>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_info_lot>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_invoice_link>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_kind>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_line_sequence>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_mass_action>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_partner_note>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_product_link>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_progress>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_purchase_order_link>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_quick>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_restrict_cancel_printed>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_sale_order_link>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_send_by_mail>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_show_backorder>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_show_return>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_start>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_supplier_ref>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_to_batch_group_fields>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_warn_message>=16.0dev,<16.1dev',
        'odoo-addon-stock_procurement_customer>=16.0dev,<16.1dev',
        'odoo-addon-stock_product_set>=16.0dev,<16.1dev',
        'odoo-addon-stock_putaway_hook>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_package_dimension>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_package_dimension_total_weight_from_packaging>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_package_product_packaging>=16.0dev,<16.1dev',
        'odoo-addon-stock_receipt_lot_info>=16.0dev,<16.1dev',
        'odoo-addon-stock_restrict_lot>=16.0dev,<16.1dev',
        'odoo-addon-stock_rule_reserve_max_quantity>=16.0dev,<16.1dev',
        'odoo-addon-stock_split_picking>=16.0dev,<16.1dev',
        'odoo-addon-stock_valuation_layer_usage>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
