class Individual:
    def __init__(self, key, initial_age=0):
        self.key = key
        self.age_in_days = initial_age

    def increment_age(self):
        self.age_in_days += 1
