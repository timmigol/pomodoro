import tkinter as tk
from PIL import Image, ImageTk
from timer import Timer  # Make sure timer.py is in the same folder

class Gui:
    def __init__(self):
        # Root window
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Pomodoro")
        self.root.configure(bg="#F8EDE3")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Header
        self.lbl_header = tk.Label(text="Work", font=("Helvetica", 32), bg="#F8EDE3")

        # Frame for image + timer
        self.frame_image = tk.Frame(self.root, width=300, height=300, bg="#F8EDE3")

        # Image
        original = Image.open("./tomato.png")
        resized = original.resize((300, 300))
        self.image = ImageTk.PhotoImage(resized)
        self.lbl_image = tk.Label(self.frame_image, image=self.image, bg="#F8EDE3")
        self.lbl_image.place(x=0, y=0, relwidth=1, relheight=1)

        # Timer label (over image)
        self.lbl_timer = tk.Label(self.frame_image, text="25:00", font=("Helvetica", 32, "bold"),
                                  bg="#F52515", fg="#F8EDE3")
        self.lbl_timer.place(relx=0.5, rely=0.6, anchor="center")

        # ✅ Create timer before button commands
        self.timer = Timer(self.root, self.update_timer_display)

        # Buttons
        self.btn_start = tk.Button(text="Start", command=self.timer.start)
        self.btn_pause = tk.Button(text="Pause", command=self.timer.pause)
        self.btn_reset = tk.Button(text="Reset", command=self.timer.reset)

        # Layout
        self.lbl_header.grid(row=0, column=1, pady=20)
        self.frame_image.grid(row=1, column=1)
        self.btn_start.grid(row=2, column=0, padx=20, pady=20)
        self.btn_pause.grid(row=2, column=1, padx=20, pady=20)
        self.btn_reset.grid(row=2, column=2, padx=20, pady=20)

    def update_timer_display(self, text):
        self.lbl_timer.config(text=text)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = Gui()
    gui.run()
