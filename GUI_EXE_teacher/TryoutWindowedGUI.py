from tkinter import *
from tkinter import ttk

def write_csv_file(data, filename):
    afile = open(filename,"a")
    afile.write(str(data)+"\n")
    afile.close

# Definitie van wat een MyWindow is
class MyWindow:
    def __init__(self, win):
        #INVOERVELD GETAL 1
        #label maken
        self.lbl1=Label(win, text='First number')
        #label op window plaatsen
        self.lbl1.place(x=100, y=50)
        #label invoerveld maken
        self.t1=Entry(bd=3)
        #invoerveld op window plaatsen
        self.t1.place(x=200, y=50)

        #INVOERVELD GETAL 2
        self.lbl2=Label(win, text='Second number')
        self.lbl2.place(x=100, y=100)
        self.t2=Entry()
        self.t2.place(x=200, y=100)

        #BUTTON ADD
        self.b1=Button(win, text='Add', command=self.add) # command=self.add definieert wat moet gebeuren bij klikken op button
        self.b1.place(x=100, y=150)

        #BUTTON SUBTRACT
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub) # bind definieert wat moet gebeuren bij klikken op button
        self.b2.place(x=200, y=150)

        #RESULTAAT VELD
        self.lbl3=Label(win, text='Result')
        self.lbl3.place(x=100, y=200)
        self.t3=Entry()
        self.t3.place(x=200, y=200)

        #BUTTON SAVE RESULTS
        self.b3=Button(win, text='Save', command=self.save)
        self.b3.place(x=200, y=250)

        #UITVOER VELD
        self.lbl4=Label(win, text='Output')
        self.lbl4.place(x=100, y=300)
        self.t4=Entry()
        self.t4.place(x=200, y=300)

    def add(self):
        # resultaat veld leegmaken
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        # resultaat veld vullen met resultaat van berekening
        self.t3.insert(END, str(result))
        
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

    def save(self):
        # een lijst variabele vullen met waarden van de twee invoervelden en het resultaat veld
        uitvoer_lst=[]
        uitvoer_lst.append(int(self.t1.get()))
        uitvoer_lst.append(int(self.t2.get()))
        uitvoer_lst.append(int(self.t3.get()))

        # een string variabele vullen met waarden van de twee invoervelden en het resultaat veld
        uitvoer_str=self.t1.get()
        uitvoer_str=uitvoer_str+';'+self.t2.get()
        uitvoer_str=uitvoer_str+';'+self.t3.get()

        # invoervelden leeg maken
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

        # de gebruiker tonen wat wordt weggeschreven (in list vorm)
        self.t4.insert(END, str(uitvoer_lst))

        # aanroepen van functie die een regel toevoegt aan een file
        write_csv_file(uitvoer_str, 'rwa_filetest.csv')

# code waarmee een tkinter GUI gedefinieerd wordt
window=Tk()
# code de hierboven gedefinieerde MyWindow als tkinter window wordt gedefinieerd
mywin=MyWindow(window)
# titel van window wijzigen/zetten
window.title('GUI test in Python met tkinter')
# grootte van window wijzigen/zetten
window.geometry("400x400+10+10")
# window/programma starten/draaien
window.mainloop()