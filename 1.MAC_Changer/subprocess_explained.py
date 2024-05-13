import subprocess
#since we are only using call, you could also type: from subprocess import call

subprocess.call('ifconfig', shell=True)
#where I wrote you put the command you want to execute
