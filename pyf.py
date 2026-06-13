import tkinter as tk
import random
from tkinter import filedialog

filename = None
data = None
corruptionVal = 1
corruptionRange = None
digitio = 0

def corrupt_file():
    global filename, data, corruptionRange, digitio
    if filename!="":
        offset = 0x002500
        corruptionRange = 0
        for i in range(int(len(data)*0.991)):
            if random.randint(1, 1200)==10:
                data[offset+digitio] = 0x26

            digitio=digitio+1

        save_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4 Video", "*.mp4")]
        )
        with open(save_path, "wb") as f:
            f.write(data)
    else:
        print("Pick a .mp4 first!")


def open_file():
    global filename, data
    filename = filedialog.askopenfilename()
    if filename!="":
        if filename.lower().endswith(".mp4"):
            with open(filename, "rb") as f:
                data = bytearray(f.read())
          
        else:
            print("Invalid file picked. Please pick a mp4 file.")




root = tk.Tk()

root.geometry("400x300")      # Set the initial size
root.resizable(False, False)  # Prevent resizing
root.title("vidBreaker")

label = tk.Label(root, text="Hello, world!")
label.pack()
label.place(x=50, y=100, width=00, height=40)
button = tk.Button(root, text="Open", command=open_file)
button.pack()
button.place(x=50, y=50, width=90, height=40)
button2 = tk.Button(root, text="Corrupt", command=corrupt_file)
button2.pack()
button2.place(x=50, y=100, width=90, height=40)

root.mainloop()