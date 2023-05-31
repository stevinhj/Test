import random
import time
random.seed()
class Weapon:
    def __init__(self):
        raise NotImplementedError("Dop not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Sword(Weapon):
    def __init__(self):
        self.name = "칼"
        self.description = " 기본무기,1~10데미지"
        self.value = 101
        self.damage = 1
    def __str__(self):
        return "{}{}".format(self.name,self.description)


class Harpoon(Weapon):
    def __init__(self):
        self.name = "작살"
        self.description = " 고래도 잡는 작살,10~20데미지"                            
        self.damage = 2
        self.value = 150
        

class Pistol(Weapon):
    def __init__(self):
        self.name = "권총"
        self.description = " 짧은총,20~30데미지"                           
        self.damage =3
        self.value = 500
      

class Gun(Weapon):
    def __init__(self):
        self.name = "소총"
        self.description = " 긴~총,30~40데미지"                           
        self.damage = 4
        self.value = 600
        

class Cannon(Weapon):
    def __init__(self):
        self.name = "대포"
        self.description = " 대포는 항상 옳다,50~100데미지"
        self.damage = 5
        self.value = 1000
        
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "초급수리키트"
        self.healing_value = 100
        self.description = " 내구도를 100만큼 수리한다"
        self.value = 50


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "고급수리키트"
        self.healing_value = 500
        self.description = " 내구도를 500만큼 수리한다"
        self.value = 100
