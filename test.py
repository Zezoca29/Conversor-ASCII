import hashlib
import tkinter as tk
from tkinter import Entry, Label, StringVar, Button
import pyperclip

def gerar_epc_ascii():
    # Obtém o valor digitado pelo usuário
    epc_string = entrada_epc.get()

    # Converte para maiúsculas e filtra apenas caracteres alfanuméricos
    epc_string = ''.join(filter(str.isalnum, epc_string.upper()))

    # Verifica se o campo está vazio após a filtragem
    if not epc_string:
        resultado_var.set("Por favor, digite um valor para o EPC contendo números.")
        return

    # Aplica a função de hash SHA-256
    hashed_epc = hashlib.sha256(epc_string.encode()).hexdigest()

    # Pega os primeiros 24 caracteres do hash
    truncated_hashed_epc = hashed_epc[:24].upper()

    # Atualiza o label com o valor gerado
    resultado_var.set("EPC em ASCII (24 caracteres): " + truncated_hashed_epc)

    # Atualiza o valor na área de transferência
    pyperclip.copy(truncated_hashed_epc)

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerador de EPC")

if tk.TkVersion >= 8.6:
    janela.iconbitmap(default='Sem título-2.ico')  

# Cria um campo de entrada para o usuário digitar o EPC
entrada_epc = Entry(janela, font=("Helvetica", 12), width=30)
entrada_epc.pack(pady=10)

# Cria um botão para gerar o EPC
botao_gerar = tk.Button(janela, text="Gerar EPC", command=gerar_epc_ascii)
botao_gerar.pack(pady=10)

# Cria um label para mostrar o resultado
resultado_var = StringVar()
resultado_label = Label(janela, textvariable=resultado_var, font=("Helvetica", 12))
resultado_label.pack(pady=20)

# Cria um botão para copiar o valor gerado
botao_copiar = Button(janela, text="Copiar para Área de Transferência", command=lambda: pyperclip.copy(resultado_var.get().split(": ")[1]))
botao_copiar.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
