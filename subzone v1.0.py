#!d:\python 3.6.5\python.exe

#imports
import argparse
import requests
import urllib3
import json
import subprocess
import os

logo = '''example'''
print(Copyright: © 2008 etc.)


def args_parser():
	#parse required argument/s needed for program
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help='domain - to find subdomains(ex use. http(s)://facebook.com)')
	parser.add_argument('-o', '--output', type=str, required=False, help='filename - file for output data(ex use. facebook.txt)')
	args = parser.parse_args()
	return args



class Abuse_certificate_transparency:
	def __init__(self):
		self.domain = args_parser().domain
		self.output = args_parser().output


	def parse_url(self):
		#parse host from scheme, to use for certificate transparency abuse
		host = urllib3.util.url.parse_url(self.domain).host
		return host


	def request_json(self):
		subdomains = []
		r = requests.get(f'https://crt.sh/?q=%.{abuse.parse_url()}&output=json')
		#r = requests.get('https://crt.sh/?q=%.facebook.com&output=json')
		if r.status_code != 200:
			print('{!} host status-code: %s\n ~ unable to access records using this abuse certificate transparency method' % (r.status_code))
		else:
			try:
				json_data = json.loads('[%s]' % (r.text.replace('}{', '},{')))
				for sub in (json_data):
					subdomains.append(sub['name_value'])
			except:
				pass
		return subdomains


	def log_file(self):
		#log all subdomains found to file for further use by actor
		try:
			if self.output is not None:
				if abuse.request_json() != []:
					xtra = self.output.split('.txt')[0]
					filename = '%s_subdomains.txt' % (xtra)
					with open(filename, 'w') as fp:
						for sub in abuse.request_json():
							fp.write(sub+'\n')
						else:
							pass
				else:
					pass
		except Exception as e:
			print(e)


	def output_console(self):
		#output all subdomains found to veiw in real-time
		try:
			for sub in enumerate(abuse.request_json()):
				print(sub)
		except Exception as e:
			print(e)



class Dns_zone_transfer:
	def __init__(self):
		self.domain = args_parser().domain
		self.output = args_parser().output


	def nslookup(self):
		#nslookup to find nameservers of target domain
		try:
			nameservers = []
			with open('nslookup.txt','w') as ns:
				cmd = subprocess.call('nslookup -type=ns zonetransfer.me', stdout=ns)#NEED TO CHANGE URL TO SELF>DOMAIN
				with open('nslookup.txt','r') as ns:
					for line in ns.readlines():
						if 'nameserver' in line:
							ns = line.split(' ')[2]
							nameservers.append(ns)
						else:
							pass
			os.remove('nslookup.txt')
		except Exception as e:
			print(e)
		return nameservers



	def dns_records(self):
		#zone transfer - to get dns records if dns server is not configured properly
		try:
			for ns in zone.nslookup():
				with open('gogo.txt','w') as go:
					go.write('nslookup\nset type=all\nserver %s\nls -d %s\n.\n' % (ns,abuse.parse_url()))

				if self.output is not None:
					xtra = self.output.split('.txt')[0]
					filename = '%s_Dns_records.txt' % (xtra)
					if len(ns) == int(1):
						with open(filename,'w') as file:
							with open('gogo.txt','r') as fp:
								cmd = subprocess.call('cmd.exe', stdin=fp, stdout=file)
					elif len(ns) > int(1):
						with open(filename,'a')as file:
							with open('gogo.txt','r') as fp:
								cmd = subprocess.call('cmd.exe', stdin=fp, stdout=file)
					else:
						pass
				else:
					with open('gogo.txt','r') as fp:
						cmd = subprocess.call('cmd.exe', stdin=fp)
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
	abuse = Abuse_certificate_transparency()
	abuse.parse_url()
	abuse.request_json()
	abuse.log_file()
	abuse.output_console()

	zone = Dns_zone_transfer()
	zone.nslookup()
	zone.dns_records()