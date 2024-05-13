import subprocess

#network interface
ni = input('Enter desired network interface: ')
ni = str(ni)
#new mac adress
nma = input('Enter new mac adress: ')

#Safe way: word by word
subprocess.call(['ifconfig', ni, 'down'])
subprocess.call(['ifconfig', ni,'hw', 'ether', nma])
subprocess.call(['ifconfig', ni, 'up'])


#This is the simpler way of doing it. The only problem is that if someone writes in the ni variable blablabla;ls. The program will be hijacked. It would read blablabla and change the MAC adress for blablabla, but it would also execute ls because ';' un linux means 'also execute this command'.

# subprocess.call('ifconfig ' + ni + ' down', shell = True)
# subprocess.call('ifconfig ' + ni + ' hw ether ' + nma , shell = True)
# subprocess.call('ifconfig ' + ni + ' up', shell = True)
