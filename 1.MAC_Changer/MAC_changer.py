import subprocess
import optparse

parser = optparse.OptionParser()

#We now give the parser what to expect from the user input
parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC adress')
#dest is the variable in which we will store the value of the interface. help is the help message displayed if the user needs help

parser.parse_args()


interface = input('Network Interface: ')
new_mac = input('New MAC: ')

print('[+] Changing MAC adress for ' + interface + ' to ' + new_mac)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])
