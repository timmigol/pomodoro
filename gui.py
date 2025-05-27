import tkinter as tk
from PIL import Image, ImageTk

class Gui:
    def __init__(self):
        # styling the GUI
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Pomodoro")
        self.root.configure(bg="#F8EDE3")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        
        # create label for header
        self.lbl_header = tk.Label(text="Work",font=("Helvetica", 32),bg="#F8EDE3")

        # create a frame
        self.frame_image = tk.Frame(self.root, width=300, height=300, bg="#F8EDE3")
        
        # create label  containing image 
        original = Image.open("./tomato.png")
        resized = original.resize((300, 300))  # Try 100x100 or adjust as needed
        self.image = ImageTk.PhotoImage(resized)
        self.lbl_image = tk.Label(self.frame_image, image=self.image, bg="#F8EDE3")
        self.lbl_image.place(x=0, y=0, relwidth=1, relheight=1)

        
        # create label for countdown
        self.lbl_timer = tk.Label(self.frame_image, text="25:00", font=("Helvetica", 32,"bold"), bg="#F52515",fg="#F8EDE3")
        self.lbl_timer.place(relx=0.5, rely=.6, anchor="center")

        # create buttons
        self.btn_start = tk.Button(text="Start")
        self.btn_pause = tk.Button(text="Pause")
        self.btn_reset = tk.Button(text="Reset")

        # place elements
        # placle header
        self.lbl_header.grid(row=0, column=1, pady=20)
        # place image label
        self.frame_image.grid(row=1, column=1)
        # self.lbl_image.grid(row=1, column=1, pady=20)
        # place countdown label
        # self.lbl_countdown.grid(row=1, column=1, pady=20)
        # place buttons
        self.btn_start.grid(row=2, column=0, padx=20, pady=20)
        self.btn_pause.grid(row=2, column=1, padx=20, pady=20)
        self.btn_reset.grid(row=2, column=2, padx=20, pady=20)

    def run(self):
        self.root.mainloop()

