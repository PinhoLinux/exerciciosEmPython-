import tkinter as tk
from tkinter import Label, Entry, Button

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    # Aqui vocÃª pode adicionar lÃ³gica para verificar as credenciais

# Criar a janela
janela = tk.Tk()
janela.title("Tela de Login")

# Elementos da interface
label_usuario = Label(janela, text="UsuÃ¡rio:")
label_senha = Label(janela, text="Senha:")
entry_usuario = Entry(janela)
entry_senha = Entry(janela, show="*")  # Para esconder a senha
botao_login = Button(janela, text="Login", command=fazer_login)

# Posicionar elementos na janela
label_usuario.grid(row=0, column=0)
label_senha.grid(row=1, column=0)
entry_usuario.grid(row=0, column=1)
entry_senha.grid(row=1, column=1)
botao_login.grid(row=2, column=1)

# Iniciar o loop da interface grÃ¡fica
janela.mainloop()
