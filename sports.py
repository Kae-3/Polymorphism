class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
        else:
            print("Error: score cannot be negative.")


class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
        else:
            print("Error: score cannot be negative.")


Cricket = Cricket("Jarvmi", 76)
Football = Football("Rashant", 3)

for player in (Cricket, Football):
    player.info()
    player.play()

Cricket.__score = 999
print(f"Cricket score remains: {Cricket.get_score()}")


Cricket.set_score(Cricket.get_score() + 1)
Football.set_score(Football.get_score() + 1)
print(f"Updated Cricket score: {Cricket.get_score()}")
print(f"Updated Football score: {Football.get_score()}")
