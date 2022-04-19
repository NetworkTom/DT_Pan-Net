#!/usr/bin/python
from socket import *
import sys
import struct


ipRangeArg = sys.argv[1]
ipRange = ipRangeArg.split("-")
if len(ipRange) == 1:
    start = ipRange[0]
    end = start
if len(ipRange) == 2:
    start = ipRange[0]
    end = ipRange[1]

start = struct.unpack('>I', inet_aton(start))[0]
end = struct.unpack('>I', inet_aton(end))[0]+1
ipAddreses = [inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]
for ipAddress in ipAddreses:
    print(ipAddress)
    for tcpPort in [53,80,443,8080,139,135]:
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((ipAddress, tcpPort))
        if(conn == 0):
            print ('* %d/tcp open' % (tcpPort,))
            s.close()