# Import de bibliotecas

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog, simpledialog

# Criando a janela
root = Tk()
root.title("Bloco de notas")
root.resizable(0, 0)


# Criando o bloco para texto da janela
blocoDeTexto = ScrolledText(root, width = 60, height = 20)
filename = ''

# Criando as funções
def cmdNovo():      # Novo arquivo no Menu
    global nomeArquivo
    if len(blocoDeTexto.get('1.0', END+ '-1c')) > 0:
        if messagebox.askyesno("Bloco de Notas", "Salvar as alterações do arquivo?"):
            cmdSalvar()
        else:
            blocoDeTexto.delete(0.0, END)
    root.title("Bloco de notas")

def cmdAbrir():     # Abrir arquivo no Menu
    fd = filedialog.askopnfile(parent = root, mode = 'r')
    t = fd.read()
    blocoDeTexto.delete(0.0, END)
    blocoDeTexto.insert(0.0, t)

def cmdSalvar():     # Salvar arquivo no Menu
    fd = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if fd != None:
        dados = blocoDeTexto.get('1.0', END)
    try:
        fd.write(dados)
    except:
        messagebox.showerror("Error", "Erro ao salvar arquivo")

def cmdSalvarComo():    # Salvar como no Menu
    fd = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    t = blocoDeTexto.get(0.0, END)
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror("Error", "Erro ao salvar arquivo")

def cmdSair():      # Sair no Menu
    if messagebox.askyesno("Bloco de Notas", "Tem certeza que deseja sair?"):
        root.destroy()

def cmdCortar():
    blocoDeTexto.event_generate("<<Cut>>")

def cmdCopiar():
    blocoDeTexto.event_generate("<<Copy>>")

def cmdColar():
    blocoDeTexto.event_generate("<<Paste>>")

def cmdApagar():
    blocoDeTexto.event_generate("<<Clear>>")

def cmdEncontrar():
    blocoDeTexto.tag_remove("Found", '1.0', END)
    find = simpledialog.askstring("Procurar", "O que deseja procurar?")
    if find:
        idx = '1.0'
    while 1:
        idx = blocoDeTexto.search(find, idx, nocase = 1, stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' % (idx, len(find))
        blocoDeTexto.tag_add('Found', idx, lastidx)
        idx = lastidx
    blocoDeTexto.tag_config('Found', foreground= 'white', background= 'yellow')
    blocoDeTexto.bind("<1>", click)

def click(event):
    blocoDeTexto.tag_config('Found', foreground= 'black', background= 'white')

def cmdSelecinarTudo():     # Selecionar tudo no Menu
    blocoDeTexto.event_generate("<<SelectAll>>")

# Criando o Menu de itens 'Arquivo' e 'Editar' e adicionando as opções
menuBloco = Menu(root)
root.configure(menu = menuBloco)

arquivosMenu = Menu(menuBloco, tearoff= False)
menuBloco.add_cascade(label = "Arquivo", menu = arquivosMenu)

arquivosMenu.add_command(label = "Novo", command = cmdNovo)
arquivosMenu.add_command(label = "Abrir", command = cmdAbrir)
arquivosMenu.add_command(label = "Salvar", command = cmdSalvar)
arquivosMenu.add_command(label = "Salvar como", command = cmdSair)
arquivosMenu.add_separator()
arquivosMenu.add_command(label = "Sair", command = cmdSair)

editarMenu = Menu(menuBloco, tearoff = False)
menuBloco.add_cascade(label = "Editar", menu = editarMenu)

editarMenu.add_command(label = "Cortar", command = cmdCortar)
editarMenu.add_command(label = "Copiar", command = cmdCopiar)
editarMenu.add_command(label = "Colar", command = cmdColar)
editarMenu.add_command(label = "Apagar", command = cmdApagar)
editarMenu.add_separator()
editarMenu.add_command(label = "Procurar", command = cmdEncontrar)
editarMenu.add_separator()
editarMenu.add_command(label = "Selecionar Tudo", command = cmdSelecinarTudo)

# Chamando a aplicação
blocoDeTexto.pack()
root.mainloop()