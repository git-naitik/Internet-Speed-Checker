from tkinter import *
import speedtest

def speed():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    up=str(round(sp.upload()/(10**6),3))+" Mbps"
    lb_down.config(text=down)
    lb_up.config(text=up)
    
sp = Tk()
sp.geometry("300x500")
sp.title("Internet Speed Test")
sp.config(bg="blue")

lb=Label(sp,text="Internet Speed Test",font=("Times New Roman",19,"bold"),foreground="#CEFFFD",bg="blue",justify="center")    
lb.place(x=44,y=40,height=50)

lb=Label(sp,text="Download Speed",font=("Times New Roman",16,"bold italic"),foreground="black",justify="center")    
lb.place(x=75,y=140,height=40)

lb_down=Label(sp,text="00",font=("Times New Roman",13,"bold"),foreground="black",justify="center")    
lb_down.place(x=101,y=190,height=22,width=100)

lb=Label(sp,text="Upload Speed",font=("Times New Roman",16,"bold italic"),foreground="black",justify="center")    
lb.place(x=87,y=260,height=40)

lb_up=Label(sp,text="00",font=("Times New Roman",13,"bold"),foreground="black",justify="center")    
lb_up.place(x=101,y=310,height=22,width=100)

button=Button(sp,text="Check Speed",font=("Times New Roman",17,"bold"),background="red",relief=RAISED,command=speed)
button.place(x=75,y=380)

sp.mainloop()
