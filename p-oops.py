class Car:

    def __init__(self, door, window, engine):

        self.door = door
        self.window = window
        self.engine = engine

    def engineType(self):
        return "The Car of type window {} has engine {}".format({self.window}, {self.engine})


lemo = Car(2, 2, 'LPG')


# print(lemo.door)

# print(lemo.engineType())


class Tv:

    model = 'LG'
    volume = 1

    def volumeUp(self):

        return self.volume+1

    def volumeDown(self):

        self.volume = self.volume-1


LG = Tv()

print(LG.volumeUp())
