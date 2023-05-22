import json
import tkinter
import customtkinter
import subprocess
import sys
import CTkMessagebox

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
    for i in range(0,var):
        ora_minut_pauza_values.append ((ora_pauza_values[i] *100) + minut_pauza_values[i])




    with open("variabile.json", "w") as file:
        data["nr_pauze"] = var
        data["ora_pauza"] = ora_minut_pauza_values
        file.write(json.dumps(data))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)



# for variabile in data['variabile']:
var = tkinter.IntVar(master=frame,value=data['nr_pauze'])

label = customtkinter.CTkLabel(master=frame,text="Pauze Muzicale")

label.pack(pady=12,padx=10)

entries = []
nuentries=[]
ora=[]
minut=[]

ora1=[]
minut1=[]

pauze_M = False


def ok1():
    numar = int(entry1.get())
    if numar >16:
        subprocess.run(["python", "MessageBox.py"])
        numar = 16
    # Destroy the existing table
    for tx in ora:
        tx.destroy()
    for en in entries:
        en.destroy()
    for en1 in minut:
        en1.destroy()

    # Clear the lists
    ora.clear()
    entries.clear()
    minut.clear()

    # Create the new table
    for i in range(numar):
        tx = customtkinter.CTkTextbox(label, width=200, height=20)
        tx.grid(row=i + 10, column=0)
        tx.insert("0.0", "A " + str(i + 1) + " Pauza")
        tx.configure(state="disabled")
        ora.append(tx)

        en = customtkinter.CTkEntry(label, placeholder_text="ora")
        en.grid(row=i + 10, column=1)
        entries.append(en)

        en1 = customtkinter.CTkEntry(label, placeholder_text="minut")
        en1.grid(row=i + 10, column=2)
        minut.append(en1)


def Stop():
    sys.exit()
def Start():
    subprocess.run(["python", "hello.py"])
def Prediction():
    subprocess.run(["python", "hello.py"])

#def hallo():
    #for entry in entries:
        #print(int(entry.en.get())*100+int(entry.en1.get()))

def export2_fct(var_pm, durata_pm, ora_values, minut_values):
    print("Hello World")
    data = {
        "nr_pauze_mari": var_pm,
        "durata_pauza_mare": durata_pm,
        "ora_values": ora_values,
        "minut_values": minut_values
    }
    with open("variabile.json", "w") as file:
        file.write(json.dumps(data))


def ok2(var_pm, durata_pm):
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.place(x=230, y=270)

    for en2 in ora1:
        en2.destroy()
    for en3 in minut1:
        en3.destroy()

    # Clear the lists
    ora1.clear()
    minut1.clear()
    for i in range(var_pm):
        en2 = customtkinter.CTkEntry(frame_1, placeholder_text="ora")
        en2.grid(row=i + 10, column=0)
        ora1.append(en2)

        en3 = customtkinter.CTkEntry(frame_1, placeholder_text="minut")
        en3.grid(row=i + 10, column=1)
        minut1.append(en3)

    export2_btn = customtkinter.CTkButton(master=frame_1, text="Export2",
                                          command=lambda: get_entries(var_pm, durata_pm))
    export2_btn.grid(pady=12, padx=5)


def get_entries(var_pm, durata_pm):
    ora_values = []
    minut_values = []

    for entry in ora1:
        ora_values.append(entry.get())
    for entry in minut1:
        minut_values.append(entry.get())

    export2_fct(var_pm, durata_pm, ora_values, minut_values)


def pauzaMare():
    pauze_M = True

    Count_pauze_mari = customtkinter.CTkTextbox(master=frame, width=200, height=20)
    Count_pauze_mari.place_configure(relx=0.12,
                           width=190,
                           rely=0.25,
                           anchor="sw")
    Count_pauze_mari.insert("0.0", "Numar de Pauze MARI:")
    Count_pauze_mari.configure(state='disabled')


    entry2 = customtkinter.CTkEntry(master=frame)
    entry2.place_configure(relx=0.24,
                           rely=0.25,
                           width=40,
                           anchor="sw")

    Durata_pauze_mari = customtkinter.CTkTextbox(master=frame, width=200, height=20)
    Durata_pauze_mari.place_configure(relx=0.12,
                                     width=190,
                                     rely=0.30,
                                     anchor="sw")
    Durata_pauze_mari.insert("0.0", "Durata Pauze MARI:")
    Durata_pauze_mari.configure(state='disabled')

    entry3 = customtkinter.CTkEntry(master=frame)
    entry3.place_configure(relx=0.24,
                           rely=0.30,
                           width=40,
                           anchor="sw")

    def ok2_callback():
        var_pm = int(entry2.get()) if entry2.get().isdigit() else 0
        durata_pm = int(entry3.get()) if entry3.get().isdigit() else 0
        ok2(var_pm, durata_pm)

    ok2_btn = customtkinter.CTkButton(master=frame, width=45, text="Ok2", command=ok2_callback)
    ok2_btn.place(rely=0.245, relx=0.27)



button1=customtkinter.CTkButton(master=frame,text="FILTREAZA",fg_color="purple",command=Prediction)
button1.place(rely=0.8,
            relx=0)
button2=customtkinter.CTkButton(master=frame,text="START PROGRAM",hover_color="darkgreen",fg_color="green",command=Start)
button2.place(rely=0.8,
            relx=0.45)
button2=customtkinter.CTkButton(master=frame,text="STOP PROGRAM",hover_color="darkred",fg_color="red",command=Stop)
button2.place(rely=0.8,
            relx=0.9)

print("merge01")

text_1 = customtkinter.CTkTextbox(master=frame, width=200, height=20)
text_1.place_configure(relx=0.12,
            width=150,
             rely=0.12,
            anchor="sw")
text_1.insert("0.0", "Numar de Pauze:")
text_1.configure(state='disabled')

print('merge02')
entry1=customtkinter.CTkEntry(master=frame, textvariable=var,placeholder_text="Numar Pauze: ")
entry1.place_configure(relx=0.22,
            rely=0.12,
            width=45,
            anchor="sw")
ok1=customtkinter.CTkButton(master=frame,
          width=45,text="Ok1",command=ok1)
ok1.place(rely=0.085,
            relx=0.255)



button = customtkinter.CTkButton(master=frame,text="Export",command=login)
button.pack(pady=12, padx=10)


checkbox = customtkinter.CTkCheckBox(master=frame, text="Exista Pauza Mare?",command=pauzaMare)
checkbox.place(relx=0.12,
            rely=0.20,
            anchor="sw")


root.mainloop()