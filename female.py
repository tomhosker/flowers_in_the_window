from random import random, choice

from constants import FERTILISATION_RATE
from individual import Individual
from male import Male

class Female(Individual):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fetus = None

    def increment_age(self):
        super().increment_age()
        if self.fetus:
            self.fetus.increment_age()

    def envelop(self, male):
        if random() < FERTILISATION_RATE:
            self.fetus = make_fetus(male, self)
            return True
        return False

    def give_birth(self):
        if isinstance(self.fetus, Male):
            baby = Male(self.fetus.key)
        else:
            baby = Female(self.fetus.key)
        self.fetus = None
        return baby

def make_fetus(father, mother):
    GenderClass = choice([Male, Female])
    fetus_key = father.key*mother.key
    result = GenderClass(fetus_key)
    return result
