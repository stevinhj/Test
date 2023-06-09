
import random
import Characters



class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class EndTile(MapTile):
    def intro_text(self):
        return """이뒤에는 드넓은 바다뿐이다(선택하셨던 방향의 반대방향으로 가십시오)"""
    
class StartTile(MapTile):
    def intro_text(self):
        return """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⣄⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠇⣼⡟⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠉⠰⠻⢸⣹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠰⣄⣀⣶⠿⠶⠶⣦⣤⣈⠉⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢤⡤⠞⠉⠉⠻⠄⠀⠀⠙⢿⡉⣹⠲⣄⠙⢿⣿⣆⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣯⠀⢨⣷⣄⠙⢶⣶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⡄⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡷⣼⣿⡟⣆⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣄⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⠀⣷⠙⢿⡇⠘⣆⣿⠟⣄⡀⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡟⢧⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⣿⠀⠀⠀⢶⢷⡀⢻⣹⠀⠈⢳⡄⠀⠀⣰⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠈⢳⡀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢿⠀⠀⠀⠀⠀⢷⡈⣿⠀⠀⠀⢻⣆⢠⢿⠇⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡗⡇⠀⠳⣼⣇⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⣾⠀⠀⠀⠀⠀⠀⣻⣏⠀⠀⠀⠀⣿⢧⣾⠄⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠋⢰⠀⠙⣿⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⣿⠀⠀⠀⠀⠀⠀⠙⣿⣄⡀⠀⢠⠿⡞⣿⡀⠀⠀⢹⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣅⠀⢸⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⣾⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⢿⠉⠀⢀⠟⣠⡇⠈⣷⡀⠀⠀⢻⣿⡙⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣏⢹⢠⢸⠀⠀⠸⣿⡄⠀⠀⠀⠀⣰⠃⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⡀⢀⡟⢠⣿⣿⠀⢻⣷⠀⠀⠈⢿⣿⣎⢳⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⢸⠈⠘⠀⠀⠀⣿⡿⡄⠀⠀⢠⡏⠀⠀⣼⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡞⢀⣿⡟⣿⠀⠀⢹⣇⠀⠀⠘⣿⣿⣧⡙⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⡎⠀⠸⡆⠀⠀⠀⢿⣷⠷⠀⠀⡿⠀⠀⣰⢃⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⣾⣽⠀⡇⠀⠀⠀⣧⠀⠀⠀⢹⣟⢹⡇⠘⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⣻⠃⠁⠀⠓⠀⢀⣤⢸⡹⡇⠀⣼⠃⠀⢀⠏⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⢿⠇⢸⠁⠈⠀⠀⢸⡀⠀⠀⠀⢿⣾⣿⠀⠸⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣷⠃⠀⠀⠀⠀⠀⣺⡿⠈⡇⣷⢠⡏⠀⢀⡟⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡾⡾⠀⣾⠀⡀⠀⠀⢸⡇⠀⠀⠀⠘⣿⣿⠀⠀⢻⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠀⠚⠛⢰⡄⣷⢹⡿⠀⠀⡼⣠⠏⠀⠀⠀⠀⢀⠀⢠⣿⠈⠀⠄⢿⣣⠁⠀⡟⠀⠀⠀⢠⢸⡇⠀⠀⠀⠀⢿⡟⢰⣶⣾⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠏⢀⣀⣤⣀⣴⡄⣴⣶⣦⠾⡇⢹⢸⠁⠀⣰⣣⡏⡀⣤⢠⣤⢶⣿⡿⡿⣏⠀⡞⠀⡞⡟⠀⣸⠃⠀⠀⠀⡞⡆⡇⠀⠀⠀⠀⢸⣷⢾⣿⡟⠀⠀⠀
⠀⠀⠀⢀⣴⢋⣴⣿⣟⣽⣿⣇⣇⣿⣿⣿⣴⣤⣼⣿⣧⣰⣿⡿⢣⣿⣿⣿⣻⠙⠻⢷⢱⠟⣶⣷⣸⣅⡇⠐⣿⠃⠀⠀⢰⣇⣇⡇⠀⠀⠀⢠⣾⣿⣿⣿⠇⠀⠀⠀
⢶⣴⣶⡿⠿⠿⠿⠿⠾⠿⠿⢿⠭⣍⣉⣻⠿⠿⣿⣿⣿⣿⣏⣷⣿⠿⣿⣿⣿⡶⠶⣶⣄⣀⠋⠠⣿⣿⠇⢸⡟⠀⢀⢠⣾⣿⣿⡇⠀⠀⣠⠏⢸⣿⣿⠇⠀⠀⠀⠀
⠀⠈⠛⠿⢷⣦⣄⠀⠀⢀⣀⣾⣰⣇⣿⡏⢙⣶⣿⣿⣿⣿⠛⢹⠃⠀⣿⣿⣿⠃⣰⠋⢹⣿⣻⢦⣛⣿⣆⡟⠁⢤⣸⣻⣿⣞⣿⡇⠀⡼⠃⠀⣸⣿⣁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⣻⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣾⣿⣽⣿⢀⡿⣀⣴⢿⢿⣿⣶⠏⠀⣼⢸⣿⣠⠻⣿⣿⣷⣶⣿⣿⣛⣉⣿⢿⣧⡞⣁⣤⢾⡟⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠶⠾⡏⣿⢺⡿⣿⣾⣸⣸⣿⣿⣷⣶⣿⣾⣼⣇⣸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⠿⠟⢉⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⢿⠿⣿⣿⣿⣧⣤⣷⣈⠉⠉⠙⠓⢿⢿⢻⣿⣻⡿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣧⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⣿⣻⣽⣿⣷⣶⣶⣼⣿⣀⣉⣉⠙⣶⡇⣾⠽⢿⣿⢿⣽⣿⣉⣽⣿⣿⣿⣿⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣀⣠⣤⣀⣀⣀⣴⣶⣼⠿⢿⣿⣿⡛⣠⣾⣿⡿⠿⢿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣼⣿⣯⣽⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠉⠳⠶⡋⠁⠀⣈⣭⠼⣍⠤⠴⠷⠋⠉⠉⠀⣀⣀⣉⣝⣿⣿⣯⠛⠻⠿⠿⢿⣿⣿⣯⣿⠿⠛⠙⠉⠻⢿⣻⡿⢿⣿⠿⣇⣠⣤⢤⠤⠶⠶⠶⠶⠶⠶⠦⠄
⠀⠀⠀⠰⠶⣾⣳⡶⠋⠉⠀⢀⣀⣀⣀⣤⠶⠶⠒⠉⠉⠉⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣃⠘⠛⡛⣷⣶⣶⢄⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠀⢲⣒⠛⠛⠻⠿⠿⠶⣤⣕⣶⠄⠰⠊⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣓⠒⠚⠛⠉⠉⣹⣻⠿⠟⠉⠁⠀⠀⠉⡉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠖⠀⠀⠀⠀⠀⠀⠈⠉⠓⠶⣤⣀⣀⣉⣳⣶⣶⡾⠿⢿⣶⣶⣶⣤⣤⡴⠶⠶⠖⠒⠋⠉⣉⣽⡶⠶⣟⡉⠀⠀⠀⠀⠀⣠⡴⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠿⠿⣿⣲⢤⣀⡀⠀⠀⠀⠀⢀⣀⣀⣠⠶⠟⠋⠉⠀⠀⠀⠉⠙⠳⠶⠖⠚⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠛⠛⠒⠾⠟⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


class BoringTile(MapTile):
    def intro_text(self):
        return """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⠾⠿⠿⠯⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣾⠛⠁⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠁⠀⠀⠀⢀⣤⣾⣟⣛⣛⣶⣬⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠃⠀⠀⠀⠀⠀⣾⣿⠟⠉⠉⠉⠉⠛⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠋⠀⠀⠀⠀⠀⠀⠀⣿⡏⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣤⣤⣠⣤⣤⡤⡶⣶⢿⠟⠹⠿⠄⣿⣿⠏⠀⣀⣤⡦⠀⠀⠀⠀⣀⡄
