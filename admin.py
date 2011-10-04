import dbControl


def changeStatus(dbname, value):
    if dbControl.testif(dbname):
        dbControl.db_cur.execute("UPDATE ADMIN SET status=?", (value,))


def changeTime(dbname, value):
    # 0 = day0, 1 = night0, 2 = day1, etc.
    if dbControl.testifdb(dbname):
        dbControl.db_cur.execute("UPDATE ADMIN SET gtime=?", (value,))
