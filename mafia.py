import sqlite3
import os
import bcrypt
import getpass

db = None
db_cur = None

def timechange():
    db_cur.execute('SELECT gtime FROM ADMIN');
    gtime = db_cur.fetchone()[0]+.5
    db_cur.execute('UPDATE ADMIN SET gtime=?;',gtime)
    if gtime % 2 == 0:
        db_cur.execute('SELECT name FROM PLAYERS;')
        players = db_cur.fetchall()
        for i in range(len(players)):
            db_cur.execute('INSERT INTO VOTES (name,gtime) values (?);',players[i][0])
    else:
        db_cur.execute('INSERT INTO ROLEMOVES (gtime) values (?);',gtime)
    db_cur.commit()


def lynch(player,gtime):
    db_cur.execute('UPDATE PLAYER SET status=0 WHERE player=?;',[player])
    db_cur.execute('INSERT INTO LYNCHED (gtime,player) values (?,?);',[gtime,player])
    db_cur.commit()
    timechange()


def vote(voter,candidate):
    db_cur.execute('SELECT gtime FROM ADMIN;')
    gtime = db_cur.fetchone()[0]
    db_cur.execute('UPDATE PLAYERS SET candidate=? WHERE gtime=? AND player=?;',[candidate,gtime,voter])
    db_cur.execute('SELECT votes FROM VOTES WHERE player=?;',candidate)
    votes = db_cur.fetchone()[0]
    db_cur.execute('UPDATE PLAYERS SET votes=? WHERE gtime=? AND player=?;',[votes,gtime,candidate])
    db.commit()
    if votes >= 5: # Set this to something variable~ish for larger games in the future!
        lynch(candidate)


def getvariation():
    x = random.randint(0,5)
    if x == 0: return ["goon","mcop","townie","townie","townie","townie","townie","cop","doctor"]
    elif x == 1: return ["goon","mcop","townie","townie","townie","townie","townie","cop","jailkeeper"]
    elif x == 2: return ["goon","mcop","townie","townie","townie","townie","townie","doctor","jailkeeper"]
    elif x == 3: return ["goon","mcop","townie","townie","townie","townie","townie","townie","cop"]
    elif x == 4: return ["goon","mcop","townie","townie","townie","townie","townie","townie","jailkeeper"]
    elif x == 5: return ["goon","mcop","townie","townie","townie","townie","townie","townie","doctor"]


def distribroles(dbname):
    roles = getvariation()
    random.shuffle(roles) # Note, random.shuffle() does not return anything.  It modifies the list.
    db_cur.execute('SELECT name FROM PLAYERS;')
    players = db_cur.fetchall()
    x = 0
    for i in range(len(players)):
        db_cur.execute('UPDATE PLAYERS SET role=? WHERE name=?;',[roles[i],players[i][0]])
    db.commit()


def displayopts(user):
    db_cur.execute('SELECT role FROM PLAYERS WHERE name=?;',[user])
    role = db_cur.fetchone()[0]
    if role == "goon":
		if gtime % 2 == 0.5:
			x = raw_input("Type 'kill [user]' to submit your kill for the night: ")
			target = x.split('kill')
	elif role == "mcop":
	elif role == "cop":
	elif role == "doctor":
	elif role == "jailkeeper":


def mainscreen(user):
    db_cur.execute('SELECT gtime FROM ADMIN;')
    gtime = db_cur.fetchone()[0]
    print "Phase " + gtime
    db_cur.execute('SELECT name FROM PLAYERS WHERE status=1;')
    print "Alive Players: ", db_cur.fetchall()
    db_cur.execute('SELECT name FROM PLAYERS WHERE status=0;')
    print "Dead players: ", db_cur.fetchall()
    displayopts(user,gtime)


def register():
    user = raw_input("Please enter your username: ")
    db_cur.execute('select name from players where name=?',[user])
    if len(user) <= 3 or len(db_cur.fetchall()) >= 1:
        print "That username is invalid, or in use.  Please enter a username over 3 characters."
        return 1
    pw = getpass.getpass("Please enter your password: ")
    if pw == getpass.getpass("Please enter your password again: ") and len(pw) > 5:
        hashed = bcrypt.hashpw(pw,bcrypt.gensalt(12))
        db.execute('INSERT INTO PLAYERS (name, password) values (?, ?)', [user,hashed])
        db.commit()
    else:
        print "Either your passwords did not match, or they were not over 5 characters."
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
    if  gstatus == 0 and numplayers < gsize:
        raw_input("Please press enter to register for the new game")
    while register() == 1:
		register()
    else:
        login()


