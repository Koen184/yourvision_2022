from tkinter import Button as bt, Label as lb
import webbrowser
import MenuGUI

class NotebookGUI():
    
    def __init__(self, window, canvas, backgroundImage, logoSpotify):
        
        canvas.create_image( 0, 0, image = backgroundImage, anchor = "nw")
        canvas.create_text(84, 454, font = ("Eurovision Song Contest 2015 V2", 48), text = "N\no\nt\ne\nb\no\no\nk", fill = "black")
        canvas.create_text(80, 450, font = ("Eurovision Song Contest 2015 V2", 48), text = "N\no\nt\ne\nb\no\no\nk", fill = "white")
        
        canvas.create_rectangle(30, 30, 115, 115, outline = "white", fill = "black")
        canvas.create_rectangle(30, 875, 115, 790, outline = "white", fill = "black")
        
        canvas.create_rectangle(180, 0, 530, 900, outline = "white", fill = "black")
        
        buttonExit = bt(window, text = "X", font = ("Arial", 32), height = 1, width = 3, bg = "#FF0000", command = lambda: [NotebookGUI.close_NotebookGUI(canvas, label1, label2, buttonPlayYT, buttonPlaySpotify), MenuGUI.MenuGUI.open_MenuGUI(window, canvas, backgroundImage, logoSpotify)])
        buttonUp = bt(window, text = "⇑", font = ("Arial", 32), height = 1, width = 3, bg = "#B5BBFF", command = lambda: [NotebookGUI.move_Up(self), NotebookGUI.generate_ListCountries(window, canvas, self.flag, label1, label2, buttonPlayYT, buttonPlaySpotify)])
        buttonDown = bt(window, text = "⇓", font = ("Arial", 32), height = 1, width = 3, bg = "#B5BBFF", command = lambda: [NotebookGUI.move_Down(self), NotebookGUI.generate_ListCountries(window, canvas, self.flag, label1, label2, buttonPlayYT, buttonPlaySpotify)])
        
        canvas.create_window(50, 10, anchor = "nw", window = buttonExit) 
        canvas.create_window(40, 20, anchor = "nw", window = buttonUp) 
        canvas.create_window(40, 780, anchor = "nw", window = buttonDown) 
        
        label1 = lb(window, font = ("Eurovision Song Contest 2015 V2", 112), text = " ", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2 = lb(window, font = ("Helvetica", 32), text = " ", bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")
        label1.place(x = 580, y = 20)
        label2.place(x = 580, y = 220)
        
        buttonPlayYT = bt(window, text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164")
        buttonPlayYT.place(x = 581, y = 740)
        
        buttonPlaySpotify = bt(window, text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371")
        buttonPlaySpotify.place(x = 1562, y = 740, anchor = "ne")

        self.flag = 0
        NotebookGUI.generate_ListCountries(window, canvas, self.flag, label1, label2, buttonPlayYT, buttonPlaySpotify)
        
        window.mainloop()

    def move_Up(self):
        
        if (self.flag == 0):
            self.flag = 0
        else:
            self.flag -= 1
            
    def move_Down(self):
        
        if (self.flag == 3):
            self.flag = 3
        else:
            self.flag += 1
        
    def generate_ListCountries(window, canvas, flag, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        if (flag == 0):
            
            buttonAlbania = bt(window, text = "Albania", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoAlbania(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 20, anchor = "nw", window = buttonAlbania)
            
            buttonArmenia = bt(window, text = "Armenia", font =("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoArmenia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 107, anchor = "nw", window = buttonArmenia) 
            
            buttonAustralia = bt(window, text = "Australia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoAustralia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 194, anchor = "nw", window = buttonAustralia) 
            
            buttonAustria = bt(window, text = "Austria", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoAustria(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 281, anchor = "nw", window = buttonAustria) 
            
            buttonAzerbaijan = bt(window, text = "Azerbaijan", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoAzerbaijan(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 368, anchor = "nw", window = buttonAzerbaijan) 
            
            buttonBelgium = bt(window, text = "Belgium", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoBelgium(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 455, anchor = "nw", window = buttonBelgium) 
            
            buttonBulgaria = bt(window, text = "Bulgaria", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoBulgaria(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 542, anchor = "nw", window = buttonBulgaria) 
            
            buttonCroatia = bt(window, text = "Croatia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoCroatia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 629, anchor = "nw", window = buttonCroatia) 
            
            buttonCyprus = bt(window, text = "Cyprus", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoCyprus(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 716, anchor = "nw", window = buttonCyprus) 
            
            buttonCzechia = bt(window, text = "Czechia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoCzechia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 803, anchor = "nw", window = buttonCzechia) 
            
        if (flag == 1):
            
            buttonDenmark = bt(window, text = "Denmark", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoDenmark(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 20, anchor = "nw", window = buttonDenmark)
            
            buttonEstonia = bt(window, text = "Estonia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoEstonia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 107, anchor = "nw", window = buttonEstonia) 
            
            buttonFinland = bt(window, text = "Finland", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoFinland(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 194, anchor = "nw", window = buttonFinland) 
            
            buttonFrance = bt(window, text = "France", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoFrance(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 281, anchor = "nw", window = buttonFrance) 
            
            buttonGermany = bt(window, text = "Germany", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoGermany(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 368, anchor = "nw", window = buttonGermany) 
            
            buttonGeorgia = bt(window, text = "Georgia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoGeorgia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 455, anchor = "nw", window = buttonGeorgia) 
            
            buttonGreece = bt(window, text = "Greece", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoGreece(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 542, anchor = "nw", window = buttonGreece) 
            
            buttonIceland = bt(window, text = "Iceland", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoIceland(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 629, anchor = "nw", window = buttonIceland) 
            
            buttonIreland = bt(window, text = "Ireland", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoIreland(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 716, anchor = "nw", window = buttonIreland) 
            
            buttonIsrael = bt(window, text = "Israel", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoIsrael(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 803, anchor = "nw", window = buttonIsrael)
            
        if (flag == 2):
            
            buttonItaly = bt(window, text = "Italy", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoItaly(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 20, anchor = "nw", window = buttonItaly)
            
            buttonLatvia = bt(window, text = "Latvia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoLatvia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 107, anchor = "nw", window = buttonLatvia) 
            
            buttonLithuania = bt(window, text = "Lithuania", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoLithuania(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 194, anchor = "nw", window = buttonLithuania) 
            
            buttonMalta = bt(window, text = "Malta", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoMalta(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 281, anchor = "nw", window = buttonMalta) 
            
            buttonMoldova = bt(window, text = "Moldova", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoMoldova(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 368, anchor = "nw", window = buttonMoldova) 
            
            buttonMontenegro = bt(window, text = "Montenegro", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoMontenegro(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 455, anchor = "nw", window = buttonMontenegro) 
            
            buttonThe_Netherlands = bt(window, text = "The Netherlands", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoThe_Netherlands(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 542, anchor = "nw", window = buttonThe_Netherlands) 
            
            buttonNorth_Macedonia = bt(window, text = "North Macedonia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoNorth_Macedonia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 629, anchor = "nw", window = buttonNorth_Macedonia) 
            
            buttonNorway = bt(window, text = "Norway", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoNorway(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 716, anchor = "nw", window = buttonNorway) 
            
            buttonPoland = bt(window, text = "Poland", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoPoland(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 803, anchor = "nw", window = buttonPoland)
            
        if (flag == 3):
            
            buttonPortugal = bt(window, text = "Portugal", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoPortugal(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 20, anchor = "nw", window = buttonPortugal)
            
            buttonRomania = bt(window, text = "Romania", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoRomania(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 107, anchor = "nw", window = buttonRomania) 
            
            buttonSan_Marino = bt(window, text = "San Marino", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoSan_Marino(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 194, anchor = "nw", window = buttonSan_Marino) 
            
            buttonSerbia = bt(window, text = "Serbia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoSerbia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 281, anchor = "nw", window = buttonSerbia) 
            
            buttonSlovenia = bt(window, text = "Slovenia", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoSlovenia(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 368, anchor = "nw", window = buttonSlovenia) 
            
            buttonSpain = bt(window, text = "Spain", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoSpain(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 455, anchor = "nw", window = buttonSpain) 
            
            buttonSweden = bt(window, text = "Sweden", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoSweden(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 542, anchor = "nw", window = buttonSweden) 
            
            buttonSwitzerland = bt(window, text = "Switzerland", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoSwitzerland(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 629, anchor = "nw", window = buttonSwitzerland) 
            
            buttonUkraine = bt(window, text = "Ukraine", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoUkraine(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 716, anchor = "nw", window = buttonUkraine) 
            
            buttonUnited_Kingdom = bt(window, text = "United Kingdom", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: NotebookGUI.show_InfoUnited_Kingdom(window, label1, label2, buttonPlayYT, buttonPlaySpotify))
            canvas.create_window(200, 803, anchor = "nw", window = buttonUnited_Kingdom)
        
    def show_InfoAlbania(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Albania", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Festivali i Këngës 60\nRepresentant: Ronela Hajati\nSong Title: Sekret\nSongwriters: Ronela Hajati, Marko Polo\n\nSemi Final Results: 12th place, 58 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")
  
        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=iMu47raqbcc"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0zC65JcBBk4GYAjL2tHKXa?si=5094fd4c302b4c13"))
        
    def show_InfoArmenia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Armenia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Rosa Linn\nSong Title: Snap\nSongwriters: Rosa Linn and her team\n\nSemi Final Results: 5th place, 187 points\nFinal Results: 20th place, 61 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=gVqGKkm7xBE"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0QPRDC97rIQB3Jh3hrVJoH?si=2b623f5022cc4cec"))
        
    def show_InfoAustralia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Australia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Eurovision – Australia Decides\nRepresentant: Sheldon Riley\nSong Title: Not the Same\nSongwriters: Sheldon Riley, Cam Nacson,\nTimi Temple\n\nSemi Final Results: 2nd place, 243 points\nFinal Results: 15th place, 125 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=ByUD4d89_is"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/27ThQIsofXro6xEz3SzQWi?si=13ac929e42314190"))
        
    def show_InfoAustria(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Austria", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Lum!x ft. Pia Maria\nSong Title: Halo\nSongwriters: Luca Michlmayr and his team\n\nSemi Final Results: 15th place, 42 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=tF6LY7lnVFU"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/6WVHfpzYW3HooQaCC80opC?si=d6e6cae2e84347cf"))
        
    def show_InfoAzerbaijan(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Azerbaijan", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Nadir Rustamli\nSong Title: Fade to Black\nSongwriters: Andreas Stone Johansson,\n Anderz Wrethov\n\nSemi Final Results: 10th place, 96 points\nFinal Results: 16th place, 106 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=TGd1AFKR_-E"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/7aX4w6c7gSqbTBoU8g2lnm?si=008ef310b97a4ca3"))
        
    def show_InfoBelgium(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Belgium", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Jérémie Makiese\nSong Title: Miss You\nSongwriters: Jérémie Makiese and his team\n\nSemi Final Results: 8th place, 151 points\nFinal Results: 19th place, 64 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=GZ3mLO4uFjY"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/4VgSGm7CroAlCCt9GKQ75Z?si=048aa2d5d18f4c4a"))
        
    def show_InfoBulgaria(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Bulgaria", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Inteligent Music Project\nSong Title: Intention\nSongwriters: Milen Vrabevski\n\nSemi Final Results: 16th place, 29 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=HySI2igCcx4&t=78s"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/15z4ROfFailed to QualifyCoxnzr2uOBYBn?si=0db1346026644584"))
        
    def show_InfoCroatia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Croatia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Dora\nRepresentant: Mia Dimšić\nSong Title: Guilty Pleasure\nSongwriters: Mia Dimšić and her team\n\nSemi Final Results: 11th place, 75 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=DFBwe2w0zO4"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/70HQXHPuU7EyUroOYkOzdk?si=8c713eb3ad694d78"))
        
    def show_InfoCyprus(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Cyprus", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Andromache\nSong Title: Ela\nSongwriters: International team\n\nSemi Final Results: 12th place, 63 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=GM8CY08UT6I"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0er8krd7cEtPxVEEv0ZEHi?si=dec55cdf4c9f491f"))
        
    def show_InfoCzechia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Czechia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Eurovision Song CZ\nRepresentant: We Are Domi\nSong Title: Lights Off\nSongwriters: We Are Domi and their team\n\nSemi Final Results: 4th place, 227 points\nFinal Results: 22nd place, 38 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=QRgj3enaAhI"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0tOKpglJb9cza4WdTtxsv7?si=54aac6b25bf1415c"))
        
    def show_InfoDenmark(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Denmark", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Dansk Melodi Grand Prix\nRepresentant: Reddi\nSong Title: The Show\nSongwriters: Chief 1 and his team\n\nSemi Final Results: 13th place, 55 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=xqakAZP4D24"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/68UTfPKNrG4L9zKYcnD8fQ?si=af87b8671b0d4963"))
        
    def show_InfoEstonia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Estonia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Eesti Laul\nRepresentant: Stefan\nSong Title: Hope\nSongwriters: Stefan Airapetjan,\nKarl-Ander Reismann\n\nSemi Final Results: 5th place, 209 points\nFinal Results: 13th place, 141 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=bKhSlSx00-I"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/6sSq38pmQxG0YuvbipDoEi?si=cdedc8ce2dea4557"))

    def show_InfoFinland(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Finland", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Uuden Musiikin Kilpailu\nRepresentant: The Rasmus\nSong Title: Jezebel\nSongwriters: Lauri Ylönen, Desmond Child\n\nSemi Final Results: 7th place, 162 points\nFinal Results: 21st place, 38 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=IwHijzdNN2A"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/2NehRqeFiEGV72lFfqJGUn?si=ab502810412f4963"))
        
    def show_InfoFrance(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "France", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: C'est vous qui décidez\nRepresentant: Alvan and Ahez\nSong Title: Fullen\nSongwriters: Marine Lavigne,\nAlvan Morvan Rosius\n\nSemi Final Results: Automatic Qualifier\nFinal Results: 24th place, 17 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=CO07xLUlK2g"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/20zRSC9mnT7m2kQXrZP0rH?si=74164df37207447a"))
        
    def show_InfoGermany(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Germany", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Germany 12 Points\nRepresentant: Malik Harris\nSong Title: Rockstars\nSongwriters: Malik Harris, Marie Kobylka,\nRobin Karow\n\nSemi Final Results: Automatic Qualifier\nFinal Results: 25th (last) place, 6 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=Oy-s-IZIHkI"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0KBS6MmhnlB2i1AjcYiDlN?si=ee610fee75274573"))

    def show_InfoGeorgia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Georgia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Circus Mircus\nSong Title: Lock Me In\nSongwriters: Circus Mircus\n\nSemi Final Results: 18th (last) place, 22 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=qgukml7zDAA"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/7ed3JsAPk6u0NjRhylnKmY?si=aa086fef3f914609"))

    def show_InfoGreece(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Greece", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Amanda Tenfjord\nSong Title: Die Together\nSongwriters: Amanda Tenfjord and her team\n\nSemi Final Results: 3rd place, 211 points\nFinal Results: 8th place, 215 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=Uv7PcRKXZDg"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/35b0iM96Uid8KI5s83IEHM?si=e22128a136f0447a"))

    def show_InfoIceland(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Iceland", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Söngvakeppnin\nRepresentant: Systur\nSong Title: Með Hækkandi Sól\nSongwriters: Lovísa Elísabet\nSigrúnardóttir\n\nSemi Final Results: 10th place, 103 points\nFinal Results: 23rd place, 20 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=vk9D10EyxHA"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/4t3gM4Rl5rz5du0Qn2Yd8K?si=981bbde52814412e"))
        
    def show_InfoIreland(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Ireland", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Eurosong\nRepresentant: Brooke\nSong Title: That's Rich\nSongwriters: Brooke Scullion, Izzy Warner,\nKarl Zine\n\nSemi Final Results: 15th place, 47 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=pkHzvy-Pscw"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/1oS41M8cx60aAeNe3k5Csw?si=f932240d3b14476d"))
        
    def show_InfoIsrael(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Israel", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: The X Factor Israel\nRepresentant: Michael Ben David\nSong Title: I.M\nSongwriters: Chen Aharoni, Lidor Saadia,\nAsi Tal\n\nSemi Final Results: 13th place, 61 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=WNFeohWlA20"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/4Bpz4FBsoe9lhuiCWZv21x?si=032aa6c9bac0454b"))
        
    def show_InfoItaly(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Italy", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Sanremo Music Festival\nRepresentant: Mahmood and Blanco\nSong Title: Brividi\nSongwriters: Mahmood, Blanco,\nMichele Zocca\n\nSemi Final Results: Automatic Qualifier\nFinal Results: 6th place, 268 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=Beqe14HYY5o"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/1ZMGp9MTXbtAPvcKa0U3zS?si=244d84082cba4a62"))

    def show_InfoLatvia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Latvia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Supernova\nRepresentant: Citi Zēni\nSong Title: Eat Your Salad\nSongwriters: Citi Zēni\n\nSemi Final Results: 14th place, 55 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=DbDj9mBI4g0"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0rNIEBlBuo5108lnHyGbqJ?si=a2ae1ce40a9b4163"))
        
    def show_InfoLithuania(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Lithuania", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Pabandom Iš Naujo\nRepresentant: Monika Liu\nSong Title: Sentimentai\nSongwriters: Monika Liubinaitė\n\nSemi Final Results: 7th place, 159 points\nFinal Results: 14th place, 128 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=acya6UcJP1k"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0JNPmXGU9K9DJpV9eHppZz?si=5e037a13f67540a0"))
        
    def show_InfoMalta(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Malta", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Malta Eurovision Song Contest\nRepresentant: Emma Muscat\nSong Title: I Am What I Am\nSongwriters: Emma Muscat and her team\n\nSemi Final Results: 16th place, 47 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=df-fks-Pj-8"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/1FtqYazfNvsqR4CQvzrrD3?si=9d7adf6e8eb945ca"))
        
    def show_InfoMoldova(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Moldova", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Zdob și Zdub\nSong Title: Trenulețul\nSongwriters: Zdob și Zdub\n\nSemi Final Results: 8th place, 154 points\nFinal Results: 7th place, 253 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=C9RJQPZsj8E"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/63idiVcxkGB3hgH6n3qKqM?si=23483d3c9f7a465f"))
        
    def show_InfoMontenegro(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Montenegro", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Vladana\nSong Title: Breathe\nSongwriters: Vladana Vučinić,\nDarko Dimitrov\n\nSemi Final Results: 17th place, 33 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=7e3GiXy7SLc"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/4vvVUzVIVVpXRdzdlU765E?si=fa03cb64b0b14731"))
        
    def show_InfoThe_Netherlands(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "The Netherlands", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: S10\nSong Title: Die Diepte\nSongwriters: Stien den Hollander,\nArno Krabman\n\nSemi Final Results: 2nd place, 221 points\nFinal Results: 11th place, 171 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=v2m-MGSys0k"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/7uQ7e7nzbtyX87eIYHpj6Z?si=33c360b2e1ee43fb"))
        
    def show_InfoNorth_Macedonia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "North Macedonia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Za Evrosong\nRepresentant: Andrea\nSong Title: Circles\nSongwriters: Aleksandar Masevski,\nAndrea Koevska\n\nSemi Final Results: 11th place, 76 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=EzOpAduUlmo"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/7uQ7e7nzbtyX87eIYHpj6Z?si=33c360b2e1ee43fb"))

    def show_InfoNorway(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Norway", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Melodi Grand Prix\nRepresentant: Subwoolfer\nSong Title: Give That Wolf a Banana\nSongwriters: Keit, Jim,\nDj Astronaut\n\nSemi Final Results: 6th place, 177 points\nFinal Results: 10th place, 182 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=O_AvUlCQ_Cc"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/50Cf2eYv8zT3v2HAkwhIiL?si=1a2aa5d6288840a1"))
        
    def show_InfoPoland(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Poland", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Tu Bije Serce Europy\nRepresentant: Ochmann\nSong Title: River\nSongwriters: Krystian Ochamnn,\n Mikołaj Trybulec\n\nSemi Final Results: 6th place, 198 points\nFinal Results: 12th place, 151 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=wh47vgUwInU"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/2fSz6MBKMPjOApUhGYfPid?si=754e9cfb3f404f2b"))
        
    def show_InfoPortugal(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Portugal", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Festival da Canção\nRepresentant: Maro\nSong Title: Saudade, Saudade\nSongwriters: Maro, John Blanda\n\nSemi Final Results: 4th place, 208 points\nFinal Results: 9th place, 207 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=eQul-rkcGPQ"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/4S4Amrpr631M16IIXqRk73?si=9b99d5cff007413f"))

    def show_InfoRomania(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Romania", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Selecția Națională\nRepresentant: WRS\nSong Title: Llámame\nSongwriters: WRS and his team\n\nSemi Final Results: 9th place, 118 points\nFinal Results: 18th place, 65 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=Ru3y4ivY3lQ"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/3n9qn38IhqkC7DcdIRaM9q?si=c68e0acaaf3844ff"))
        
    def show_InfoSan_Marino(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "San Marino", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Una voce per San Marino\nRepresentant: Achille Lauro\nSong Title: Stripper\nSongwriters: Achille Lauro and his team\n\nSemi Final Results: 14th place, 50 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=P-RloZ-Fv38"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/1PpH00KzrWRN3um8vSbi7A?si=49e186a38f244e47"))

    def show_InfoSerbia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Serbia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Pesma za Evroviziju '22\nRepresentant: Konstrakta\nSong Title: In Corpore Sano\nSongwriters: Ana Đurić,\nMilovan Bošković\n\nSemi Final Results: 3rd place, 237 points\nFinal Results: 5th place, 312 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=3S1jrYq87Zw"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/1JaOUMmaSZlWfONvT4HTlg?si=c2ddd54699b940d1"))
        
    def show_InfoSlovenia(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Slovenia", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Evrovizijska Melodija\nRepresentant: LPS\nSong Title: Disko\nSongwriters: LPS\n\nSemi Final Results: 17th (last) place, 15 points\nFinal Results: Failed to Qualify",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=g8Ezl7xucCU"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/5bx4DPSuvBUn6luswgF7Ez?si=a135a02e83624bfb"))
        
    def show_InfoSpain(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Spain", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Benidorm Fest\nRepresentant: Chanel\nSong Title: SloMo\nSongwriters: International team\n\nSemi Final Results: Automatic Qualifier\nFinal Results: 3rd place, 459 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=N3eiW6E0ldc"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/3XREkzDHsWdBL5tybyCDBH?si=46297f4662de47b1"))
        
    def show_InfoSweden(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Sweden", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Melodifestivalen\nRepresentant: Cornelia Jakobs\nSong Title: Hold Me Closer\nSongwriters: Cornelia Jakobsdotter, Isa Molin,\n David Zandén\n\nSemi Final Results: 1st place, 396 points\nFinal Results: 4th place, 438 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=wWDThAfryW4"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/697bFWgzBRm6bmnYWd8GyD?si=62870b9ffeaa4364"))

    def show_InfoSwitzerland(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Switzerland", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Marious Bear\nSong Title: Boys Do Cry\nSongwriters: Marius Hügli, Martin Gallop\n\nSemi Final Results: 9th place, 118 points\nFinal Results: 17th place, 78 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=EnsqrM40uaY"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/5A3JxIX04W5Ttu6Rxy5tWW?si=7c3711330170404d"))

    def show_InfoUkraine(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "Ukraine", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Vidbir (2nd place was chosen)\nRepresentant: Kalush Orchestra\nSong Title: Stefania\nSongwriters: Kalush Orchestra\n\nSemi Final Results: 1st place, 337 points\nFinal Results: 1st place, 637 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=UiEGVYOruLk"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/0unPBMjVwn0HpWget3DBze?si=18c3903b0a8c41a9"))
        
    def show_InfoUnited_Kingdom(window, label1, label2, buttonPlayYT, buttonPlaySpotify):
        
        label1.config(font = ("Eurovision Song Contest 2015 V2", 112), text = "United Kingdom", bg = "white", height = 1, width = 15, borderwidth = 2, relief = "solid")
        label2.config(font = ("Helvetica", 32), text = "Selection Process: Internal Selection\nRepresentant: Sam Ryder\nSong Title:Space Man\nSongwriters: Sam Ryder, Amy Wadge,\nMax Wolfgang\n\nSemi Final Results: Automatic Qualifier\nFinal Results: 2nd place, 466 points",
                           bg = "white", height = 10, width = 39, borderwidth = 2, relief = "solid")

        buttonPlayYT.config(text = "Play on YT  ▶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#FE4164", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=udsMTb2NIak"))
        buttonPlaySpotify.config(text = "Play on Spotify 🎶", font = ("Helvetica", 24), height = 2, width = 15, bg = "#3CB371", command = lambda: webbrowser.open("https://open.spotify.com/track/3nhGk6VnrDHy67pXvMhdPa?si=c4140487d58d4b99"))

    def open_NotebookGUI(window, canvas, backgroundImage, logoSpotify):

        NotebookGUI(window, canvas, backgroundImage, logoSpotify)
        
    def close_NotebookGUI(canvas, label1, label2, buttonPlayYT, buttonPlaySpotify):

        canvas.delete("all")
        label1.destroy()
        label2.destroy()
        buttonPlayYT.destroy()
        buttonPlaySpotify.destroy()