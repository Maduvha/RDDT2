import nmap
from socket import *
from uuid import getnode as get_mac
import socket
import MySQLdb
nm = nmap.PortScanner()
nm.scan('146.64.204.48-108')

db = MySQLdb.connect("localhost", "root", "", "detect")
cursor = db.cursor()


Name = ''
Product = ''
IP = ''
Port =''
for host in nm.all_hosts():
    print('------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    #print('State : %s' % nm[host].state())
    IP = host
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport.sort()
        count = 0

        for port in lport:
            Product = nm[host][proto][port]['product']
            Name = nm[host][proto][port]['name']
            Port = port
            #print ('Port' + '\t'  + '\t' + 'Name ' + '\t'  + '\t' +'Application/Product')
            #print port +'\t'+ '\t' + nm[host][proto][port]['name'] + '\t'  + '\t' + nm[host][proto][port]['product']
            print ('port : %s\tname : %s\t Product :%s' % (port, nm[host][proto][port]['name'],nm[host][proto][port]['product']))
            count = count + 1

            sql = "INSERT INTO port (IP_Address,ports,P_name,Product) VALUES ( '%s', '%s', '%s' ,'%s')" % (IP, Port, Name, Product)

            try:
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()

            except:
                db.rollback()


        print ( "TOTAL OF OPEN PORTS IS :", count)

        if count > 0 and count <= 2:
            St = "LOW"
            print St
        elif count >= 3 and count <= 5:
            St = "MEDIUM"
            print St
        else:
            St = "HIGH"
            print St

        sqli = "INSERT INTO count (IP_Address,OpenPorts,Vulnerability) VALUES ('%s','%s','%s')" % (
            host, count, St)

        try:
            cursor.execute(sqli)
            # Commit your changes in the database
            db.commit()

        except:
            db.rollback()



db.close()







































































