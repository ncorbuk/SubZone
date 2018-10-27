#!d:/python 3.6.5/python.exe

#imports
from colorama import init, Fore, Back, Style
import requests
import json
import argparse
import socket
import time
import urllib3
import subprocess
import os
import sys

#Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter)


init(autoreset=True)


print(Back.BLACK+Style.BRIGHT+Fore.CYAN+'''
                      ███████╗██╗   ██╗██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗                      
▄ ██╗▄▄ ██╗▄▄ ██╗▄    ██╔════╝██║   ██║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║██╔════╝    ▄ ██╗▄▄ ██╗▄▄ ██╗▄
 ████╗ ████╗ ████╗    ███████╗██║   ██║██████╔╝  ███╔╝ ██║   ██║██╔██╗ ██║█████╗       ████╗ ████╗ ████╗
▀╚██╔▀▀╚██╔▀▀╚██╔▀    ╚════██║██║   ██║██╔══██╗ ███╔╝  ██║   ██║██║╚██╗██║██╔══╝      ▀╚██╔▀▀╚██╔▀▀╚██╔▀
  ╚═╝   ╚═╝   ╚═╝     ███████║╚██████╔╝██████╔╝███████╗╚██████╔╝██║ ╚████║███████╗      ╚═╝   ╚═╝   ╚═╝ 
                      ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                      ''')


print(Back.BLACK+Fore.GREEN+r'''
	             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DOS!    |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------''')


a = (Back.BLACK+Fore.RED+r'''
____ _  _ ___  ___  ____ _  _ ____ _ _  _ ____ 
[__  |  | |__] |  \ |  | |\/| |__| | |\ | [__  
___] |__| |__] |__/ |__| |  | |  | | | \| ___],''')


b = (Back.BLACK+Fore.WHITE+r'''
___  _  _ ____ ____ ____ ____ ____ ____ ___  ____ 
|  \ |\ | [__  |__/ |___ |    |  | |__/ |  \ [__  
|__/ | \| ___] |  \ |___ |___ |__| |  \ |__/ ___],''')


d = (Back.BLACK+Fore.BLUE+r'''
 ____ __ _ ___ 
 |--| | \| |__>''')

e = (Back.BLACK+Fore.BLUE+r'''
_  _ ____ ____ ____  
|\/| |  | |__/ |___  
|  | |__| |  \ |___ !''')

print('%s %s  %s %s' % (a,b,d,e))


print(Back.BLACK+Fore.YELLOW+('''

49 66 79 6F 75 61 72 65 72 65 61 64 69 6E 67 74 68 69 73 74 68 65 6E 68 69 73 74 61 72 74 68 69 73 72 65 70 6F 61 6E 64\n'''))

print(Fore.CYAN+Back.BLACK+'[\n  Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter) </>\n  ]\n')
print('')



def args_parser():
	#parse required argument/s needed for program
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help='domain - to find subdomains(ex use. http(s)://facebook.com)')
	parser.add_argument('-o', '--output', type=str, required=True, help='filename - file for output data(ex use. facebook.txt)')
	args = parser.parse_args()
	return args



def requirements_check():
	#check requirements are met for software/program to run correctly
	checks = True
	requirements = 'requirements.txt'
	with open(requirements, 'r') as rfp:
		for line in rfp.readlines():
			try:
				exec("import " + line)
			except:
				print("[ERROR] Missing module:", line)
				checks = False
	if checks == False:
		sys.exit(1)




active_subdomains = []
nameservers = []

