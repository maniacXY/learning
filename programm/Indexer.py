from programm.Mapping import Mapper
from pprint import pprint

class Indexer(Mapper):
    def __init__(self, pathToHeader, placeHolder) -> None:
        super().__init__()
        self.htmlstringList = self.replaceStyleCSS(pathToHeader, placeHolder)
        self.placeholder = "<PLACEHOLDER>"
        self.__compose()
        
    def __str__(self) -> str:
        return "index.html wird erstellt"
    
    def __compose(self):
        # setting file up
        self.htmlstringList.append(self.__ueberschrift())
        for dir in self.getDirs():
            filelist = []
            for file in self.getFolderFiles(dir, "html"):
                filelist.append(file)
            self.__chapter(dir, filelist)
        self.htmlstringList.append("</body></html>")
        self.__writeFile()
        
    def __ueberschrift(self):
        return '<h1 id="alle-seiten">Alle Seiten</h1>'

    def __chapter(self, Überschrift:str, Files:list):
        
        self.htmlstringList.append(f'<h2 id="{Überschrift.lower()}">{Überschrift}</h2><ul>')
        for file in Files:
            self.htmlstringList.append(f'<li><a href="{Überschrift}{file}">{file}</a></li>')
        self.htmlstringList.append('</ul>')
        
    def __writeFile(self):
        
        with open("index.html", "w") as file:
            file.writelines(self.htmlstringList)





