import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import tkinter.font as tkfont

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END).rstrip())
        messagebox.showinfo("Info", "File saved successfully!")

def about():
    messagebox.showinfo("About", "Simple Text Editor using Tkinter\nCreated by Jaspreet.")

def on_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def change_font():
    current_font = tkfont.Font(font=text['font'])

    font_family = simpledialog.askstring("Font", "Enter font family (e.g., Arial, Helvetica):", initialvalue=current_font.actual('family'))
    font_size = simpledialog.askinteger("Size", "Enter font size:", initialvalue=current_font.actual('size'))

    if font_family and font_size:
        new_font = (font_family, font_size)
        text.config(font=new_font)

# Main Window
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)
menu.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
menu.add_cascade(label="Edit", menu=edit_menu)

# Font Menu
font_menu = tk.Menu(menu, tearoff=0)
font_menu.add_command(label="Change Font", command=change_font)
menu.add_cascade(label="Font", menu=font_menu)

# Help Menu
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=help_menu)

# Text Area with Scrollbar
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True)

scroll = tk.Scrollbar(text_frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(text_frame, wrap=tk.WORD, font=("Helvetica", 12), fg="blue", yscrollcommand=scroll.set)
text.pack(expand=True, fill=tk.BOTH)

scroll.config(command=text.yview)



 

# Exit protocol
root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()
