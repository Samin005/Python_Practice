from ClassPractice.Cat import Cat
from ClassPractice.Dog import Dog
from ClassPractice.Fox import Fox

cat = Cat("Mini")
print(f'{cat.name} {cat.make_sound()}s')

dog = Dog("Scooby", 4)
print(f"{dog.name} has {dog.leg_count} legs and he {dog.make_sound()}s")

fox = Fox('Swiper the fox')
print(f'{fox.name} {fox.make_sound()}s')
