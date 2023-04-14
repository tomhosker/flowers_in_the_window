from constants import DAYS_IN_A_YEAR, AGE_IN_DAYS_AT_MENARCHE
from male import Male
from female import Female
from group import Group

INITIAL_MALE = Male(2, initial_age=AGE_IN_DAYS_AT_MENARCHE)
INITIAL_BLEEDERS = [
    Female(3, initial_age=AGE_IN_DAYS_AT_MENARCHE),
    Female(5, initial_age=AGE_IN_DAYS_AT_MENARCHE)
]
SIMULATION_LENGTH_IN_DAYS = 200*DAYS_IN_A_YEAR

def run():
    group = Group(INITIAL_MALE, INITIAL_BLEEDERS)
    for _ in range(SIMULATION_LENGTH_IN_DAYS):
        group.increment_days()
    group.report()

if __name__ == "__main__":
    run()
