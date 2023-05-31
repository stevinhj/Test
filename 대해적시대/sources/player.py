import items
import world
import random
import time
random.seed()
class Player:
    def __init__(self):
        self.inventory = [items.Sword(),
                          items.CrustyBread(),
                          items.CrustyBread()]

        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 1000
        self.gold = 10000
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("인벤토리:")
        for item in self.inventory:
            print("*" + str(item))
        print("*골드 : {}".format(self.gold))
        best_weapon = self.most_powerful_weapon()
        print("지금 당신의 무기는 : {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        max_value = 100
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage >= max_damage:
                   best_weapon = item
                   max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        diceran = [1,2,3]
        self.x += dx
        self.y += dy

    def move_north(self):
        dice_ran = [1,2,3]
        randdice=random.choice(dice_ran)
        self.move(dx=0, dy=-randdice)
        print("북쪽으로 {}만큼 이동하셨습니다!".format(randdice))

    def move_south(self):
        dice_ran = [1,2,3]
        randdice=random.choice(dice_ran)
        self.move(dx=0, dy=randdice)
        print("남쪽으로 {}만큼 이동하셨습니다!".format(randdice))

    def move_east(self):
        dice_ran = [1,2,3]
        randdice=random.choice(dice_ran)
        self.move(dx=randdice, dy=0)
        print("동쪽으로 {}만큼 이동하셨습니다!".format(randdice))

    def move_west(self):
        dice_ran = [1,2,3]
        randdice=random.choice(dice_ran)
        self.move(dx=-randdice, dy=0)
        print("서쪽으로 {}만큼 이동하셨습니다!".format(randdice))

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("""
{}로 적을 공격했습니다!""".format(best_weapon.name, enemy.name))
        sran = random.randint(1,10)
        hran = random.randint(10,20)
        pran = random.randint(20,30)
        gran = random.randint(30,40)
        cran = random.randint(50,100)
        if best_weapon.name == "칼":
            best_weapon.damage = sran
            enemy.hp -= sran
        if best_weapon.name == "작살":
            best_weapon.damage = hran
            enemy.hp -= hran
        if best_weapon.name == "권총":
            best_weapon.damage = pran
            enemy.hp -= pran
        if best_weapon.name == "소총":
            best_weapon.damage = gran
            enemy.hp -= gran
        if best_weapon.name == "대포":
            best_weapon.damage = cran
            enemy.hp -= cran
        if not enemy.is_alive():
            print("{}를 무찔렀습니다!".format(enemy.name))
        else:
            print("""당신은 {}의 데미지를 입혔습니다.
{}의 체력 {}.""".format(best_weapon.damage, enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("수리에 필요한 아이템이 없습니다!")
            return

        for i, item in enumerate(consumables,1):
            print("어떤 아이템으로 수리하실껀가요?: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("현재 내구도: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid Choice, try again.")

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

