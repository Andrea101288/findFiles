import os
from os import path
import glob
from shutil import copyfile, copy 

class copyFiles():	
	
	def getFileExt(self):	
		ext = input("Insert file extention you are interested in(ex: json, jpg, png, txt..)\n")	 
		if '"' in ext:
				ext = ext.replace('"', '')
		return ext
		
	def getSourcePath(self):	
		while True:    
			rootdir = input("Insert source directory where you want to find the files\n")
			if '"' in rootdir:
				rootdir = rootdir.replace('"', '')
			if(path.exists(rootdir) is False):
				print("Wrong path, the folder path doesn't exist..")
			if(path.exists(rootdir) is True):  
				break  
		return rootdir
		
	def getDestinationPath(self):	
		while True:    
			dstDir = input("Insert destination directory where you want to save the files\n")
			if '"' in dstDir:
				dstDir = dstDir.replace('"', '')
			if(path.exists(dstDir) is False):
				print("Wrong path, the folder path doesn't exist..")
			if(path.exists(dstDir) is True):  
				break  
		return dstDir
	
	def choise(self):	
		while True: 
			try:
				folder = int(input("Type 0) Find only in the source folder\nPress 1) Find also in all subdirectories\n"))
				break
			except:
				print("Input not valid.")
				
		return folder

	
	def copyFiles(self, ext, srcDir, dstDir, choice):
		numFiles = 0;	
		while True: 						
			if(choice == 0):
				try:
					for file in os.listdir(srcDir):
						if file.endswith("."+ext):
							numFiles += 1;
							filePath = os.path.normpath(srcDir+"/"+file)
							copy(filePath, dstDir)
					if(numFiles == 0):
						print("No ."+ext+" files found..")							
					break
				except ValueError:
					print("Problems copying files..")
												
			elif(choice == 1):
				try:
					path = os.path.normpath('%s/**/*.'+ext)
					for file in glob.iglob(os.path.normpath(path % srcDir), recursive=True):
						numFiles += 1;
						copy(file, dstDir)
					if(numFiles == 0):
						print("No ."+ext+" files found..")
					break
				except ValueError:
					print("Problems copying files..")	
			else:
				print("Insert 0 or 1\n")
			
		return numFiles			
					
# Main function					
if __name__ == "__main__":

	object = copyFiles()
	docType = object.getFileExt()
	srcPath = object.getSourcePath()
	dstPath = object.getDestinationPath()
	n = object.choise()
	num = object.copyFiles(docType, srcPath, dstPath, n)
	if(num > 0):
		if(n == 0):
			print("Done. All ."+ docType +" found files copied from " + srcPath + " into "+dstPath)
		else:
			print("Done. All ."+ docType +" found files copied from " + srcPath + "and its subfolders into "+dstPath)
		
		
		
		
		