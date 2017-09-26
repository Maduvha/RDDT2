import nmap
import MySQLdb

#def portScan():
nm = nmap.PortScanner()
nm.scan('146.64.204.89')


print(nm.csv())
