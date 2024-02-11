from tkinter import Canvas as cv, Toplevel as tp
import MenuGUI

class HelpGUI:
    
    def __init__(self, flag):

        window = tp()
        
        if flag == 1:

            fileHelp = open("Texts\helptext.txt", "r")
            helptext = fileHelp.read()

        if flag == 2:

            fileHelp = open("Texts\helptopmakertext.txt", "r")
            helptext = fileHelp.read()

        if flag == 3:

            fileHelp = open("Texts\helpspotitext.txt", "r")
            helptext = fileHelp.read()

        window.title('Yourvision_2022_Help')
        window.geometry("800x450")

        window_height = 450
        window_width = 800
        
        MenuGUI.MenuGUI.windowSizePosition(window, window_height, window_width)

        canvasH = cv(window, width = 800, height = 450)
        canvasH.pack(fill = "both", expand = True)

        canvasH.create_text(10, 10, font = ("Helvetica", 12), text = helptext, fill = "black", anchor = "nw")
        
        fileHelp.close()
        window.mainloop()
        
    def open_HelpGUI(flag):

        HelpGUI(flag)