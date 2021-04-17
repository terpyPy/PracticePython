#!/usr/bin/python3
import re
syslog = open('syslog', 'r')
syslogLine = syslog.readlines()
syslog.close()
dateTimestampIPport = re.compile(r'(^\w{3} {1,2}\d{1,2} \d\d:\d\d:\d\d) ' + \
                                 r'.* SRC=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' + \
                                 r'.* DPT=(\d{1,5})')
for line in syslogLine:
    searchResult = dateTimestampIPport.search(line)
    if searchResult == None:
        print('no match in', line, end='')
        continue
    timeStamp, sourceIP, port = searchResult.groups()
    port = int(port)
    #print(line, end='')
    print(timeStamp, sourceIP.ljust(15), port)
