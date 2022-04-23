# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    technical_sheet = fields.Binary();
    