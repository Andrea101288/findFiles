import os
from os import path
import glob
from shutil import copyfile, copy 

class CopyFiles():	


	# method to get file extention
	def get_file_ext(self):	
		ext = input("Insert file extention you are interested in(ex: json, jpg, png, txt..)\n")	 
		if '"' in ext:
				ext = ext.replace('"', '')
		return ext
	
    # Method to get source folder path
	def get_source_path(self):	
		while True:    
			root_dir = input("Insert source directory where you want to find the files\n")
			if '"' in root_dir:
				root_dir = root_dir.replace('"', '')
			if(path.exists(root_dir) is False):
				print("Wrong path, the folder path doesn't exist..")
			if(path.exists(root_dir) is True):  
				break  
		return root_dir
	
    # method to get Destination folder path
	def get_dest_path(self):	
		while True:    
			dest_dir = input("Insert destination directory where you want to save the files\n")
			if '"' in dest_dir:
				dest_dir = dest_dir.replace('"', '')
			if(path.exists(dest_dir) is False):
				print("Wrong path, the folder path doesn't exist..")
			if(path.exists(dest_dir) is True):  
				break  
		return dest_dir
	
    # method to get the choise recursive or not from the user
	def choise(self):	
		while True: 
			try:
				folder = int(input("Type 0) Find only in the source folder\nPress 1) Find also in all subdirectories\n"))
				break
			except:
				print("Input not valid.")
				
		return folder

	# Method to copy the desired files from the source to the destination folder
	def copy_files(self, ext, src_dir, dest_dir, choice):
		num_files = 0;	
		while True: 	
            # not recursive search
			if(choice == 0):
				try:
					for file in os.listdir(src_dir):
						if file.endswith("."+ext):
							num_files += 1;
							file_path = os.path.normpath(src_dir+"/"+file)
							copy(file_path, dest_dir)
					if(num_files == 0):
						print("No ."+ext+" files found..")							
					break
				except ValueError:
					print("Problems copying files..")
								
            # recursive search
			elif(choice == 1):
				try:
					path = os.path.normpath('%s/**/*.'+ext)
					for file in glob.iglob(os.path.normpath(path % src_dir), recursive=True):
						num_files += 1;
						copy(file, dest_dir)
					if(num_files == 0):
						print("No ."+ext+" files found..")
					break
				except ValueError:
					print("Problems copying files..")	
			else:
				print("Insert 0 or 1\n")
			
		return num_files			
					
# Main function					
if __name__ == "__main__":

	object = CopyFiles()
	docType = object.get_file_ext()
	srcPath = object.get_source_path()
	dstPath = object.get_dest_path()
	n = object.choise()
	num = object.copy_files(docType, srcPath, dstPath, n)
	if(num > 0):
		if(n == 0):
			print("Done. All ."+ docType +" found files copied from " + srcPath + " into "+dstPath)
		else:
			print("Done. All ."+ docType +" found files copied from " + srcPath + "and its subfolders into "+dstPath)
		
		
		
		
		