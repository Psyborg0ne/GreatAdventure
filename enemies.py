import colors
from classes import NPC
from time import sleep
from codeblin_utils import printc

class Slime(NPC):
    def __init__(self):
        self.name = "Slime"
        self.desc = "A sticky, jelly like creature. Looks tasty!"
        self.stats = {'str': 1, 'agi': 1, 'int': 0}
        self.hpMult = 10
        self.mpMult = 0
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

class Wolf(NPC):
    def __init__(self):
        self.name = "Wolf"
        self.desc = "A fierce creature. Ate little red riding hood's grandma."
        self.stats = {'str': 2, 'agi': 4, 'int': 0}
        self.hpMult = 10
        self.mpMult = 0
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

class Tarantula(NPC):
    def __init__(self):
        self.name = "Tarantula"
        self.desc = "A very big hairy spider. Has venomous bite and can web you in place ."
        self.stats = {'str': 3, 'agi': 8, 'int': 6}
        self.hpMult = 20
        self.mpMult = 3
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

    def spBite(self, enemy: NPC):
        # TODO Add logic for poison special attack
        printc(f"{self.name} bites {enemy.name}")
        sleep(1)
        printc(f"{self.name} fangs inject a deadly {colors.GREEN} poison  {colors.RESET}in {enemy.name} body!")

    def spWeb(self, enemy: NPC):
        # TODO Add logic for root special attacks
        printc(f"{self.name} spits web on {enemy.name}")
        sleep(1)
        printc(f"The web hardens as it comes in contact with air, {colors.BOLD}rooting {colors.RESET}{enemy.name} in place!")