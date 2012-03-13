import cmd
from Database import Database
import getpass
import Exceptions


class MafiaCmd(cmd.Cmd, object):
    """MafiaCmd acts as the shell for the entire game.

    From MafiaCmd, players can interact with the game, ranging from creating
    and connecting to the game, registering, logging in, and submitting moves.
    """

    _player = None
    _db = None

    def __init__(self):
        super(MafiaCmd, self).__init__()
##############################################################################

    def do_create(self, s):
        """Creates the game, after a sanity check."""
        dbname = s.split()[0]
        try:
            self._db = Database.create(dbname)
        except Exceptions.DBNoDB:
            print "Already exists, but not as a Database"
        except Exceptions.DBExists:
            print "That game already exists!"
        else:
            print "Created and Connected!"

    def do_connect(self, s):
        """Attempts to connect to the supplied game name."""
        if not s:
            print "No argument"
            self.help_connect()
            return
        dbname = s.split()[0]
        self._db = Database.connect(dbname)

    def do_register(self, s):
        """Allows the user to register for the game, after sanity checks."""
        if not self._db:
            print "Not connected to a database."
            return
        if not self._db.isStarted():
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

    def do_exit(self, s):
        """Allows the user to exit the game cleanly."""
        self._db.exit()
        return True
    do_EOF = do_exit

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

    def help_exit(self):
        """Help for the exit function."""
        print "Exit the interpreter."
        print "You can also use the Ctrl-D shortcut."
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
