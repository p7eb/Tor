import urllib2
import sys
from bs4 import BeautifulSoup

#Checks to make sure that there are 3 argments or if the help flag was called. Quits the script.
if len(sys.argv) <> 2 or sys.argv[1]=="-h" or sys.argv[1]=="--help":
	print "###################################"
	print "#     Tor Exit Node Collector     #"
	print "###################################\n"
	print "Sample Usage: \n python TorExit.py TorExitTriples.nt"
	quit()

oFile = open(sys.argv[1], 'w')

response = urllib2.urlopen('https://collector.torproject.org/recent/exit-lists/')
html = response.read()

r = requests.get('https://dan.me.uk/torlist/', allow_redirects=False,verify=False)

parser = BeautifulSoup(html, 'html.parser')
exitList = response.read().splitlines()
