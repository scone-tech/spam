  
import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		; Author : ALBANIAN-SECURITY;    
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
NOTE: Ky mjet funksionon vetëm për telefonin me numër në Kosov.

1. SMS Gratis
2. OTP Call
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Filma24.ai
""")
		pilih=int(input('scone/> '))
		if zgjedh == 1:
			import src.call
		elif zgjedh == 2:
			import src.call
		elif zgjedh == 3:
			import src.alodok
		elif zgjedh == 4:
			import src.olx
		elif zgjedh == 5
			import src.filma
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
