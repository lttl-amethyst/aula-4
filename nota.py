import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get()

    if nota_texto.replace(".", "", 1).isdigit():
        nota = float(nota_texto)

        if nota >= 7:
            resultado = "aprovado"
        elif nota >= 5:
            resultado = "recuperação"
        else:
            resultado = "reprovado"

        messagebox.showinfo("resultado", f"situação: {resultado}")
    else:
        messagebox.showerror("erro", "digite um número válido")

root = tk.Tk()
root.title("verificador de nota")
root.geometry("500x100")
root.configure(bg="#ffcb7a")

tk.Label(root, text = "digite a nota do aluno:", bg="#ffcb7a", fg="black", font=("Times New Roman", 11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(root, text = "verificar", command= verificar_nota, bg= "light blue", fg="white", font=("Times New Roman", 11, "bold")).pack(pady=15)

root.mainloop()