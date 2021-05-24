T = 3
lines = ['SUVOJITSU', '651SUVOMN', '$$$$$SUVOSUVOJIT$$$$$']

import pdb

for line in lines:
    suvojit = 0
    suvo = 0
    if line.find('SUVOJIT') != -1 or line.find('SUVO') != -1:

        while len(line) >= len('SUVO'):
            if line.find('SUVOJIT') == line.find('SUVO') and line.find('SUVOJIT') != -1: 
        # there is SUVOJIT present
                suvojit += 1
                print (line.index('SUVOJIT'))
                line = line[line.index('SUVOJIT') + len ('SUVOJIT') :]
            elif line.find('SUVO') != -1:
                suvo += 1
                line = line[line.index('SUVO') + len ('SVO'):]
            else:
                break
    print ("SUVO = {}, SUVOJIT = {}".format(suvo, suvojit))