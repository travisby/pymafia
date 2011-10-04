import hashlib
import getpass
import random
import dbControl
import os
db = None
db_cur = None


def timechange():
    db_cur.execute('SELECT gtime FROM ADMIN;')
    gtime = db_cur.fetchone()[0] + .5
    db_cur.execute('UPDATE ADMIN SET gtime=?;', gtime)
    if gtime % 2 == 0:
        db_cur.execute('SELECT name FROM PLAYERS;')
        players = db_cur.fetchall()
        for i in range(len(players)):
            db_cur.execute('INSERT INTO VOTES \
            (name,gtime) values (?);', players[i][0])
    else:
        db_cur.execute('INSERT INTO ROLEMOVES (gtime) values (?);', gtime)
    db.commit()


def kill(player, gtime, killer):
    db_cur.execute('UPDATE PLAYER SET status=0 WHERE player=?;', [player])
    if killer == "town":
        db_cur.execute('\
        INSERT INTO LYNCHED (gtime, player) values (?,?);', [gtime, player])
    else:
        db_cur.execute('\
        INSERT INTO MURDERED (gtime, player) values (?,?);', [gtime, player])

    db.commit()
    timechange()


def vote(voter, candidate):
    db_cur.execute('SELECT gsize FROM ADMIN;')
    gsize = db_cur.fetchone()[0]
    db_cur.execute('SELECT gtime FROM ADMIN;')
    gtime = db_cur.fetchone()[0]
    db_cur.execute('UPDATE PLAYERS \
    SET candidate=? WHERE gtime=? AND player=?;', [candidate, gtime, voter])
    db_cur.execute('SELECT votes FROM VOTES WHERE player=?;', candidate)
    votes = db_cur.fetchone()[0]
    db_cur.execute('UPDATE PLAYERS \
    SET votes=? WHERE gtime=? AND player=?;', [votes, gtime, candidate])
    db.commit()
    if votes > gsize / 2:
        kill(candidate)


def getvariation():
    x = random.randint(0, 5)
    if x == 0:
        return ["goon", "mcop", "townie", \
        "townie", "townie", "townie", "townie", "cop", "doctor"]
    elif x == 1:
        return ["goon", "mcop", "townie", \
        "townie", "townie", "townie", "townie", "cop", "jailkeeper"]
    elif x == 2:
        return ["goon", "mcop", "townie", \
        "townie", "townie", "townie", "townie", "doctor", "jailkeeper"]
    elif x == 3:
        return ["goon", "mcop", "townie", \
        "townie", " townie", "townie", "townie", "townie", "cop"]
    elif x == 4:
        return ["goon", "mcop", "townie", \
        "townie", "townie", "townie", "townie", "townie", "jailkeeper"]
    elif x == 5:
        return ["goon", "mcop", "townie", \
        "townie", "townie", "townie", "townie", "townie", "doctor"]


def distribroles(dbname):
    roles = getvariation()
    random.shuffle(roles)
    db_cur.execute('SELECT name FROM PLAYERS;')
    players = db_cur.fetchall()
    for i in range(len(players)):
        db_cur.execute('UPDATE PLAYERS \
        SET role=? WHERE name=?;', [roles[i], players[i][0]])
    db.commit()


def displayopts(user, gtime, players):
    db_cur.execute('SELECT role FROM PLAYERS WHERE name=?;', [user])
    role = db_cur.fetchone()[0]
    user = "glob!"
    if gtime % 2 == 0:
    # 0 = day0, 1 = night0, 2 = day1, etc.
        name = None
        while name not in players and name is not user:
            name = raw_input("Who would you like to vote for? [q to quit]: ")
            if (name == 'q'):
                return
        vote(user, name, gtime)

    else:
        if role == "goon":
            x = raw_input("Type 'kill [user]' to submit your kill: ")
            kill(x.split('kill'), user)
        elif role == "mcop":
            print "mcop"
        elif role == "cop":
            print "cop"
        elif role == "doctor":
            print "doctor"
        elif role == "jailkeeper":
            print "jailkeeper"
        else:
            print "You have no night time roles.  Please wait until day time."


