#!/usr/bin/python3
import sys
import os
import shutil
import zipfile

maxBackupNumber = 2
#
# the first command line argument is the directory to contain
# the backup files
# the second command line arg is the directory to be backed up
#


progName = os.path.basename(sys.argv[0])
print(progName)
if len(sys.argv) != 3:
    print('usage:' + progName + ' <directory containing backups>' + \
          ' <directory to be backed up>')
    sys.exit(1)

backupDirectory, directoryToBackup = sys.argv[1:]
print(backupDirectory)
exit = 0
if os.path.isdir(backupDirectory) == False:
    print(backupDirectory + ' is not a directory')
    sys.exit(1)

if os.path.isdir(directoryToBackup) == False:
    print(directoryToBackup + 'is not a directory')
    sys.exit(1)
if exit > 0:
    sys.exit(1)

print(backupDirectory + ' contains backups and' + directoryToBackup + \
      ' will be backed up there.')

#
#
#
recentFileTime = 0

for directoryName, subDirectory, fileName in os.walk(directoryToBackup):
    print('directoryName:', directoryName)
    print('subDirectory:', subDirectory)
    print('fileName:', fileName)
    for filePath in fileName:
        print('filePath', filePath)
        pathName = os.path.join(directoryName, filePath)
        print('pathName:', pathName)
        pathTime = os.path.getmtime(pathName)
        print('pathTime:', pathTime)
        if (pathTime > recentFileTime):
            recentFileTime = pathTime

print('recentFileTime:', recentFileTime)

backupFile = os.path.join(backupDirectory, 'backup.0.zip')
youngestBackupTime = 0
if (os.path.exists(backupFile) == True):
    youngestBackupTime = os.path.getmtime(backupFile)
print('youngestBackupTime:', youngestBackupTime)

if (youngestBackupTime >= recentFileTime):
    print('No new files to backup')
    sys.exit(0)
#
# There must be files to backup. we need to preform another backup
#

#
# rotate the existing backups so that backup.0.zip is available
#
newBackupName = os.path.join(backupDirectory,
                             'backup.' + str(maxBackupNumber) + '.zip')
for i in range(maxBackupNumber -1, -1, -1):
    oldBackupName = newBackupName
    newBackupName = os.path.join(backupDirectory,
                                 'backup.' + str(i) + '.zip')
    if (os.path.exists(newBackupName) == False):
        continue
    shutil.move(newBackupName, oldBackupName)
#
# open our new backup zip file
#
backupZip = zipfile.ZipFile(newBackupName, 'w')

#
# find each file in dirtobackup and zip a copy into our new backup
#
for directoryName, subDirectory, fileName in os.walk(directoryToBackup):
    for directoryPath in subDirectory:
        pathName = os.path.join(directoryName, directoryPath)
        #print('backup directory named: '+ pathName)
        backupZip.write(pathName)
    for filePath in fileName:
        pathName = os.path.join(directoryName, filePath)
        #print('backup file named: '+ pathName)
        backupZip.write(pathName)
# close our backup file
backupZip.close()