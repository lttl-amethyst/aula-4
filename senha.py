

import tkinter as tk
from tkinter import messagebox


def verificar_nota():
    senha = entry_nota.get()
    
    if len(senha) == 8:
        if senha.replace(".", "", 1).isdigit(): 
            senha = float(senha)
        else:
            messagebox.showerror("Erro", "Digite um número válido.")


        messagebox.showinfo("resultado", "sua senha é válida")
    else:
        messagebox.showerror("Erro", "Digite um número válido.")

# Janela principal
root = tk.Tk()
root.title("Verificador de Senha",bg="#F08CE3" )
root.geometry("500x200")
root.configure(bg="#F08CE3") 

# Widgets
tk.Label(root, text="digite uma senha:", bg="#F08CE3", fg="black", font=("Times New Roman", 11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=10)


tk.Button(root, text="verificar", command=verificar_nota, bg="light pink", fg="black", font=("Times New Roman", 11, "bold")).pack(pady=15)


root.mainloop()



