#!/usr/bin/env python3
#-----------------------------------------------------------
# Takes a directory from argv, walks the directory structure
# and returns a list of duplicate files and their md5sums
#-----------------------------------------------------------

import os
import hashlib
from sys import argv

class dedupe:
    def __init__(self, basepath):
        self.basedir = basepath
    def walkthedir(self):
        filelist = []
        try:
            self.dirtree = list(os.walk(self.basedir))
            for d, subds, fnames in self.dirtree:
                for fname in fnames:
                    filelist.append(os.path.join(d,fname))
        excpect Exception as e:
            print(e)
            break
        finally:
            break
        return filelist
    def hashthefiles(self, filelist):
        hashlist = {}
        for f in filelist:
            md5 = hashlib.md5()
            blocksize = os.statvfs(f).f_blocks
            try:
                fhandler = open(f, 'rb', buffering=blocksize)
                while True:
                    buff = fhandler.read(blocksize)
                    if not buff:
                        break
                    md5.update(buff)
                h = md5.hexdigest()
                if h in hashlist.keys():
                    hashlist[h].append(f)
                else:
                    hashlist[h] = [f]
            except Exception as e: 
                print(e)
                break
            finally:
                fhandler.close()
        return hashlist


if __name__ == '__main__':
    basepath = argv[1]
    x = dedupe(basepath)
    filelist = x.walkthedir()
    hashes = x.hashthefiles(filelist)
    print(str(hashes))
