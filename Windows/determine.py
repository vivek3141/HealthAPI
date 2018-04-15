import sqlite3

ing = "CARBONATED WATER, HIGH FRUCTOSE CORN SYRUP, CITRIC ACID, NATURAL FLAVORS, SODIUM CITRATE, SODIUM BENZOATE (TO PROTECT TASTE)."
ing = ing.upper()
with open("user.txt", "r") as f:
    li = f.read().strip().split("\n")
c = sqlite3.connect("data.db")
cur = c.cursor()
cur.execute()