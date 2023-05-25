# Factory Method pattern
class Level:
    def __init__(self, name):
        self.name = name

    def play(self):
        pass

class EasyLevel(Level):
    def play(self):
        print("Playing easy level: {}".format(self.name))

class MediumLevel(Level):
    def play(self):
        print("Playing medium level: {}".format(self.name))

class HardLevel(Level):
    def play(self):
        print("Playing hard level: {}".format(self.name))

class LevelFactory:
    def create_level(self, level_type, name):
        if level_type == 'easy':
            return EasyLevel(name)
        elif level_type == 'medium':
            return MediumLevel(name)
        elif level_type == 'hard':
            return HardLevel(name)

# Abstract Factory pattern
class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("{} attacks with sword!".format(self.name))

class Mage(Character):
    def attack(self):
        print("{} casts fireball!".format(self.name))

class CharacterFactory:
    def create_character(self, character_type, name):
        if character_type == 'warrior':
            return Warrior(name)
        elif character_type == 'mage':
            return Mage(name)

# Singleton pattern
class GameManager:
    instance = None

    @staticmethod
    def get_instance():
        if GameManager.instance is None:
            GameManager.instance = GameManager()
        return GameManager.instance

    def __init__(self):
        self.level_factory = LevelFactory()
        self.character_factory = CharacterFactory()

    def play_game(self, level_type, character_type):
        level = self.level_factory.create_level(level_type, 'Level 1')
        character = self.character_factory.create_character(character_type, 'Player 1')
        level.play()
        character.attack()

# Builder pattern
class MapBuilder:
    def __init__(self):
        self.map = []

    def add_row(self, row):
        self.map.append(row)

    def get_map(self):
        return self.map

class MapDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_map(self):
        self.builder.add_row(['X', 'O', 'X'])
        self.builder.add_row(['O', 'O', 'O'])
        self.builder.add_row(['X', 'O', 'X'])


builder = MapBuilder()
director = MapDirector(builder)
director.construct_map()
map = builder.get_map()
print(map)

game_manager = GameManager.get_instance()

print("Welcome to the game!")
level_type = input("Choose a level (easy, medium, hard): ")
character_type = input("Choose a character (warrior, mage): ")

game_manager.play_game(level_type, character_type)
