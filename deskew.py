#!/usr/bin/env python
# encoding: utf-8
"""
correct.py

Created by Vincent Ahrend on 2012-02-24.
Copyright (c) 2012 Vincent Ahrend. All rights reserved.
"""

import os
from PIL import Image


def main():
    """ Load an image file, de-skew it, and save it back """
    dircontents = os.walk(os.getcwd()).next()
    
    # compile list of .jpeg files in current directory
    filelist = list()
    for fname in dircontents[2]:
        if fname[-3:].lower() == 'jpg' or fname[-4:].lower() == 'jpeg':
            filelist.append(os.path.join(os.getcwd(), fname))
    
    if len(filelist) == 0:
        print "No files found.\nPlease put some .jpg or .jpeg files in this directory to deskew them."
            
    print "Processing %d files" % len(filelist)
    
    for filename in filelist:
        print filename, "..."
        im = Image.open(filename)
        w, h = im.size
        pa = im.load()
        for line in range(h):
            _buf = list()
            for col in range(w):
                _buf.append(pa[(col+line)%w, line])
            for col in range(w):
                pa[col, line] = _buf[col]
        
        im.save(filename)


if __name__ == '__main__':
    main()

