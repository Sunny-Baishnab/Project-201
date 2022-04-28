from tkinter import *
window = Tk()

window.title('Interest Calculator')
window.geometry('400x400')
window.configure(bg = '#ECECEB')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(Time.get())
    i = (p*r*t)/100
    interest = round(i,2)
    show_label.destroy()

    output_message = Label(show_frame,text = 'your Interest is Rs. '+str(interest),bg = '#f9a828',fg = '#07617d',font = ('Times',10),width = 55)
    output_message.place(x=20,y=40)
    output_message.pack()


heading_label = Label(window,text = 'Interest Calculator',bg = '#f9a828',fg = '#07617d',font = ('Courier',25),bd= 5)
heading_label.place(x =70,y = 20)

principle_label = Label(window,text = 'Enter Total Amount in Rs.',bg = '#f9a828',fg = '#07617d',font = ('Times',20),bd= 1)
principle_label.place(x = 20,y=90)

principle = Entry(window,text = '',bd = 2,width= 22)
principle.place(x = 325,y=100)

rate_label = Label(window,text = 'Enter Rate of Interest',bg = '#f9a828',fg = '#07617d',font = ('Times',20),bd= 1)
rate_label.place(x = 20,y=140)

rate = Entry(window,text = '',bd = 2,width= 22)
rate.place(x = 265,y=150)

time_label = Label(window,text = 'Enter Time Period',bg = '#f9a828',fg = '#07617d',font = ('Times',20),bd= 1)
time_label.place(x = 20,y=185)

Time = Entry(window,text = '',bd = 2,width= 22)
Time.place(x = 230,y=195)

calculate_button = Button(window,text = 'Calculate',bg = '#f9a828',fg = '#07617d',bd = 4,command = calculate_interest)
calculate_button.place(x=20,y=250)

show_frame = LabelFrame(window,text = 'Result',bg = '#f9a828',fg = '#07617d',font=('Times',12))
show_frame.pack(padx = 20,pady = 20)
show_frame.place(x = 20,y = 300)

show_label = Label(show_frame,text = '',bg = '#f9a828',fg = '#07617d',font = ('Times',20),width = 45)
show_label.place(x = 20,y = 20)
show_label.pack()


window.mainloop()