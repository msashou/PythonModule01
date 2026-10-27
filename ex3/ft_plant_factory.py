class Plant:
    def __init__(
        self, name: str, height: float, plant_age: int,
        growth_rate: float = 0.5
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
    plants = [
        Plant('Rose', 25.0, 30),
        Plant('Oak', 200.0, 365),
        Plant('Cactus', 5.0, 90),
        Plant('Sunflower', 80.0, 45),
        Plant('Fern', 15.0, 120)
        ]

    print('=== Plant Factory Output ===')
    for plant in plants:
        print('Created: ', end="")
        plant.show()
