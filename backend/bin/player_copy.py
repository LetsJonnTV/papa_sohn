from user_data import user_res, user


from res import geld, xp, level


class Karakter_Stats:
    def __init__(self, geld, xp, level):
        self.__geld__ = geld
        self.__xp__ = xp
        self.__level__ = level
    def returnen(self):
        dic = {"Geld": self.__geld__, "XP": self.__xp__, "Level": self.__level__}
class Resurcen_Stats:
    def __init__(self, holz, stein):
        self.__holz__ = holz
        self.__stein__ = stein
    def returnen(self):
        dic = {"Holz": self.__holz__, "Stein": self.__stein__}
        return dic

class Player:
    def __init__(self, username, passwort, res_stats, kar_stats):
        self.__username__ = username
        self.__passwort__ = passwort
        self.__res_stats__ = res_stats
        self.__karakter_stats__ = kar_stats

    def returnen(self):
        dic = {"Username": self.__username__, "Passwort": self.__passwort__, "Res_Stats": self.__res_stats__, "Kar_Stats": self.__karakter_stats__}


main_kar_stats = Karakter_Stats(geld, xp, level)
main_res_stats = Resurcen_Stats(user_res[1][2], user_res[1][3])
main_player = Player(user[0],user[1], main_res_stats.returnen(), main_kar_stats.returnen())