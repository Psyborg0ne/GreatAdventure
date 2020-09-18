from codeblin_utils import printc
from time import sleep
import colors


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

    def spDivineLight(self):
        # TODO Heal the character and maybe add 1 turn of invinsibility (Holy Shield)
        printc(f"{self.name} raises his hand and calls forth a divine beam of light {colors.YELLOW}healing {colors.RESET}him")

class Assasin(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "A stealthy character that relies on agility to kill his foes quickly."
        self.stats = {'str': 8, 'agi': 12, 'int': 0}
        self.hpMult = 10
        self.mpMult = 2
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

    def spShadowStep(self, enemy: NPC):
        # Double weapon DMG and chance to instakill or stun
        printc(f"{self.name} hides and emerges from the shadows behind {enemy.name} striking a weak spot.")


class Shaman(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "A magic user that summons minions to fight for him"
        self.stats = {'str': 6, 'agi': 1, 'int': 13}
        self.hpMult = 10
        self.mpMult = 3
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

    def spGaiaFlower(self, enemy: NPC):
        # Roots the target enemy with chance to inflict poison?
        printc(f"{self.name} touches the ground calling the spirits of the forest")
        sleep(1)
        printc(f"Thorny vines emerge from below and {colors.BOLD}root {colors.RESET}{enemy.name} in place")

class Blacksmith(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "A very strong character that dual wield hammers to deal massive amounts of damage."
        self.stats = {'str': 18, 'agi': 2, 'int': 0}
        self.hpMult = 7
        self.mpMult = 0
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

    def spInferno(self, enemy: NPC):
        # TODO Add Ablaze effect
        printc(f"{self.name} starts hitting the ground violently with his hammers causing a magma eruption below {enemy.name}")

class Scavenger(NPC):
    def __init__(self, name):
        self.name = name
        self.desc = "An agile character that recycles everything he finds around to his benefit."
        self.stats = {'str': 6, 'agi': 10, 'int': 4}
        self.hpMult = 10
        self.mpMult = 3
        super().__init__(self.name, self.desc, self.stats, self.hpMult, self.mpMult)

    def spScavenge(self, item: Item):
        # TODO make new battle items? find battle items?
        printc(f"{self.name} takes a quick look around and finds a {colors.CYAN}{item.name} under a pile of trash.")