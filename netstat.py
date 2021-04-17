import time
import subprocess

stdout = [None, None]
stderr = [None, None]
# cmd line arg for net stats full, human parasable stdout, given a short time frame.
# collect the stdout for netstat through Popen, pipe both stdin and out
netstat = subprocess.Popen(['netstat', '-s'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)
#time the first Popen start
startTime = time.ctime()
#store the the output from run1
stdout[0], stderr[0] = netstat.communicate()
#store the text
stdout[0] = stdout[0].split('\n')

time.sleep(10)

netstat = subprocess.Popen(['netstat', '-s'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)
# collect the time at end of run
endTime = time.ctime()

stdout[1], stderr[1] = netstat.communicate() # store your end stats

stdout[1] = stdout[1].split('\n') # format the string on new line char

if (len(stdout[0]) != len(stdout[1])):
    print('they aren\'t the same length') # you got diffrent outputs, mismatch

print(startTime.rjust(40), '|', endTime)

for i in range(len(stdout[0])):
    # init all headers we care to collect, 
    # no regex cuz suprocess objs can parse like basic regex 
    header = stdout[0][i].startswith('IPv')
    header2 =stdout[0][i].startswith('ICMP')
    header3 = stdout[0][i].startswith('TCP')
    header4 = stdout[0][i].startswith('UPD')
    # check for each header once per index of stdout
    if header == True:
        header = stdout[0][i]
        print(header)
    if header2 == True:
        header2 = stdout[0][i]
        if header2 == stdout[0][i] == stdout[1][i]:
            continue
        print(header2)
    if header3 == True:
        header3 = stdout[0][i]
        if header3 == stdout[0][i] == stdout[1][i]:
            continue
        print(header3)
    if header4 == True:
        header4 = stdout[0][i]
        if header4 == stdout[0][i] == stdout[1][i]:
            continue
        print(header4)

    if stdout[0][i] == stdout[1][i]:
        continue
    print(stdout[0][i].ljust(60), '|', stdout[1][i])

