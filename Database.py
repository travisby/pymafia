import sqlite3
import hashlib
import Exceptions


class Database:
    """The Database Class acts as the interface for all classes to connect.

    Only the Database Class is allowed to handle queries, even for grabbing
    player information.  The Database class creates, connects, sanitizes input,
    and performs sanity checks for everything.
    """

    def __init__(self, dbname):
        """Makes sure we're connected to a database"""
        self._db = sqlite3.connect(dbname)
        self._db_cur = self._db.cursor()

    def __del__(self):
        """Makes sure the database is cleanly closed."""
        self.exit()

    def exit(self):
        """Allows interfacing applications to close the database"""
        self._db.commit()
        self._db.close()

##############################################################################

    @staticmethod
    def create(dbname):
        """Create the Database, if possible"""
        try:
            Database._testifdb(dbname)
        except Exceptions.DBNoDB:
            raise Exceptions.DBNoDB
        except Exceptions.DBDNE:
                return Database._newdb(dbname)
        raise Exceptions.DBExists

    @staticmethod
    def connect(dbname):
        """Attempt to connect to the Database"""
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
        #Now attempt to open the file
        db = sqlite3.connect(dbname)
        db_cur = db.cursor()
        try:
            db_cur.execute('CREATE TABLE TEST (a INTEGER);')
        except sqlite3.DatabaseError:
            db.close()
            raise Exceptions.DBNoDB
        db.execute('DROP TABLE TEST;')
        db.commit()
        db.close()
        return True

    @staticmethod
    def _newdb(dbname):
        """Creates the Database schema and default state"""
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
            time SMALLINT,
            player VARCHAR,
            candidate VARCHAR,
            votes SMALLINT);

            CREATE TABLE ROLEMOVES (
            time SMALLINT,
            mafia VARCHAR,
            doctor VARCHAR,
            mcop VARCHAR,
            cop VARCHAR,
            jail VARCHAR);

            CREATE TABLE LYNCHED (
            time SMALLINT,
            player VARCHAR);

            CREATE TABLE MURDERED (
            time SMALLINT,
            player VARCHAR);

            INSERT INTO ADMIN (time,size) values (0,9);
            ''')
        db.commit()
        return Database(dbname)

##############################################################################

    def register(self, user, pw):
        """Register user/pw into the database"""
        if self.isStarted():
            raise Exceptions.Started
        hashed = hashlib.sha512(pw).hexdigest()
        self._db_cur.execute('''INSERT INTO PLAYERS (name, password)
                                        values (?, ?)''', [user, hashed])
        self._db.commit()

    def login(self, user, pw):
        """Attempt to login with the supplied user/pass"""
        if not self.isStarted():
            raise Exceptions.NotStarted
        pass

##############################################################################

    def setAllRoles(self, roles):
        """Distribute roles from a list to all registered players"""
        self._db_cur.execute('SELECT name FROM PLAYERS;')
        players = self._db_cur.fetchall()
        for i in range(len(players)):
            self._db_cur.execute('''UPDATE PLAYERS SET role=? WHERE name=?;''',
                                                    [roles[i], players[i][0]])
        self._db.commit()

##############################################################################

    def getTime(self):
        """Return what phase the game is in"""
        self._db_cur.execute('SELECT time FROM ADMIN;')
        return self._db_cur.fetchone()[0]

    def isStarted(self):
        """Returns boolean whether the game has started or not."""
        return self.getTime() != 0

    def isDay(self):
        """Returns boolean whether the game is in the day or night phase."""
        return self.getTime() % 1 == 0

    def getSize(self):
        """Return the amount of players in the game"""
        self._db_cur.execute('SELECT size FROM ADMIN;')
        return self._db_cur.fetchone()[0]

    def isPlayer(self, name):
        """Returns boolean whether the player exists yet or not."""
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
        time = self.getTime()
        self._db_cur.execute('''UPDATE PLAYER SET status=0 WHERE player=?;''',
                                                                    [player])
        if killer == "town":
            self._db_cur.execute('''INSERT INTO LYNCHED (time, player)
                                            values (?,?);''', [time, player])
        else:
            self._db_cur.execute('''INSERT INTO MURDERED (time, player)
                                            values (?,?);''', [time, player])
        self._db.commit()

    def incrementTime(self):
        """Update the time by one phase"""
        self._db_cur.execute('UPDATE ADMIN SET time=?;', self.getTime() + .5)

    def changeGameState(self, bool):
        """Change the game's "started"/"stopped" phase."""
        status = 0
        #If the game isn't started, enter time=1.  If it is started, insert 0
        if not self.getTime():
            status = 1
        self._db_cur.execute("UPDATE ADMIN SET time=?", (status,))

##############################################################################

    def insertVote(self, voter, votee):
        """This will be the interface for the Vote class to insert votes
        """
        pass