⢀⣄⣠⣶⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠚⠋⠉⠀⠀⠀⠀⠀⠀⠈⠛⡛⡻⠿⠿⠙⠓⢒⣺⡿⠋⠁
⠉⠉⠉⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀
오랜만에 아무일도없는 평범한 바다입니다...
        """


class VictoryTile(MapTile):
    def intro_text(self):
        return """
⠀⠀⠀⠀⠀⠀⠀⢀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⠀⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣧⡀⠀⠀⣼⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⢀⣴⡶⠀⠀⠀⠀⠀
⠀⢸⣿⣧⠀⣰⡏⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣈⣧⠈⠻⣿⣦⣀⣀⠀⠀⠀⣸⣿⣿⣿⣆⠀⠀⠀⣴⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠘⡏⢿⣧⣿⠀⢀⣿⠁⠀⢀⣾⡇⠀⠀⠀⣀⠤⠖⠂⠉⠉⠀⠀⠀⠀⠀⠸⡏⣀⣀⣭⣷⣄⠉⠉⠒⢻⣿⣿⣿⣿⡆⢀⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⣤⣇⠘⣿⠇⠀⢸⡇⠀⢠⣾⣿⣀⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢻⣽⣿⣿⣿⣧⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⢸⣿⣿⡀⢻⡇⢠⡿⠀⣰⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣷⡀⢸⣿⣿⣿⣿⠏⠙⢿⣿⣿⣇⠀⠀⠀⠀⢀⣶
⢸⣿⣿⣧⣈⣧⡿⠁⢠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⡏⠀⠀⣼⢹⣿⣿⠀⠀⠀⢀⣾⣿
⣿⡟⢿⣿⣿⣿⠁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠳⡀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡆⢹⣿⣿⠁⠀⢀⢛⣼⣿⣿⠳⣄⢀⣾⣿⣿
⢻⡇⠀⢻⣿⣇⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠘⢦⣀⡀⠀⠀⠈⠻⣿⣿⣿⣇⠀⣿⡟⠀⠀⡞⣿⣿⣿⣿⠀⠘⣿⡗⣿⣿
⠈⣧⠀⠈⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠈⠙⡓⠶⣤⣄⡈⠻⣿⣿⣧⣸⡇⡆⠀⢳⣿⣿⣿⡇⠀⣸⣏⠁⣿⣿
⠀⠹⡆⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠉⠳⢦⡈⠛⠷⣿⣿⣿⣿⣅⠁⠀⣿⣿⣿⡟⠀⢰⣿⠃⠀⣼⣿
⠀⠀⢻⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⣄⣌⣲⣄⠸⣿⡿⣿⣿⣷⣴⣿⣿⠟⠀⠀⣿⡿⠀⠀⣸⡟
⠀⠀⠘⣿⡏⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⣿⣿⢿⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣷⣿⣧⠈⠻⢿⣿⣿⠋⠀⠀⢸⣿⠇⠀⣼⡿⣇
⠀⣀⡴⢋⣴⣿⣿⣿⣿⣿⡷⠿⣿⣿⣿⢣⣾⣿⣿⣿⣿⣷⣭⣙⠶⡄⠀⠀⢰⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣧⠀⠘⠛⣿⣆⠀⠀⣿⡇⠀⢀⣿⠇⢸
⠀⢻⠀⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠈⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡄⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣇⠀⠀⠈⢻⡆⢸⠃⠀⠀⣾⠏⠀⢸
⠀⠈⡇⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⡄⠀⠀⢿⡟⠀⣠⣼⣿⠇⠀⢼
⠀⠸⣅⢷⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⡇⠀⠀⢧⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⢠⣿⣿⣿⡿⣿⣿⠀⠀⡟
⠀⣀⡿⠈⢿⣿⣿⡇⢻⣿⡗⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣸⠁⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⠿⠋⣴⣿⣿⠀⢀⡟
⠀⡿⠁⠀⠼⠛⢹⣯⣸⣿⣷⡄⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⡿⠛⠁⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠉⢿⡿⠿⠟⣻⡟⠁⢠⡾⠛⢩⣿⣰⡿⠀
⠸⡇⠀⠀⠀⠀⢸⠇⠿⠋⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠁⠀⠀⣠⡴⢻⣿⣿⣶⣶⣶⣾⡿⠀⡖⢸⡇⠀⢠⡟⣠⡾⣋⣴⣴⠟⣽⣿⠃⠀
⠀⢷⠀⢀⡾⣤⣼⣶⡖⠶⣿⠃⠀⠀⠀⠀⠀⢲⣷⣶⡶⠶⠆⣀⣀⣠⣴⠟⡟⠀⠀⠻⣿⣿⣿⣿⣿⠁⢨⠃⣸⣿⣦⣿⣟⣩⣾⡿⠋⣡⣾⣿⠃⠀⠀
⠀⠀⠉⠉⠀⢰⠏⠈⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣏⣴⣾⣿⡟⠁⠀⠀⣸⡇⠀⠀⠀⢿⠻⠿⢫⠏⠀⠀⠀⣿⣿⣿⣿⣿⠿⠁⣶⣴⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⢀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⠏⣿⡇⠀⢀⣾⣿⠧⠀⠀⠀⢸⡄⣰⠟⠀⠀⠀⢠⣿⣿⣿⣯⣁⣠⣾⣿⣿⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠋⢰⣿⣿⣶⡾⣿⣿⠇⠀⣠⠞⢉⠜⠁⡴⠀⢀⣴⡟⠉⠀⠉⠛⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣹⣶⡦⣴⢲⣴⢦⡤⣤⣤⣄⣤⣤⣤⣤⣤⣴⡿⠋⠙⢿⣯⣿⣿⠀⡰⠃⠀⠋⠀⡼⠁⠀⡞⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡏⣿⢰⡇⢰⠇⢸⡇⣸⣨⣇⣸⣏⣸⢇⣾⣿⣀⣠⠤⠤⠵⣫⠏⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣟⢿⢿⣿⣷⣿⣹⣇⣿⣸⣧⠥⠿⠴⠜⠋⠁⠀⠀⡴⠞⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠛⠉⠉⠙⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣴⣶⠾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⣠⣾⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⢀⣀⡀⣀⡀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⠶⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢷⣂⣀⣀⣀⣍⣳⣶⣾⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
당신은 험난한 여정끝에 보물섬을 찾으셨습니다! 당신의 명성이 영원히 울려 퍼질겁니다!
        """

    def modify_player(self, player):
        player.victory = True

class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class alligator(Enemy):
    def __init__(self,damage=None):
        self.name = "정글출신악어떼"
        self.hp = 15
        if damage is None:
            damage = random.randint(1,10)
        self.damage = damage

class pirates(Enemy):
    def __init__(self,damage=None):
        self.name = "스패로우일당"
        self.hp = 40
        if damage is None:
            damage = random.randint(10,20)
        self.damage = damage

class shark(Enemy):
    def __init__(self,damage=None):
        self.name = "사람먹는죠스"
        self.hp = 75
        if damage is None:
            damage = random.randint(20,30)
        self.damage = damage

class kraken(Enemy):
    def __init__(self,damage=None):
        self.name = "전설의크라켄"
        self.hp = 100
        if damage is None:
            damage = random.randint(30,50)
        self.damage = damage
        
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = alligator()
            self.alive_text = """
