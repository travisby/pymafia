import sqlite3
import bcrypt
import getpass
import random


def getvariation():
    x = random.randint(0,5)
    if x == 0: return ["goon","mcop","townie","townie","townie","townie","townie","cop","doctor"]
    elif x == 1: return ["goon","mcop","townie","townie","townie","townie","townie","cop","jailkeeper"]
    elif x == 2: return ["goon","mcop","townie","townie","townie","townie","townie","doctor","jailkeeper"]
    elif x == 3: return ["goon","mcop","townie","townie","townie","townie","townie","townie","cop"]
    elif x == 4: return ["goon","mcop","townie","townie","townie","townie","townie","townie","jailkeeper"]
    elif x == 5: return ["goon","mcop","townie","townie","townie","townie","townie","townie","doctor"]


def distribroles(dbname):
    db = sqlite3.connect(dbname)
    db_cur = db.cursor()
    roles = getvariation()
    random.shuffle(roles) # Note, random.shuffle() does not return anything.  It modifies the list.
    db_cur.execute('SELECT name FROM PLAYERS;')
    players = db_cur.fetchall()
    x = 0
    for i in range(len(players)):
        db_cur.execute('UPDATE PLAYERS SET role=? WHERE name=?;',[roles[i],players[i][0]])
	db.commit()
    db.close()


def displayopts(dbname,user):
    db = sqlite3.connect(dbname)
    db_cur = db.cursor()
    db_cur.execute('SELECT role FROM PLAYERS WHERE name=?;',[user])
    db.close()


def mainscreen(dbname,user):
    db = sqlite3.connect(dbname)
    db_cur = db.cursor()
    print "Phase: " + db_cur.execute('SELECT gtime FROM ADMIN;')
    db_cur.execute('SELECT name FROM PLAYERS WHERE status=1;')
    print "Alive Players: ", db_cur.fetchall()
    db_cur.execute('SELECT name FROM PLAYERS WHERE status=0;')
    print "Dead players: ", db_cur.fetchall()
    db.close()
    displayopts(dbname,user)


def register(dbname):
    user = raw_input("Please enter your username: ")
    pw = getpass.getpass("Please enter your password: ")
    if pw == getpass.getpass("Please enter your password again: "):
        hashed = bcrypt.hashpw(pw,bcrypt.gensalt(12))
        db = sqlite3.connect(dbname)
        db.execute('INSERT INTO PLAYERS (name, password) values (?, ?)', [user,hashed])
        db.commit()
        db.close()
    else:
        register(dbname)


def main(dbname):
    db = sqlite3.connect(dbname)
    db_cur = db.cursor()
    db_cur.execute('SELECT status FROM ADMIN;')
    gstatus = db_cur.fetchone()[0]
    db.close()
    if  gstatus == 0:
        raw_input("Please press enter to register for the new game")
        register(dbname)
    else:
        login(dbname)


def login(dbname):
    user = raw_input("Username: ")
    pw = getpass.getpass("Password: ")
    db = sqlite3.connect(dbname)
    db_cur = db.cursor()
    db_cur.execute("SELECT password FROM PLAYERS WHERE name = ?;", [user])
    try:
        dbhashed = db_cur.fetchone()[0]
    except TypeError:
        db.close()
        print "Incorrect username/password, please try again"
        login(dbname)
    db.close()
    if bcrypt.hashpw(pw, dbhashed) == dbhashed:
        print "Login successful!"
        mainscreen(dbname,user)
    else:
        print "Incorrect username/password, please try again"
        login(dbname)
