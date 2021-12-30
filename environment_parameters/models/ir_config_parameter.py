import os
from odoo import models, tools, api



class ConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    @api.model
    def get_param(self, key, default=False, env_prefix=False):
        """Retrieve the value for a given key.

        Override to first take a look into os.environ.get(key) or tools.config.get(key)
        and add extra arg: env_prefix

        :param string key: The key of the parameter value to retrieve.
        :param string default: default value if parameter is missing.
        :param string env_prefix: environment prefix if needed.

        :return: The value of the parameter, or ``default`` if it does not exist.
        :rtype: string or False
        """


        env_prefix = env_prefix or os.environ.get('ODOO_ENV_CODE') or tools.config.get('ODOO_ENV_CODE')

        if env_prefix:
            key = '{}_{}'.format(env_prefix, key)

        value = os.environ.get(key) or tools.config.get(key) or self._get_param(key) or default

        return value

