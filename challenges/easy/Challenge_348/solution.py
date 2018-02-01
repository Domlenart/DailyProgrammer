class Rabbit(object):
    def __init__(self, gender, age=2):
        self.gender = gender
        self.age = age
        self.alive = True

    def live(self):
        self.age += 1

        if self.age >= 96:
            self.alive = False

        if self.gender == 'Female' and self.age > 4:
            return self.breed()

    def breed(self):
        females = [Rabbit('Female', 0) for _ in range(9)]
        males = [Rabbit('Male', 0) for _ in range(5)]
        born = males + females
        return born


def population_limit(male, female, limit):
    total_alive = 0
    rabbits = [Rabbit('Male') for _ in range(male)] + [Rabbit('Female') for _ in range(female)]
    epochs = 0

    while total_alive < limit:
        epochs += 1
        born_list = []
        for rabbit in rabbits:
            born = rabbit.live()
            if born:
                born_list.extend(born)
        rabbits.extend(born_list)
        total_alive = len(rabbits)
        print(total_alive)
        print(epochs)

population_limit(2, 4, 1500000)

