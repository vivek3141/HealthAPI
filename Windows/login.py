import sqlite3
import sys


class Login():
    def login(self, user, pasw):
        user = user
        pasw = pasw
        c = sqlite3.connect("data.db")
        cur = c.cursor()
        cur.execute("select * from user where username='" + user + "' and pasw='" + pasw + "'")
        li = cur.fetchall()
        if li == [()]:
            return False
        with open("user.txt", "w") as f:
            for x in li[0]:
                f.writelines(str(x) + "\n")
        return True