정글출신악어떼가 저마다의 입을 크게 벌리며 물 속을 엉금엉금 기어온다\n""" \
                           	"굶주린 악어떼가 공격해옵니다."
            self.dead_text = "악어들의 시체가 즐비합니다"
        elif r < 0.70:
            self.enemy = pirates()
            self.alive_text = "철벅철벅 바다를 가르며 스패로우일당이 돌격해온다"\
                              "괴성을 지르며 공격해옵니다."
            self.dead_text = "해적들이 쓰러져있습니다..."
        elif r < 0.90:
            self.enemy = shark()
            self.alive_text = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
거대하고 날카로운 이빨을 가진 사람먹는죠스가 빠른 속도로 다가온다\n""" \
                              "상어가 점점다가오더니 공격해옵니다.."
            self.dead_text = "죽어있는 상어가 보입니다."
        else:
            self.enemy = kraken()
            self.alive_text = "바다가 진동합니다!\n"\
		        "전설의크라켄이 깊은 바다 속에서부터 천천히 그 자체를 드러낸다"	
            self.dead_text = "크라켄의 거대한 시체가 떠있습니다."

        super().__init__(x, y)
    
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        if self.enemy.name == "정글출신악어떼" and self.enemy.hp == 15:
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⢾⣿⣿⣻⡛⠛⠛⠻⠿⣶ ⢵⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢋⣻⣾⡿⢿⣿⠿⢷⣦⡴⣄⠈ ⠓⣯⢻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⣷⠖⣏⣅⡼⠗⠛⠙⠻⢷⣽⣿⣿⣿ ⡀⠈⢧⠙⠛⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⢋⣿⠛⣦⠎⠁⠀⠀⠀⠀⠀⠀⠈⢻⡟⣿ ⣿⣤⡸⢧⠘⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣳⡿⣷⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿ ⣿⣥⠄⠘⣇⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⡟⣷⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣹ ⣿⡀⠐⠒⢿⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⢀⣴⡿⣿⠿⣽⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿ ⣼⠗⠒⠲⡟⢼⣷⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣟⠳⣴⡾⢿⣿⣟⣻⡾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣁ ⢯⠀⠀⡼⠁⡿⣯⣹⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⣿⣿⣯⡼⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣉⣴⣴⡋ ⠉⠉⡾⠁⣼⢻⢿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⡴⠞⢿⠃⣴⠿⠉⠈ ⣥⠾⢧⣼⣟⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⠵⣚⣿⣧⣤⣖⡟⠛⣥⣴⢞ ⠙⣢⣞⣉⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣖⣻⢍⣯⣼⠿⠿⢬⡞⠉⢉⣻⡾⣻⠉⢻ ⣾⡟⣨⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡴⣾⣿⡅⢠⣽⠿⠉⠛⠶⠊⢠⣝⣶⣞⡫⠄⠈⣳⣿ ⣋⣹⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠿⣇⣠⣤⠿⠯⣄⡴⠂⢀⢤⣷⠛⠡⢮⡀⠀⢀⣼⠏⠁ ⢈⣿⠉⠙⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡃⣠⣴⡏⠙⣾⠲⠂⣠⠿⠷⠿⠿⢷⣅⠀⠀⣣⣴⠟⠛⢲⡄ ⣸⠏⢘⠃⠈⢿⣍⣷⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⢹⠟⠯⠽⢟⣡⡶⠚⠻⣥⡄⠀⠋⣠⣄⣵⣶⣯⠈⠳⣴⣀⣿ ⠏⠀⣯⣦⡖⢠⠟⣛⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣠⡤⠤⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠤⣤⡴⣯⡴⠷⣤⣯⣤⢾⣵⠞⠻⠦⣼⠋⣡⣴⣶⣞⠿⠉⠀⠈⣿⣴⣤⡿⠛⁁ ⣠⣾⣿⣿⣿⣶⡄⡿⣽⣿⣇⠀⠀⠀⠀
⠀⣠⠞⣫⣥⠀⠀⢠⣤⣽⢦⣤⣄⣠⡤⠤⠶⢋⣡⡴⠶⠛⠻⣉⣹⢶⣷⣚⠉⠽⠧⠚⠁⢀⣾⠿⠭⡓⠈⢻⡄⢀⣴⣤⣤ ⣿⣿⣿⡟⠻⢿⣿⣿⢿⡿⠛⠶⢤⣄⡀
⣾⢡⠾⠋⠁⠀⠀⠈⠋⠁⠀⠉⠻⣭⢦⣤⣼⠋⠁⠀⠤⠴⠛⠹⠿⠿⣯⣽⣓⢦⠴⠞⠋⠁⠾⢿⣰⠿⣟⡿⠿⠭⠾ ⣿⣿⣿⠃⠀⢠⣿⣍⠤⣴⣌⠛⢮⣻⣿
⠙⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣘⠃⠒⠠⡀⠀⠀⠀⠀⠀⡠⠤⠤⠤⠄⠀⠉⠀⠢⡶⣶⣴⣶⡀⣳⣴⠿⠂⣤⠐⣷⣴⣶⣶⣾⣿⣿ ⠟⠋⠀⠀⠀⠀⠀⠁⠀⠀⠈⠙⠛⠛⠛
⠀⠙⠻⣿⣶⣤⣬⣥⣶⡶⡾⡿⣶⣯⠀⢀⣀⣴⣦⣄⠸⠂⠀⣀⣀⣀⣠⣀⡀⠀⢰⠀⠀⠋⣿⣿⣿⠉⠻⡄⠀⢀⠀⠈⢿⡯⣿⣿⣻ ⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠻⢾⠀⠈⠈⠛⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣨⣿⠀⢀⡞⠀⠀⠀⠛⣿⣿⣾⣷⣿⣤⣷⣤⣀⣤⠞⠉⠀⠀⠀ ⠀⢙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢟⠛⢛⡾⣡⣿⠿⠛⠋⠉⠙⢻⣿⡁⠨⠷⡟⠀⢀⠸⣿⣤⣿⣿⣿⣿⣿⣿⡿⣿⣟⡥⠴⠶⣿⣿⠛ ⣣⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢿⣿⡵⠋⡠⠋⠁⠀⡠⠂⢀⣰⠛⠉⢀⣠⡴⠃⢘⣟⣽⢏⡟⠛⠛⠛⠛⠋⠁⠀⣾⠋⠀⣀⠀⠉⢩⣿ ⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠦⣄⣤⢶⣯⣉⡿⢿⠋⠶⠚⠁⠀⠀⣀⡤⠶⠛⠁⠀⢀⡾⠋⣁⣶⣞⠟⣰⠟⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⢀⣓⣦⣤⣾⡿ ⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡾⠦⠟⣉⣴⣞⡁⠀⡞⢳⣤⣶⡦⠾⡟⠉⠡⢖⡓⡀⣰⣻⣶⣾⣿⣿⡷⠚⠁⠀⠀⠀⠀⠀⠀⠀⢀⣾⣇⠀⢸⣾⣦⣽⡻ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣿⣦⣄⣀⠀⢨⡲⣽⠟⠷⣾⣿⣿⣶⡶⢟⣻⣽⠟⠋⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⠀⠀⠈⢿⡄⢙⡗⠈ ⣳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⣬⣉⣛⣇⢹⣋⣩⡤⠖⠛⠛⠛⠛⠓⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣭⣥⠤⢾⡇⠀⢈⡿⢿⣄⣻ ⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣢⠏⠀⠀⠙⣿ ⣿⣻⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        if self.enemy.name == "스패로우일당" and self.enemy.hp == 40:
            print("""
⣴⣶⢶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣶⣶⡄
⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡇
⠙⠋⠻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡄⠀⠀⠀⠀⠀⣴⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠙⠁
⠀⠀⠀⠈⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⡟⠛⠀⠛⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⡿⠿⠟⠀⠀⠀⠛⠻⣿⣷⣄⠀⠀⠀⢀⣴⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣷⣄⣤⣾⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⣤⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠻⣷⡀⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⣠⠛⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣶⣦⣠⣴⣾⣿⠟⠉⠙⢆⠈⠻⡦⡈⠳⡄⠀⠀⠀⠀⠀⠀⣠⠊⢠⣾⠟⢀⠜⠉⠉⢻⣿⣶⣤⢤⣶⣦⠀⠀⠀
⠀⠀⠈⢿⣿⣬⣿⠋⠋⠀⠀⠀⠀⠑⢄⠙⢾⢦⠈⢢⡀⠀⢠⠞⢁⣴⠟⢁⡴⠋⠀⠀⠀⠈⠛⢻⣿⣽⣿⠛⠀⠀⠀
⠀⠀⠀⠸⠏⠉⠋⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠑⢕⢄⢙⡖⠁⣰⡟⠁⡠⠊⠀⠀⠀⠀⠀⠀⠀⠈⠋⠁⠻⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣀⡵⠋⡠⡾⠋⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢠⠾⠋⢀⠞⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⢁⠔⠃⢀⣴⠉⢢⣀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⡰⠋⢀⡴⠋⠀⠑⢄⠙⢥⣄⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⡠⠎⠁⡠⠋⠀⠀⠀⠀⠀⠳⣄⠙⢧⡈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠁⣠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠐⠆⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⠃⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠑⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠜⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠈⢦⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣏⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⣣⡀⠀⠀⠀
⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀
""")
        if self.enemy.name == "사람먹는죠스" and self.enemy.hp == 75:
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠋⠉⠉⠙⠻⢿⣿⣷⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⠻⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣷⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣠⣤⣶⣶⣾⣿⣿⣿⢿⣿⣷⣦⣄⠀⠀⠙⣷⣄⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡿⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⠿⠛⠛⣏⠉⠉⢻⡄⠀⢹⠉⠛⣿⣧⡀⠀⠈⢿⣷⡄⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠁⠀⠀⠀⢀⣤⣾⣿⣿⠿⠋⠉⣿⡀⠀⠀⢸⣦⠀⢸⣷⠀⢸⣧⠀⣿⠙⣿⡄⠀⠈⣿⣿⣦⡀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠃⠀⠀⢀⣴⣿⣿⡿⠋⠹⣦⡀⠀⢿⣿⣆⠀⣿⣿⣇⣿⣿⣦⣿⣿⣄⣿⡇⣿⢻⡀⠀⠘⣿⣿⣿⣆⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⢠⣿⣿⠟⠁⢢⡀⠀⣿⣿⣦⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⢀⣧⠀⠀⢹⣿⣿⣿⣷ ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⣾⣿⠛⣆⠀⠘⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⣿⣿⣿⣿ ⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⣿⡇⠀⠹⣿⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠈⢿⣿⣿ ⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⢿⡗⣦⣄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠙⢿ ⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀⢸⣇⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠻⢿⣿⡷⠈⢿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀ ⠙⢿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣧⠀⠀⢿⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢻⣿⣿⡇⠀⠀⢻⠇⠀⠀⢿⠙⡟⢻⣉⡿⠀⠀⠀⠀⠀ ⠀⠀⠙⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡀⠀⠈⢷⣽⣿⣿⣿⣿⣿⣿⡏⠻⣿⣿⠀⠀⠙⢿⣇⣀⣤⣬⣤⣤⣤⡤⠶⠖⠋⠉⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠈⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣧⠀⠈⠙⠂⣠⣴⠿⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠘⣿⣿⣿⣿⡌⠛⠆⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢻⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠹⣿⡻⢄⣙⡴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠸⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠚⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣷⣮⣛⠿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣷⣄⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡀⠀
⠀⠀⠀⢀⣀⣠⣶⣾⣿⡿⠿⠛⠿⢿⣿⣿⣷⣾⣥⣄⣀⣀⣀⣀⣀⣀⠀⢀⣠⣶⣄⡀⢤⣀⣀⣀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿ ⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀
⠈⠉⠉⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠛⠛⣉⣤⣾⣿⣿⣿⣿⣿⣦⣀⠉⠛⠛⠛⠛⠛⠛⠛⠉⠀⠀⠀ ⠿⠿⢿⣿⣿⣿⣶⣶⣶⣶⠶⠶⠶⠚⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⣿⣿⣿⠿⠛⠉⠉⠛⠻⢿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠴⠶⠿⠿⠿⠛⠛⠋⠉⠀⡀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠶⢶⣤⣤⣄⡀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
        if self.enemy.name == "전설의크라켄" and self.enemy.hp == 100:
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠒⠛⠒⠒⠢⠤⠐⠲⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⢀⣾⣦⡶⠀⠀⠀⠀⠀⡼⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⠴⠓⠉⠁⠀⠀⠀⢠⠄⢰⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠉⠀⠀⠀⠀⠀⠀⢠⡏⠀⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡚⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⢁⡾⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠺⠥⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠖⠒⠖⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠾⠛⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡔⣡⣿⠿⠛⠿⣦⡌⢦⠀⠀⠀⠀⠀⠀⠀⣠⠎⢁⡤⠒⢢⣄⠈⠳⡄⠀⢀⣤⠀⣦⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡀⢀⣼⣵⠟⠁⢀⣀⣀⣈⣿⠘⣆⠀⠀⠀⠀⣠⣴⡃⠀⢸⡄⣿⣿⠟⡇⠀⢻⡆⣤⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⢿⡿⠟⠉⡴⠊⣁⣤⣀⡀⠉⠳⢬⣓⠒⢊⡉⠀⠉⠁⠀⠈⠳⠼⠤⠞⠁⢀⠞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠞⡰⠊⠀⢀⣀⣨⣷⣤⣄⣈⣉⣁⣀⠔⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢷⣤⣴⣫⣿⣶⣾⡿⢿⠛⢛⣩⣿⣿⠿⠛⠋⠀⣠⡞⠀⡠⠀⣼⠗⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢁⣿⠟⠉⣠⣴⣞⣿⣿⣿⡟⢁⡤⣶⣲⣯⣿⡇⠀⡇⠀⡇⠀⠀⠀⣀⡤⠤⠒⠒⠒⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣏⠏⢀⣾⣿⡟⠋⠉⠁⠀⣇⠘⣶⣿⡿⢻⣿⣧⠀⠻⣄⠙⠒⠒⠋⣀⠤⠶⠛⠛⠛⠲⡄⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⠀⢸⣿⡇⠀⠀⠀⠀⣠⣾⣦⡘⢿⡀⠈⣿⣿⣷⣄⡈⠳⣖⡒⠉⠀⠀⠀⠀⠀⠀⣰⢻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢹⡿⡀⠀⣿⡇⠀⠀⢠⣾⣽⠟⠉⠑⢄⠱⡀⠙⣿⣿⡸⡏⠒⠤⠍⡑⠒⢄⠀⠀⠀⠀⣿⢻⡀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣇⢳⡴⠿⠃⠀⠀⣿⣿⠁⠀⠀⠀⢸⢂⡇⠀⠈⣿⣷⣽⣄⠀⠀⠈⠱⡄⢱⡀⠀⠀⠈⠓⠛⠻⠿⠛⠟⠓⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢦⠱⡄⠀⠀⠘⣿⣿⠀⠀⢀⡴⣫⠞⠁⠀⠀⠘⣇⢻⠫⡳⡀⠀⠀⡇⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠳⣜⣆⠀⠀⠈⢻⣧⠀⢺⣿⠁⠀⠀⠀⠀⣰⠟⢸⠀⠘⢯⣢⡀⣅⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡓⢤⣀⠀⠿⠀⠀⠉⠁⠀⠀⣠⢞⣣⠔⠋⠀⠀⠀⢻⣧⠘⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡧⣾⣻⣦⠀⠀⠀⠀⠀⠀⣴⡿⠉⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠈⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣇⢿⣿⣿⠀⠀⠀⠀⠀⠀⠹⣷⠄⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣚⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣝⠻⢆⠀⠀⠀⠀⣠⣶⣿⣿⣟⣷⣶⠤⢤⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⢰⠧⠝⠛⠛⠻⠿⠴⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
        return text
    
    def modify_player(self, player):
        if self.enemy.name=="정글출신악어떼" and self.enemy.is_alive():
            aran=random.randint(1,10)
            player.hp = player.hp - aran
            print("정글출신악어떼가 {} 만큼 피해를 주었습니다. 현재 체력: {} HP."
                  .format(aran, player.hp))
        elif self.enemy.name=="스패로우일당"and self.enemy.is_alive():
            pran=random.randint(10,20)
            player.hp = player.hp - pran
            print("스패로우일당이 {} 만큼 피해를 주었습니다. 현재 체력:{} HP."
                  .format(pran, player.hp))
        elif self.enemy.name=="사람먹는죠스"and self.enemy.is_alive():
            sran=random.randint(20,30)
            player.hp = player.hp - sran
            print("사람먹는죠스가 {} 만큼 피해를 주었습니다. 현재 체력: {} HP."
                  .format(sran, player.hp))
        elif self.enemy.name=="전설의크라켄"and self.enemy.is_alive():
            kran=random.randint(30,50)
            player.hp = player.hp - kran
            print("전설의 크라켄이 {} 만큼 피해를 주었습니다.현재 체력:{} HP."
                  .format(kran, player.hp))   


