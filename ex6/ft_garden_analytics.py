class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def add_grow(self) -> None:
            self._grow_count += 1

        def add_age(self) -> None:
            self._age_count += 1

        def add_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f'Stats: {self._grow_count} grow, '
                  f'{self._age_count} age, {self._show_count} show')

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
        self._stats = Plant.Statistics()

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f'{self._name}: {round(self._height, 2)}cm, '
              f'{self._plant_age} days old')
        self._stats.add_show()

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats.add_grow()

    def age(self, days: int = 1) -> None:
        self._plant_age += days
        self._stats.add_age()

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

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> "Plant.Statistics":
        return self._stats

    @staticmethod
    def check_year_old(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False


class Flower(Plant):
    def __init__(
        self, name: str, height: float, plant_age: int,
        color: str, growth_rate: float = 8.0,
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
    class TreeStats(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def add_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f'{self._shade_count} shade')

    def __init__(
        self, name: str, height: float, plant_age: int,
        trunk_diameter: float, growth_rate: float = 0.5,
    ) -> None:
        super().__init__(name, height, plant_age, growth_rate,)
        self._trunk_diameter = trunk_diameter
        self._tree_stats = Tree.TreeStats()
        self._stats = self._tree_stats

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter}cm')

    def produce_shade(self) -> None:
        print(f'Tree {self._name} now produces a shade of '
              f'{self._height}cm long and {self._trunk_diameter}cm wide.')
        self._tree_stats.add_shade()


class Seed(Flower):
    def __init__(
        self, name: str, height: float, plant_age: int,
        color: str, growth_rate: float = 8.0,
    ) -> None:
        super().__init__(name, height, plant_age, color, growth_rate,)
        self._seeds_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f'Seeds: {self._seeds_count}')


def display_stats(plant: Plant) -> None:
    print(f'[statistics for {plant.get_name()}]')
    plant.get_stats().display()


if __name__ == "__main__":
    print('=== Garden statistics ===')
    print('=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.check_year_old(30)}')
    print(f'Is 400 days more than a year? -> {Plant.check_year_old(400)}')
    print('')

    print('=== Flower')
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    display_stats(rose)
    print('[asking the rose to grow and bloom]')
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print('')

    print('=== Tree')
    oak = Tree('Oak', 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    display_stats(oak)
    print('')

    print('=== Seed')
    sunflower = Seed('Sunflower', 80.0, 45, 'yellow', 30.0)
    sunflower.show()
    print('[make sunflower grow, age and bloom]')
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print('')

    print('=== Anonymous')
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)
