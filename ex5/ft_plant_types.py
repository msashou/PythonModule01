class Plant:
    def __init__(
        self, name: str, height: float, plant_age: int,
        growth_rate: float = 0.5
    ) -> None:
        self._name = name
        self._height = 0.0
        self._plant_age = 0
        self._growth_rate = growth_rate
        self.set_height(height)
        self.set_age(plant_age)

    def show(self) -> None:
        print(f'{self._name}: {round(self._height, 2)}cm, '
              f'{self._plant_age} days old')

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._plant_age += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f'{self._name}: Error, height can\'t be negative')
            print('Height update rejected')
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f'{self._name}: Error, age can\'t be negative')
            print('Age update rejected')
        else:
            self._plant_age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age


class Flower(Plant):
    def __init__(
        self, name: str, height: float, plant_age: int,
        color: str, growth_rate: float = 0.5,
    ) -> None:
        super().__init__(name, height, plant_age, growth_rate,)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f'Color: {self._color}')
        if self._bloomed:
            print(f'{self._name} is blooming beautifully!')
        else:
            print(f'{self._name} has not bloomed yet')


class Tree(Plant):
    def __init__(
        self, name: str, height: float, plant_age: int,
        trunk_diameter: float, growth_rate: float = 0.5,
    ) -> None:
        super().__init__(name, height, plant_age, growth_rate,)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter}cm')

    def produce_shade(self) -> None:
        print(f'Tree {self._name} now produces a shade of '
              f'{self._height}cm long and {self._trunk_diameter}cm wide.')


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, plant_age: int,
        harvest_season: str, growth_rate: float = 0.5,
    ) -> None:
        super().__init__(name, height, plant_age, growth_rate)
        self._nutritional_value = 0.0
        self._harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self._harvest_season}')
        print(f'Nutritional value: {round(self._nutritional_value)}')

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5


if __name__ == "__main__":
    print('=== Garden Plant Types ===')
    rose = Flower('Rose', 15.0, 10, 'red')
    oak = Tree('Oak', 200.0, 365, 5.0)
    tomato = Vegetable('Tomato', 5.0, 10, 'April', 2.1)

    print('=== Flower')
    rose.show()
    print('[asking the rose to bloom]')
    rose.bloom()
    rose.show()
    print()

    print('=== Tree')
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print()

    print('=== Vegetable')
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    for _ in range(20):
        tomato.age()
        tomato.grow()
    tomato.show()
