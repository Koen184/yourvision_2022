from tkinter import Tk as tk, Canvas as cv, PhotoImage as pi
import pyglet
import MenuGUI    

pyglet.font.add_file("Fonts\Eurovision_Song_Contest_2015_V2.ttf")
pyglet.font.load("Eurovision Song Contest 2015 V2")

window = tk()

window.title('Yourvision_2022')

window_height = 900
window_width = 1600

MenuGUI.MenuGUI.windowSizePosition(window, window_height, window_width)

backgroundImage = pi(file = "Images\Background.png")
logoSpotify = pi(file = "Images\LogoSpotify.png")

canvas = cv(window, width = 1600, height = 900)
canvas.pack(fill = "both", expand = True)

MenuGUI.MenuGUI(window, canvas, backgroundImage, logoSpotify)
   
window.mainloop()