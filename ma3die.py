import tkinter as tk 
import osc_client

def reti():
    receive_ip = "127.0.0.1"
    receive_port = 6942
    addr = "/print"
    message = "HELLOOOOOOOOOOOO" 

    send_message(receive_ip,receive_port,addr,message)

def osc():
    osc_client.reti()

def function1():
    print("This is function 1")

def function2():
    print("This is function 2")

def function3():
    print("This is function 3")

def function4():
    print("This is function 4")

def function5():
    print("This is function 5")

def function6():
    print("This is function 6") 

def volume_change(x):
    global var 
    if x == 1:
        var = var + 1

    else:
        var = var - 1
    print(var)

main = tk.Tk()
var = 0

title = tk.Label(main,text="NYP OSC DEMO CLASS", font="20")
title.grid(row=0, column=0, columnspan=3)

button1 = tk.Button(main,text="Functional", font="20",command=function1)
button2 = tk.Button(main,text="Functional", font="20",command=function2)
button3 = tk.Button(main,text="Functional", font="20",command=function3)
button4 = tk.Button(main,text="Functional", font="20",command=function4)
button5 = tk.Button(main,text="Functional", font="20",command=function5)
button6 = tk.Button(main,text="Functional", font="20",command=function6)
oscbutton = tk.Button(main,text="OSC", font="20",command=osc)

volumeup = tk.Button(main,text="Volume +",font="20",command=lambda m=1:volume_change(m))
volumedown = tk.Button(main,text="Volume -",font="20", command=lambda n=0:volume_change(n))

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
oscbutton.grid(row=4,column=1)


volumeup.grid(row=3,column=0)
volumedown.grid(row=3,column=2)
main.mainloop()


