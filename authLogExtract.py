import re, pprint
import operator

authLog = open('auth.log', 'r')
authLogLine = authLog.readlines()
authLog.close()

dateTimestampIPuser = re.compile(r'^(\w{3} {1,2}\d{1,2} \d\d:\d\d:\d\d)' + \
                                 r'.* \w+ (invalid user '
                                 r'[\wa-zA-Z0-9!$* \-]{1,64}'
                                 r'|root|[\wa-zA-Z0-9!$*\-]{6,})' + \
                                 r'.* (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
#
#  For every line, break it into the pieces of interest
#
ipCount = {}
userCount = {}
for line in authLogLine:
    authLine = dateTimestampIPuser.search(line)
    if authLine:
        print(line)
    date, user, IP = authLine.groups()

    if 'invalid' in user:
        user = user.split(sep=' ')
        user = user[2]
    elif 'invalid' not in user:
        user = user.split()
        user = user[0]
    if IP not in ipCount:
        ipCount[IP] = 1

    if IP in ipCount:
        ipCount[IP] += 1

    if user not in userCount:
        userCount[user] = 1

    if user in userCount:
        userCount[user] += 1

topIP = max(ipCount.items(), key=operator.itemgetter(1))[0]
topUser = max(userCount.keys(), key=lambda key:
              userCount[key])


pprint.pprint(ipCount)
pprint.pprint(userCount)
print(topIP, ':', ipCount[topIP])
print(topUser, ':', userCount[topUser])