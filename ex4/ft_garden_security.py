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


if __name__ == "__main__":
    rose = Plant('Rose', 15.0, 10)

    print('=== Garden Security System ===')
    print('Plant created: ', end="")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print(f'Height updated: {rose.get_height()}cm')
    print(f'Age updated: {rose.get_age()} days')
    print()

    rose.set_height(-25)
    rose.set_age(-30)
    print()

    print('Current state: ', end="")
    rose.show()
