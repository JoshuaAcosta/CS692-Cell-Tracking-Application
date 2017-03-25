from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x500")


main_frame = Frame(root)
main_frame.master.title("CellTracker")
main_frame.grid(row=0, column=0, rowspan=10, columnspan=6)

first_frame = Frame(root)
first_frame.grid(row=0, column=0, rowspan=8, columnspan=3, sticky=W+E+N+S)

second_frame = Frame(root)
second_frame.grid(row=8, column=0, rowspan=1, columnspan=3, sticky=W+E+N+S)

third_frame = Frame(root)
third_frame.grid(row=0, column=3, rowspan=9, columnspan=3, sticky=W+E+N+S)


#Images
img = Image.open("Frame001.png")
photo = ImageTk.PhotoImage(img)
pic = Label(third_frame, image=photo)

# Buttons
a = Button(first_frame, text="Open")
b = Button(first_frame, text="Save")
c = Button(first_frame, text="Start")
d = Button(first_frame, text="Track")
e = Button(first_frame, text="Pause")
f = Button(first_frame, text="Track One Frame")
g = Button(first_frame, text="Divide")

# Frame Labels
number_label = Label(first_frame, text="N. of Frames:")
current_label = Label(first_frame, text="Current Frame:")

number = Label(first_frame, text="1")
current_frame_num = Label(first_frame, text="1")

# Compaction
compaction_label = Label(first_frame, text="Compaction")
h = Button(first_frame, text="Start")
i = Button(first_frame, text="End")

# Blastocyst Caviation
blastocyst_label = Label(first_frame, text="Blastocyst Cavitation")
j = Button(first_frame, text="Start")

# Text box
instruction = "Instructional text \n will display in this text box. \n"
T = Label(second_frame, text=instruction, relief=RIDGE, height=15, width=32)

a.grid(row=0, column=0, columnspan=2)
b.grid(row=0, column=1, columnspan=2)
number_label.grid(row=1, column=0)
current_label.grid(row=2, column=0)
number.grid(row=1, column=1)
current_frame_num.grid(row=2, column=1)
c.grid(row=3, column=0, columnspan=2)
d.grid(row=4, column=0, columnspan=2)
e.grid(row=4, column=1, columnspan=2)
f.grid(row=5, column=0, columnspan=3)
g.grid(row=6, column=0, columnspan=3)
compaction_label.grid(row=7, column=0, columnspan=2)
h.grid(row=8, column=0)
i.grid(row=8, column=1)
blastocyst_label.grid(row=7, column=2)
j.grid(row=8, column=2)
T.grid()
pic.grid()

root.mainloop()
