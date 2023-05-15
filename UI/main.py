import json
import tkinter
import customtkinter

with open("variabile.json", "r") as v:
    data = json.load(v)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#variabile


def login():
    print("NU Test")
    var = int(entry1.get())

    ora_pauza_values = []
    minut_pauza_values =[]
    ora_minut_pauza_values =[]

    for entry in entries:
        ora_pauza_values.append(int(entry.get()))
    for entry in nuentries:
        minut_pauza_values.append(int(entry.get()))
    for i in range(0,10):
        ora_minut_pauza_values.append ((ora_pauza_values[i] *100) + minut_pauza_values[i])



    with open("variabile.json", "w") as file:
        data["nr_pauze"] = var
        data["ora_pauza"] = ora_minut_pauza_values
        file.write(json.dumps(data))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)



# for variabile in data['variabile']:
var = tkinter.IntVar(master=frame,value=data['nr_pauze'])

label = customtkinter.CTkLabel(master=frame,text="Muzica In Pauze")

label.pack(pady=12,padx=10)

entries = []
nuentries=[]
ora=[]
minut=[]

for i in range(10):
    tx = customtkinter.CTkTextbox(label,width=200, height=20)
    tx.grid(row=i + 10, column=0)
    tx.insert("0.0", "A "+str(i+1)+" Pauza")
    tx.configure(state="disabled")

    ora.append(tx)
    en = customtkinter.CTkEntry(label,placeholder_text="ora")
    en.grid(row=i+10, column=1)
    entries.append(en)

    minut.append(tx)
    en1 = customtkinter.CTkEntry(label,placeholder_text="minut")
    en1.grid(row=i + 10, column=2)
    nuentries.append(en1)

def hallo():
    for entry in entries:
        print(int(entry.en.get())*100+int(entry.en1.get()))


def pauzaMare():
    pauze_M = True


    entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="Cate Pauze Mari ? ")
    entry2.place_configure(relx=0.12,
                           rely=0.25,
                           width=150,
                           anchor="sw")

button1=customtkinter.CTkButton(master=frame,text="krijg",command=pauzaMare)
button1.place(rely=0.7,
            relx=0.5)


print("merge01")

text_1 = customtkinter.CTkTextbox(master=frame, width=200, height=20)
text_1.place_configure(relx=0.12,
            width=150,
             rely=0.12,
            anchor="sw")
text_1.insert("0.0", "Numar de Pauze:")

print('merge02')
entry1=customtkinter.CTkEntry(master=frame, textvariable=var,placeholder_text="Numar Pauze: ")
entry1.place_configure(relx=0.22,
            rely=0.12,
            width=45,
            anchor="sw")


button = customtkinter.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12, padx=10)


checkbox = customtkinter.CTkCheckBox(master=frame, text="Exista Pauza Mare?",command=pauzaMare)
checkbox.place(relx=0.12,
            rely=0.20,
            anchor="sw")


root.mainloop()