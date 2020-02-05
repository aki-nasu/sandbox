import tkinter as tk
from tkinter import messagebox as mbox
import record_costs_excel as ex

# 文字種チェック、必須チェック(TBD)
def validation_check():
    return

def register_click():
    # validation_check()
    send_data = [int(text_1.get()),int(text_2.get()),int(text_3.get()),int(text_4.get())]
    ex.w_xl(send_data)
    mbox.showinfo('dialog', 'Registered.')
    return

win = tk.Tk()
win.title('Record Utility Costs')
win.geometry('400x300')

label_1 = tk.Label(win, text='対象年月(yyyymm)')
label_1.pack()
text_1 = tk.Entry(win)
text_1.pack()
text_1.insert(tk.END, '202001')

label_2 = tk.Label(win, text='ガス料金')
label_2.pack()
text_2 = tk.Entry(win)
text_2.pack()

label_3 = tk.Label(win, text='電気料金')
label_3.pack()
text_3 = tk.Entry(win)
text_3.pack()

label_4 = tk.Label(win, text='水道料金')
label_4.pack()
text_4 = tk.Entry(win)
text_4.pack()

register_button = tk.Button(win,text='Register', command=register_click)
register_button.pack()

win.mainloop()