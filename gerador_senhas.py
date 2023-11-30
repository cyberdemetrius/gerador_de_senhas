# Gerador de Senhas Seguras em Python
# Leia o README :)
# Em caso de dúvidas, entre em contato

# Importando a biblioteca tkinter para criar a interface gráfica
# Importando a biblioteca messagebox para exibir mensagens na interface
# Importando as bibliotecas random e string para geração de senhas aleatórias

import tkinter as tk
from tkinter import messagebox
import random
import string

# Função para copiar a senha para a área de transferência
def copiar_para_area_transferencia(senha):
    root.clipboard_clear()
    root.clipboard_append(senha)
    root.update()  

# Função principal para gerar a senha
def gerar_senha():
    comprimento = entry_comprimento.get().strip()
    
    # Se o campo estiver vazio, a senha terá 10 caracteres por padrão
    if not comprimento:
        comprimento = 10
    else:
        comprimento = int(comprimento)

    usar_letras = var_letras.get()
    usar_numeros = var_numeros.get()
    usar_caracteres_especiais = var_caracteres_especiais.get()
    copiar_para_transferencia = var_copiar.get()

# Construir o conjunto de caracteres com base nas escolhas do usuário
    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_caracteres_especiais:
        caracteres += string.punctuation

# Verificar se o usuário selecionou pelo menos um tipo de caractere
    else:
        messagebox.showerror('Erro', 'Selecione pelo menos um tipo de caractere.')
        return

# Gerar a senha usando os caracteres selecionados
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

# Copiar a senha para a área de transferência, se selecionado pelo usuário    
    if copiar_para_transferencia:
        copiar_para_area_transferencia(senha)
        messagebox.showinfo('Senha Gerada', f'Sua senha gerada é:\n\n{senha}\n\n\nCopiada para a Área de Transferência.')
    else:
        messagebox.showinfo('Senha Gerada', f'Sua senha gerada é:\n\n{senha}')

# Configurando a janela principal
root = tk.Tk()
root.title('Gerador de Senhas Seguras')

largura = 600
altura = 400
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

posicao_x = (largura_tela - largura) // 2
posicao_y = (altura_tela - altura) // 2

root.geometry(f'{largura}x{altura}+{posicao_x}+{posicao_y}')
root.configure(bg='#1f1f1f')

# Elementos da interface gráfica
label_comprimento = tk.Label(root, text='\n\n\nComprimento da senha\n(N.º de caracteres)', font=('Roboto', 12, 'bold'), bg='#1f1f1f', fg='white')
label_comprimento.pack(pady=1)

entry_comprimento = tk.Entry(root, font=('Roboto', 11))
entry_comprimento.pack(pady=(0, 15))

# Variáveis de controle para os tipos de caracteres
var_letras = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_caracteres_especiais = tk.BooleanVar()
var_copiar = tk.BooleanVar()

# Checkbuttons para selecionar os tipos de caracteres
check_letras = tk.Checkbutton(root, text='Letras', variable=var_letras, font=('Roboto', 12), bg='#1f1f1f', fg='white', selectcolor='green', activeforeground='green', activebackground='#1f1f1f', highlightthickness=0)
check_letras.pack()

check_numeros = tk.Checkbutton(root, text='Números', variable=var_numeros, font=('Roboto', 12), bg='#1f1f1f', fg='white', selectcolor='green', activeforeground='green', activebackground='#1f1f1f', highlightthickness=0)
check_numeros.pack()

check_caracteres_especiais = tk.Checkbutton(root, text='Caracteres Especiais', variable=var_caracteres_especiais, font=('Roboto', 12), bg='#1f1f1f', fg='white', selectcolor='green', activeforeground='green', activebackground='#1f1f1f', highlightthickness=0)
check_caracteres_especiais.pack()

check_copiar = tk.Checkbutton(root, text='Copiar senha para Área de Transferência', variable=var_copiar, font=('Roboto', 12, 'italic'), bg='#1f1f1f', fg='white', selectcolor='green', activeforeground='green', activebackground='#1f1f1f', highlightthickness=0)
check_copiar.pack()

# Botão para gerar a senha
botao_gerar = tk.Button(root, text='Gerar Senha', command=gerar_senha, font=('Roboto', 16, 'bold'), bg='#4CAF50', fg='white')
botao_gerar.pack(pady=10)

# Adicionando uma recomendação de segurança ao usuário
observacao = tk.Label(root, text="Obs.: Recomenda-se marcar todas as opções para uma senha mais segura.\nConsidere utilizar 8 caracteres ou mais.", font=('Roboto', 11, 'italic'), bg='#1f1f1f', fg='white')
observacao.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
