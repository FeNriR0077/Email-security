#!/usr/bin/python3

import email
import re,sys
import argparse
from colorama import Fore, Back, Style

print(Fore.GREEN+"""
                         _ _      _    _____      __   __
         _ __ ___   __ _(_) |____| |  |   _ |____|  | / /
        | '_ ` _ \ / _` | | |  __| |__|  |_||  __|  |/ /
        | | | | | | (_| | | | |__|  _ |  |__| |__|    \_
        |_| |_| |_|\__,_|_|_|____|_||_|_____|____|__|\_\__

	    	    Made By: Shardul(FeNriR)                                    
   
   A tool to analyze email header to identify spoofed emails for phishing and spam !!!!
	""")

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="enter the raw(original) email file",type=str)
args=parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

# Reading the file Need to take the file as command line arguments argparse
f = open(args.file)
msg = email.message_from_file(f)
f.close()

parser.print_help()
print(Style.RESET_ALL)
parser = email.parser.HeaderParser()
headers = parser.parsestr(msg.as_string())


mailcheck={
	"message-id":"",
	"spf-record":False,
	"dkim-record":False,
	"dmarc-record":False,
	"spoofed":False,
	"ip-address":"",
	"sender-client":"",
	"spoofed-mail":"",
	"dt":"",
	"content-type":"",
	"subject":""
}

for h in headers.items():

	# Message ID
	if h[0].lower()=="message-id":
		mailcheck["message-id"]=h[1]


	# Mail server sending the mail
	if h[0].lower()=="received":
		mailcheck["sender-client"]=h[1]

	# Authentication detected by mail server
	if h[0].lower()=="authentication-results":

		if(re.search("spf=pass",h[1])):
			mailcheck["spf-record"]=True;

		if(re.search("dkim=pass",h[1])):
			mailcheck["dkim-record"]=True
	
		if(re.search("dmarc=pass",h[1])):
			mailcheck["dmarc-record"]=True

		if(re.search("does not designate",h[1])):
			mailcheck["spoofed"]=True
			
		if(re.search("(\d{1,3}\.){3}\d{1,3}", h[1])):
			ip=re.search("(\d{1,3}\.){3}\d{1,3}", h[1])
			mailcheck["ip-address"]=str(ip.group())
			# print("IP Address: "+ip.group()+"\n")

	if h[0].lower()=="reply-to":
		mailcheck["spoofed-mail"]=h[1]

	if h[0].lower()=="date":
		mailcheck["dt"]=h[1]

	if h[0].lower()=="content-type":
		mailcheck["content-type"]=h[1]

	if h[0].lower()=="subject":
		mailcheck["subject"]=h[1]

print(Fore.BLUE+"\n=========================Results=========================\n"+Style.RESET_ALL)

print(Fore.GREEN+"[+] Message ID"+mailcheck["message-id"])

if(mailcheck["spf-record"]):
	print(Fore.GREEN+"[+] SPF Records: PASS")
else:
	print(Fore.RED+"[+] SPF Records: FAIL")

if(mailcheck["dkim-record"]):
	print(Fore.GREEN+"[+] DKIM: PASS")
else:
	print(Fore.RED+"[+] DKIM: FAIL")

if(mailcheck["dmarc-record"]):
	print(Fore.GREEN+"[+] DMARC: PASS")
else:
	print(Fore.RED+"[+] DMARC: FAIL")

if(mailcheck["spoofed"] and (not mailcheck["spf-record"]) and (not mailcheck["dkim-record"]) and (not mailcheck["dmarc-record"])):
	print(Fore.RED+"[+] Spoofed Email Received")
	print(Fore.RED+"[+] Mail: "+mailcheck["spoofed-mail"])
	print(Fore.RED+"[+] IP-Address:  "+mailcheck["ip-address"])
else:
	print(Fore.GREEN+"[+] Authentic Email Received")
	print(Fore.GREEN+"[+] IP-Address:  "+mailcheck["ip-address"])

print(Fore.GREEN+"[+] Provider "+mailcheck["sender-client"])
print(Fore.GREEN+"[+] Content-Type: "+mailcheck["content-type"])
print(Fore.GREEN+"[+] Date and Time: "+mailcheck["dt"])
print(Fore.GREEN+"[+] Subject: "+mailcheck["subject"]+"\n\n")