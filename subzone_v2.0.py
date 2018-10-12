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



def requirements_check():
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
		exit(1)
	else:
		pass


init(autoreset=True)

print(Back.RED+Style.BRIGHT+Fore.GREEN+'''
                      ███████╗██╗   ██╗██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗                      
▄ ██╗▄▄ ██╗▄▄ ██╗▄    ██╔════╝██║   ██║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║██╔════╝    ▄ ██╗▄▄ ██╗▄▄ ██╗▄
 ████╗ ████╗ ████╗    ███████╗██║   ██║██████╔╝  ███╔╝ ██║   ██║██╔██╗ ██║█████╗       ████╗ ████╗ ████╗
▀╚██╔▀▀╚██╔▀▀╚██╔▀    ╚════██║██║   ██║██╔══██╗ ███╔╝  ██║   ██║██║╚██╗██║██╔══╝      ▀╚██╔▀▀╚██╔▀▀╚██╔▀
  ╚═╝   ╚═╝   ╚═╝     ███████║╚██████╔╝██████╔╝███████╗╚██████╔╝██║ ╚████║███████╗      ╚═╝   ╚═╝   ╚═╝ 
                      ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                      ''')

print(Fore.GREEN+'''
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗        
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝        
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║███████╗        
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║╚════██║        
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████║▄█╗     
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     
                                                                                          
██████╗ ███╗   ██╗███████╗    ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███████╗   
██╔══██╗████╗  ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝   
██║  ██║██╔██╗ ██║███████╗    ██████╔╝█████╗  ██║     ██║   ██║██████╔╝██║  ██║███████╗   
██║  ██║██║╚██╗██║╚════██║    ██╔══██╗██╔══╝  ██║     ██║   ██║██╔══██╗██║  ██║╚════██║   
██████╔╝██║ ╚████║███████║    ██║  ██║███████╗╚██████╗╚██████╔╝██║  ██║██████╔╝███████║▄█╗
╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝
                                                                                          
   ██╗       ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗                                      
   ██║       ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║                                      
████████╗    ██╔████╔██║██║   ██║██████╔╝█████╗  ██║                                      
██╔═██╔═╝    ██║╚██╔╝██║██║   ██║██╔══██╗██╔══╝  ╚═╝                                      
██████║      ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████╗██╗                                      
╚═════╝      ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  
''')
print(Back.RED+Fore.GREEN+'Coded by: Nathan.Corbin 2018.\n          @ncorbuk (Twitter).')
print('')


def args_parser():
	#parse required argument/s needed for program
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help='domain - to find subdomains(ex use. http(s)://facebook.com)')
	parser.add_argument('-o', '--output', type=str, required=True, help='filename - file for output data(ex use. facebook.txt)')
	args = parser.parse_args()
	return args



class Abuse_certificate_transparency:
	def __init__(self):
		self.domain = args_parser().domain
		self.output = args_parser().output


	def parse_url(self):
		#parse host from scheme, to use for certificate transparency abuse
		try:
			host = urllib3.util.url.parse_url(self.domain).host
		except Exception as e:
			print('parse_url//Error: %s' % (e))
			pass
		return host


	def request_json(self):
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
					print('json_data:Error %s' % (e))
					pass
		except Exception as e:
			print('request_json//Error: %s' % (e))
			pass
		return subdomains


	def active_subs(self):
		global seen
		active_subdomains = []
		if seen == False:
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
					(Fore.RED+Back.BLACK+str(number_all), Fore.RED+Back.BLACK+'REGISTERED', Fore.GREEN+'subdomains with this domain.'))
				time.sleep(2)
				for index, sub in enumerate(abuse.request_json()):
					print(Fore.GREEN+str(index),Fore.RED+str(sub))

				print('\n',Fore.GREEN+'''{!} There are %s %s %s''' %
					(Fore.RED+Back.BLACK+str(number_active), Fore.RED+Back.BLACK+'ACTIVE', Fore.GREEN+'subdomains with this domain'))
				time.sleep(2)

				print(Fore.RED+Back.GREEN+str('DNS SERVER:\t\t\tSUBDOMAIN:\t\t\tIP-ADDR:\t\t\t'))
				time.sleep(1.3)

				for index, sub in enumerate(active_subdomains):
					print(Fore.RED+str(index),Fore.GREEN+str(sub[0]),Fore.RED+str(sub[1]),Fore.GREEN+str(sub[2]))

			except Exception as e:
					print('{!} active_subdomains//Error: %s' % (e))
					pass

		return active_subdomains


	def write_file(self):
		global seen
		try:
			reg = 'REGISTERED_'+self.output
			active = 'ACTIVE_'+self.output
			if self.output is not None:
				with open(reg,'w') as r:
					for index, sub in enumerate(abuse.request_json()):
						text = '%s %s\n' % (index,sub)
						r.write(text)
				with open(active,'w') as a:
					for index, sub in enumerate(abuse.active_subs()):
						text = '%s %s\n' % (index,sub)
						a.write(text)
		except Exception as e:
			print('write_file//Error: %s' % (e))
			pass
		seen = True



class Dns_zone_transfer:
	def __init__(self):
		self.domain = abuse.parse_url()
		self.output = args_parser().output


	def nslookup(self):
		#nslookup to find nameservers of target domain
		try:
			nameservers = []
			with open('nslookup.txt','w') as output_vale:
				cmd = subprocess.call('nslookup -type=ns %s' % (self.domain), stdout=output_vale)
				with open('nslookup.txt','r') as ns2:
					for line in ns2.readlines():
						if 'nameserver' in line:
							line = line.split(' ')[2]
							nameservers.append(line)
						else:
							pass
			ns2.close()
			os.remove('nslookup.txt')
			#print(nameservers)
		except Exception as e:
			print(e)
		return nameservers


	def dns_records(self):
		#zone transfer - to get dns records if dns server is not configured properly
		count = 0
		try:
			for ns in zone.nslookup():                                                 
                                                      
				with open('gogo.txt','w') as go:
					go.write('nslookup\nset type=all\nserver %s\nls -d %s\n.\n' % (ns,abuse.parse_url()))

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

	seen = False

	abuse = Abuse_certificate_transparency()
	abuse.parse_url()
	abuse.request_json()
	abuse.active_subs()
	abuse.write_file()

	zone = Dns_zone_transfer()
	zone.nslookup()
	zone.dns_records()
