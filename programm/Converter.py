import os

class Converter:

    def __init__(self) -> None:
        pass


    def MDtoHTML(self, filePath):
        # use linux commands 
        # import os
        # cmd = 'ls -l'
        # os.system(cmd)
        
        command = f"pandoc {filePath} -o {filePath[:-2]}html"
        os.system(command)