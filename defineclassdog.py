class Dog:
    """Blueprint of a dog"""

    # class variable
    # for all instances

    species = ["canius lupus"]

    def __init__(self, n, c):
        self.name = n
        self.state = "sleeping"
        self.color = c

    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "sit":
            self.state = "sit"
        else:
            self.state = "wag tail"

    def bark(self, freq):
        for i in range(freq):
            print(self.name + ":Woof!")


bello = Dog("bello", "black")  # black
alice = Dog("alice", "white")  # white
bello.bark(2)  # bello: woof!

alice.command("sit")
print("alice:" + alice.state)  # alice: sit

bello.command("no")
print("bello:", bello.state)  # bello: wag ail 2 times

alice.command("alice")

bello.species += ["wulf"]
