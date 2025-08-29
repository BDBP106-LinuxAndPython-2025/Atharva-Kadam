#!/bin/bash

ls
ls > listoffiles
cat listoffiles
ls 1> listoffiles
cat listoffiles

ls -l . newdir
ls -l . newdir 1>presentfiles 2>filesnotpresent
cat filesnotpresent
cat presentfiles
#the output shows the error shown after we tried to check the contents of newdir when it doesnt exist
#while presentfiles contains all the files of the current directories

ls -l . newdir >listoffiles
cat listoffiles
#here the standard output is saved in listoffiles only the successful part of the command gets saved to that file the error part of the command doesnt get saved to the file because the error code 2> is not given with the file name
