import sqlite3

# Will connect to a database that python creates if it doesn't exist
db = sqlite3.connect("userData.db")

c = db.cursor()

c.execute("CREATE TABLE User (UserID INTEGER PRIMARY KEY AUTOINCREMENT, User_name TEXT)")

c.execute("CREATE TABLE Watchlist (WatchlistID INTEGER PRIMARY KEY AUTOINCREMENT, Watchlist TEXT, UserID INTEGER, FOREIGN KEY(UserID) REFERENCES User(UserID))")

db.commit()