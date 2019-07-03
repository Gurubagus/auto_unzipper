#!/usr/bin/python3.4

import sys
import os
import time
import zipfile
import errno
import paths


def main():
	global fname
	cwd = paths.unzipper_paths
	for path in cwd:
		f = os.listdir(path)

		for file in f:
			if file.endswith('.zip'):
				fname = str(file)
				zip_ref = zipfile.ZipFile(path +'/' + fname,'r')
				directory = path + '/Flow_' + fname[:-4]
				directory = directory.rsplit('_',1)[0]
				if not os.path.exists(os.path.dirname(directory)):
					try:
						os.makedirs(os.path.dirname(directory))
					except OSError as exc:
						if exc.errno != errno.EEXIST:
							raise
				zip_ref.extractall(directory)
				filelist = zip_ref.namelist()
				for f in filelist:
					os.chmod(directory +'/'+ f, 0o777)
				zip_ref.close()
				os.remove(path +'/'+ fname)

if __name__== "__main__":
	main()
        
    
