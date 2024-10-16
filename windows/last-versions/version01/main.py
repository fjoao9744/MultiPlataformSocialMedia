from tkinter import *
from tkinter.font import Font

screen = Tk()
screen.config(bg="grey")
screen.state("zoomed")


custom_font = Font(size=17)
message_entry = Entry(screen, width=70, font=custom_font, relief=GROOVE, bd=5)
message_entry.pack(side=BOTTOM, pady=100)




mainloop()