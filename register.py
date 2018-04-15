import sqlite3
class Register():
    def register(self, user, pasw, l, h, s):
        with sqlite3.connect("data.db") as c:
            cur = c.cursor()
            u = user
            pa = pasw
            try:
                cur.execute("INSERT INTO user VALUES(?,?,?,?,?)", (u, pa, l, h, s))
            except sqlite3.Error as e:
                if str(e) == "UNIQUE constraint failed: user.username":
                    return "Username already taken!!"
                else:
                    return str(e)
            c.commit()
