from tkinter import *
from PIL import Image, ImageTk


class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("CellTracker")

        master.geometry("800x500")

        main_frame = Frame(master)
        main_frame.grid(row=0, column=0, rowspan=10, columnspan=6)

        first_frame = Frame(master)
        first_frame.grid(row=0, column=0, rowspan=8, columnspan=3,
                         sticky=W+E+N+S)

        second_frame = Frame(master)
        second_frame.grid(row=8, column=0, rowspan=1, columnspan=3,
                          sticky=W+E+N+S)

        third_frame = Frame(master)
        third_frame.grid(row=0, column=4, rowspan=9, columnspan=3,
                         sticky=W+E+N+S)

    # Images
        img = Image.open("Frame001.png")
        photo = ImageTk.PhotoImage(img)
        pic = Label(third_frame, image=photo)

        # Buttons
        open_btn = Button(first_frame, text="Open")
        save_btn = Button(first_frame, text="Save")
        start_btn = Button(first_frame, text="Start")
        track_btn = Button(first_frame, text="Track")
        pause_btn = Button(first_frame, text="Pause")
        trk_one_btn = Button(first_frame, text="Track One Frame")
        divide_btn = Button(first_frame, text="Divide")

        # Frame Labels
        number_label = Label(first_frame, text="N. of Frames:")
        current_label = Label(first_frame, text="Current Frame:")

        number = Label(first_frame, text="1")
        current_frame_num = Label(first_frame, text="1")

        # Compaction
        compaction_label = Label(first_frame, text="Compaction")
        comp_start_btn = Button(first_frame, text="Start")
        comp_end_btn = Button(first_frame, text="End")

        # Blastocyst Caviation
        blastocyst_label = Label(first_frame, text="Blastocyst Cavitation")
        bc_start_btn = Button(first_frame, text="Start")

        # Text box
        instruction = "Instructional text \n will display in this text box. \n"
        inst = Label(second_frame, text=instruction, relief=RIDGE, height=15,
                     width=32)

        open_btn.grid(row=0, column=0, columnspan=2)
        save_btn.grid(row=0, column=1, columnspan=2)
        number_label.grid(row=1, column=0)
        current_label.grid(row=2, column=0)
        number.grid(row=1, column=1)
        current_frame_num.grid(row=2, column=1)
        start_btn.grid(row=3, column=0, columnspan=2)
        track_btn.grid(row=4, column=0, columnspan=2)
        pause_btn.grid(row=4, column=1, columnspan=2)
        trk_one_btn.grid(row=5, column=0, columnspan=3)
        divide_btn.grid(row=6, column=0, columnspan=3)
        compaction_label.grid(row=7, column=0, columnspan=2)
        comp_start_btn.grid(row=8, column=0)
        comp_end_btn.grid(row=8, column=1)
        blastocyst_label.grid(row=7, column=2)
        bc_start_btn.grid(row=8, column=2)
        inst.grid()
        pic.grid()

if __name__ == "__main__":
    root = Tk()
    main = MainApplication(root)
    root.mainloop()
