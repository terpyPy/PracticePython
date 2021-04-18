#!/usr/bin/python3
import pathlib
import os
import re

#
pythonScript = []
textFiles = []
imageFiles = []



#
#
# call our function to descend our home directory and collect
# those files we think are python scripts, image files,
# word docs, pdf's, txt files and image files
def searchDirectory(path):
    #
    # find all the items under the given directory
    #
    for fileName in os.listdir(path):
        pathName = (os.path.join(path, fileName))
        try:
            if os.path.isdir(pathName):
                searchDirectory(pathName)
                continue
        except PermissionError:
            #   print(pathName, 'directory can not be accessed')
            continue
        # if this is a directory, call oneself to search this directory
        #
        imageCheckRE = re.compile(r"png$|mp4$")
        imageCheck = imageCheckRE.search(fileName)
        if imageCheck is not None:
            imageFiles.append(pathName)
            continue
            #
        FilenameCheckRE2 = re.compile(r"txt$|docx$|pptx$")
        Textcheck = FilenameCheckRE2.search(fileName)
        if Textcheck is not None:
            textFiles.append(pathName)
            continue
            #
        if not os.path.isfile(pathName):
            # print(pathName + 'pathName is not a file!')
            continue
            #
        # print(pathName + ' is a file')
        # if not a file skip it
        # open the file
        try:
            fileToSearch = open(pathName, 'r')

        except PermissionError and IndexError:
            print(pathName, 'file can not be opened')
            continue
            # if you cant open it skip it
        try:
            fileLine = fileToSearch.readlines()
            # print(fileLine[0])
        except UnicodeDecodeError:
            fileToSearch.close()
            continue
        # check to see if the extension on the file is .py
        FilenameCheckRE = re.compile(r"py$|pyc$")
        #
        FilenameCheck = FilenameCheckRE.search(fileName)
        #
        # if so add it to he script list
        if FilenameCheck is not None:
            pythonScript.append(pathName)
            continue
        #
        # read the content if not sure
        # if we cant read the file or file empty skip it
        shebangLineCheckRE = re.compile(r"#!/usr/bin/python3")
        try:
            shebangLine = shebangLineCheckRE.search(fileLine[0])
            # print(fileName)
        except IndexError:
            fileToSearch.close()
            continue
        #
        # Check for shebang if there add to the list
        if shebangLine is not None:
            pythonScript.append(pathName)
            fileToSearch.close()
            continue
            # close file
            # print(pathName)
    
#
# searchDirectory(userPath)
# if the list has any entries, print the list
searchDirectory(userPath)
if len(pythonScript) > 0:
    print()
    for pathName in pythonScript:
        print(os.path.relpath(pathName, userPath))
if len(textFiles) > 0:
    print(
        )
    for pathName in textFiles:
        print(os.path.relpath(pathName, userPath))
if len(imageFiles) > 0:
    print(
        )
    for pathName in imageFiles:
        print(os.path.relpath(pathName, userPath))
