import Tkinter
from Tkinter import *
import Nsound as ns

#sound generation section
#(octave 0-4, note 0-23)
#frequencies provided by  https://www.liutaiomottola.com/formulae/freqtab.htm
note_frequencies = ((16.531, 17.324, 18.354, 19.445, 20,601, 21.827, 23.124, 24.499, 25.956, 27.5, 29.135, 30.868, 32.703, 34.648, 36.708, 38.891, 41.203, 43.654, 46.249, 48.999, 51.913, 55.0, 58.27, 58.27, 61.735),
                    (65.406, 69.296, 73.416, 77.782, 82.407, 87.307, 92.499, 97.999, 103.826, 110.0, 116.541, 123.471, 130.813, 138.591, 146.832, 155.563, 164.814, 174.614, 184.997, 195.998, 207.652, 220.0, 233.082, 246.942),
                    (261.626, 277.183, 293.665, 311.127, 329.628, 349.228, 369.994, 391.995, 415.305, 440.0, 466.164, 493.83, 523.251, 554.365, 587.33, 622.254, 659.255, 698.456, 739.989, 783.991, 830.609, 880.0, 932.328, 987.767),
                    (1046.502, 1108.731, 1174.659, 1244.508, 1318.51, 1396.913, 1479.978, 1567.982, 1661.219, 1760.0, 1864.655, 1975.533, 2093.005, 2217.461, 2349.016, 2637.021, 2793.826, 2959.955, 3135.964, 3322.438, 3520.0, 3729.31, 3951.066),
                    (4186.009, 4434.922, 4698.636, 4978.032, 5274.042, 5587.652, 5919.91, 6271.928, 6644.876, 7040.0, 7458.62, 7902.132, 8372.018, 8869.844, 9397.272, 9956.064, 10548.084, 11175.304, 11839.82, 12543.856, 13289.752, 14080.0, 14917.24, 15804.264))

def freq_sel(octave, note):
    try:
        frequency = note_frequencies[octave][note]
    except IndexError:
        return 0
    else:
        return frequency

ns.use("portaudio")
def play_sound():
    buff = ns.Buffer()
    i = 0
    for x in inc_freq:
        if (x):
            buff = buff + ns.Sine(sr).generate(1, (freq[i] + (scale_val/100.0)*freq[i]))
        i += 1
    
    while (True in inc_freq):
        buff >> ns.AudioPlayback(sr, 2, 32)
        
#callbacks
inc_freq = [False] * 24
freq = [0.0] * 24

def n10_freq():
    freq[0] = freq_sel(oct, 0)
    inc_freq[0] = not inc_freq[0]
    play_sound()
    return

def n11_freq():
    freq[1] = freq_sel(oct, 1)
    inc_freq[1] = not inc_freq[1]
    play_sound()
    return

def n12_freq():
    freq[2] = freq_sel(oct, 2)
    inc_freq[2] = not inc_freq[2]
    play_sound()
    return

def n13_freq():
    freq[3] = freq_sel(oct, 3)
    inc_freq[3] = not inc_freq[3]
    play_sound()
    return

def n20_freq():
    freq[4] = freq_sel(oct, 4)
    inc_freq[4] = not inc_freq[4]
    play_sound()
    return

def n21_freq():
    freq[5] = freq_sel(oct, 5)
    inc_freq[5] = not inc_freq[5]
    play_sound()
    return

def n22_freq():
    freq[6] = freq_sel(oct, 6)
    inc_freq[6] = not inc_freq[6]
    play_sound()
    return

def n23_freq():
    freq[7] = freq_sel(oct, 7)
    inc_freq[7] = not inc_freq[7]
    play_sound()
    return

def n30_freq():
    freq[8] = freq_sel(oct, 8)
    inc_freq[8] = not inc_freq[8]
    play_sound()
    return

def n31_freq():
    freq[9] = freq_sel(oct, 9)
    inc_freq[9] = not inc_freq[9]
    play_sound()
    return

def n32_freq():
    freq[10] = freq_sel(oct, 10)
    inc_freq[10] = not inc_freq[10]
    play_sound()
    return

def n33_freq():
    freq[11] = freq_sel(oct, 11)
    inc_freq[11] = not inc_freq[11]
    play_sound()
    return

def n40_freq():
    freq[12] = freq_sel(oct, 12)
    inc_freq[12] = not inc_freq[12]
    play_sound()
    return

def n41_freq():
    freq[13] = freq_sel(oct, 13)
    inc_freq[13] = not inc_freq[13]
    play_sound()
    return

def n42_freq():
    freq[14] = freq_sel(oct, 14)
    inc_freq[14] = not inc_freq[14]
    play_sound()
    return

def n43_freq():
    freq[15] = freq_sel(oct, 15)
    inc_freq[15] = not inc_freq[15]
    play_sound()
    return

