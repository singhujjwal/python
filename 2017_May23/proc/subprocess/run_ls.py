from subprocess import Popen

#child = Popen("ls -l /")
#child = Popen(["ls", "-l", "/"])

child = Popen("ls -l / ", shell=True)

print "child process launched..."


