#!/usr/bin/env python3
# encoding = utf-8
#  ▓▓▓▓▓▓▓▓▓▓ 
# ░▓ Author ▓ Abdullah <https://abdullah.today/> 
# ░▓▓▓▓▓▓▓▓▓▓ 
# ░░░░░░░░░░ 
# This program renames multiple file names how you answer the questions asked by the program.

#Copyright 2019 Abdullah (abdullah@abdullah.today)

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os

path = str(input("Type the path where your files are located? e.g. /home/ak/Documents\n " ))
realpath = str(path + str('/'))
extension = str(input("Type the extension of the files you wanna rename? e.g. .jpg, .png, .mp3\n "))
prefix = str(input("Type the prefix you wanna replace the file names with? e.g. if you enter 'ak' here, all files will be renamed like ak1.jpg, ak2.jpg\n "))


def main():
    i = 1
    for x in os.listdir(realpath):
        destination = prefix + str(i) + extension
        source = realpath + x
        destination = realpath + destination

        os.rename(source, destination)
        i += 1

if __name__ == '__main__':
    main()
