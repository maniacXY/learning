from programm.Mapping import Mapper
from pprint import pprint

# md struktur
# ['#[BACK](../index.html)\n',
#  '\n',
#  '# Inhaltsangabe\n',
#  '- [Elektolehre Basics](#elektrolehre-basics)\n',
#  '\t- [Spannungseinheiten](#spannungseinheiten)\n',
#  '\t- [Verhätnisse-Quotienten](#verhätnisse-quotienten)\n',
#  '\t- [Potentialunterschied](#potentialunterschied)\n',
#  '\t- [Reihenschaltung](#reihenschaltung)\n',
#  '\t- [Parallelschaltung](#parallelschaltung)\n',
#  '- [Widerstand](#widerstand)\n',
#  '\t- [Wattberechung](#wattberechung) \n',
#  '- [Schein-Wirkleistung](#schein-wirkleistung)\n',
#  '\n',
#  '# Elektolehre Basics\n',
#  'Steckdose immer 230V bemessen\n',
#  '\n',
#  '## Spannungseinheiten\n',

# vor jedem chapter ein [top](#) außer beim ersten da ein Back bzw da startet inhaltsanagbe


# was noch ? Inhaltsangabe, Backbutton-top, topbutton after chapter

class MarkdownFinisher(Mapper):
    def __init__(self) -> None:
        super().__init__()
        self.backbutton = "# [BACK](../index.html)\n"
        self.topbutton = "[TOP](#)\n\n"
        self.topbuttons = False

    def __linkConverter(self, linkToConvert:str) -> str:
        tmpWord = linkToConvert.lower()
        tmpWord = tmpWord.replace(" ", "-")
        return tmpWord
    def replaceHash(self, lineofString: str):
        replacing = ("#", "\n", "\t")
        tmpLine = lineofString
        for item in replacing:
            tmpLine = tmpLine.replace(item, "")
        return tmpLine.strip()


    def __listHighLevel(self,ueberschriftHigh:str) -> str:
        link = self.__linkConverter(ueberschriftHigh)
        return f"- [{ueberschriftHigh}](#{link})\n"
    
    def __listLowerLevel(self,ueberschriftLower:str) -> str:
        link = self.__linkConverter(ueberschriftLower)
        return f"\t- [{ueberschriftLower}](#{link})\n"



    def inhaltsangabeTopButtons( self ) ->None: 
        files = self.getMDFiles()
        for file in files:
        
            readFile = self.readFile(file)
            topbuttonIndex = []
            if self.backbutton in readFile:
                continue
            inhaltsangabe = [self.backbutton ,"# Inhaltsangabe\n"]
            
            for i in range(len(readFile)):
                line = readFile[i]
                
                if "##" in line[:4]:
                    cleaned = self.replaceHash(line)
                    headerlow = self.__listLowerLevel(cleaned)
                    inhaltsangabe.append(headerlow )
                    
                elif "#" in line[:4]:
                    cleaned = self.replaceHash(line)
                    headerhigh = self.__listHighLevel(cleaned)
                    topbuttonIndex.append(i)
                    inhaltsangabe.append(headerhigh)
            inserted = 0
            topbuttonIndex.pop(0)
            for ind in topbuttonIndex:
                readFile.insert(ind + inserted, self.topbutton)   
                inserted += 1  
            inhaltsangabe.append("\n")
            retList = inhaltsangabe + readFile
            with open (file, "w") as f:
                f.writelines(retList)
        

class HTMLFinisher(Mapper):
    def __init__(self, templatePath: str, nameHeaderfile : str, nameFooterfile:str, placeHolder:str) -> None:
        """example Path = ./testdir/ Filename = myfile.txt"""
        super().__init__()
        self.__templatePath = templatePath
        self.__nameHeader = nameHeaderfile
        self.__nameFooter = nameFooterfile
        self.__header = []
        self.__footer = []
        self.readHeaderFooter(placeHolder)

    def readHeaderFooter(self, placeHolder:str) -> None:
        self.__header = self.replaceStyleCSS(self.__templatePath+self.__nameHeader, placeHolder, "../style.css")
        with open(self.__templatePath+ self.__nameFooter, "r") as f:
            tmplist = f.readlines()
        self.__footer = tmplist
        
        

    def headerFooterCompose(self):
        files = self.getHTMLFiles()
        for file in files:
            with open (file, "r") as f:
                tmpfile = f.readlines()
            tmpfile = self.__header + tmpfile + self.__footer
            pprint(tmpfile)
            with open (file, "w") as f:
                f.writelines(tmpfile)
                
    