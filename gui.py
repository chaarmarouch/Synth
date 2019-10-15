import Tkinter
from Tkinter import *

root = Tk()
n = Frame(root)  #notes section 
o = Frame(root)  #options section
n.pack(side = LEFT)
o.pack(side = RIGHT)

#notes section 
n1 = Frame(n)
n10 = Button(n1, text="C", width = 2, height = 2)
n10.pack(side = LEFT)
n11 = Button(n1, text="C#", width = 2, height = 2)
n11.pack(side = LEFT)
n12 = Button(n1, text="D", width = 2, height = 2)
n12.pack(side = LEFT)
n13 = Button(n1, text="D#", width = 2, height = 2)
n13.pack(side = LEFT)
n1.grid(row = 0)
n2 = Frame(n)
n20 = Button(n2, text="E", width = 2, height = 2)
n20.pack(side = LEFT)
n21 = Button(n2, text="F", width = 2, height = 2)
n21.pack(side = LEFT)
n22 = Button(n2, text="F#", width = 2, height = 2)
n22.pack(side = LEFT)
n23 = Button(n2, text="G", width = 2, height = 2)
n23.pack(side = LEFT)
n2.grid(row = 1)
n3 = Frame(n)
n30 = Button(n3, text="G#", width = 2, height = 2)
n30.pack(side = LEFT)
n31 = Button(n3, text="A", width = 2, height = 2)
n31.pack(side = LEFT)
n32 = Button(n3, text="A#", width = 2, height = 2)
n32.pack(side = LEFT)
n33 = Button(n3, text="B", width = 2, height = 2)
n33.pack(side = LEFT)
n3.grid(row = 2)
n4 = Frame(n)
n40 = Button(n1, text="C", width = 2, height = 2)
n40.pack(side = LEFT)
n41 = Button(n1, text="C#", width = 2, height = 2)
n41.pack(side = LEFT)
n42 = Button(n1, text="D", width = 2, height = 2)
n42.pack(side = LEFT)
n43 = Button(n1, text="D#", width = 2, height = 2)
n43.pack(side = LEFT)
n4.grid(row = 3)
n5 = Frame(n)
n50 = Button(n2, text="E", width = 2, height = 2)
n50.pack(side = LEFT)
n51 = Button(n2, text="F", width = 2, height = 2)
n51.pack(side = LEFT)
n52 = Button(n2, text="F#", width = 2, height = 2)
n52.pack(side = LEFT)
n53 = Button(n2, text="G", width = 2, height = 2)
n53.pack(side = LEFT)
n5.grid(row = 4)
n6 = Frame(n)
n60 = Button(n3, text="G#", width = 2, height = 2)
n60.pack(side = LEFT)
n61 = Button(n3, text="A", width = 2, height = 2)
n61.pack(side = LEFT)
n62 = Button(n3, text="A#", width = 2, height = 2)
n62.pack(side = LEFT)
n63 = Button(n3, text="B", width = 2, height = 2)
n63.pack(side = LEFT)
n6.grid(row = 5)

#options section
o1 = Frame(o)
o1_label = Label(o1, text="Octave")
o1_label.pack(side = TOP)
octave_select = Listbox(o1, selectmode = SINGLE, height = 5, width = 3)
octave_select.insert(0, "0-1")
octave_select.insert(1, "2-3")
octave_select.insert(2, "4-5")
octave_select.insert(3, "6-7")
octave_select.insert(4, "8-9")
octave_select.pack()
try:
    j = octave_select.curselection()[0]
except:
    oct = 2
else:
    oct = j
o1.pack()

#common sampling rates 44.1kHz is most common
#0-12
sample_rates = (8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000)
o2 = Frame(o)
o2_label = Label(o2, text="Sample Rate")
o2_label.pack(side = TOP)
sample_select = Listbox(o2, selectmode = SINGLE, height = 13, width = 6)
sample_select.insert(0, "8000")
sample_select.insert(1, "11025")
sample_select.insert(2, "16000")
sample_select.insert(3, "22050")
sample_select.insert(4, "32000")
sample_select.insert(5, "44100")
sample_select.insert(6, "48000")
sample_select.insert(7, "88200")
sample_select.insert(8, "96000")
sample_select.insert(9, "176400")
sample_select.insert(10, "192000")
sample_select.insert(11, "352800")
sample_select.insert(12, "384000")
sample_select.pack()
o2.pack(side = RIGHT)
try:
    i = sample_select.curselection()[0]
except:
    sr = sample_rates[5]
else:
    sr = sample_rates[i]
    
o3 = Frame(o)
o3_label = Label(o3, text="Pitch Adjust")
o3_label.pack(side = TOP)
scale_val = DoubleVar()
pitch_slide = Scale(o3, from_ = -20, to = 20, variable = scale_val)
pitch_slide.pack()
o3.pack(side = LEFT)

root.mainloop()