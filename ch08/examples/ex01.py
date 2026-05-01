class Thing:
    pass


class Inanimate(Thing):
    pass


class Animate(Thing):
    pass


class Sidewalk(Inanimate):
    pass


class Animal(Animate):
    pass


class Mammal(Animal):
    pass


class Giraffe(Mammal):
    pass


reginald = Giraffe()
