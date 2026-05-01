class Thing:
    pass


class Inanimate(Thing):
    pass


class Animate(Thing):
    pass


class Sidewalk(Inanimate):
    pass


class Animal(Animate):
    def breathe(self):
        print('breathing')

    def move(self):
        print('moving')

    def eat_food(self):
        print('eating food')


class Mammal(Animal):
    def feed_young_with_milk(self):
        print('feeding young')


class Giraffe(Mammal):
    def __init__(self, spots=100):
        self.giraffe_spots = spots

    def find_food(self):
        self.move()
        print('I\'ve found leaves!')
        self.eat_food()

    def eat_leaves_from_trees(self):
        print('tear leaves from branches')
        self.eat_food()

    def left_foot_forward(self):
        print('left foot forward')

    def right_foot_forward(self):
        print('right foot forward')

    def left_foot_backward(self):
        print('left foot back')

    def right_foot_backward(self):
        print('right foot back')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()


harriet = Giraffe()
harriet.dance()
print(harriet.giraffe_spots)