class TraderTile(MapTile):
    def intro_text(self):
        return """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠉⠉⠉⠓⢦⡀⠀⠀⠀⠀⢀⡤⠚⠉⠉⠉⠑⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠤⠔⠒⠶⠏⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠙⠶⠒⠲⠤⣄⠀⠀⠀⠀
⠀⠀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣇⠀⠀⣸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀
⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠚⠉⠉⠀⠀⠉⠉⠓⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⣀⣠⡤⣤⡀⠀⠀⠀⣤⡤⣄⣀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠸⠛⠉⠁⠉⠀⠀⠀⠀⠉⠉⠉⠛⢥⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠀
⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⡾⠀⡴⠋⠉⠉⠳⣄⠀⠀⠀⠀⢠⠖⠉⠉⠙⢦⠀⢧⠀⠀⠀⠀⠀⠀⠀⣼⡃⠀
⢀⡞⠁⠀⠀⠀⠀⠀⠀⣾⠃⡜⠀⠀⠀⡆⠀⠘⡆⠀⠀⢰⠃⠀⢰⠀⠀⠀⢳⠈⡇⠀⠀⠀⠀⠀⠀⠀⢷⡀
⢸⠀⠀⠀⠀⢀⡴⠒⠒⣿⣰⠁⠀⣠⣴⣿⣤⠀⢹⠀⠀⡎⠀⣰⣾⣧⣄⠀⠈⡆⣿⠖⠒⢦⡀⠀⠀⠀⠈⡇
⠘⣆⠀⠀⠀⢸⠀⢠⠀⠉⣿⠀⠀⢿⣿⣿⣿⠀⢸⣆⣀⡇⠀⣿⣿⣿⣿⠀⠀⣿⠃⠀⡄⠀⣷⠀⠀⠀⣰⠃
⠀⠈⠳⣄⣀⢸⡄⠀⣧⢠⠋⠳⢄⣀⡙⡟⢡⡶⣿⣿⣿⣿⣦⡈⢻⠓⣀⣠⠴⠛⡄⢸⠁⢀⡏⣀⣠⠞⠁⠀
⠀⠀⠀⠀⠀⠉⠹⡄⠁⢸⡶⠒⠒⢲⡄⠁⣾⣡⣠⡿⠁⠈⣿⣷⠈⢀⣴⠛⠒⢶⠆⠀⢀⡎⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡁⠒⡖⠃⢰⠀⢻⣿⣏⡀⣀⣴⣿⡟⠀⡜⠈⢲⠖⠈⡇⠀⢸⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢧⠀⠈⡇⠀⢱⠀⠀⢣⠀⠙⠻⠿⠿⠟⠋⠀⡰⠁⠀⡜⠀⢰⠁⠀⡾⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠣⡀⠘⡄⠀⠱⣄⠀⠉⠒⠤⠄⠠⠤⠖⠊⠀⢀⠞⠀⢠⠇⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⢦⡈⠢⡀⠈⠑⢤⣄⣀⣀⣀⣀⣠⣤⠞⠁⢀⡴⢃⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠿⣦⡈⠐⠢⠀⠉⠙⠛⠛⠛⠉⠀⠀⠐⢁⣴⡿⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣶⣶⣿⣦⡀⠀⠀⠀⠀⠉⠀⠀⠀⢀⣴⣿⣵⣶⣶⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣵⣾⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠈⠙⢿⣟⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠛⠛⠓⠛⠙⠋⠋⠛⠟⠛⠟⠃⠚⠻⠛⠛⠀⠀⠃⠸⠛⠛⠓⠏⠟⠛⠰⠟⠂⠀⠀⠀⠀⠀
골드만있다면 누구에게나 물건을 거래하는 떠돌이상인이나타났다.
        """
    def __init__(self,x,y):
        self.trader = Characters.Trader()
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {}, {} - {} Gold".format(i, item.name, item.description, item.value))
        while True:
            user_input = input("아이템을 고르거나 q를 입력해서 나가기")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice-1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("올바른 선택지가 아닙니다.")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("그정도론 살수없네")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("거래완료!")

    def check_if_trade(self, player):
        while True:
            print("물건을 사겠나(B)아님 팔겠나(S).(떠나기(Q))")
            user_input = input()
            if user_input in ['q', 'Q']:
                return
            elif user_input in ['B', 'b']:
                print("내가 가진물건은 이정도라네: ")
                self.trade(buyer = player, seller = self.trader)
            elif user_input in ['S', 's']:
                print("자네가 팔수있을만한 물건은 그정돈가?")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("올바른 선택지가 아닙니다.")