class Abuse_certificate_transparency:
	def __init__(self):
		self.domain = args_parser().domain
		self.output = args_parser().output


	def parse_url(self):
		#parse host from scheme, to use for certificate transparency abuse
		try:
			host = urllib3.util.url.parse_url(self.domain).host
		except Exception as e:
			print(f'Invalid - Domain, try again...')
			sys.exit(1)
		return host


	def request_json(self):
		#request json data to get list of registered subdomains with cert trans records
		subdomains = []
		try:
			r = requests.get(f'https://crt.sh/?q=%.{abuse.parse_url()}&output=json')
			#r = requests.get('https://crt.sh/?q=%.facebook.com&output=json')
			if r.status_code != 200:
				print('{!} host status-code: %s\n ~ unable to access records using this abuse certificate transparency method' % (r.status_code))
			else:
				try:
					json_data = json.loads('[%s]' % (r.text.replace('}{', '},{')))
					for sub in (json_data):
						subdomains.append(sub['name_value'])
				except Exception as e:
					print(f'json_data:Error {e}')
					pass
		except Exception as e:
			print(f'request_json//Error: {e}')
			pass
		return subdomains


	def active_subs(self):
		#check registered subdomains to see if active or not
		global active_subdomains

		for sub in abuse.request_json():
			try:
				sub = socket.gethostbyname_ex(sub)
				active_subdomains.append(sub)
			except:
				pass
		number_all = len(abuse.request_json())
		number_active = len(active_subdomains)

		Style.RESET_ALL

		try:
			print('\n',Fore.GREEN+'''{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_all), Fore.RED+Back.BLACK+'REGISTERED', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			line = Fore.CYAN+Back.BLACK+str('*****************************')
			print('\n%s\n%s %s\n%s\n' % (line, index, sub_red, line))
			time.sleep(1.3)

			for index, sub in enumerate(abuse.request_json()):
				print(Fore.GREEN+str(index),Fore.RED+str(sub))

			print('\n',Fore.GREEN+'''{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_active), Fore.RED+Back.BLACK+'ACTIVE', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			dns_white = Fore.WHITE+Back.BLACK+str('DNS SERVER:white')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			ip_yell = Fore.BLUE+Back.BLACK+str('IP_ADDR:blue')
			line = Fore.CYAN+Back.BLACK+str('************************************************************')
			print('\n%s\n%s %s %s %s\n%s\n' % (line, index, dns_white, sub_red, ip_yell, line))
			time.sleep(1.3)

			for index, sub in enumerate(active_subdomains):
				print(Fore.GREEN+str(index), Fore.WHITE+Back.BLACK+str(sub[0]), Fore.RED+Back.BLACK+str(sub[1]), Fore.BLUE+Back.BLACK+str(sub[2]))

		except Exception as e:
			print(f'active_subdomains//Error: {e}')
			pass

		return active_subdomains


	def write_file(self,):
		#write registerd subdomains and active subdomains to file
		global active_subdomains
		try:
			reg = 'REGISTERED_'+self.output
			active = 'ACTIVE_'+self.output
			if self.output is not None:
				with open(reg,'w') as r:
					for index, sub in enumerate(abuse.request_json()):
						text = f'{index} {sub}\n'
						r.write(text)
				with open(active,'w') as a:
					for index, sub in enumerate(active_subdomains):
						text = f'{index} {sub}\n'
						a.write(text)
		except Exception as e:
			print(f'write_file//Error: {e}')
			pass



class Dns_zone_transfer:
	def __init__(self):
		self.domain = abuse.parse_url()
		self.output = args_parser().output


	def nslookup(self):
		global nameservers
		#nslookup to find nameservers of target domain
		dns_white = Fore.RED+Back.BLACK+str('Dns records')
		sec_bit = Fore.GREEN+Back.BLACK+str('for this domain.\n')
		print(Fore.GREEN+Back.BLACK+str('\n {!} %s %s' % (dns_white, sec_bit)))
		try:
			with open('nslookup.txt','w') as output_vale:
				cmd = subprocess.call(f'nslookup -type=ns {self.domain}', stdout=output_vale)
			with open('nslookup.txt','r') as ns2:
				for line in ns2.readlines():
					if 'nameserver' in line:
						line = line.split(' ')[2]
						nameservers.append(line)

			os.remove('nslookup.txt')
			#print(nameservers)
		except Exception as e:
			#print(e)
			pass
		return nameservers


	def dns_records(self):
		global nameservers
		#zone transfer - to get dns records if dns server is not configured properly
		count = 0
		try:
			for ns in nameservers:                                                 
                                                      
				with open('gogo.txt','w') as go:
					go.write(f'nslookup\nset type=all\nserver {ns}\nls -d {abuse.parse_url()}\n.\n')

				if self.output is not None:
					filename = 'DNS_RECORDS_%s' % (self.output)
					if count == 0:
						with open(filename,'w') as fp:
							fp.write('**********DNS RECORDS**********\n\n')
							with open('gogo.txt','r') as go:
								cmd = subprocess.call('cmd.exe', stdin=go, stdout=fp)
							count +=1
					else:
						with open(filename,'a') as write_here:
							with open('gogo.txt','r') as go:
								cmd = subprocess.call('cmd.exe', stdin=go, stdout=write_here)
				else:
					with open('gogo.txt','r') as fp:
						cmd = subprocess.call('cmd.exe', stdin=fp)
					fp.close()
		except Exception as e:
			print(e)

		try:
			os.remove('gogo.txt')
		except:
			pass

		try:
			with open(filename,'r') as rd:
				for line in rd.readlines():
					print(line)
		except:
			pass








if __name__=='__main__':
	#main
	requirements_check()

	abuse = Abuse_certificate_transparency()
	abuse.parse_url()
	abuse.request_json()
	abuse.active_subs()
	abuse.write_file()

	zone = Dns_zone_transfer()
	zone.nslookup()
	zone.dns_records()

#Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter)
