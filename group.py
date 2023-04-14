from random import choice

from constants import (
    AGE_IN_DAYS_AT_MENARCHE,
    AGE_IN_DAYS_AT_MENOPAUSE,
    AGE_IN_DAYS_OF_FETUS_AT_BIRTH
)
from male import Male
from female import Female

class Group:
    def __init__(self, initial_male, initial_bleeders):
        self.male = initial_male
        self.kits = []
        self.bleeders = initial_bleeders
        self.breeders = []
        self.days = 0

    def increment_days(self):
        self.check_kits()
        self.check_bleeders()
        self.check_breeders()
        self.days += 1

    def check_kits(self):
        for kit in self.kits:
            kit.increment_age()
            if kit.age_in_days > AGE_IN_DAYS_AT_MENARCHE:
                self.kits.remove(kit)
                self.bleeders.append(kit)

    def check_bleeders(self):
        for bleeder in self.bleeders:
            bleeder.increment_age()
            if bleeder.age_in_days > AGE_IN_DAYS_AT_MENOPAUSE:
                self.bleeders.remove(bleeder)
        if self.bleeders:
            chosen = choice(self.bleeders)
            if chosen.envelop(self.male):
                self.bleeders.remove(chosen)
                self.breeders.append(chosen)

    def check_breeders(self):
        for breeder in self.breeders:
            breeder.increment_age()
            if breeder.fetus.age_in_days > AGE_IN_DAYS_OF_FETUS_AT_BIRTH:
                baby = breeder.give_birth()
                if isinstance(baby, Male):
                    pass
                else:
                    self.kits.append(baby)
                self.breeders.remove(breeder)
                self.bleeders.append(breeder)

    def report(self):
        print("Kits count: "+str(len(self.kits)))
        print("Bleeders count: "+str(len(self.bleeders)))
        print("Breeders count: "+str(len(self.breeders)))
        print("Days: "+str(self.days))
