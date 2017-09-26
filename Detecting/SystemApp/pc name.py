from socket import *
from uuid import getnode as get_mac
import socket
import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "detect")
cursor = db.cursor()
#Device details function
#def device_details():
print('running~')

network = '146.64.204.'

for ip in xrange(84, 90):
    addr = network + str(ip)
    mac = (get_mac())
    theVal = ''
    theNam = addr
    theStat = (getfqdn(addr))
    cursor = db.cursor()


    if (getfqdn(addr) == addr):
        print 'Ip Address'  + '\t' + '' + '\t' + '' + '\t' + 'Pc Name' '\t' + '' + '\t' + 'Status'
        print (addr)  + '\t' + '' + '\t'+ '' + '\t'+ (getfqdn(addr))+ '\t' + ('Off')


        try:
            # Execute the SQL command
            cursor.execute('UPDATE count SET PC_Name = "%s" WHERE IP_Address = "%s"' % (getfqdn(addr), addr))
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
