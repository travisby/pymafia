import sqlite3
import hashlib
import Exceptions


class Database:

    def __init__(self, dbname):
        """Makes sure we're connected to a database"""
        self._db = sqlite3.connect(dbname)
        self._db_cur = self._db.cursor()

    def __del__(self):
        self._db.close()

    def close(self):
        self._db.close()

##############################################################################

    @staticmethod
    def create(dbname):
<<<<<<< HEAD
        """Create the Database, if possible"""
        try:
            Database._testifdb(dbname)
        except Exceptions.DBNoDB:
            raise Exceptions.DBNoDB
        except Exceptions.DBDNE:
                return Database._newdb(dbname)
=======
        try:
            Database._testifdb(dbname)
        except Exceptions.DBDNE:
                return Database._newdb(dbname)
        except Exceptions.DBNoDB:
            raise Exceptions.DBNoDB
            return
>>>>>>> 3811b0dff8880c8c6a13939c16cbb9bea759cf08
        raise Exceptions.DBExists

    @staticmethod
    def connect(dbname):
<<<<<<< HEAD
        """Attempt to connect to the Database"""
=======
>>>>>>> 3811b0dff8880c8c6a13939c16cbb9bea759cf08
        try:
            Database._testifdb(dbname)
        except Exceptions.DBError:
            return None
        return Database(dbname)

    @staticmethod
    def _testifdb(dbname):
        """Test if the database exists

            See if the file suggested first exists, and then if it is a sqlite
            database file.  If the file does not exist, run _newdb, and return
            true.  If the file exists, but is not an sqlite database, return
            False
        """
        try:
            open(dbname)
        except IOError:
            raise Exceptions.DBDNE
            return False
        #Now attempt to open the file
        db = sqlite3.connect(dbname)
        db_cur = db.cursor()
        try:
            db_cur.execute('CREATE TABLE TEST (a INTEGER);')
        except sqlite3.DatabaseError:
            db.close()
            raise Exceptions.DBNoDB
            return False
        db.execute('DROP TABLE TEST;')
        db.commit()
        db.close()
        return True

    @staticmethod
    def _newdb(dbname):
<<<<<<< HEAD
        """Creates the Database schema and default state"""
=======
        """Creates the Database"""
>>>>>>> 3811b0dff8880c8c6a13939c16cbb9bea759cf08
        db = sqlite3.connect(dbname)
        db_cur = db.cursor()
        db_cur.executescript('''
            CREATE TABLE PLAYERS (
            id SMALLINT PRIMARY KEY,
            name VARCHAR,
            password CHARACTER(129),
            status SMALLINT default 1,
            role VARCHAR,
            known VARCHAR default "" );

            CREATE TABLE ADMIN (
            time SMALLINT,
            size SMALLINT );

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

            INSERT INTO ADMIN (time,size) values (0,9);
            ''')
        db.commit()
        return Database(dbname)

##############################################################################

    def register(self, user, pw):
        """Register user/pw into the database"""
        if (self.isStarted()):
            raise Exceptions.Started
            return
        hashed = hashlib.sha512(pw).hexdigest()
        self._db_cur.execute('''INSERT INTO PLAYERS (name, password)
                                        values (?, ?)''', [user, hashed])
        self._db.commit()

    def login(self, user, pw):
        """Attempt to login with the supplied user/pass"""
        if(not self.isStarted()):
            raise Exceptions.NotStarted
            return
        pass

##############################################################################

    def setAllRoles(self, roles):
        """Distribute roles from a list to all registered players"""
        self._db_cur.execute('SELECT name FROM PLAYERS;')
        players = self._db_cur.fetchall()
        for i in range(len(players)):
            self._b_cur.execute('''UPDATE PLAYERS SET role=? WHERE name=?;''',
                                                    [roles[i], players[i][0]])
        self._db.commit()

##############################################################################

    def getTime(self):
        """Return what phase the game is in"""
        self._db_cur.execute('SELECT time FROM ADMIN;')
        return self._db_cur.fetchone()[0]

    def isStarted(self):
        return self.getTime() != 0

    def isDay(self):
        return self.getTime() % 1 == 0

    def getSize(self):
        """Return the amount of players in the game"""
        self._db_cur.execute('SELECT gsize FROM ADMIN;')
        return self._db_cur.fetchone()[0]

    def isPlayer(self, name):
        self._db_cur.execute("SELECT name FROM PLAYERS WHERE name = ?;",
                                                                    [name])
        try:
            self._db_cur.fetchone()[0]
        except TypeError:
            return False
        return True

##############################################################################

    def kill(self, player, killer):
        """Kills the player, and enters the data into the database"""
        gtime = self._getTime()
        self._db_cur.execute('''UPDATE PLAYER SET status=0 WHERE player=?;''',
                                                                    [player])
        if killer == "town":
            self._db_cur.execute('''INSERT INTO LYNCHED (gtime, player)
                                            values (?,?);''', [gtime, player])
        else:
            self._db_cur.execute('''INSERT INTO MURDERED (gtime, player)
                                            values (?,?);''', [gtime, player])
        self._db.commit()

    def incrementTime(self):
        """Update the time by one phase"""
        self._db_cur.execute('UPDATE ADMIN SET gtime=?;', self.getTime() + .5)

    def changeGameState(self, bool):
        """Change the game's "started"/"stopped" phase."""
        status = 0
        #If the game isn't started, enter time=1.  If it is started, insert 0
        if self.getTime(self) == 0:
            status = 1
        self._db_cur.execute("UPDATE ADMIN SET time=?", (status,))

##############################################################################

    def insertVote(self, voter, votee):
        """
            This will be the interface for the Vote class to insert votes
        """
        pass
