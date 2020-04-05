# class team
# batsman, bowler, properties
# method to print  the batting style of the cricketers
# static method - which will check if the person if the person is right handed or left handed
class Team:
    classVariable = "Cricket"

    def __init__(self, batsman=None, bowler=None, wicketkeeper=None):
        self.batsman = batsman
        self.bowler = bowler
        self.wicketkeeper = wicketkeeper

    def style(self):
        return print(self.batsman, self.bowler, self.wicketkeeper)

    @staticmethod
    def batsmanStyle(batsman):
        if batsman == "Right-handed":
            print("He is surely  right-handed batsman")
        elif batsman == "Left-handed":
            print("He is a bowler")
        else:
            print("wicketkeeper")

    @staticmethod
    def bowlerStyle(bowler):
        if bowler == "Right-Handed":
            print("He is surely right hand bowler")
        elif bowler == "Lef-handed":
            print("He is a left hand bowler")
        else:
            print("invalid value entered")


testTeam = Team()
testTeam.batsmanStyle("Right-handed")
# testTeam.bowlerStyle()
# testTeam.wicketkeeperStyle()
