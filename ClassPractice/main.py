from ClassPractice.Cat import Cat
from ClassPractice.Dog import Dog
from ClassPractice.Fox import Fox

cat = Cat("Mini")
print(f'{cat.name} {cat.make_sound()}s')

dog = Dog("Scooby", 4)
print(f"{dog.name} has {dog.leg_count} legs and he {dog.make_sound()}s")

fox = Fox('Swiper the fox')
print(f'{fox.name} {fox.make_sound()}s')


# Task 3
class Player:
    def __init__(self, player_name):
        self.name = player_name


class Team:
    def __init__(self, name=""):  # serves as a multi-purpose constructor, if the value of name is not given it will take "".
        self.name = name
        self.players = []

    def set_name(self, team_name):
        self.name = team_name

    def add_player(self, player: Player):
        self.players.append(player.name)

    def print_detail(self):
        print('====================================')
        print('Team:', self.name)
        print('List of Players:')
        print(self.players)
        print('====================================')


b = Team()
b.set_name('Bangladesh')
Mashrafi = Player("Mashrafi")
b.add_player(Mashrafi)
Tamim = Player("Tamim")
b.add_player(Tamim)
b.print_detail()
a = Team("Australia")
ponting = Player("ponting")
a.add_player(ponting)
lee = Player("lee")
a.add_player(lee)
a.print_detail()
