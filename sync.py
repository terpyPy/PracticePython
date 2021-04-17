#!/usr/bin/python3
#
#  Author:      Richard Barton
#  Date:        17 November 2018
#  Description: Given two directories as arguments, make sure
#               each directory contains the same files with the
#               same modification times as the other directory.
#

import sys
import os
import shutil

#
#  Find the name of this script using basename() and argv[]
#  for use in error messages.
#
progName = os.path.basename(sys.argv[0])
print(progName)

#
#  Make sure the user gave us two arguments.  If not, exit with
#  a non-zero exit code.
#
if len(sys.argv) != 3:
    print('usage:' + progName + ' <directory to sync.py with>' + \
          ' <directory to be sync>')
    sys.exit(1)
#
#  Get those two arguments into varibles named first and second.
#
first, second = sys.argv[1:]
# print(first, second)
#
#  Make sure first and second both are paths to an existing
#  directory using isdir().  Exit with a non-zero exit code after
#  displaying an error message if there's something wrong with
#  either argument.
#
#
exit = 0
if os.path.isdir(first) == False:
    print(first + ' is not a directory')
    exit += 1
if os.path.isdir(second) == False:
    print(second + ' is not a directory')
    exit += 1
if exit > 0:
    sys.exit(1)
print(first + ' <contains to be synced> ' + second + \
      ' <will be synced there.>')


#
#  Define a method named checkCopy that takes two arguments.
#  The method assumes both arguments are directories that
#  exist.  It goes through all the files contained in the first
#  argument using listdir().  For each, it creates a full path to
#  the file using join().  It uses isfile() to skip files that
#  aren't real files.  It uses getmtime() to get the modification
#  time of the file.  It creates a full path to the corresponding
#  file in the second directory.  If the file doesn't exist in the
#  second directory, it prints that it's copying the first path
#  to the second path and then uses copy2() to perform the copy
#  preserving the modification time.  If the file does exist in the
#  second directory, it gets that second file's modification time.
#  If the first file is newer than the second, it prints that it's
#  copying the first path to the second path and then uses copy2()
#  to perform the copy preserving the modification time.
#
def checkCopy(firstDir, secondDir):
    #
    # get every file in the first directory
    #

    files = (os.listdir(firstDir))
    for i in range(len(files)):
        #
        # join the items in the list files to the first directory to create the path
        #
        file = os.path.join(firstDir, files[i])
        if (os.path.isfile(file) is True):
            fileTime = os.path.getmtime(file)
            print(file, 'is a file')
            syncFile = os.path.join(secondDir, files[i])



        if (os.path.exists(syncFile) is False):
            print('copying ' + file + ' to location ' + syncFile)
            shutil.copy2(file, syncFile)

        elif (os.path.exists(syncFile) is True):
            print('this file exsits already in ' + syncFile)
            modTime = os.path.getmtime(syncFile)
        if fileTime > modTime:
            modTime = fileTime
            print(file, 'has a newer modification time then', syncFile)
            print('copying newest file to ' + syncFile +
                  ' from ' + file)
            shutil.copy2(file, syncFile)

        if (os.path.isfile(file) is False):
            print('not a real file')


#
#  checkCopy is called to copy files from first to second and
#  then from second to first.
#
checkCopy(first, second)
