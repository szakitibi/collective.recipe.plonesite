import unittest

import zc.buildout

from collective.recipe.plonesite import Recipe


class TestDroppedOptionsWarn(unittest.TestCase):

    def test_products_option_raises_user_error(self):
        options = {'products': 'MyProduct'}
        with self.assertRaises(zc.buildout.UserError) as cm:
            Recipe(buildout={}, name='plonesite', options=options)
        self.assertIn('products', str(cm.exception))

    def test_products_initial_option_raises_user_error(self):
        options = {'products-initial': 'MyProduct'}
        with self.assertRaises(zc.buildout.UserError) as cm:
            Recipe(buildout={}, name='plonesite', options=options)
        self.assertIn('products-initial', str(cm.exception))
