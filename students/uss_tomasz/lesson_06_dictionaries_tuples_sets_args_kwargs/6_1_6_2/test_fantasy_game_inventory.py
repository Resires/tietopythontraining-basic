import unittest
from fantasy_game_inventory import add_to_inventory


class TestInventory(unittest.TestCase):
    def test_add_items(self):
        self.assertEqual(add_to_inventory(
            {'gold coin': 42,
             'rope': 1},
            ['gold coin',
             'dagger',
             'gold coin',
             'gold coin',
             'ruby']),
            {'gold coin': 45,
             'rope': 1,
             'ruby': 1,
             'dagger': 1})


if __name__ == '__main__':
    unittest.main()
