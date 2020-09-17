from codeblin_utils import printc

class NPC():
    def __init__(self, name: str, desc: str, stats: dict, hpMult: int, mpMult: int):
        self.name = name
        self.desc = desc
        self.stats = stats
        self.hp = self.maxHp = hpMult * self.stats['str']
        self.mp = self.maxMp = mpMult * self.stats['int']

    def printStats(self):
        printc(f"{len(self.name) * '_'}")
        printc(f'|{self.name}|')
        printc(f"+{len(self.name) * '-'}+")
        printc(f'HP: {self.hp}/{self.maxHp}')
        printc(f'MP: {self.mp}/{self.maxMp}')
        for i, j in self.stats.items():
            printc(f"{i.upper()}: {j}") if (len(str(j)) > 1) else printc(f"{i.upper()}:  {j}")

        printc(self.desc)

    def attack(self, enemy):
        printc(f"{self.name} attacks {enemy.name}")
        # TODO Add formula to calculate and apply damage

class Paladin(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "A tanky character that utilizes holy spells to heal."
        self.stats = {'str': 15, 'agi': 0, 'int': 5}
        self.hpMult = 10
        self.mpMult = 2
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

class Assasin(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "A stealthy character that relies on agility to kill his foes quickly."
        self.stats = {'str': 8, 'agi': 12, 'int': 0}
        self.hpMult = 10
        self.mpMult = 2
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

class Shaman(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "A magic user that summons minions to fight for him"
        self.stats = {'str': 6, 'agi': 1, 'int': 13}
        self.hpMult = 10
        self.mpMult = 3
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

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



hero1 = Paladin("Nikos")
hero2 = Assasin("Orfeas")
hero3 = Shaman("Akis")
enemy1 = Slime()
enemy2 = Wolf()

hero1.printStats()
hero2.printStats()
hero3.printStats()
enemy1.printStats()
enemy2.printStats()
