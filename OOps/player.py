# problem solve by using Instance & Class Attributes 
class Player:

    player_count = 0

    def __init__(self, name, level):

        self.name = name
        self.level = level

        Player.player_count += 1

    def display_info(self):

        print("Name:", self.name)

        print("Level:", self.level)

        print()

p1 = Player("Taha", 5)
p2 = Player("Ali", 10)
p3 = Player("Ahmed", 7)

p1.display_info()
p2.display_info()
p3.display_info()

print("Total Players:", Player.player_count)