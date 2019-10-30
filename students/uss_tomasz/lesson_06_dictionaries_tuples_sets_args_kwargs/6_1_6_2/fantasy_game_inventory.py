def display_inventory(player_inventory):
    print('Inventory:')
    total_items = 0
    for k, v in player_inventory.items():
        print(v, k)
        total_items += v
    print("Print total number of items:", total_items)


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory


if __name__ == '__main__':
    player_inv = {'gold coin': 42,
                  'rope': 1}
    dragon_loot = ['gold coin',
                  'dagger',
                  'gold coin',
                  'gold coin',
                  'ruby']
    inv = add_to_inventory(player_inv, dragon_loot)
    display_inventory(player_inv)