def login():
    user = raw_input("Username: ")
    pw = getpass.getpass("Password: ")
    db_cur.execute("SELECT password FROM PLAYERS WHERE name = ?;", [user])
    try:
        dbhashed = db_cur.fetchone()[0]
    except TypeError:
        db.close()
        print "Incorrect username/password, please try again"
        login()
    db.close()
    if bcrypt.hashpw(pw, dbhashed) == dbhashed:
        print "Login successful!"
        mainscreen(user)
    else:
        print "Incorrect username/password, please try again"
        login()


def newdb(dbname): # At some point, we need to remove the "9" gsize insert, and use a variable
#   gsize = Use a user-inputted variable to set gsize in insert statement
    db.executescript('''
        CREATE TABLE PLAYERS (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        password CHARACTER(60),
        status SMALLINT default 1,
        role VARCHAR,
        known VARCHAR default "" );

        CREATE TABLE ADMIN (
        status SMALLINT,
        gtime SMALLINT,
        gsize SMALLINT );

        CREATE TABLE VOTES (
        gtime SMALLINT,
        player VARCHAR,
        candidate VARCHAR,
        votes SMALLINT);

        CREATE TABLE ROLEMOVES (
			gtime SMALLINT,
			mafia VARCHAR,
			doctor VARCHAR,
			mcop VARCHAR,
			cop VARCHAR,
			jail VARCHAR);

        CREATE TABLE LYNCHED (
            gtime SMALLINT,
            player VARCHAR);

        INSERT INTO ADMIN (status,gtime,gsize) values (0,0,9);
        ''')
    db.commit()
    main()


def testifdb(dbname):
    globals()["db"] = sqlite3.connect(dbname)
    globals()["db_cur"] = db.cursor()
    try:
        db_cur.execute('CREATE TABLE TEST (a INTEGER);')
    except sqlite3.DatabaseError:
        db.close()
        return 1
    db.execute('DROP TABLE TEST;')
    db.commit()
    return 0


def init():
    print '''


                                                 ffffffffffffffff    iiii
                                                f::::::::::::::::f  i::::i
                                               f::::::::::::::::::f  iiii
                                               f::::::fffffff:::::f
       mmmmmmm    mmmmmmm     aaaaaaaaaaaaa    f:::::f       ffffffiiiiiii   aaaaaaaaaaaaa
     mm:::::::m  m:::::::mm   a::::::::::::a   f:::::f             i:::::i   a::::::::::::a
    m::::::::::mm::::::::::m  aaaaaaaaa:::::a f:::::::ffffff        i::::i   aaaaaaaaa:::::a
    m::::::::::::::::::::::m           a::::a f::::::::::::f        i::::i            a::::a
    m:::::mmm::::::mmm:::::m    aaaaaaa:::::a f::::::::::::f        i::::i     aaaaaaa:::::a
    m::::m   m::::m   m::::m  aa::::::::::::a f:::::::ffffff        i::::i   aa::::::::::::a
    m::::m   m::::m   m::::m a::::aaaa::::::a  f:::::f              i::::i  a::::aaaa::::::a
    m::::m   m::::m   m::::ma::::a    a:::::a  f:::::f              i::::i a::::a    a:::::a
    m::::m   m::::m   m::::ma::::a    a:::::a f:::::::f            i::::::ia::::a    a:::::a
    m::::m   m::::m   m::::ma:::::aaaa::::::a f:::::::f            i::::::ia:::::aaaa::::::a
    m::::m   m::::m   m::::m a::::::::::aa:::af:::::::f            i::::::i a::::::::::aa:::a
    mmmmmm   mmmmmm   mmmmmm  aaaaaaaaaa  aaaafffffffff            iiiiiiii  aaaaaaaaaa  aaaa


    by Travis Beatty (travisby@gmail.com)


    '''

    dbname = raw_input("Please enter the game name you wish to connect to, or the name of a new game: ")

    if os.path.isfile(dbname) == True:
        if testifdb(dbname) == 0:
            main()
        else:
            print "The filename you provided is not an sqlite database.  Please try again, or contact an administrator."
            return 1
    else:
        if raw_input("Are you sure you wish to create a new game? (y/n)") == "y":
            newdb(dbname)
        else:
            return 0
init()
