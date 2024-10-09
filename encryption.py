from tkinter import *
from customtkinter import *
import random
set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")

class ENCRYPTIONDECRIPTION:
    
    def __init__(self,root):
        
        
        self.root=root
        self.root.geometry("550x500+0+0")
        #Title in Window
        self.root.title("Encryption & Decription Software  >> Developed By Hanska Ravishan")
        self.root.config(bg="black")

        self.encryp=StringVar()
        self.msg=StringVar()
        #tab View
        self.tabview = CTkTabview(self.root, width=490,height=460)
        self.tabview.place(x=30,y=20)
        self.tabview.add("Encription")
        self.tabview.add("Decription")
        #Encription View
        lable=CTkLabel(self.tabview.tab("Encription"),text="Enter Massage ",font=("times new roman",20),text_color="White").place(x=10,y=7)
        self.textmsg=CTkTextbox(self.tabview.tab("Encription"),width=460,height=130)
        self.textmsg.place(x=10,y=33)
    
        encrypt_btn=CTkButton(self.tabview.tab("Encription"),text="Encrypt",font=("times new roman",25),command=self.encrypt,width=250).place(x=120,y=180)

        lable=CTkLabel(self.tabview.tab("Encription"),text="Encrypted Massage ",font=("times new roman",20),text_color="white").place(x=10,y=220)
        self.text=CTkTextbox(self.tabview.tab("Encription"),width=460,height=130)
        self.text.place(x=10,y=245)

        #Decription Tab
        lable=CTkLabel(self.tabview.tab("Decription"),text="Enter Encrypted Massage ",font=("times new roman",20),text_color="White").place(x=10,y=7)
        self.detextmsg=CTkTextbox(self.tabview.tab("Decription"),width=460,height=130)
        self.detextmsg.place(x=10,y=33)
    
        Decription_btn=CTkButton(self.tabview.tab("Decription"),text="Decrypt",font=("times new roman",25),command=self.decription,width=250).place(x=120,y=180)

        delable=CTkLabel(self.tabview.tab("Decription"),text="Decrypt Massage ",font=("times new roman",20),text_color="white").place(x=10,y=220)
        self.detext=CTkTextbox(self.tabview.tab("Decription"),width=460,height=130)
        self.detext.place(x=10,y=245)

    def encrypt(self):
        Userdialog = CTkInputDialog(text="Enter User Name :", title="User Name")
        user=Userdialog.get_input()
        text=self.textmsg.get("0.0", "end")
        
        ranint = random.randint(1500,3000)
        ranint2= random.randint(3100,5000)
        
        encrypt_text = ""
        lentext=len(text)
        i=0
        while i<lentext:
            char=text[i]
            if char.isalpha():
                shifted = ord(char) + ranint
                encrypt_text += chr(shifted)
            elif char.isspace():
                shifted = "#"
                encrypt_text += shifted
            else:
                shifted = ord(char) + ranint 
                encrypt_text += chr(shifted)
            i=i+2
        i=1
        while i<lentext:
            char=text[i]
            if char.isalpha():
                shifted = ord(char) + ranint
                encrypt_text += chr(shifted)
            elif char.isdigit():
                shifted = ord(char) + ranint 
                encrypt_text += chr(shifted)
            elif char.isspace():
                shifted = "#"
                encrypt_text += shifted
            else:
                shifted = ord(char) + ranint 
                encrypt_text += chr(shifted)
            i=i+2


        for characters in user:
            shifted = ord(characters) + ranint2
            encrypt_text += chr(shifted)


        encrypt_text=encrypt_text+ chr(ranint2)
        encrypt_text=encrypt_text+ chr(ranint)
        self.text.delete('1.0',END)
        self.text.insert("0.0",encrypt_text,"end")
        
    def decription(self):
        Userdialog = CTkInputDialog(text="Enter User Name :", title="User Name")
        user=Userdialog.get_input()
        text=self.detextmsg.get("0.0", "end")
        
        var_shift=-1580
        user_len=len(user)
        encrypt_text = ""
        lentext=len(text)
        lenth=lentext - user_len -3
        text1=text[0:lenth]
        id1=text[lentext-2]
        var_code=ord(id1)
        var_code1=int(var_code)
        ranint = -var_code1
        id2=text[lentext-3]
        var_code2=ord(id2)
        var_code3=int(var_code2)
        ranint2 = -var_code3
        evar_user=text[lentext-user_len-3:lentext-3]
        var_user=""

        for characters in evar_user:
            shifted = ord(characters) +ranint2
            var_user += chr(shifted)
        i=0
        

        if var_user==user:
            if (lenth%2)==1 :
                var=int(lenth/2)+1
            else:
                var=int(lenth/2)
            count=0
            while count<var:
                i=count
                while i<lenth:
                    char=text1[i]
                    
                    if char=="#":
                        shifte = " "
                        encrypt_text +=shifte       
                    else:  
                        
                        shifte = ord(char) + ranint
                        encrypt_text += chr(shifte)
                        
                    i=i+var
                count=count+1
            self.detext.insert("0.0",encrypt_text,"end")
        else:
            self.detext.insert("0.0","User Name Wrong","end")
        



if __name__=="__main__":
    root=Tk()
    obj=ENCRYPTIONDECRIPTION(root)
    root.mainloop()