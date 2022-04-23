# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    datasheet_name = fields.Char();
    datasheet_file = fields.Binary();

    manual_name = fields.Char();
    manual_file = fields.Binary();
    
    schema_name = fields.Char();
    schema_file = fields.Binary();

    certificate_name = fields.Char();
    certificate_file = fields.Binary();

    misc_name = fields.Char();
    misc_file = fields.Binary();