def n50_freq():
    freq[16] = freq_sel(oct, 16)
    inc_freq[16] = not inc_freq[16]
    play_sound()
    return

def n51_freq():
    freq[17] = freq_sel(oct, 17)
    inc_freq[17] = not inc_freq[17]
    play_sound()
    return

def n52_freq():
    freq[18] = freq_sel(oct, 18)
    inc_freq[18] = not inc_freq[18]
    play_sound()
    return

def n53_freq():
    freq[19] = freq_sel(oct, 19)
    inc_freq[19] = not inc_freq[19]
    play_sound()
    return

def n60_freq():
    freq[20] = freq_sel(oct, 20)
    inc_freq[20] = not inc_freq[20]
    play_sound()
    return

def n61_freq():
    freq[21] = freq_sel(oct, 21)
    inc_freq[21] = not inc_freq[21]
    play_sound()
    return

def n62_freq():
    freq[22] = freq_sel(oct, 22)
    inc_freq[22] = not inc_freq[22]
    play_sound()
    return

def n63_freq():
    freq[23] = freq_sel(oct, 23)
    inc_freq[23] = not inc_freq[23]
    play_sound()
    return

#gui section
root = Tk()
n = Frame(root)  #notes section 
o = Frame(root)  #options section
n.pack(side = LEFT)
o.pack(side = RIGHT)

#notes section 
n1 = Frame(n)
n10 = Button(n1, text="C", width = 2, height = 2, command=n10_freq)
n10.pack(side = LEFT)
n11 = Button(n1, text="C#", width = 2, height = 2, command=n11_freq)
n11.pack(side = LEFT)
n12 = Button(n1, text="D", width = 2, height = 2, command=n12_freq)
n12.pack(side = LEFT)
n13 = Button(n1, text="D#", width = 2, height = 2, command=n13_freq)
n13.pack(side = LEFT)
n1.grid(row = 0)
n2 = Frame(n)
n20 = Button(n2, text="E", width = 2, height = 2, command=n20_freq)
n20.pack(side = LEFT)
n21 = Button(n2, text="F", width = 2, height = 2, command=n21_freq)
n21.pack(side = LEFT)
n22 = Button(n2, text="F#", width = 2, height = 2, command=n22_freq)
n22.pack(side = LEFT)
n23 = Button(n2, text="G", width = 2, height = 2, command=n23_freq)
n23.pack(side = LEFT)
n2.grid(row = 1)
n3 = Frame(n)
n30 = Button(n3, text="G#", width = 2, height = 2, command=n30_freq)
n30.pack(side = LEFT)
n31 = Button(n3, text="A", width = 2, height = 2, command=n31_freq)
n31.pack(side = LEFT)
n32 = Button(n3, text="A#", width = 2, height = 2, command=n32_freq)
n32.pack(side = LEFT)
n33 = Button(n3, text="B", width = 2, height = 2, command=n33_freq)
n33.pack(side = LEFT)
n3.grid(row = 2)
n4 = Frame(n)
n40 = Button(n1, text="C", width = 2, height = 2, command=n40_freq)
n40.pack(side = LEFT)
n41 = Button(n1, text="C#", width = 2, height = 2, command=n41_freq)
n41.pack(side = LEFT)
n42 = Button(n1, text="D", width = 2, height = 2, command=n42_freq)
n42.pack(side = LEFT)
n43 = Button(n1, text="D#", width = 2, height = 2, command=n43_freq)
n43.pack(side = LEFT)
n4.grid(row = 3)
n5 = Frame(n)
n50 = Button(n2, text="E", width = 2, height = 2, command=n50_freq)
n50.pack(side = LEFT)
n51 = Button(n2, text="F", width = 2, height = 2, command=n51_freq)
n51.pack(side = LEFT)
n52 = Button(n2, text="F#", width = 2, height = 2, command=n52_freq)
n52.pack(side = LEFT)
n53 = Button(n2, text="G", width = 2, height = 2, command=n53_freq)
n53.pack(side = LEFT)
n5.grid(row = 4)
n6 = Frame(n)
n60 = Button(n3, text="G#", width = 2, height = 2, command=n60_freq)
n60.pack(side = LEFT)
n61 = Button(n3, text="A", width = 2, height = 2, command=n61_freq)
n61.pack(side = LEFT)
n62 = Button(n3, text="A#", width = 2, height = 2, command=n62_freq)
n62.pack(side = LEFT)
n63 = Button(n3, text="B", width = 2, height = 2, command=n63_freq)
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
scale_val = 0.0
pitch_slide = Scale(o3, from_ = 20, to = -20, variable = scale_val)
pitch_slide.pack()
o3.pack(side = LEFT)

root.mainloop()
