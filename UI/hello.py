import customtkinter

print("Hello World")
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password",show="*")
entry2.pack(pady=12, padx=10)


for variabile in data['variabile']:
    var=variabile['nr_pauze']