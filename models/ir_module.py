# Copyright 2021 OdooGAP (http://www.odoogap.com)
# @author Diogo Duarte
from odoo import models, _
from odoo.exceptions import ValidationError


class ModuleModule(models.Model):
    _inherit = "ir.module.module"

    def _state_update(self, newstate, states_to_update, level=100):
        lock_list = self.env['ir.config_parameter'].sudo().get_param('base.module_lock_list', default=False)
        if lock_list:
            for module in self:
                if (module.name not in lock_list) and module.application:
                    raise ValidationError(_(
                        "Sorry you cannot install this app!\n"
                        "Check you have purchased the app then update:\n"
                        "System Parameter: 'base.module_lock_list'"))
        return super(ModuleModule, self)._state_update(newstate, states_to_update, level)
