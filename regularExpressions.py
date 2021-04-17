#!/usr/bin/python3

import re

sample = ['What does (803) 822-3250 represent?',
          'What does 803-822-3250 represent?',
          'What does 803.822.3250 represent?',
          'What does 803 822 3250 represent?',
          'What does 912-34-5678 represent?',
          'What does 3/18/13 represent?',
          'What does 3/18/2013 represent?',
          'What does 18 Mar 2013 represent?',
          'What does 6011 3295 2214 2618 represent?',
          'What does 192.168.43.201 represent?',
          'What does 2001:db8:0123:4567:89ab:cdef:0123:4567 represent?',
          'What does ca:36:44:11:46:ea represent?',
          'What does Fred T. Sanford represent?',
          'What does 316 South Beltline Boulevard represent?',
          'What does 316 Beltline Boulevard represent?',
          'What does 316 Beltline Blvd represent?',
          'What does Columbia, SC 29205 represent?',
          'What does Columbia, SC 29205-3624 represent?',
          'What does Columbia SC 29205-3624 represent?',
          'what does coolcam2@live.com represent']

phoneNumberRE = re.compile(r'\(?\d\d\d\)?[-. ]\d\d\d[-. ]\d\d\d\d')
SSN_RE = re.compile(r'\d\d\d-\d\d-\d\d\d\d')
dateRE = re.compile(r'\d{1,2}/\d{1,2}/\d{2}(\d{2})?')
date2RE = re.compile(r'\d{1,2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{2}(\d{2})?')
creditCardRE = re.compile(r'(\d{4} ){4}')
ipv4AddressRE = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
ipv6AddressRE = re.compile(r'([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}')
MAC_RE = re.compile(r'([\da-fA-F]{2}:){5}[\da-fA-F]{1,2}')
nameRE = re.compile(r'^What does ([\w\s\d.]+) represent\?$')
streetAddressRE = re.compile(r'^What does (\d+ [\w ]+) represent\?$')
cityStateZIP_RE = re.compile(r'^What does ([\w\s-]+,? \w{2} \d{5}(-\d{4})?) represent\?$')
emailRE = re.compile(r'([\da-zA-Z]+)(@)(live|hotmail|msn|outlook)(.[\wa-z]{3})')
for line in sample:
    noMatch = True
    print('=-=-= ' + line + ' =-=-=')
    match = phoneNumberRE.search(line)
    if (match != None):
        print(match.group() + ' is a phone number')
        continue

    match = SSN_RE.search(line)
    if (match != None):
        print(match.group() + ' is a Social Security Number')
        continue

    match = dateRE.search(line)
    if (match != None):
        print(match.group() + ' is a date')
        continue

    match = date2RE.search(line)
    if (match != None):
        print(match.group() + ' is a date')
        continue

    match = creditCardRE.search(line)
    if (match != None):
        print(match.group() + 'is a credit card number')
        continue

    match = ipv4AddressRE.search(line)
    if (match != None):
        print(match.group() + ' is an IPV4 address')
        continue

    match = ipv6AddressRE.search(line)
    if (match != None):
        print(match.group() + ' is an IPV6 address')
        continue

    match = MAC_RE.search(line)
    if (match != None):
        print(match.group() + ' is a MAC address')
        continue

    match = nameRE.search(line)
    if (match != None):
        noMatch = False
        print(' '.join(match.groups()) + ' might be a name')

    match = streetAddressRE.search(line)
    if (match != None):
        noMatch = False
        print(' '.join(match.groups()) + ' might be a street address')

    match = cityStateZIP_RE.search(line)
    if (match != None):
        noMatch = False
        print(match.groups()[0] +
              ' might be a city, state & ZIP')

    match = emailRE.search(line)
    if match is not None:
        noMatch = False
        print(match.group() + ' might be an email address')

    if (noMatch == True):
        print('No match')
