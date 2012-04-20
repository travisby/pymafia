import cmd
from Database import Database
import getpass
import Exceptions


class MafiaCmd(cmd.Cmd, object):
    """MafiaCmd acts as the shell for the entire game.

    From MafiaCmd, players can interact with the game, ranging from creating
    and connecting to the game, registering, logging in, and submitting moves.
    """

    _user = None
    _db = None

    def __init__(self):
        super(MafiaCmd, self).__init__()
##############################################################################

    def do_create(self, s):
        """Creates the game."""
        # Sanity Check
        if not s:
            print "No argument"
            self.help_create()
            return
        dbname = s.split()[0]
        try:
            self._db = Database.create(dbname)
        except Exceptions.DBNoDB:
            print "Already exists, but not as a Database"
        except Exceptions.DBExists:
            print "That game already exists!"
        # End Sanity Check
        else:
            print "Created and Connected!"

    def do_connect(self, s):
        """Attempts to connect to the supplied game name."""
        # Sanity Check
        if not s:
            print "No argument"
            self.help_connect()
            return
        # End Sanity Check
        dbname = s.split()[0]
        self._db = Database.connect(dbname)
        # If it doesn't actually exist?
        if self._db is None:
            print "Doesn't exist!  Still not connected."

    def do_register(self, s):
        """Allows the user to register for the game."""
        # Sanity Check
        if not self._db:
            print "Not connected to a database."
            return
        if self._db.isStarted():
            print "Game is already started.  Please login"
            return
        if self._db.isFull():
            print "Game is full, sorry."
            return
        # End Sanity Check
        user = raw_input("Please enter your username over 3 characters: ")
        if len(user) <= 3 or self._db.isPlayer(user):
            print "That username is invalid, or in use."
        pw = getpass.getpass("Please enter your password over 5 " +
                                                        "characters: ")
        if (pw == getpass.getpass("Please enter your password again: ")
                                                        and len(pw) > 5):
            self._db.register(user, pw)
        else:
            print "Invalid password"

    def do_login(self, s):
        """Allows the user to login to their console."""
        # Sanity Check
        if not self._db:
            print "Not connected to a database."
            return
        if not self._db.isStarted():
            print "The game has not started yet."
            return
        # End Sanity Check
        # If they supply a username, roll with it.
        if len(s) > 0:
            user = s[0]
        # ...or else ask for it
        else:
            user = raw_input("Uusername: ")
        pw = getpass.getpass("Password: ")
        self._user = self._db.login(user, pw)
        while not self._user:
            self._user = self._db.login(user, pw)

    def do_info(self, s):
        if self._user:
            self._db.stats()
        else:
            print "Not connected or logged in."

    def do_vote(self, s):
        if not s:
            print "No argument"
            self.help_vote()
            return

    def do_exit(self, s):
        """Allows the user to exit the game cleanly."""
        return True

    def do_EOF(self, s):
        """Allows the user to exit the game cleanly with ctrl+D."""
        return True

##############################################################################
    def help_create(self):
        """Help for the create function."""
        print 'Usage: create [FILE]'
        print 'Creates the database [FILE], and preloads the game'

    def help_connect(self):
        """Help for the Connect function."""
        print 'Usage: connect [FILE]'
        print 'connect connects to the database [FILE]'

    def help_register(self):
        """Help for the register function."""
        print 'Usage: register'
        print 'Register for the currently connected game'

    def help_login(self):
        """Help for the login function."""
        print 'Usage: login <username>'
        print 'Usage: login'
        print 'Login with <username> or be prompted for one'

    def help_info(self):
        """Help for the info function."""
        print "Prints recent votes, game time, phase, etc."

    def help_exit(self):
        """Help for the exit function."""
        print "Exit the interpreter."

    def help_EOF(self):
        """Help for the EOF function."""
        print "Exit the interpreter with the Ctrl-D shortcut."
#
#    def help_vote(self):
#        pass
#
#    def do_kill(self, s):
#        pass
#
#    def help_kill(self):
#        pass
#
#    def do_help(self, s):
#        pass
#
#    def do_protect(self, s):
#        pass
#
#    def help_protect(self):
#        pass
#
#    def do_jail(self, s):
#        pass
#
#    def help_jail(self):
#        pass
#
#    def do_investigate(self, s):
#        pass
#
#    def help_investigate(self):
#        pass
#
#    def do_register(self, s):
#        pass
#

#TODO REMOVE
    def do_admintime(self, s):
        print self._db.getTime()
        self._db.changeGameState()
        print self._db.getTime()

    def do_adminfill(self, s):
        self._db.regfull()
        self._db.changeGameState()