class DamageTile(MapTile):
    
    def intro_text(self):
            return"""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⡿⠿⠭⠤⠀⠀⠀⠈⠉⠉⠙⠛⠷⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⠟⠋⠁⠀⠀⠀⠒⠒⠲⠶⠶⢶⣶⣶⣤⣤⣤⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣾⣿⣿⣿⣿⡿⠶⠶⠤⠤⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠘⣿⣿⡿⠋⠉⣀⣀⣠⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣴⣶⡿⠛⠋⠉⣁⣀⣀⣀⣀⣀⣀⣀⣀⠰⣿⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣏⠀⠀⠀⠀⠈⠉⠉⣉⣉⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⠿⢿⣦⡀⠀⠀⠀⠈⠉⠉⠉⠉⢉⠉⠛⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢈⣻⣶⣶⡶⠿⠟⠛⠛⠛⠛⠛⠛⠛⢿⣿⣶⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠿⣦⡀⠀⠀⠀⣀⣀⡀⠠⣤⣸⡟⠋⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣈⣻⣦⣤⣤⣄⣉⣛⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠂⠈⠉⠉⠉⠉⠙⢿⣍⠛⠛⠻⠿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⢀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣇⠀⢀⣼⠿⠟⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀
폭풍우에 갇혔습니다!
            """
    def modify_player(self, player):
        damrand = random.randint(30,80)
        player.hp = player.hp - damrand
        print("{} 만큼 배가 손상되었습니다..현재 내구도 : {}".format(damrand,player.hp))

