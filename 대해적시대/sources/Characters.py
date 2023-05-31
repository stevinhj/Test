import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 10000000
        self.inventory = [items.CrustyBread(),
                          items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion(),
                          items.HealingPotion(),
                          items.Harpoon(),
                          items.Pistol(),
                          items.Gun(),
                          items.Cannon()
                          ]
