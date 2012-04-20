class Error(Exception):
    pass


class GameErrors(Error):
    pass


class DBError(Error):
    pass

##############################################################################


class DBDNE(DBError):
    pass


class DBNoDB(DBError):
    pass


class DBExists(DBError):
    pass

##############################################################################


class Started(GameErrors):
    pass


class Full(GameErrors):
    pass


class NotStarted(GameErrors):
    pass


class IncorrectUPCombination(GameErrors):
    pass