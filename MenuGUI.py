from tkinter import Button as bt
from tkinter import BOTTOM
import NotebookGUI
import TopMakerGUI
import SpotifyAppGUI
import HelpGUI

class MenuGUI():
    
    def __init__(self, window, canvas, background, logoSpotify):

        canvas.create_image( 0, 0, image = background, anchor = "nw")
        canvas.create_text(800, 150, font = ("Eurovision Song Contest 2015 V2", 142), text = "Yourvision 2022", fill = "black")
        canvas.create_text(800, 150, font = ("Eurovision Song Contest 2015 V2", 138), text = "Yourvision 2022", fill = "white")
        canvas.create_text(800, 270, font = ("Helvetica", 32), text = "Select the module you want to use 😄", fill = "white")

        canvas.create_rectangle(280, 320, 570, 820, outline = "white", fill = "black")
        canvas.create_rectangle(680, 320, 970, 820, outline = "white", fill = "black")
        canvas.create_rectangle(1080, 320, 1370, 820, outline = "white", fill = "black")
        canvas.create_rectangle(1470, 850, 1548, 772, outline = "white", fill = "black")
        canvas.create_rectangle(1470, 730, 1548, 642, outline = "white", fill = "black")

        self.flagHelp = 1

        buttonNotebook = bt(window, text = "Notebook\n📓🤓", font = ("Helvetica", 32), height = 10, width = 12, bg = "#FFB5FC", command = lambda: [MenuGUI.close_MenuGUI(canvas), NotebookGUI.NotebookGUI.open_NotebookGUI(window, canvas, background, logoSpotify)])
        buttonTopMaker = bt(window, text = "Top\nMaker\n🥇 🥈 🥉", font = ("Helvetica", 32), height = 10, width = 12, bg = "#ECB5FF", command = lambda: [MenuGUI.close_MenuGUI(canvas), TopMakerGUI.TopMakerGUI.open_TopMakerGUI(window, canvas, background, logoSpotify)])
        buttonSpotify = bt(window, text = "Spotify\nApp\n", font = ("Helvetica", 32), image = logoSpotify, compound = BOTTOM, height = 519, width = 300, bg = "#D4B5FF", command = lambda: [MenuGUI.close_MenuGUI(canvas), SpotifyAppGUI.SpotifyAppGUI.open_SpotifyAppGUI(window, canvas, background, logoSpotify)])
        buttonHelp = bt(window, text = "🤔", font = ("Helvetica", 32), height = 1, width = 3, bg = "#B5BBFF", command = lambda: HelpGUI.HelpGUI.open_HelpGUI(self.flagHelp))
        buttonExit = bt(window, text = "❌", font = ("Arial", 32), height = 1, width = 3, bg = "#FF0000", command = lambda: MenuGUI.CLOSE_MenuGUI(window))

        canvas.create_window(400, 600, anchor = "center", window = buttonNotebook) 
        canvas.create_window(800, 600, anchor = "center", window = buttonTopMaker) 
        canvas.create_window(1200, 600, anchor = "center", window = buttonSpotify)
        canvas.create_window(1500, 822, anchor = "center", window = buttonHelp)
        canvas.create_window(1500, 692, anchor = "center", window = buttonExit)
        
    def open_MenuGUI(window, canvas, background, logoSpotify):

        MenuGUI(window, canvas, background, logoSpotify)
        
    def close_MenuGUI(canvas):

        canvas.delete("all")
        
    def CLOSE_MenuGUI(window):

        window.destroy()
        
    def windowSizePosition(window, window_height, window_width):
    
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))