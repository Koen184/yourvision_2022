from tkinter import Button as bt, Label as lb, Entry as en, Listbox as li, StringVar as sv
from tkinter import CENTER, ANCHOR
import subprocess
import Data
import MenuGUI
import HelpGUI

class TopMakerGUI:
   
    def __init__(self, window, canvas, backgroundImage, logoSpotify):

        canvas.create_image( 0, 0, image = backgroundImage, anchor = "nw")
        canvas.create_text(84, 454, font = ("Eurovision Song Contest 2015 V2", 48), text = "T\no\np\n\nM\na\nk\ne\nr", fill = "black")
        canvas.create_text(80, 450, font = ("Eurovision Song Contest 2015 V2", 48), text = "T\no\np\n\nM\na\nk\ne\nr", fill = "white")
        
        canvas.create_rectangle(180, 0, 530, 900, outline = "white", fill = "black")
        
        canvas.create_rectangle(30, 30, 115, 115, outline = "white", fill = "black")
        canvas.create_rectangle(30, 875, 115, 790, outline = "white", fill = "black")
        canvas.create_rectangle(1470, 850, 1548, 772, outline = "white", fill = "black")

        self.flagHelp = 2
        
        buttonExit = bt(window, text = "❌", font = ("Arial", 32), height = 1, width = 3, bg = "#FF0000", command = lambda: [TopMakerGUI.close_TopMakerGUI(canvas, buttonExit, buttonHelp, buttonFile, label1), MenuGUI.MenuGUI.open_MenuGUI(window, canvas, backgroundImage, logoSpotify)])
        buttonHelp = bt(window, text = "🤔", font = ("Helvetica", 32), height = 1, width = 3, bg = "#B5BBFF", command = lambda: HelpGUI.HelpGUI.open_HelpGUI(self.flagHelp))
        buttonFile = bt(window, text = "📁", font = ("Helvetica", 32), height = 1, width = 3, bg = "#B5BBFF", command = TopMakerGUI.open_Explorer)

        canvas.create_window(40, 20, anchor = "nw", window = buttonExit)
        canvas.create_window(40, 780, anchor = "nw", window = buttonHelp) 
        canvas.create_window(1500, 822, anchor = "center", window = buttonFile)

        label1 = lb(window, font = ("Helvetica", 64), text = "Which type of top you\nwant to do today 🧐", bg = "white", height = 2, width = 18, borderwidth = 2, relief = "solid")
        label1.place(x = 580, y = 20)
        
        self.flag = 0
        self.number = 0
        self.number2 = 0
        self.count = 0
        self.sum = 0
        self.place = 0

        TopMakerGUI.choose_Main(self, window, canvas)
        
        window.mainloop()
        
    def change_flag(self, value):
        self.flag = value
        
    def choose_Main(self, window, canvas):
              
        if self.flag == 0:
            TopMakerGUI.choose_topType(self, window, canvas)
            
        if self.flag == 1:
            TopMakerGUI.full_Top(self, window, canvas)
            
        if self.flag == 2:
            TopMakerGUI.add_Rates(self, window, canvas)
        
    def choose_topType(self, window, canvas):
        
        shade1 = canvas.create_rectangle(680, 320, 970, 820, outline = "white", fill = "black")
        shade2 = canvas.create_rectangle(1080, 320, 1370, 820, outline = "white", fill = "black")

        buttonTop = bt(window, text = "Full Top\n🥇 🥈 🥉", font = ("Helvetica", 32), height = 10, width = 12, bg = "#ECB5FF", command = lambda: [TopMakerGUI.change_flag(self, 1), TopMakerGUI.choose_Main(self, window, canvas), 
                                                                                                                                                    TopMakerGUI.destroy_topType(buttonTop, buttonRates, canvas, shade1, shade2)])
        buttonRates = bt(window, text = "Just add rates\n 😎", font = ("Helvetica", 32), height = 10, width = 12, bg = "#D4B5FF", command = lambda: [TopMakerGUI.change_flag(self, 2), TopMakerGUI.choose_Main(self, window, canvas), 
                                                                                                                                                        TopMakerGUI.destroy_topType(buttonTop, buttonRates, canvas, shade1, shade2)]) 

        canvas.create_window(800, 600, anchor = "center", window = buttonTop) 
        canvas.create_window(1200, 600, anchor = "center", window = buttonRates)
        
    def destroy_topType(button1, button2, canvas, object1, object2):
        
        button1.destroy()
        button2.destroy()
        canvas.delete(object1)
        canvas.delete(object2)
        
    def full_Top(self, window, canvas):
        
        buttonReset = bt(window, text = "Reset ❌", font = ("Helvetica", 24), height = 1, width = 16, bg = "#FF0000", command = lambda: [TopMakerGUI.change_flag(self, 0), TopMakerGUI.choose_Main(self, window, canvas), TopMakerGUI.numbers_Reset(self), 
                                                                                                                                            TopMakerGUI.destroy_Top(buttonReset, buttonExit, buttonSF1, buttonSF2, buttonBig5, buttonFinal, buttonFull, buttonSubmit, 
                                                                                                                                                                    buttonSubmitTop, buttonSubmitName, labelQ, labelI, labelM, labelListTop, entryRate, entryName, listbox)])
        canvas.create_window(200, 803, anchor = "nw", window = buttonReset) 
        
        buttonExit = bt(window, text = "❌", font = ("Arial", 32), height = 1, width = 3, bg = "#FF0000", command = lambda: [TopMakerGUI.change_flag(self, 0), TopMakerGUI.choose_Main(self, window, canvas), TopMakerGUI.numbers_Reset(self), 
                                                                                                                                TopMakerGUI.destroy_Top(buttonReset, buttonExit, buttonSF1, buttonSF2, buttonBig5, buttonFinal, buttonFull, buttonSubmit, 
                                                                                                                                                        buttonSubmitTop, buttonSubmitName, labelQ, labelI, labelM, labelListTop, entryRate, entryName, listbox)])
        canvas.create_window(40, 20, anchor = "nw", window = buttonExit)
            
        labelQ = lb(window, font = ("Helvetica", 32), text = "In which group\nof songs want\nyou make top\n🧐", bg = "white", height = 4, width = 13, borderwidth = 2, relief = "solid")
        labelQ.place(x = 190, y = 20)
            
        buttonSF1 = bt(window, text = "Semi Final I", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 5), TopMakerGUI.show_InfoTop(self, labelI), 
                                                                                                                                           TopMakerGUI.chooseSongs4Top(self, canvas, labelM, entryRate, entryName, buttonSubmitName, buttonSubmitTop, buttonSubmit, listbox, labelListTop)])
        canvas.create_window(200, 281, anchor = "nw", window = buttonSF1) 
           
        buttonSF2 = bt(window, text = "Semi Final II", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 6), TopMakerGUI.show_InfoTop(self, labelI), 
                                                                                                                                            TopMakerGUI.chooseSongs4Top(self, canvas, labelM, entryRate, entryName, buttonSubmitName, buttonSubmitTop, buttonSubmit, listbox, labelListTop)])
        canvas.create_window(200, 368, anchor = "nw", window = buttonSF2) 
            
        buttonBig5 = bt(window, text = "Big 5 Countries", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 7), TopMakerGUI.show_InfoTop(self, labelI), 
                                                                                                                                               TopMakerGUI.chooseSongs4Top(self, canvas, labelM, entryRate, entryName, buttonSubmitName, buttonSubmitTop, buttonSubmit, listbox, labelListTop)])
        canvas.create_window(200, 455, anchor = "nw", window = buttonBig5) 
            
        buttonFinal = bt(window, text = "Final", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 8), TopMakerGUI.show_InfoTop(self, labelI), 
                                                                                                                                      TopMakerGUI.chooseSongs4Top(self, canvas, labelM, entryRate, entryName, buttonSubmitName, buttonSubmitTop, buttonSubmit, listbox, labelListTop)])
        canvas.create_window(200, 542, anchor = "nw", window = buttonFinal) 
            
        buttonFull = bt(window, text = "All Songs", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 9), TopMakerGUI.show_InfoTop(self, labelI), 
                                                                                                                                         TopMakerGUI.chooseSongs4Top(self, canvas, labelM, entryRate, entryName, buttonSubmitName, buttonSubmitTop, buttonSubmit, listbox, labelListTop)])
        canvas.create_window(200, 629, anchor = "nw", window = buttonFull) 
        
        labelM = lb(window, font = ("Helvetica", 32), anchor = "n", bg = "white", height = 15, width = 39, borderwidth = 2, relief = "solid")
        labelI = lb(window, font = ("Helvetica", 32), height = 2, width = 37, bg = "white")
        
        entryRate = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid") 
        
        labelListTop = lb(window, font = ("Helvetica", 24), anchor = "n", height = 18, width = 25, bg = "white")
        
        buttonSubmit = bt(window, text = "✔️", font = ("Arial", 32), height = 1, width = 3, bg = "#00FF00")
        
        listbox = li(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid", height = 14, selectmode = "extended", justify = CENTER)
        
        entryName = en(window, font = ("Helvetica", 24), borderwidth = 2, relief = "solid")
        buttonSubmitName = bt(window, text = "     ✔️", font = ("Arial", 24), anchor = "center", height = 1, width = 3, bg = "#00FF00")
        buttonSubmitTop = bt(window, text = "Add to your top 😁", font = ("Helvetica", 24), anchor = "center", height = 1, width = 16, bg = "#00FF00")
        
    def destroy_Top(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, label1, label2, label3, label4, entry1, entry2, listbox):
        
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        button9.destroy()
        button10.destroy()
        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        entry1.destroy()
        entry2.destroy()
        listbox.destroy()
        
    def show_InfoTop(self, label1):
        
        if self.flag == 5:
            group = "Semi Final I"
        elif self.flag == 6:
            group = "Semi Final II"
        elif self.flag == 7:
            group = "big 5 countries"
        elif self.flag == 8:
            group = "Final"
        elif self.flag == 9:
            group = "all"

        label1.config(text = ("\nYou are making top of " + group + " songs"))
        label1.place(x = 602, y = 22)
        
    def chooseSongs4Top(self, canvas, label, entry, entry2, buttonName, buttonTop, button, listbox, labelListTop):
        
        if self.flag == 5:
            songs_List = Data.SemiFinal1
            self.count = 18
        elif self.flag == 6:
            songs_List = Data.SemiFinal2
            self.count = 19
        elif self.flag == 7:
            songs_List = Data.Big5
            self.count = 6
        elif self.flag == 8:
            songs_List = Data.Final
            self.count = 26
        elif self.flag == 9:
            songs_List = Data.Full
            self.count = 41
        
        label.config(text = ("\n\n\nFirst you need to add rates to songs 😁\nTo start adding rates click on\ngreen button once without rate 😅"))
        label.place(x = 580, y = 20)
            
        canvas.create_window(762, 342, anchor = "nw", window = entry)
        canvas.create_window(1260, 327, anchor = "nw", window = button)
        
        button.config(command = lambda: TopMakerGUI.add_RateTop(self,canvas, songs_List, entry, entry2, buttonName, buttonTop, label, listbox, labelListTop))
        
    def add_RateTop(self, canvas, songs_List, entry, entry2, buttonName, buttonTop, label, listbox, labelListTop):
        
        if self.number2 < self.count:
            
            song_Text = songs_List[self.number2]
            
            label.config(text = "\n\n\nFirst you need to add rates to songs 😁\nAdd rate for:\n" + song_Text[0])
            
            grade = int(entry.get())
            
            if (self.number2 - 1) < 0:
                pass

            else:
                song_Text = songs_List[self.number2 - 1]
                song_Text[3] = grade
                self.sum = self.sum + grade        

            self.number = self.number + 1
            self.number2 = self.number2 + 1    
        
        else:
            average = self.sum / (self.number - 1)
            average = round(average, 2)
    
            songs_List = TopMakerGUI.sortTop(songs_List)
            TopMakerGUI.createListTop(listbox, songs_List)
            TopMakerGUI.creatingTop(self, canvas, listbox, labelListTop, entry2, buttonName, buttonTop, average)
            
    def sortTop(songs_List):
        
        songs_List.pop(-1)
        songs_List = sorted(songs_List, key = lambda k: k[3], reverse = True)
        return songs_List
    
    def createListTop(listbox, songs_List):
        
        country_List = []
            
        for song in songs_List:
            country_List.append(song[0] + " - " + str(song[3]))
            
        country_ListVar = sv(value = country_List)
            
        listbox.config(listvariable = country_ListVar)
        listbox.place(x = 1550, y = 36, anchor = "ne")
            
    def creatingTop(self, canvas, listbox, label, entry, buttonName, buttonTop, average):
            
        label.config(text = "\nNow, based on the entered\n ratings,sort your top\n by selecting next countries\n from the list on the right ➡️\nBut, first name your top\n(file in which it will be saved) 😉")
        label.place(x = 586, y = 36)
            
        canvas.create_window(600, 322, anchor = "nw", window = entry)
        canvas.create_window(980, 307, anchor = "nw", window = buttonName)
            
        buttonName.config(command = lambda: TopMakerGUI.start_TopFile(self, canvas, entry, label, buttonTop, listbox, average))
        
    def start_TopFile(self, canvas, entry, label, buttonTop, listbox, average):

        file_name = entry.get()
        path = "TopMakerFiles/" + file_name + ".txt"
        
        f = open(path, "a")
        
        if self.flag == 5:
            group = "Semi Final I"
        elif self.flag == 6:
            group = "Semi Final II"
        elif self.flag == 7:
            group = "big 5 countries"
        elif self.flag == 8:
            group = "Final"
        elif self.flag == 9:
            group = "all"
        
        f.write("There are my top of " + group + " songs ^^\n\nPLACE \ ARTIST \ SONG \ COUNTRY \ RATE\n\n")
        
        label.config(text = "\nNow, based on the entered\n ratings,sort your top\n by selecting next countries\n from the list on the right ➡️\nBut, first name your top\n(file in which it will be saved) 😉\n\n\n\nStart adding songs to your top <3\nTo start click button below 😁")
        canvas.create_window(830, 517, anchor = "center", window = buttonTop)
        
        buttonTop.config(command = lambda: TopMakerGUI.add_toTop(self, listbox, label, f, average))
        
    def add_toTop(self, listbox, label, file, average):
        
        if listbox.size() == 0:
            file.write("\nMy average rate: " + str(average) + "\n")
            file.close()
            label.config(text = "\nNow, based on the entered\n ratings,sort your top\n by selecting next countries\n from the list on the right ➡️\nBut, first name your top\n(file in which it will be saved) 😉\n\n\n\nStart adding songs to your top <3\nTo start click button below 😁\n\n\n\nWhole top created 🥳\nYou can find your top in\nTopMakersFile folder 😁")  
        
        else:
            self.place = self.place + 1
            country = listbox.get(ANCHOR)
            
            info = country.split(" - ")
            
            for song in Data.Full:
                if song[0] == info[0]:
                    info2 = song
            
            file.write(str(self.place) + ". " + info2[2] + " - " + info2[1] + " - " +  info2[0] + " - " +  info[1] + "\n")
            
            listbox.delete(ANCHOR)
        
    def add_Rates(self, window, canvas):

        buttonReset = bt(window, text = "Reset ❌", font = ("Helvetica", 24), height = 1, width = 16, bg = "#FF0000", command = lambda: [TopMakerGUI.change_flag(self, 0), TopMakerGUI.choose_Main(self, window, canvas), TopMakerGUI.numbers_Reset(self),
                                                                                                                                            TopMakerGUI.destroy_Rates(buttonReset, buttonExit, buttonSF1, buttonSF2, buttonBig5, buttonFinal, buttonFull, buttonSubmit, labelQ, labelM, labelI, entryName, entryRate)])
        canvas.create_window(200, 803, anchor = "nw", window = buttonReset) 
        
        buttonExit = bt(window, text = "❌", font = ("Arial", 32), height = 1, width = 3, bg = "#FF0000", command = lambda: [TopMakerGUI.change_flag(self, 0), TopMakerGUI.choose_Main(self, window, canvas), TopMakerGUI.numbers_Reset(self),
                                                                                                                                            TopMakerGUI.destroy_Rates(buttonReset, buttonExit, buttonSF1, buttonSF2, buttonBig5, buttonFinal, buttonFull, buttonSubmit, labelQ, labelM, labelI, entryName, entryRate)])
        canvas.create_window(40, 20, anchor = "nw", window = buttonExit)
            
        labelQ = lb(window, font = ("Helvetica", 32), text = "In which group\nof songs want\nyou add rates\n🧐", bg = "white", height = 4, width = 13, borderwidth = 2, relief = "solid")
        labelQ.place(x = 190, y = 20)
            
        buttonSF1 = bt(window, text = "Semi Final I", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 5), TopMakerGUI.show_InfoRates(self, labelI), TopMakerGUI.insert_Name(self, canvas, entryName, buttonSubmit, labelM, labelI)])
        canvas.create_window(200, 281, anchor = "nw", window = buttonSF1) 
           
        buttonSF2 = bt(window, text = "Semi Final II", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 6), TopMakerGUI.show_InfoRates(self, labelI), TopMakerGUI.insert_Name(self, canvas, entryName, buttonSubmit, labelM, labelI)])
        canvas.create_window(200, 368, anchor = "nw", window = buttonSF2) 
            
        buttonBig5 = bt(window, text = "Big 5 Countries", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 7), TopMakerGUI.show_InfoRates(self, labelI), TopMakerGUI.insert_Name(self, canvas, entryName, buttonSubmit, labelM, labelI)])
        canvas.create_window(200, 455, anchor = "nw", window = buttonBig5) 
            
        buttonFinal = bt(window, text = "Final", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 8), TopMakerGUI.show_InfoRates(self, labelI), TopMakerGUI.insert_Name(self, canvas, entryName, buttonSubmit, labelM, labelI)])
        canvas.create_window(200, 542, anchor = "nw", window = buttonFinal) 
            
        buttonFull = bt(window, text = "All Songs", font = ("Helvetica", 24), height = 1, width = 16, bg = "#B0C4DE", command = lambda: [TopMakerGUI.change_flag(self, 9), TopMakerGUI.show_InfoRates(self, labelI), TopMakerGUI.insert_Name(self, canvas, entryName, buttonSubmit, labelM, labelI)])
        canvas.create_window(200, 629, anchor = "nw", window = buttonFull) 
        
        labelM = lb(window, font = ("Helvetica", 32), text = ("\n\n\nName your top (file in which it will be saved) 😉"), anchor = "n", bg = "white", height = 15, width = 39, borderwidth = 2, relief = "solid")
        
        labelI = lb(window, font = ("Helvetica", 32), height = 2, width = 37, bg = "white")
        
        entryName = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid")

        buttonSubmit = bt(window, text = "✔️", font = ("Arial", 32), height = 1, width = 3, bg = "#00FF00", command = lambda: [TopMakerGUI.create_File(self, window, canvas, labelM, entryName, entryRate)])
        
        entryRate = en(window, font = ("Helvetica", 32), borderwidth = 2, relief = "solid")     
        
    def destroy_Rates(button1, button2, button3, button4, button5, button6, button7, button8, label1, label2, label3, entry1, entry2):
        
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        button7.destroy()
        button8.destroy()
        label1.destroy()
        label2.destroy()
        label3.destroy()
        entry1.destroy()
        entry2.destroy()
        
    def show_InfoRates(self, label):
        
        if self.flag == 5:
            group = "Semi Final I"
        elif self.flag == 6:
            group = "Semi Final II"
        elif self.flag == 7:
            group = "big 5 countries"
        elif self.flag == 8:
            group = "Final"
        elif self.flag == 9:
            group = "all"

        label.config(text = ("\nYou are adding rates to " + group + " songs"))

    def create_File(self, window, canvas, label, entry, entry2):
        
        file_name = entry.get()
        path = "TopMakerFiles/" + file_name + ".txt"
        
        f = open(path, "a")
        
        if self.flag == 5:
            songs_List = Data.SemiFinal1
            self.count = 18
            group = "Semi Final I"
        elif self.flag == 6:
            songs_List = Data.SemiFinal2
            self.count = 19
            group = "Semi Final II"
        elif self.flag == 7:
            songs_List = Data.Big5
            self.count = 6
            group = "big 5 countries"
        elif self.flag == 8:
            songs_List = Data.Final
            self.count = 26
            group = "Final"
        elif self.flag == 9:
            songs_List = Data.Full
            self.count = 41
            group = "all"
        
        f.write("There are my rates of " + group + " songs ^^\n\n")
        
        label.config(text = "\n\n\nName your top (file in which it will be saved) 😉\n\n\nFile with top created, start adding your rates 😁\n\nTo start adding rates click on\ngreen button once without rate 😅")

        canvas.create_window(762, 542, anchor = "nw", window = entry2)
        
        buttonSubmit = bt(window, text = "✔️", font = ("Arial", 32), height = 1, width = 3, bg = "#00FF00", command = lambda: TopMakerGUI.add_Rate(self, f, songs_List, entry2, label))
        canvas.create_window(1260, 527, anchor = "nw", window = buttonSubmit) 

    def add_Rate(self, file, songs_List, entry, label):
        
        if self.number2 < self.count:
            
            number_str = str(self.number)
            
            song_Text = songs_List[self.number2]
            
            label.config(text = "\n\n\nName your top (file in which it will be saved) 😉\n\n\nFile with top created, start adding your rates 😁\n\nAdd rate for:\n" + song_Text[0])
            
            grade = str(entry.get())
            gradeInt = int(entry.get())

            song_Input = songs_List[self.number2 - 1]
            
            if (self.number2 - 1) < 0:
                pass

            else:
                file.write(number_str + ". " + song_Input[0] + " - " + song_Input[1] + " - " + grade + "\n")
                self.sum = self.sum + gradeInt        

            self.number = self.number + 1
            self.number2 = self.number2 + 1    
        
        else:
            average = self.sum / (self.number - 1)
            average = round(average, 2)
            
            file.write("\nMy average rate: " + str(average) + "\n")
            file.close()
            label.config(text = "\n\n\nName your top (file in which it will be saved) 😉\n\n\nFile with top created, start adding your rates 😁\n\nAdd rate for:\nAll rates added 🥳\n\n\nYou can find your file with rates\nin TopMakersFile folder")
    
    def insert_Name(self, canvas, entry, button, label1, label2):

        canvas.create_window(762, 242, anchor = "nw", window = entry)
        canvas.create_window(1260, 227, anchor = "nw", window = button) 

        label1.place(x = 580, y = 20)
        label2.place(x = 602, y = 22)

    def numbers_Reset(self):
        
        self.number = 0
        self.number2 = 0
        self.count = 0
        self.sum = 0

    def open_Explorer():
        subprocess.Popen('explorer "TopMakerFiles"')
        
    def open_TopMakerGUI(window, canvas, backgroundImage, logoSpotify):

        TopMakerGUI(window, canvas, backgroundImage, logoSpotify)
        
    def close_TopMakerGUI(canvas, button, button2, button3, label):

        canvas.delete("All")
        button.destroy()
        button2.destroy()
        button3.destroy()
        label.destroy()