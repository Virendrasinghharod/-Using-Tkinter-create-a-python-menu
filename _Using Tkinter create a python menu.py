#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import Menu

def on_new_file():
    print("New file created")

def on_open_file():
    print("Open file chosen")

def on_save_file():
    print("Save file chosen")

def on_exit():
    root.quit()

def on_cut():
    print("Cut chosen")

def on_copy():
    print("Copy chosen")

def on_paste():
    print("Paste chosen")

def on_undo():
    print("Undo chosen")

def on_redo():
    print("Redo chosen")

root = tk.Tk()
root.title("Python Menu Example")

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_new_file)
file_menu.add_command(label="Open", command=on_open_file)
file_menu.add_command(label="Save", command=on_save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)

# Create Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=on_cut)
edit_menu.add_command(label="Copy", command=on_copy)
edit_menu.add_command(label="Paste", command=on_paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=on_undo)
edit_menu.add_command(label="Redo", command=on_redo)

# Create Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

root.mainloop()



# In[ ]:




