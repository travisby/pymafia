import sqlite3

db = None
db_cur = None


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
    return True


def newdb(dbname):
# gsize = Use a user-inputted variable to set gsize in insert statement
    globals()["db"] = sqlite3.connect(dbname)
    globals()["db_cur"] = db.cursor()
    db_cur.executescript('''
        CREATE TABLE PLAYERS (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        password CHARACTER(129),
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

        CREATE TABLE MURDERED (
        gtime SMALLINT,
        player VARCHAR);

        INSERT INTO ADMIN (status,gtime,gsize) values (0,0,9);
        ''')

    db.commit()
    print "Successfully created!"
    return 0
