from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory


class MainApplication(Frame):
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
        self.pic = Label(third_frame, image=photo)
        self.pic.image = photo
        self.currentFrame = 1
        self.timerStarted = False

        # Buttons
        open_btn = Button(first_frame, text="Open", command=self.load_images)
        save_btn = Button(first_frame, text="Save")
        start_btn = Button(first_frame, text="Start",
                           command=self.btn_start_event)
        track_btn = Button(first_frame, text="Track")
        pause_btn = Button(first_frame, text="Pause")
        trk_one_btn = Button(first_frame, text="Track One Frame")
        divide_btn = Button(first_frame, text="Divide")

        # Frame Labels
        number_label = Label(first_frame, text="N. of Frames:")
        current_label = Label(first_frame, text="Current Frame:")

        number = Label(first_frame, text="1")
        self.current_frame_num = Label(first_frame, text=str(self.currentFrame
                                                             ))

        # Compaction
        compaction_label = Label(first_frame, text="Compaction")
        comp_start_btn = Button(first_frame, text="Start")
        comp_end_btn = Button(first_frame, text="End")

        # Blastocyst Caviation
        blastocyst_label = Label(first_frame, text="Blastocyst Cavitation")
        bc_start_btn = Button(first_frame, text="Start")

        # Text box
        instruction = "Click Open to load frames"
        self.inst = Label(second_frame, text=instruction, relief=RIDGE,
                          height=13, width=32)

        back_btn = Button(first_frame, text="Back")
        next_btn = Button(first_frame, text="Next")

        open_btn.grid(row=0, column=0, columnspan=2)
        save_btn.grid(row=0, column=1, columnspan=2)
        number_label.grid(row=1, column=0)
        current_label.grid(row=2, column=0)
        number.grid(row=1, column=1)
        self.current_frame_num.grid(row=2, column=1)
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
        back_btn.grid(row=9, column=0, columnspan=2)
        next_btn.grid(row=9, column=1, columnspan=2)
        self.inst.grid()
        self.pic.grid()

    def load_images(self):
        self.dir_name = askdirectory()
        self.dataset_root = self.dir_name
        self.inst.config(text="Press Start to Track")

    def set_current_frame(self, value):
        filename = self.dataset_root + "/Frame" + str(value).zfill(3) + ".png"
        embryo_img = Image.open(filename)
        embryo_photo = ImageTk.PhotoImage(embryo_img)
        self.pic.config(image=embryo_photo)
        self.pic.image = embryo_photo

    def timer_event(self):
        self.currentFrame += 1
        self.current_frame_num.config(text=str(self.currentFrame))
        self.set_current_frame(self.currentFrame)
        if self.timerStarted:
            self.after(100, self.timer_event())

    def btn_start_event(self):
        self.timerStarted = True
        self.after(100, self.timer_event())


if __name__ == "__main__":
    root = Tk()
    main = MainApplication(root)
    root.mainloop()
