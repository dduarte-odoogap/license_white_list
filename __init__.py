# Copyright 2021 OdooGAP (http://www.odoogap.com)
# @author Diogo Duarte
from . import models
from odoo import SUPERUSER_ID, api


def _post_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].sudo().set_param(
        'base.module_lock_list',
        ','.join(env['ir.module.module'].search([
            ('application', '=', True),
            ('state', '=', 'installed')
        ]).mapped('name')))
