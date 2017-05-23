from subprocess import Popen, PIPE

p = Popen(["/sbin/ifconfig"], stdout=PIPE)

#for line in p.stdout:
#    if "inet" in line:
#        print line.split()[1]

ip_addresses = [ line.split()[1] for line in p.stdout if "inet" in line ]
print ip_addresses
