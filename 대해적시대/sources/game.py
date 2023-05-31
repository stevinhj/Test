import world
import random
from player import Player
from collections import OrderedDict


def play():
    print()
    print()
    print("""
□□□□□□□■□□■□□□□■■□□□■□□■□■■■■■■■□■■□□□□□■□□□□□■□□□□□□□□■□□■
□■■■■■□■□□■□□■■■■■■□■□□■□□□□■□□□□■■□□□□□■□□□□□■□□■■■■■□■□□■
□■□□□□□■□□■□□■■■■■■□■□□■□□□□■□□□□■■□□□□□■□□□□□■□□■□□□□□■□□■
□■□□□□□■□□■□□□■■■■□□■□□■□□□■■■□■■■■□□□□□■□□□□□■□□■□□□□□■□□■
□■□□□□□■■■■□□■■■■■■□■■■■□□■■■■■□□■■□□□□■■□□□□□■□□■□□□□□■■■■
□■□□□□□■□□■□□■■□□■■□■■■■□■■■□■■■□■■□□□□■■■□□□□■□□■□□□□□■□□■
□■□□□□□■□□■□□■■□□□■□■□□■■■□□□□□■□□■□□□■■■■■□□□■□□■□□□□□■□□■
□■□□□■■■□□■□□■■□□■■□■□□■□□■■■■■■■■■□□■■□□■■■□□■□□■□□□■■■□□■
□■■■■■■■□□■□□□■■■■□□■□□■□□□□□□□□□□■□■■□□□□□■□□■□□■■■■■■■□□■
□□□□□□□■□□■□□□□□□□□□■□□■□□□□□□□□□□■□□□□□□□□□□□■□□□□□□□□■□□■
□□□□□□□■□□■□□□□□□□□□■□□■□□□□□□□□□□■□□□□□□□□□□□■□□□□□□□□■□□■
□□□□□□□■□□■□□□□□□□□□■□□■□□□□□□□□□□■□□□□□□□□□□□■□□□□□□□□■□□■
""")
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("""

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
깊은 바다에 잠긴 또 하나의 해적이 되었습니다..""")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("다음 행동을 선택하세요")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "인벤토리확인")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "거래")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "공격")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "북쪽으로 주사위만큼이동(1~3)")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "남쪽으로 주사위만큼이동(1~3)")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "동쪽으로 주사위만큼이동(1~3)")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "서쪽으로 주사위만큼이동(1~3)")
        if player.hp < 1000:
            action_adder(actions, 'h', player.heal, "해적선수리")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{} : {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("행동: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("올바른선택지가아닙니다!")


play()
