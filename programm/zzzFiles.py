import os
from glob import glob

# use linux commands 
# import os
# cmd = 'ls -l'
# os.system(cmd)

class ReadDirs:
    def __init__(self) -> None:
        pass

    def getFolders(self) -> list : 
        folders = glob("./*/")
        return folders

    def getFiles(self, folder:str) -> list :
        files = os.listdir(f"{folder}")
        return files

class FilesNotIncluded:
    def __init__(self) -> None:
        self.notIncludedFiles = []
    def addFile(self, path:str):
        self.notIncludedFiles.append(path)
        
    def printNotIncluded(self):
        print(self.notIncludedFiles)

class FolderFiles:
    def __init__(self) -> None:
        self.dir = ""
        self.htmlFiels = []
        self.mdFiles = []

    def mapFiles(self, filelist:list, folder:str, notincluded:FilesNotIncluded):
        
        for file in filelist:
            if "html" in file[-4:]:
                self.htmlFiels.append(file)
            elif "md" in file[-2:]:
                self.mdFiles.append(file)
            else:
                ret = folder + file
                notincluded.addFile(ret)
                
        print(f"Mapping für {self.dir} abgeschlosen.")
    def getDir(self):
        print(self.dir)
        return self.dir
        


class GetAllFiles:
    def __init__(self) -> None:
        self.readDirs = ReadDirs() 
        self.folders = self.readDirs.getFolders()
        self.FileCollection = []
        self.notIncluded = FilesNotIncluded()

    def mapDirFiles(self):
        for folder in self.folders:
            fileStorage = FolderFiles()
            fileStorage.dir = folder
            files = self.readDirs.getFiles(folder)
            fileStorage.mapFiles(files, folder, self.notIncluded)  
            self.FileCollection.append(fileStorage)
        print("Mapping abgeschlossen")
    
    




    