class HealTile(MapTile):
    
    def intro_text(self):
            return"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠶⣦⣄⠀⠀⢀⣴⣿⣷⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡇⡖⠂⠙⠗⣠⣾⣿⣿⣿⣥⣀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣇⢣⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢧⠘⠿⠟⠛⣉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⠳⣄⠀⠀⣿⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⣉⣁⡿⠀⠀⠀⠀⠀
⠀⢀⣤⣤⣤⣤⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣿⣷⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⢩⣿⣿⣿⠋⠀⠈⠻⢿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⡿⠁⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
해적항구에서 배불리 먹고 배를 수리했습니다!
            """
    def modify_player(self, player):
        healrand = random.randint(300,500)
        player.hp = player.hp + healrand
        print("{} 만큼 배가 수리되었습니다..현재 내구도 : {}".format(healrand,player.hp))
    
class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(100, 300)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} 골드를 얻었습니다!".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠔⠂⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢤⠀
⠀⠀⠀⠀⠀⠀⠀⠠⡎⢠⣀⠀⠀⣀⣸⠀⠀⠀⠀⠀⢀⡠⠤⢊⣁⣀⣠⡗
⠀⠀⠀⠀⠀⠀⠀⠀⢷⣿⣻⣿⣿⣿⠁⠀⠀⣀⠤⠔⢋⢀⣠⣬⣛⣷⡟⠃
⠀⠀⠀⣠⠖⠒⠢⣔⠟⣿⣿⣿⣿⣷⣱⣀⠎⠀⣠⠰⣿⣿⣷⡿⠟⠁⠀⠀
⠀⠀⢸⡁⠀⠀⠀⠈⠉⠉⠻⣟⣟⣮⢿⣅⣄⡴⠙⣷⣿⡽⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣶⣀⠀⠀⠀⢹⣿⣾⣿⣿⣟⣫⣶⠟⣻⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣨⠆⢿⣿⣵⣦⣶⣾⣿⣿⣿⣿⢿⡛⣡⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠏⠀⠈⢳⣾⣿⣿⣿⣿⣿⣿⢿⣩⢧⣽⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣷⣀⠀⠀⠙⠳⣿⣿⢿⣻⣿⣾⣷⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡼⠉⠻⣴⡀⠀⠀⣸⣿⢯⣷⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠀⠀⢸⣧⣼⣿⣿⣻⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣸⠁⠀⠱⣾⣿⣿⣿⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢱⠀⠀⠰⡟⠋⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡜⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 골드가있었던것 같은데...
            """
        else:
            return"""
⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣿⣲⣶⣿⣇⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠣⣽⣿⢻⡿⣿⣏⣩⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣿⣼⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣿⣽⣿⣿⡿⠥⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡤⠛⠻⠋⠁⠀⠀⠑⠄⠑⢯⢳⢢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣶⣿⠛⠁⣠⣤⣼⣿⣇⠀⠀⠀⠀⠉⠳⣗⢕⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⡞⢡⠟⠁⠀⣾⣿⠛⣿⣿⢿⣷⡆⠀⠀⠀⠀⠻⡕⠬⣣⠀⠀⠀⠀⠀⠀
⠀⡜⣥⠕⠁⠀⠀⠀⠹⣿⣶⣿⡟⠀⠉⠀⠀⠀⠀⠀⠀⢊⢔⢪⣷⠀⠀⠀⠀⠀
⡜⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⢐⢕⢭⣺⡇⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⢶⣷⡀⣼⣿⠈⣿⣿⠀⠀⠀⠀⠀⠀⢐⡵⣫⣿⡇⠀⠀⠀⠀
⠃⢀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⣠⣻⣾⣟⢏⠇⠀⠀⠀⠀
⠘⡼⡷⣀⠀⠀⠀⠀⠀⠀⠛⠛⠀⠀⠀⠀⠀⢀⣆⠔⠉⢪⢞⢕⣟⣀⣀⠀⠀⠀
⠀⠘⢌⠺⣶⡄⣤⣀⣤⣶⣖⢔⢔⢔⢔⢖⡴⡪⡵⡪⡢⢗⣵⠽⣿⣿⣿⣿⣷⣶
⠀⠀⠀⠷⣮⣥⣭⣭⣭⣬⣭⣥⣵⣓⣓⣉⣹⣞⣕⣬⠾⠾⣻⣿⣿⠿⠿⠭⠉⠀
⠀⠀⠀⠀⠀⠉⠙⠚⠒⣻⣿⣿⣿⣿⣛⣛⡿⠿⠟⠛⠛⠟⠛⠂⠈⠁⠀⠀⠀⠀
운없는 해적이 떨어뜨린 골드를 획득했다!
            """


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