def mainscreen(user):
    quit = None
    while quit != "q":
        db_cur.execute('SELECT gtime FROM ADMIN;')
        gtime = db_cur.fetchone()[0]
        print "Phase ", gtime
        db_cur.execute('SELECT name FROM PLAYERS WHERE status=1;')
        players = db_cur.fetchall()
        for i in range(len(players)):
            players[i] = players[i][0].encode()
        print "Alive Players: ", players
        db_cur.execute('SELECT name FROM PLAYERS WHERE status=0;')
        deadPlayers = db_cur.fetchall()
        for i in range(len(deadPlayers)):
            deadPlayers[i] = deadPlayers[i][0].encode()
        print "Dead players: ", deadPlayers
        displayopts(user, gtime, players)

        quit = raw_input("Enter q to quit or enter to return to options: ")


def register():
    user = raw_input("Please enter your username over 3 characters: ")
    db_cur.execute('select name from players where name=?', [user])
    if len(user) <= 3 or len(db_cur.fetchall()) >= 1:
        print "That username is invalid, or in use."
        return 1
    pw = getpass.getpass("Please enter your password: ")
    if pw == getpass.getpass("Please enter your password again: ") and \
    len(pw) > 5:

        hashed = hashlib.sha512(pw).hexdigest()
        db_cur.execute('INSERT INTO PLAYERS \
        (name, password) values (?, ?)', [user, hashed])
        db.commit()
        return 0
    else:
        print \
"Either your passwords did not match, or they were not over 5 characters."
    return 1


def main():
    # Get a few variables we need to check if registration is still open
    db_cur.execute('SELECT status FROM ADMIN;')
    gstatus = db_cur.fetchone()[0]
    db_cur.execute('SELECT name FROM PLAYERS;')
    numplayers = len(db_cur.fetchall())
    db_cur.execute('SELECT gsize FROM ADMIN;')
    gsize = db_cur.fetchone()[0]
    # Check if registration is still open, or if they can login
    print gstatus
    if  gstatus == 0 and numplayers < gsize:
        raw_input("Please press enter to register for the new game")
        while register() == 1:
            pass
    else:
        user = login()
        mainscreen(user)


def login():
    user = raw_input("Username: ")
    pw = getpass.getpass("Password: ")
    db_cur.execute("SELECT password FROM PLAYERS WHERE name = ?;", [user])
    try:
        dbhashed = db_cur.fetchone()[0]
    except TypeError:
        print "Incorrect username/password, please try again"
        return 1
    if hashlib.sha512(pw).hexdigest() == dbhashed:
        print "Login successful!"
        return user
    else:
        print "Incorrect username/password, please try again"
        login()


def init():
    print '''

    .########..##....##.........##.....##....###....########.####....###...
    .##.....##..##..##..........###...###...##.##...##........##....##.##..
    .##.....##...####...........####.####..##...##..##........##...##...##.
    .########.....##....#######.##.###.##.##.....##.######....##..##.....##
    .##...........##............##.....##.#########.##........##..#########
    .##...........##............##.....##.##.....##.##........##..##.....##
    .##...........##............##.....##.##.....##.##.......####.##.....##


    by Travis Beatty (travisby@gmail.com)

    '''

    dbname = raw_input(" \
    Please enter the game db name, or the db name of a new game: ")
    if os.path.isfile(dbname) == True:
        if dbControl.testifdb(dbname) == True:
            globals()["db_cur"] = dbControl.db_cur
            globals()["db"] = dbControl.db
            main()
        else:
            print "The filename you provided is not an sqlite database. \
            Please try again, or contact an administrator."
            return 1
    else:
        if raw_input(\
        "Are you sure you wish to create a new game? (y/n)") == "y":
            dbControl.newdb(dbname)
        else:
            return 0


init()
