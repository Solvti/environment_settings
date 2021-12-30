from odoo.tests.common import SavepointCase
from odoo.tools import config
import os

class TestEnvironmentVariables(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        os.environ['test_key'] = 'test_token'
        os.environ['st_test_key'] = 'st_test_token'
        cls.Config = cls.env['ir.config_parameter']
        cls.Config.set_param('test_key', 'c_test_token')
        cls.Config.set_param('c_test_key', 'c_test_token')

        # mock config file
        config['test_key'] = 'cf_test_token'
        config['cf_test_key'] = 'cf_test_token'


    def test_environment_variables(self):

        self.assertEqual(self.env['ir.config_parameter'].get_param('test_key'), 'test_token')
        self.assertEqual(self.env['ir.config_parameter'].get_param('cf_test_key'), 'cf_test_token')
        self.assertEqual(self.env['ir.config_parameter'].get_param('c_test_key'), 'c_test_token')

    def test_environment_variables_env(self):

        self.assertEqual(self.env['ir.config_parameter'].get_param('test_key', env_prefix='st'), 'st_test_token')
        self.assertEqual(self.env['ir.config_parameter'].get_param('test_key', env_prefix='cf'), 'cf_test_token')
        self.assertEqual(self.env['ir.config_parameter'].get_param('test_key', env_prefix='c'), 'c_test_token')
