import requests, sys, os


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
 █▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ ▀█▀ █▀▀ █▀█
 █▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ░█░ ██▄ █▀▄
 
 ▀█▀ █▀█ █▀█ █░░
 ░█░ █▄█ █▄█ █▄▄   V 1.0.0

 Coder by : https://github.com/Nux-xader
 Contact  : https://wa.me/6281251389915
 _______________________________________________
""")


def excel_to_html(data):
	resp = requests.post("https://api.conversiontools.io/v1/files", headers=HEADERS, data={"file": data})
	print(resp.json())


def main():
	clr()
	banner()
	while True:
		path = str(input(" File excel (xlsx, csv) : "))
		try:
			data = open(path, "rb").read()
			break
		except:
			print(f" [!] File {path} not found")

	result = excel_to_html(data)

if __name__ == '__main__':
	main()