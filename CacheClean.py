import os, shutil
from time import sleep
from colorama import Fore,init,Back

cache_folders = ['C:/Windows/Prefetch','C:/Windows/Temp','C:/Users/user/AppData/Local/Temp']

folderContentsCount = 0

init(autoreset=True)
for folderName in cache_folders:
	splitFolderName = folderName.split('/')[len(folderName.split('/'))-1]
	print('\n'+('-'*35)+'\n')
	print(Fore.CYAN+'Process folder: {0}'.format(splitFolderName))
	sleep(2)
	folderContentsCount = len(os.listdir(folderName))
	for fileName in os.listdir(folderName):
		file = os.path.join(folderName, fileName)
		try:
			if os.path.isfile(file) or os.path.islink(file):
				os.unlink(file)
			elif os.path.isdir(file):
				shutil.rmtree(file)
			print(Fore.GREEN+file+" Deleted")
		except Exception as e:
			print(Fore.RED+'Delete error: {0}{1}'.format(e, '\n'))
	print(Back.GREEN+'{0} deleted contents: {1}'.format(splitFolderName, folderContentsCount))
init(autoreset=False)
sleep(3)
