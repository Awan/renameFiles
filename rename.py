#!/usr/bin/env python
# encoding = utf-8


#  ▓▓▓▓▓▓▓▓▓▓
# ░▓ Author ▓ Abdullah <https://abdullah.today/>
# ░▓▓▓▓▓▓▓▓▓▓
# ░░░░░░░░░░


#   This program renames multiple file names how you answer the questions asked
#   by the program.


#   The MIT License (MIT)
#   Copyright (c) 2019 Abdullah <abdullah at abdullah dot today>
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the "Software"),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.


from pathlib import Path
import pathlib
import os
q1 = input(str("Where are your files located?\n "))
q2 = input(str("OK, do you wanna rename all files or only with some extension?\
    Enter '*' for all files, or some extension e.g. 'mp3', '.mp4', '.jpg'\n"))
path = Path(q1)
glob = q2.strip()
q3 = input(str("Good, type the prefix you wanna replace filenames with. e.g. if\
    you enter 'AK', all of your files will be renamed to AK1, AK2, AK3.\n"))
prefix = q3
filesMatched = list(path.glob('*'+glob))
files = [str(x) for x in filesMatched]
_path = os.listdir(path)


def ext():
    i = 1
    for x in files:
        destination = prefix + str(i) + glob
        realPath = pathlib.PurePath(path, x)
        source = realPath
        destination = str(path) + '/' + destination
        os.rename(source, destination)
        i += 1


def all():
    i = 1
    for x in _path:
        destination = prefix + str(i)
        realPath = pathlib.PurePath(path, x)
        source = realPath
        destination = str(path) + '/' + destination
        os.rename(source, destination)
        i += 1


if glob == '*':
    all()
elif glob != '*':
    ext()