world_dsl = """
|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|
|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|
|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|
|ET|ET|EN|EN|  |EN|FG|TT|EN|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|  |BT|EN|VT|EN|EN|FG|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|FG|TT|EN|EN|FG|EN|TT|FG|EN|EN|ET|ET|ET|ET|
|ET|ET|  |EN|  |FG|FG|EN|EN|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|EN|HT|EN|EN|FG|EN|EN|EN|TT|EN|ET|ET|ET|ET|
|ET|ET|EN|EN|EN|EN|FG|EN|EN|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|EN|DT|  |EN|FG|EN|FG|EN|  |EN|ET|ET|ET|ET|
|ET|ET|  |EN|EN|VT|FG|EN|EN|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|FG|ST|EN|TT|TT|EN|EN|EN|EN|VT|ET|ET|ET|ET|
|ET|ET|  |EN|  |FG|FG|EN|TT|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|EN|FG|EN|EN|FG|EN|EN|EN|TT|EN|ET|ET|ET|ET|
|ET|ET|EN|TT|EN|EN|FG|EN|EN|EN|EN|EN|ET|ET|ET|ET|
|ET|ET|ET|HT|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|
|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|
|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|ET|
"""

world_map = []

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "BT": BoringTile,
                  "ET": EndTile,
                  "DT": DamageTile,
                  "HT": HealTile,
                  "  ": None}

start_tile_location = None
