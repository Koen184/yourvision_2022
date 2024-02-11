from tkinter import Button as bt, Label as lb, Entry as en, StringVar as sv, Listbox as li
from tkinter import END, CENTER, ANCHOR
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import MenuGUI
import HelpGUI

class SpotifyAppGUI:
    
    def __init__(self, window, canvas, backgroundImage, logoSpotify):
        
        user_id = 'Tu_Wpisz_ID_Uzytkownika_Spotify'
        secret = 'Tu_Wpisz_Secret_ID_Uzytkownika_Spotify'
        token = 'Tu_Wpisz_Token'

        client_credentials_manager = SpotifyClientCredentials(client_id = user_id, client_secret = secret)
        sp = spotipy.Spotify(auth = token, client_credentials_manager = client_credentials_manager)

        self.flagHelp = 3
        self.sum = 0
        self.place = 0
        self.count = 0
        self.songList = []

        canvas.create_image( 0, 0, image = backgroundImage, anchor = "nw")
        canvas.create_text(84, 444, font = ("Eurovision Song Contest 2015 V2", 48), text = "S\np\no\nt\ni\n\nA\np\np", fill = "black")
        canvas.create_text(80, 440, font = ("Eurovision Song Contest 2015 V2", 48), text = "S\np\no\nt\ni\n\nA\np\np", fill = "white")
        
        canvas.create_rectangle(180, 0, 530, 900, outline = "white", fill = "black")
        
        labelM = lb(window, font = ("Helvetica", 32), text ="\nTo start adding rates you need to load song 😄", anchor = "n", bg = "white", height = 15, width = 39, borderwidth = 2, relief = "solid")
        labelM.place(x = 580, y = 20)
        
        labelI = lb(window, font = ("Helvetica", 22), text ="If you rate all songs\nyou want, decide what\nto do now 😉", anchor = "center", bg = "white", height = 4, width = 18, borderwidth = 2, relief = "solid")
        
        entrySongTitle = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid") 
        canvas.create_window(762, 142, anchor = "nw", window = entrySongTitle)
        
        entrySongArtist = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid") 
        canvas.create_window(762, 192, anchor = "nw", window = entrySongArtist)
        
        entryRate = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid") 
        labelListTop = lb(window, font = ("Helvetica", 24), anchor = "n", height = 18, width = 25, bg = "white")
        entryName = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid") 
        
        buttonLoad = bt(window, text = "⛛", font = ("Arial", 32), height = 1, width = 3, bg = "#00FF00", command = lambda: SpotifyAppGUI.loadSong(self, canvas, entrySongTitle, entrySongArtist, entryRate, labelM, sp, buttonSubmit, buttonRating, buttonTop, buttonReset, labelI, entryName, buttonSubmit2, listbox, buttonSubmitTop, labelListTop))
        canvas.create_window(1260, 152, anchor = "nw", window = buttonLoad)
        
        buttonSubmit = bt(window, text = "✔️", font = ("Arial", 32), height = 1, width = 3, bg = "#00FF00")
        buttonSubmit2 = bt(window, text = "✔️", font = ("Arial", 32), height = 1, width = 3, bg = "#00FF00")
        
        buttonRating = bt(window, text = "Create rating\n😎", font = ("Helvetica", 24), height = 3, width = 16, bg = "#B0C4DE")
        buttonTop = bt(window, text = "Create top\n🥇 🥈 🥉", font = ("Helvetica", 24), height = 3, width = 16, bg = "#B0C4DE")
        buttonReset = bt(window, text = "Reset ❌", font = ("Helvetica", 24), height = 1, width = 16, bg = "#FF0000")

        buttonExit = bt(window, text = "❌", font = ("Arial", 32), height = 1, width = 3, bg = "#FF0000", command = lambda: [SpotifyAppGUI.close_SpotifyAppGUI(canvas, labelM, labelI, listbox, labelListTop), MenuGUI.MenuGUI.open_MenuGUI(window, canvas, backgroundImage, logoSpotify)])
        buttonHelp = bt(window, text = "🤔", font = ("Helvetica", 32), height = 1, width = 3, bg = "#B5BBFF", command = lambda: HelpGUI.HelpGUI.open_HelpGUI(self.flagHelp))
        buttonFile = bt(window, text = "📁", font = ("Helvetica", 32), height = 1, width = 3, bg = "#B5BBFF", command = SpotifyAppGUI.open_Explorer)

        listbox = li(window, font = ("Helvetica", 24), borderwidth = 2, relief = "solid", height = 19, width = 27, selectmode = "extended", justify = CENTER)
        buttonSubmitTop = bt(window, text = "Add to your top 😁", font = ("Helvetica", 24), anchor = "center", height = 1, width = 16, bg = "#00FF00")
       
        canvas.create_rectangle(30, 30, 115, 115, outline = "white", fill = "black")
        canvas.create_rectangle(30, 875, 115, 790, outline = "white", fill = "black")
        canvas.create_rectangle(1470, 850, 1548, 772, outline = "white", fill = "black")

        canvas.create_window(40, 20, anchor = "nw", window = buttonExit)
        canvas.create_window(40, 780, anchor = "nw", window = buttonHelp) 
        canvas.create_window(1500, 822, anchor = "center", window = buttonFile)
        
        window.mainloop()
        
    def loadSong(self, canvas, entry, entry2, entryRate, label, sp, buttonSubmit, buttonRating, buttonTop, buttonReset, label2, entryName, buttonSubmit2, listbox, buttonSubmitTop, labelLT):
        
        if self.count != 0:
            
            buttonReset.config(command = lambda: SpotifyAppGUI.resetSpotifyApp(self, entryRate, entryName, buttonSubmit, buttonSubmit2, label, entry, entry2,  buttonRating, buttonTop, buttonReset, label2, listbox, labelLT, buttonSubmitTop))
            buttonRating.config(command = lambda: SpotifyAppGUI.createRates(self, canvas, label, entryName, buttonSubmit2))
            buttonTop.config(command = lambda: SpotifyAppGUI.createTop(self, canvas, listbox, entryName, buttonSubmit2, buttonSubmitTop, labelLT))
            
            label2.place(x = 200, y = 20, anchor = "nw")
            canvas.create_window(200, 194, anchor = "nw", window = buttonRating)
            canvas.create_window(200, 368, anchor = "nw", window = buttonTop) 
            canvas.create_window(200, 803, anchor = "nw", window = buttonReset) 
        
        entry.delete(0, END)
        entry2.delete(0, END)
        entryRate.delete(0, END)
        
        track = sp.currently_playing()
        artists = []

        for artist in track['item']['artists']:
            artists.append(artist)

        artist_names = ', '.join([artist['name'] for artist in artists])
        title = track['item']['name']

        entry.insert(0, str(title))
        entry2.insert(0, str(artist_names))
        
        label.config(text ="\nTo start adding rates you need to load song 😄\n\n\n\nAdd rate 😄")
        
        buttonSubmit.config(command = lambda: SpotifyAppGUI.addRate(self, entry, entry2, entryRate, label))
        
        canvas.create_window(1260, 315, anchor = "nw", window = buttonSubmit)
        canvas.create_window(762, 332, anchor = "nw", window = entryRate)
            
    def addRate(self, entry, entry2, entryRate, label):
        
        gradeInt = int(entryRate.get())
        title = str(entry.get())
        artist = str(entry2.get())
        
        self.sum = self.sum + gradeInt
        self.count = self.count + 1
        
        song = [title, artist, gradeInt]
        
        self.songList.append(song)
        
        label.config(text ="\nTo start adding rates you need to load song 😄\n\n\n\nAdd rate 😄\n\n\nYou add rate to " + title + " 🎶\nPerformed by " + artist + " 🎤")
        
    def resetSpotifyApp(self, entryRate, entryName, button, button2, label, entry, entry2,  buttonRating, buttonTop, buttonReset, label2, listbox, labelLT, buttonST):
        
        self.flagHelp = 3
        self.sum = 0
        self.count = 0
        self.songList = []
        
        entryRate.destroy()
        entryName.destroy()
        button.destroy()
        button2.destroy()
        
        label.config(text ="\nTo start adding rates you need to load song 😄")
        
        entry.delete(0, END)
        entry2.delete(0, END)
        
        buttonRating.destroy()
        buttonTop.destroy()
        buttonReset.destroy()
        label2.destroy()
        
        listbox.destroy()
        labelLT.destroy()
        buttonST.destroy()
        
    def createRates(self, canvas, label, entry, buttonSubmit):
        
        label.config(text ="\nTo start adding rates you need to load song 😄\n\n\n\nAdd rate 😄\n\n\nName file in which you want to save your rates 😄")
        
        buttonSubmit.config(command = lambda: SpotifyAppGUI.saveRates(self, entry, label))

        canvas.create_window(1260, 475, anchor = "nw", window = buttonSubmit)
        canvas.create_window(762, 492, anchor = "nw", window = entry)
        
    def saveRates(self, entry, label):
        
        file_name = entry.get()
        
        path = "SpotifyAppFiles/" + file_name + ".txt"
        
        f = open(path, "a")
        f.write("There are my rates of some Spotify songs ^^\n\n")
        
        for song in self.songList:
            
            self.place = self.place + 1
            
            f.write(str(self.place) + ". " + song[0] + " - " + song[1] + " - " + str(song[2]) + "\n")
            
        average = self.sum / self.count
        average = round(average, 2)
            
        f.write("\nMy average rate: " + str(average) + "\n")
        f.close()
        
        label.config(text ="\nTo start adding rates you need to load song 😄\n\n\n\nAdd rate 😄\n\n\nName file in which you want to save your rates 😄\n\n\n\nYou can find your file with rates\nin SpotifyAppGUI folder 🥳")

    def createTop(self, canvas, listbox, entryName, buttonSubmit2, buttonTop, labelLT):
        
        SpotifyAppGUI.sortTop(self)
        SpotifyAppGUI.createListTop(self, listbox)
        SpotifyAppGUI.creatingTop(self, canvas, listbox, labelLT, entryName, buttonSubmit2, buttonTop)
    
    def sortTop(self):
        
        self.songList = sorted(self.songList, key = lambda k: k[2], reverse = True)
    
    def createListTop(self, listbox):
        
        songs_List = []
            
        for song in self.songList:
            songs_List.append(song[0] + " - " + str(song[2]))
            
        country_ListVar = sv(value = songs_List)
            
        listbox.config(listvariable = country_ListVar)
        listbox.place(x = 1550, y = 36, anchor = "ne")
        
    def creatingTop(self, canvas, listbox, label, entry, buttonName, buttonTop):
            
        label.config(text = "\nNow, based on the entered\n ratings,sort your top\n by selecting next countries\n from the list on the right ➡️\nBut, first name your top\n(file in which it will be saved) 😉")
        label.place(x = 586, y = 36)
            
        entry.config(font = ("Helvetica", 24))
        buttonName.config(font = ("Arial", 24))
        buttonName.config(text = "     ✔️")
            
        canvas.create_window(600, 322, anchor = "nw", window = entry)
        canvas.create_window(980, 307, anchor = "nw", window = buttonName)
            
        buttonName.config(command = lambda: SpotifyAppGUI.start_TopFile(self, canvas, entry, label, buttonTop, listbox))
    
    def start_TopFile(self, canvas, entry, label, buttonTop, listbox):

        file_name = entry.get()
        path = "SpotifyAppFiles/" + file_name + ".txt"
        
        f = open(path, "a")
        
        f.write("There are my top of songs ^^\n\nPLACE \ SONG \ ARTIST \ RATE\n\n")
        
        label.config(text = "\nNow, based on the entered\n ratings,sort your top\n by selecting next countries\n from the list on the right ➡️\nBut, first name your top\n(file in which it will be saved) 😉\n\n\n\nStart adding songs to your top <3\nTo start click button below 😁")
        canvas.create_window(830, 517, anchor = "center", window = buttonTop)
        
        buttonTop.config(command = lambda: SpotifyAppGUI.add_toTop(self, listbox, label, f))
        
    def add_toTop(self, listbox, label, file):
        
        if listbox.size() == 0:
            
            average = self.sum / self.count
            average = round(average, 2)
            
            file.write("\nMy average rate: " + str(average) + "\n")
            file.close()
            
            label.config(text = "\nNow, based on the entered\n ratings,sort your top\n by selecting next countries\n from the list on the right ➡️\nBut, first name your top\n(file in which it will be saved) 😉\n\n\n\nStart adding songs to your top <3\nTo start click button below 😁\n\n\n\nWhole top created 🥳\nYou can find your top in\nSpotifyAppGUI folder 😁")  
        
        else:
            self.place = self.place + 1
            song = listbox.get(ANCHOR)
            
            info = song.split(" - ")
            
            for song in self.songList:
                if song[0] == info[0]:
                    info2 = song
            
            file.write(str(self.place) + ". " + info2[0] + " - " + info2[1] + " - " +  info[1] + "\n")
            
            listbox.delete(ANCHOR)
    
    def open_Explorer():
        subprocess.Popen('explorer "SpotifyAppFiles"')
        
    def open_SpotifyAppGUI(window, canvas, backgroundImage, logoSpotify):

        SpotifyAppGUI(window, canvas, backgroundImage, logoSpotify)

    def close_SpotifyAppGUI(canvas, label, label2, listbox, label3):

        canvas.delete("all")
        label.destroy()
        label2.destroy()
        listbox.destroy()
        label3.destroy()
        
