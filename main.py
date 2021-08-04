import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror

def send_sms(number,message):
  url = 'https://www.fast2sms.com/dev/bulkV2'

params={'authorization':'QU591aLuY0xHJhokzP6fTRAGgicKtMCrWwbXVsFZ7OBdvqjEnSXLrDEQAq7d1aysj9FKWfmBcv45JhUg',

'sender_id' : 'TXTIND',

'language' : english,

'message' : 'message',

'route' : 'v3',

'number' : number
}

response=requests.get(url,params=params)
dic=response.json()
print(dic)

return dic.get('return')

def btn_click():
	   num=textnum.get()
msg = textmsg.get("1.0",END)
r=send_sms(num,msg)

if r == True:
   showinfo("SEND SUCESS","SUCESSFULLY SEND")
else:
   showerror("ERROR MESSAGE" ,"SOMETING WENT WRONG")

# GUI
obj=Tk()
obj.title("Message Sender using Python")
obj.geometry("400*400")
font = ("Helvatica",22,"bold")

textnum=Entry(obj,font=font)
textnum.pack(fill=X,paddy=20)

textmsg=text(obj)
textmsg.pack(fill=X)

sendbtn=Button(obj,text="SEND MESSAGE",command=btn_click)

sendbtn.pack()

obj.mainloop()