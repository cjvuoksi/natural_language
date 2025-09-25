from tkinter import *
from tkinter import ttk

from api import send_api, send_to_api

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
style = ttk.Style()
style.theme_use('aqua')
style.configure("Code.TLabel",
                font=('Courier', 10),      # Monospaced font
                foreground="black"
                )
ttk.Label(frm, text="Enter SQL prompt").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
userData = StringVar()
userInput = Text(frm, width=120, height=20)
userInput.grid(column=0, row=1, columnspan=15, rowspan=10)
apiOutput = StringVar()
display = ttk.Label(frm, textvariable=apiOutput, style="Code.TLabel")
display.grid(column=0, row=13)
ttk.Label(frm, text="Output:").grid(column=0, row=12)

def submit():
  user_in = userInput.get("1.0", END)
  response = send_to_api(user_in)
  userInput.delete("1.0", END)
  apiOutput.set(response)

submitButton = ttk.Button(frm, text="Submit", command=submit)
submitButton.grid(column=0, row=11)

if __name__ == '__main__':
    root.mainloop()