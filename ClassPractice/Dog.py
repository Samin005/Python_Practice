from ClassPractice.Animal import Animal


class Dog(Animal):
    # python does not support method overloading
    # def move(self, leg_count):
    #     return f'moving with {leg_count} legs!'

    # how to overload a constructor
    def __init__(self, name, leg_count):
        super().__init__(name)
        self.leg_count = leg_count

    def make_sound(self):
        return 'bark'
