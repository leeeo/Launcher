import os
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser as wb
import json

currentPath = os.getcwd()

root = tk.Tk()
root.title("Launcher")
 
class Button:
 
    row = 0
    def __init__(self, text, func, image=""):
        image = tk.PhotoImage(file=image)
        tk.Grid.rowconfigure(root, Button.row, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)
 
        self.button = tk.Button(
            root,
            text=text,
            image=image,
            compound = tk.LEFT,
            command=func)
        # self.button.pack()
        self.button.grid(sticky="nswe")
        self.button.image = image
        Button.row += 1
 
    def open(text):
        os.startfile(text)

def web(str):
    return lambda : wb.open(str)

with open(currentPath + "\\Launcher\\Launcher\\config.json", "r") as json_file:
    json_data = json.load(json_file)

data = []

for site in json_data['site']:
    data.append([site['name'], web(site['link']), site['image']])

root.geometry("200x500-0-0")

for d in data:
    b = Button(*d)
 
root.mainloop()