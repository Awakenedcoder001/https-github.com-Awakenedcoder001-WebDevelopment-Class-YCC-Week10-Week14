class WindowsXp(object):
    """docstring for ClassName"""
    def notepad(self):
        print("Notepad is to write important things")
    
    def wordpad(self):
        print("Wordpad is used to write normal things")

OS2=WindowsXp()
OS2.notepad()
class WindowsVista(WindowsXp):
    pass

OS1=WindowsVista()
OS1.notepad()
OS1.wordpad()

