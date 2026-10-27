class Plant:
    def __init__(
        self, name: str, height: float, plant_age: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f'{self.name}: {round(self.height, 2)}cm, '
              f'{self.plant_age} days old')

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.plant_age += 1


if __name__ == "__main__":
    rose = Plant('Rose', 25.0, 30, 0.8)
    start_height = rose.height

    print('=== Garden Plant Growth ===')
    rose.show()
    for i in range(1, 8):
        print(f'=== Day {i} ===')
        rose.grow()
        rose.age()
        rose.show()
    print(f'Growth this week: {round(rose.height - start_height, 2)}cm')
