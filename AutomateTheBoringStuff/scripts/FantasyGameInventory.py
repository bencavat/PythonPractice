def displayInventory(inventory):
    print("Inventory:")
    count = 0
    for item, amount in inventory.items():
        print(f"{item}: {amount}")
        count += amount
    print(f"Total number of items: {count}")

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory



def main():
    starting_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(starting_inventory)
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    new__inventory = addToInventory(starting_inventory, dragonLoot)
    displayInventory(new__inventory)


if __name__ == "__main__":
    main()
