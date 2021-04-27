import os

os.system("clear")
os.system("pip3 install bs4")
os.system("pip3 install pyasn1")
os.system("pip3 install rsa")
os.system("pip3 install pyaes")
os.system("pip3 install requests")
os.system("pip3 install telethon")

from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from bs4 import BeautifulSoup
from time import sleep
import requests, json, re, sys
import multiprocessing
numbers = []
os.system("clear")

def banner():
    banner = """
\x1b[0;30;41m                                                                \x1b[0m   
\x1b[0;30;41m|██████╗ ██╗   ██╗ ██████╗██╗  ██╗ ██████╗ ██████╗ ██╗███╗   ██╗\x1b[0m   
\x1b[0;30;41m|██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔═══██╗██║████╗  ██║\x1b[0m    
\x1b[0;30;41m|██║  ██║██║   ██║██║     █████╔╝ ██║     ██║   ██║██║██╔██╗ ██║\x1b[0m  
\x1b[0;30;41m|██║  ██║██║   ██║██║     ██╔═██╗ ██║     ██║   ██║██║██║╚██╗██║\x1b[0m    
\x1b[0;30;41m|██████╔╝╚██████╔╝╚██████╗██║  ██╗╚██████╗╚██████╔╝██║██║ ╚████║\x1b[0m
\x1b[0;30;41m|╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝\x1b[0m   
\x1b[0;30;41m                                                                \x1b[0m   

\x1b[0;30;43m|=============================================================|\x1b[0m  
\x1b[0;30;43m|\x1b[1;32;40m           \x1b[0;30;41m[ D U C K  C O I N  M I N E R ]\x1b[1;32;40m                   \x1b[0;30;43m|\x1b[0m
\x1b[0;30;43m|\x1b[3;31;40m                   VENHA MINERAR!!                           \x1b[0;30;43m|\x1b[0m
\x1b[0;30;43m|\x1b[0m\x1b[0;32;40m                   BY PATO MAKER !                           \x1b[0m\x1b[0;30;43m|\x1b[0m
\x1b[0;30;43m|=============================================================|\x1b[0m 
      \x1b[0;30;43m|\x1b[0;30;47m   [ SISTEMA DE MINERAÇAO AUTOMATICO ]   \x1b[0;30;43m|\x1b[0m
      \x1b[0;30;43m|\x1b[0;30;47m           [ VIA TELEGRAM ]              \x1b[0;30;43m|\x1b[0m
      \x1b[0;30;43m|-----------------------------------------|\x1b[0m
"""
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)

    join1 = "\x1b[0;32;40m Suporte: 55 31 996891466\x1b[0m"
    join2 = "                                                  "
    for _ in range(1):
        print(join1,end="\r")
        sleep(0.5)
        print(join2,end="\r")
        sleep(0.5)
    print(join1,end="\r")

if not os.path.exists('session'):
    os.makedirs('session')

banner()
try:
	header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
	getpass = requests.get("https://pastebin.com/raw/ANi6UNKH",headers=header).text
	print("\n\n[*] Get password here : " + str(getpass))
	pass_link = requests.get("https://pastebin.com/raw/ANi6UNKH",headers=header).text
	web = requests.get(pass_link,headers=header)
	page = BeautifulSoup(web.text,"html.parser")
	password = str(page.find("h1"))
	password = password.replace("<h1>","")
	password = password.replace("</h1>","")
	user_pass = input("[*] Enter script password >> ")
	if user_pass != password:
		print("Incorrect password! Try again. . .")
		sys.exit()
except Exception as e:
	print(e)

os.system("clear")
banner()

api_id = '5334015'
api_hash = '0f64b39b838c3304c0456479a09b04c8'
phone_number = input("\n[*] Coloque Seu Numero >> \x1b[0m")#'+639458513800'
client = TelegramClient('session/'+phone_number,api_id,api_hash)
client.connect()
if not client.is_user_authorized():
	try:
		client.send_code_request(phone_number)
		client.sign_in(phone_number,input('\x1b[0;32;40m[*] Coloque o codigo enviado >> '))
	except SessionPasswordNeededError:
		password = input('\x1b[0;32;40mColoque Sua Senha de verificaçao >> ')
		me = client.start(phone_number,password)

def claim(bot_channel):
    global client
    channel_username = bot_channel
    c = requests.session()
    ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    channel_entity = client.get_entity(channel_username)
    try:
        for ulang in range(999999999):
            print('\x1b[0;32;40m[*] Fetching URL - ' + str(bot_channel))
            client.send_message(entity=channel_entity,message='ð¥ Visit sites')
            sleep(3)
            message_history = client(GetHistoryRequest(peer=channel_entity,limit=0,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            channel_id = message_history.messages[0].id
            if message_history.messages[0].message.find('Sorry, there are no new ads available.') != -1:
                print('\x1b[3;31;40m[*] Ads run out! Try again later - ' + str(bot_channel))
                break
            url = message_history.messages[0].reply_markup.rows[0].buttons[0].url
            print('\x1b[0;32;40m[*] Visiting the URL - ' + str(bot_channel))

            r = c.get(url,headers=ua)
            soup = BeautifulSoup(r.text,"html.parser")

            if soup.find('div',class_='g-recaptcha') is None and soup.find('div',id='headbar') is None:
                sleep(2)
                message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                message = message_history.messages[0].message
                print("\x1b[0;32;40m[*] " + message + " - " + str(bot_channel))
                if message_history.messages[0].message.find('Please stay on') != -1 or message_history.messages[0].message.find('You must stay') != -1:
                    timer = re.findall(r'([\d.]*\d+)',message)
                    sleep(int(timer[0]))
                    sleep(3)
            elif soup.find('div',id='headbar') is not None:
                for data in soup.find_all('div',class_='container-fluid'):
                    code = data.get('data-code')
                    timer = data.get('data-timer')
                    token = data.get('data-token')
                    sleep(int(timer))
                    r = c.post('https://dogeclick.com/reward',data={'code': code, 'token': token},headers=ua)
                    message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                    message = message_history.messages[0].message
                    print("\x1b[0;30;43m[*] Succesful Claim - " + str(bot_channel))
            else:
                print('\x1b[3;31;40m[*] Captcha detected - ' + str(bot_channel))
                sleep(2)
                client(GetBotCallbackAnswerRequest(channel_username,channel_id,data=message_history.messages[0].reply_markup.rows[1].buttons[1].data))
                print ('\x1b[3;31;40m[*] Skip Captcha - ' + str(bot_channel), end="\r")
    except:
        print("Error Detected - " + str(bot_channel))
        sys.exit()

while True:
	p1 = multiprocessing.Process(target=claim,args=['@Dogecoin_click_bot'])
	p2 = multiprocessing.Process(target=claim,args=['@BCH_clickbot'])
	p3 = multiprocessing.Process(target=claim,args=['@Zcash_click_bot'])
	p4 = multiprocessing.Process(target=claim,args=['@Litecoin_click_bot'])
	p5 = multiprocessing.Process(target=claim,args=['@BitcoinClick_bot'])

	try:
		p1.start()
		p2.start()
		p3.start()
		p4.start()
		p5.start()
	except:
		print("Problem with the starting process . . .")

	sleep(1)

	try:
		p1.join()
		p2.join()
		p3.join()
		p4.join()
		p5.join()
	except:
		print("Problem with the joining process . . .")

	print("[*] Next Claim After 1 Hour . . .")

	for i in range(3600):
		print(str(i) + "/3600 seconds until next claim",end="\r")
		sleep(1)
