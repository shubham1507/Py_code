# print("Shri")

# print("Shri" + ' ' + "Ram")

bikes = ['trek', 'redline', 'giant', 2]

print(bikes[-1])

for b in bikes:
    print(b)

sq = []

for x in range(1, 11):
    sq.append(x**x)

print(sq)
# print list in rev order
gadi = (bikes[::-1])

print(gadi)

# Dictionaries

alien = {'color': 'green', 'points': 5}

alien['x_position'] = 0

print(alien)

for color, points in alien.items():
    print(color)

# class


class Dog():
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + " is sitting .")


my_dog = Dog("tiger")

print(my_dog.name + " is good ")

my_dog.sit()


class SarDog(Dog):
    def __init__(self, name):

        super().__init__(name)

    def search(self):

        print(self.name + " is searching")


my_dog2 = SarDog('toffie')

my_dog2.search()

user = []

user.append('val')

print(user[0])

user.insert(3, 'snj')

print(user)

del user[-1]
print(user)

l = []
for i in range(0, 5):
    l.append(i**2)

print(l)

print(l.sort(reverse=True))

for i in range(150):
    print(i, end=' ')

sq = [x**2 for x in range(1, 11)]

print(sq)

names = ['kai', 'abe', 'ada', 'gus', 'zoe']

new_name = [name.upper() for name in names]

print(new_name)

puja_path = {'abhishekh': 'durva', 'panchamrut': 'dugdh'}

print(puja_path)

del puja_path['abhishekh']

print(puja_path)

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, lang in fav_languages.items():
    print(name + " likes " + lang)
