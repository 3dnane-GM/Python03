#!/usr/bin/env python3

data_players = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal": {"type": "material",
                         "value": 1000, "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


class InventoryManager:
    """Manages player inventories and item transactions."""
    def __init__(self, players, catalog):
        """Initialize manager with players and catalog data."""
        self.players = dict(players)
        self.catalog = dict(catalog)

    def get_leaderboard(self):
        """Print the most valuable player, most items, and rarest items."""
        print("=== Inventory Analytics ===")
        biggest = {}
        for player in self.players:
            value = self.players[player]["total_value"]
            biggest.update({player: value})

        player, value = max(biggest.items())
        print(f"Most valuable player: {player.capitalize()} ({value} gold)")

        for player in self.players:
            value = self.players[player]["item_count"]
            biggest.update({player: value})

        player, value = max(biggest.items())
        print(f"Most items: {player.capitalize()} ({value} items)")

        rarest = {}
        for item in self.catalog:
            rarity = self.catalog[item]["rarity"]
            if rarity == "legendary":
                rarest.update({item: rarity})

        print("Rarest items: ", end="")

        printini = []
        for item, rarity in rarest.items():
            printini.append(f"{item}, ")
        print((''.join(printini)).strip(", "))

    def categorie_counter(self, items):
        """Count and print the number of items per category."""
        Count_list = []
        for item in items:
            Count_list.append(self.catalog[item]['type'])
        types = set(Count_list)
        print("Categories: ", end="")
        printini = []
        for type in types:
            num = Count_list.count(type)
            printini.append(f"{type}({num}), ")
        print((''.join(printini)).strip(", "))

    def player_inventory(self, pname: str):
        """Display a player's inventory details and value."""
        print(f"=== {pname.capitalize()}'s Inventory ===")

        try:
            pname = pname.lower()
            items = self.players[pname]['items']

            for item in items.keys():
                type = self.catalog[item]['type']
                rarity = self.catalog[item]['rarity']
                value = self.catalog[item]['value']
                item_count = self.players[pname]['items'][item]
                total_value = int(value*item_count)

                print(f"{item} ({type}, {rarity}): "
                      f"{item_count}x @ {value} gold each "
                      f"= {total_value} gold")

            inv_value = self.players[pname]['total_value']
            items_count = self.players[pname]['item_count']
            print(f"\nInventory value: {inv_value} gold")
            print(f"Item count: {items_count} items")
            self.categorie_counter(items)
        except KeyError:
            print(f"The player \"{pname}\" you requested is not available")

    def transact(self, giver: str, reciever: str, item: str, quantity: int):
        """Transfer items between two players, handling errors."""
        try:
            giver = giver.lower()
            reciever = reciever.lower()
            print(f"=== Transaction: {giver.capitalize()} gives "
                  f"{reciever.capitalize()} {quantity} {item} ===")

            if giver not in self.players:
                raise KeyError(f"The player \"{giver}\" "
                               "you requested is not available")
            elif reciever not in self.players:
                raise KeyError(f"The player \"{reciever}\" "
                               "you requested is not available")

            giver_inv = self.players[giver]['items']
            reciever_inv = self.players[reciever]['items']

            if (quantity < 0 or quantity > giver_inv.get(item, 0)
                    or giver_inv.get(item, 0) < 0):
                print("Transaction failed! not enough items")
            else:
                giver_inv.update({item: (giver_inv.get(item, 0))-quantity})
                reciever_inv.update({item: (reciever_inv.get(item, 0))
                                     + quantity})

                print("Transaction successful!\n")
                print("=== Updated Inventories ===")
                print(f"{giver} {item}: {giver_inv.get(item)}")
                print(f"{reciever} {item}: {reciever_inv.get(item)}")

        except KeyError as e:
            print(e)


if __name__ == "__main__":
    manager = InventoryManager(data_players["players"].items(),
                               data_players["catalog"].items())

    print()
    manager.player_inventory('alice')
    print()
    manager.transact("alice", "bob", "quantum_ring", 2)
    print()
    manager.get_leaderboard()
