import sqlite3
import os
from main import main


def newdb(dbname): # At some point, we need to remove the "9" gsize insert, and use a variable
    
    db = sqlite3.connect(dbname)
#   gsize = Use a user-inputted variable to set gsize in insert statement
    db.executescript('''
        CREATE TABLE PLAYERS (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        password CHARACTER(60),
        status SMALLINT default 1,
	role VARCHAR,
        known VARCHAR default "null");

        CREATE TABLE ADMIN (
	status SMALLINT,
	gametime SMALLINT,  
	gamesize SMALLINT);

        INSERT INTO ADMIN (status,gametime,gamesize) values (0,0,9);
        ''')
    db.commit()
    db.close()
    main(dbname)

def testifdb(dbname):
    db = sqlite3.connect(dbname)
    try:
        db.execute('CREATE TABLE TEST (a INTEGER);')
    except sqlite3.DatabaseError:
        db.close()
        return 1
    db.execute('DROP TABLE TEST;')
    db.close()
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
        if  testifdb(dbname) == 1:
            print "The filename you provided is not an sqlite database.  Please try again, or contact an administrator."
            init()
        else:
            main(dbname)

    else:
        if raw_input("Are you sure you wish to create a new game? (y/n)") == "y":
            newdb(dbname)
        else:
            init()
init()
