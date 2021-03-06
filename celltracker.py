from Tkinter import *
from PIL import Image, ImageTk
from tkFileDialog import askdirectory, asksaveasfile
import os
import numpy as np
import cv2


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
        img = Image.open("images/blank.png")
        photo = ImageTk.PhotoImage(img)
        self.pic = Label(third_frame, image=photo)
        self.pic.image = photo
        self.current_frame = 0
        self.timerStarted = False

        # Buttons
        open_btn = Button(first_frame, text="Open", command=self.load_images)
        save_btn = Button(first_frame, text="Save", command=self.save_txt_file)
        start_btn = Button(first_frame, text="Start",
                           command=self.btn_start_event)
        track_btn = Button(first_frame, text="Track")
        pause_btn = Button(first_frame, text="Pause")
        trk_one_btn = Button(first_frame, text="Track One Frame")
        prev_btn = Button(first_frame, text="Prev", command=self.prev_btn_event)
        next_btn = Button(first_frame, text="Next", command=self.next_btn_event)

        # Frame Labels
        number_label = Label(first_frame, text="N. of Frames:")
        current_label = Label(first_frame, text="Current Frame:")
        num_text = 0
        self.number = Label(first_frame, text= num_text)
        self.current_frame_num = Label(first_frame, text=str(self.current_frame
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

        open_btn.grid(row=0, column=0, columnspan=2)
        save_btn.grid(row=0, column=1, columnspan=2)
        number_label.grid(row=1, column=0)
        current_label.grid(row=2, column=0)
        self.number.grid(row=1, column=1)
        self.current_frame_num.grid(row=2, column=1)
        start_btn.grid(row=3, column=0, columnspan=2)
        track_btn.grid(row=4, column=0, columnspan=2)
        pause_btn.grid(row=4, column=1, columnspan=2)
        trk_one_btn.grid(row=5, column=0, columnspan=3)
        prev_btn.grid(row=6, column=0, columnspan=2)
        next_btn.grid(row=6, column=1, columnspan=2)
        compaction_label.grid(row=7, column=0, columnspan=2)
        comp_start_btn.grid(row=8, column=0)
        comp_end_btn.grid(row=8, column=1)
        blastocyst_label.grid(row=7, column=2)
        bc_start_btn.grid(row=8, column=2)
        self.inst.grid()
        self.pic.grid()

    def load_images(self):
        """
        Loads .png files from selected directory to an array
        and sets new instructions
        """
        self.dir_name = askdirectory()
        if self.dir_name:
            self.dataset_root = self.dir_name
            items = os.listdir(self.dataset_root)
            self.image_list = []
            for names in items:
                if names.endswith(".png"):
                    self.image_list.append(names)
            self.number.config(text=str(len(self.image_list)))
            self.inst.config(text="Press Start to Track")
            self.set_current_frame(self.current_frame)

    def set_current_frame(self, value):
        #filename = self.dataset_root + "/Frame" + str(value).zfill(3) + ".png"
        self.filename = self.dataset_root + "/" + self.image_list[self.current_frame]
        embryo_img = Image.open(self.filename)
        embryo_photo = ImageTk.PhotoImage(embryo_img)
        self.pic.config(image=embryo_photo)
        self.pic.image = embryo_photo

#    def timer_event(self):
#        self.current_frame += 1
#        self.current_frame_num.config(text=str(self.current_frame))
#        self.set_current_frame(self.current_frame)
#        if self.timerStarted:
#            self.after(100, self.timer_event())

    def circle(self, pic):
        img = cv2.imread(pic,0)
        cimg = cv2.GaussianBlur(img,(5,5),0)

        circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT,1,100,
                                    param1=100,param2=30,minRadius=0,maxRadius=0)

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            print i[0],i[1],i[2]
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(255,255,0),3)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(255,255,0),3)

        cimg_image = Image.fromarray(cimg)
        cimg_image_tk = ImageTk.PhotoImage(cimg_image)

        self.pic.config(image=cimg_image_tk)
        self.pic.image = cimg_image_tk

    def btn_start_event(self):
        """
        Finds circle around cell on first image and updates instructions
        """
        self.circle(self.dataset_root + "/" + self.image_list[self.current_frame])

    def prev_btn_event(self):
        if self.current_frame > 0:
            self.current_frame -= 1
            self.current_frame_num.config(text=str(self.current_frame))
            self.set_current_frame(self.current_frame)

    def next_btn_event(self):
        if self.current_frame < len(self.image_list):
            self.current_frame += 1
            self.current_frame_num.config(text=str(self.current_frame))
            self.set_current_frame(self.current_frame)

    def save_txt_file(self):
        self.save_txt = asksaveasfile(defaultextension="txt")


if __name__ == "__main__":
    root = Tk()
    main = MainApplication(root)
    root.mainloop()
