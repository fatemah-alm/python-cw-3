# write your code here
# part 1

favorite_animals = ["Dog", "Cat", "Monkey", "Rabbit"]

print(favorite_animals)

print(favorite_animals[1])

favorite_animals.remove("Monkey")

# part 2

favorite_animals.append("Horse")

for animal in favorite_animals:
    print(f"I love {animal}")

# part 3

numbers = [1, 2, 3, 4, 5]

numbers_sum = 0

for number in numbers:
    numbers_sum += number

print(numbers_sum)