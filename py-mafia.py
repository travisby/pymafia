from mafiaCmd import mafiaCmd
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


interpreter = mafiaCmd()
interpreter.cmdloop()
