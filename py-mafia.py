<<<<<<< HEAD
from MafiaCmd import MafiaCmd
=======
from mafiaCmd import mafiaCmd
>>>>>>> 3811b0dff8880c8c6a13939c16cbb9bea759cf08
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

#Continue asking to login until a legit username is given.

#user = raw_input("Username: ")
#pw = getpass.getpass("Password: ")
#player = db.login(user, pw)
#while (not player):
#    print "Incorrect username/password, please try again"
#    user = raw_input("Username: ")
#    pw = getpass.getpass("Password: ")
#    player = db.login()
#print "Login Successful!"
#print "Type 'help' to see all commands"


<<<<<<< HEAD
interpreter = MafiaCmd()
=======
interpreter = mafiaCmd()
>>>>>>> 3811b0dff8880c8c6a13939c16cbb9bea759cf08
interpreter.cmdloop()
