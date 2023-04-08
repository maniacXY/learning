import os 
from glob import glob
from pprint import pprint

class ReadDirs:
    def __init__(self) -> None:
        pass

    def getFolders(self) -> list : 
        folders = glob("./*/")
        folders.remove("./programm/")
        return folders

    def getFiles(self, folder:str) -> list :
        files = os.listdir(f"{folder}")
        return files

class Mapper:
    def __init__(self) -> None:
        #folder = { folderName: { 
        #               htmlFiles:[]
        #               mdFiles:[] 
        #                        }, 
        #           folder2Name ..
        #           uselessFiles:[]

        #          }
        self.__mappping = {"questionFiles":[]}
        self.__readDirs = ReadDirs()
        self.__folders = self.__readDirs.getFolders()
        self.__mapFolders()
        self.__mapFiles()

    def my_decorator(func):
        def wrapper(self):
            print("\n")
            func(self)
            print("\n")
        return wrapper

    def __mapFolders(self):
        for folder in self.__folders:
            self.__mappping[folder] = {
                "htmlFiles": [],
                "mdFiles": []
            }
        
    def __mapFiles(self) -> None:
        for folder in self.__folders:
            files = self.__readDirs.getFiles(folder)
            for file in files:
                if "html" in file[-4:]:
                    self.__mappping[folder]["htmlFiles"].append(file)
                elif "md" in file[-2:]:
                    self.__mappping[folder]["mdFiles"].append(file)
                else:
                    completePath = folder + file
                    self.__mappping["questionFiles"].append(completePath)
    
    @my_decorator
    def printDict(self)->None:
        pprint(self.__mappping)
    
    def getDirs(self) -> list:
        keys = self.__mappping.keys()
        retlist = []
        for item in keys: 
            if item != "questionFiles":
                retlist.append(item)
        return retlist

    def getQuestionFiles(self) -> list:
        return self.__mappping["questionFiles"]

    def getHTMLFiles(self) -> list:
        """
        returns .hmtl files in a list
        """
        keys = self.__folders
        htmlList= []
        for key in keys:
            if key is not "questionFiles":
                tmplist = self.__mappping[key]["htmlFiles"]    
                for file in tmplist:
                    htmlList.append(key+file)
        return htmlList
    
    def getFolderFiles(self, folder:str, format:str) -> list:
        """ retuns Files of a Folder. Format html/md"""
        formater = format.lower()
        if format == "md":
            formater = "mdFiles"
        if formater == "html":
            formater = "htmlFiles"
        filelist = self.__mappping[folder][formater]
        return filelist

    def getMDFiles(self) -> list:
        keys = self.__folders
        mdList= []
        for key in keys:
            
            tmplist = self.__mappping[key]["mdFiles"]    
            for file in tmplist:
                mdList.append(key+file)
        return mdList

