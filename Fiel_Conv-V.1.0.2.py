# FIEL CONVERSOR - Pequeno e simples, mas poderoso! O Fiel Conversor é um programa que permite converter imagens em PDF, PDF em imagens, extrair páginas selecionadas de um PDF, agrupar arquivos em PDF em um só, girar páginas, e converter imagens de texto para PDF com OCR.
Author = "Copyright (C) 2026 AUDSIS-ADG-SUBAC-Controladoria Geral do Município | Prefeitura da Cidade do Rio de Janeiro"

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

Version = "1.0.2"

import os
import subprocess
import tkinter as tk
import PyPDF2
import fitz
from PIL import Image, ImageTk
from tkinter import Tk, messagebox as mb, filedialog as fd, Frame, ttk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import sys
from Strings import *

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ==================== NOME E VERSÃO ====================
nome_prog = name_progr_txlabel
versao = Version
License = license_main_tx

# ==================== JANELA INICIAL (SPLASH) ====================
janela_inicial = tk.Tk()
janela_inicial.configure(background='lightyellow')
janela_inicial.configure(highlightbackground='lightgray', highlightcolor='lightgray', highlightthickness=10)

screen_width = janela_inicial.winfo_screenwidth()
screen_height = janela_inicial.winfo_screenheight()

janela_inicial_width = screen_width * 0.33
janela_inicial_height = screen_height * 0.77

janela_inicial_x = (screen_width - janela_inicial_width) / 2
janela_inicial_y = (screen_height - janela_inicial_height) / 2

janela_inicial.geometry(f"{int(janela_inicial_width)}x{int(janela_inicial_height)}+{int(janela_inicial_x)}+{int(janela_inicial_y)}")
janela_inicial.overrideredirect(True)

frame = tk.Frame(janela_inicial, bg='lightyellow')
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label_nomeprog = tk.Label(frame, text=nome_prog + ' - ' + versao, font=("Arial", 20, 'bold'), bg='lightyellow', foreground='orange4')
label_nomeprog.pack(side=tk.TOP, fill=tk.X, expand=True, pady=0)

img_progr = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Imagens", "img_progr.png")
foto1 = ImageTk.PhotoImage(Image.open(img_progr))

img_gpl = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Imagens", "AGPLv3.png")
foto2 = ImageTk.PhotoImage(Image.open(img_gpl))

label_imagem1 = tk.Label(frame, image=foto1, bg='lightyellow')
label_imagem1.pack(side=tk.TOP, fill=tk.X, expand=True, pady=0)

label_1 = tk.Label(frame, font=('Arial', 12, 'bold'), bg='lightyellow', foreground='orange4', text=progr_intro_txlabel)
label_1.pack(side=tk.TOP, fill=tk.X, expand=True, pady=0)

label_2 = tk.Label(frame, font=('Arial', 9, 'normal'), bg='lightyellow', foreground='orange4', text=Author, wraplength=350, justify='center')
label_2.pack(side=tk.TOP, fill=tk.X, expand=True, pady=0)

label_imagem2 = tk.Label(frame, image=foto2, bg='lightyellow')
label_imagem2.pack(side=tk.TOP, fill=tk.X, expand=True, pady=0)

label_3 = tk.Label(frame, font=('Arial', 9, 'normal'), bg='lightyellow', foreground='orange4', text=License)
label_3.pack(side=tk.TOP, fill=tk.X, expand=True, pady=0)

janela_inicial.after(3000, janela_inicial.destroy)
janela_inicial.mainloop()

# ==================== JANELA PRINCIPAL ====================
janela = Tk()
janela.title(nome_prog + " - " + versao)
img_icone = tk.PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "Imagens", "img_progr.png"))
janela.iconphoto(False, img_icone)
janela.configure(background='lightyellow')
janela.configure(highlightbackground='lightyellow', highlightcolor='lightyellow', highlightthickness=10)

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
janela_width = screen_width * 0.6
janela_height = screen_height * 0.6
janela_x = (screen_width - janela_width) / 2
janela_y = (screen_height - janela_height) / 2
janela.geometry(f"{int(janela_width)}x{int(janela_height)}+{int(janela_x)}+{int(janela_y)}")

frame_cima = Frame(janela, bg="lightyellow")
frame_baixo = Frame(janela, bg="lightyellow")

# Botões superiores
botao1 = tk.Button(frame_cima, text=imgs_to_pdf_txbutton, command=lambda: abrir_janela(janela1), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao2 = tk.Button(frame_cima, text=pdf_to_imgs_txbutton, command=lambda: abrir_janela(janela2), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao3 = tk.Button(frame_cima, text=extract_txbutton, command=lambda: abrir_janela(janela3), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao4 = tk.Button(frame_cima, text=group_txbutton, command=lambda: abrir_janela(janela4), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao9 = tk.Button(frame_cima, text=rotate_txbutton, command=lambda: abrir_janela(janela9), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao5 = tk.Button(frame_cima, text=ocr_txbutton, command=lambda: abrir_janela(janela5), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao7 = tk.Button(frame_cima, text=license_txbutton, command=lambda: abrir_janela(janela7), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao8 = tk.Button(frame_cima, text=about_txbutton, command=lambda: abrir_janela(janela8), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')

botao1.pack(side="left")
botao2.pack(side="left")
botao3.pack(side="left")
botao4.pack(side="left")
botao9.pack(side="left")
botao5.pack(side="left")
botao7.pack(side="left")
botao8.pack(side="left")

frame_cima.pack(fill="x")
frame_baixo.pack(fill="both", expand=True)

# Subframes (janelas internas)
janela1 = Frame(frame_baixo, bg="lightyellow")
janela2 = Frame(frame_baixo, bg="lightyellow")
janela3 = Frame(frame_baixo, bg="lightyellow")
janela4 = Frame(frame_baixo, bg="lightyellow")
janela5 = Frame(frame_baixo, bg="lightyellow")
janela7 = Frame(frame_baixo, bg="lightyellow")
janela8 = Frame(frame_baixo, bg="lightyellow")
janela9 = Frame(frame_baixo, bg="lightyellow")

# Labels de título das sub-janelas
label1 = tk.Label(janela1, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=imgs_to_pdf_txlabel)
label2 = tk.Label(janela2, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=pdf_to_imgs_txlabel)
label3 = tk.Label(janela3, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=extract_txlabel)
label4 = tk.Label(janela4, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=group_txlabel)
label5 = tk.Label(janela5, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=ocr_txlabel)
label7 = tk.Label(janela7, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=license_txlabel)
label8 = tk.Label(janela8, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=about_txbutton + " " + nome_prog + " - " + versao)
label9 = tk.Label(janela9, font=("Arial", 16, 'bold'), bg='lightyellow', foreground='orange4', text=rotate_txlabel)

# Botões de fechar (renomeados para evitar confusão)
close1 = tk.Button(janela1, text=close_button_txbutton, command=lambda: fechar_janela(janela1), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close2 = tk.Button(janela2, text=close_button_txbutton, command=lambda: fechar_janela(janela2), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close3 = tk.Button(janela3, text=close_button_txbutton, command=lambda: fechar_janela(janela3), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close4 = tk.Button(janela4, text=close_button_txbutton, command=lambda: fechar_janela(janela4), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close5 = tk.Button(janela5, text=close_button_txbutton, command=lambda: fechar_janela(janela5), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close7 = tk.Button(janela7, text=close_button_txbutton, command=lambda: fechar_janela(janela7), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close8 = tk.Button(janela8, text=close_button_txbutton, command=lambda: fechar_janela(janela8), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
close9 = tk.Button(janela9, text=close_button_txbutton, command=lambda: fechar_janela(janela9), font=("Arial", 14, 'bold'), bg='white', foreground='orange4')

# Posicionamento dos títulos e botões de fechar
for lbl in (label1, label2, label3, label4, label5, label7, label8, label9):
    lbl.pack(pady=10)

close1.pack(pady=10)
close2.pack(pady=10)
close3.pack(pady=10)
close4.pack(pady=10)
close5.pack(pady=10)
close7.pack(pady=10)
close8.pack(pady=10)
close9.pack(pady=10)

def abrir_janela(subframe):
    for child in frame_baixo.winfo_children():
        if child != subframe:
            child.pack_forget()
    subframe.pack(fill="both", expand=True)
    desabilitar_botoes()

def fechar_janela(subframe):
    subframe.pack_forget()
    habilitar_botoes()

    # Reset geral
    selec_img.config(state='normal')
    img_pdf.config(state='disabled')
    img_lista.clear()
    multimg_lista.clear()

    Select_PDF.config(state='normal')
    salvar_extracao.config(state='disabled')
    pagina_inicial.delete(0, "end")
    pagina_final.delete(0, "end")

    file_button.config(state='normal')
    rotate_button.config(state='disabled')
    pages_entry.delete(0, tk.END)

    # Reset da caixa de texto para Release Notes
    text_box.config(state='normal')
    text_box.delete('1.0', 'end')
    caminho_arq_release = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Release_Notes.md")
    with open(caminho_arq_release, "r", encoding="utf-8") as f:
        text_box.insert("1.0", f.read())
    text_box.config(state='disabled')

def desabilitar_botoes():
    for botao in frame_cima.winfo_children():
        botao.config(state='disabled')

def habilitar_botoes():
    for botao in frame_cima.winfo_children():
        botao.config(state='normal')

# Caixa de texto compartilhada (Release Notes)
text_box = ScrolledText(janela, width=215, height=10, font=('Arial', 12), wrap='word', bg='white', foreground='blue4')
text_box.pack(pady=15)

caminho_arq_release = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Release_Notes.md")
with open(caminho_arq_release, "r", encoding="utf-8") as f:
    text_box.insert("1.0", f.read())
text_box.config(state='disabled')

# Labels inferiores
tk.Label(janela, font=('Arial', 12, 'bold'), bg='lightyellow', foreground='orange4', text=nome_prog + " - " + versao).pack(pady=0)
tk.Label(janela, font=('Arial', 9, 'normal'), bg='lightyellow', foreground='orange4', text=Author).pack(pady=0)
tk.Label(janela, font=('Arial', 9, 'normal'), bg='lightyellow', foreground='orange4', text=License).pack(pady=0)

# ==================== VARIÁVEIS GLOBAIS ====================
img_lista = []
multimg_lista = []
pdf_files = []
file_path = ""

# ==================== IMAGENS → PDF ====================
def escolha_as_imagens():
    global files, img_lista, multimg_lista
    try:
        text_box.config(state='normal')
        text_box.delete('1.0', 'end')
        img_lista.clear()
        multimg_lista.clear()

        files = fd.askopenfilenames(
            title=select_images_tx,
            filetypes=(("JPGs", "*.jpg"), ("PNGs", "*.png"), ("GIFs", "*.gif"),
                       ("BMPs", "*.bmp"), ("TIFFs", "*.tiff"), ("WEBPs", "*.webp"),
                       (all_txopenfiles, "*.*"))
        )

        if files:
            for j in files:
                multimg_lista.append(j)
                img = Image.open(j).convert('RGB')
                img_lista.append(img)
                text_box.insert('end', image_selected_txbox + j + '\n')

            img_pdf.config(state='normal')
            selec_img.config(state='disabled')
        else:
            text_box.insert('end', no_image_txbox + '\n')

        text_box.config(state='disabled')
    except Exception as err:
        mb.showerror(msg_error_tx, f"Ocorreu um erro:\n{err}")

def converter_pdf():
    try:
        if not img_lista:
            return
        saveloc = fd.asksaveasfilename(
            title=convert_images_to_pdf_txtitle,
            initialfile=initialfile_tx,
            filetypes=[(pdf_filetype, "*.pdf")],
            defaultextension=".pdf"
        )
        if saveloc:
            if not saveloc.lower().endswith(".pdf"):
                saveloc += ".pdf"
            img_lista[0].save(saveloc, save_all=True, append_images=img_lista[1:], quality=95)

            text_box.config(state='normal')
            text_box.insert('end', saved_to_txbox + saveloc + '\n' + task_completed_txbox + '\n')
            text_box.see('end')
            text_box.config(state='disabled')

            selec_img.config(state='normal')
            img_pdf.config(state='disabled')
            img_lista.clear()
            multimg_lista.clear()
        else:
            text_box.config(state='normal')
            text_box.delete('1.0', 'end')
            text_box.insert('end', operation_canceled_txbox + '\n')
            text_box.config(state='disabled')
            selec_img.config(state='normal')
            img_pdf.config(state='disabled')
            img_lista.clear()
            multimg_lista.clear()
    except Exception as err:
        mb.showerror(msg_error_tx, f"Ocorreu um erro:\n{err}")

selec_img = tk.Button(janela1, text=select_images_tx, command=escolha_as_imagens, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
selec_img.pack(pady=10)
img_pdf = tk.Button(janela1, text=save_img_selec_txbutton, command=converter_pdf, state='disabled', font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
img_pdf.pack(pady=10)

# ==================== PDF → IMAGENS ====================
def converter_imagem():
    try:
        text_box.config(state='normal')
        text_box.delete('1.0', 'end')
        pdf_file = fd.askopenfilename(title=select_pdf_tx, filetypes=((pdf_filetype, "*.pdf"), (all_txopenfiles, "*.*")))

        if not pdf_file:
            text_box.insert('end', no_pdf_file_selected_txbox + '\n')
            text_box.config(state='disabled')
            return

        doc = fitz.open(pdf_file)
        dpi = int(quality_var.get())
        zoom = dpi / 75
        magnify = fitz.Matrix(zoom, zoom)

        text_box.insert('end', file_selected_txbox + pdf_file + '\n')
        text_box.insert('end', processing_file_txbox + '\n' + please_wait_txbox + '\n')

        folder = fd.askdirectory(title=askdirectory_txtitle)
        if not folder:
            text_box.delete('1.0', 'end')
            text_box.insert('end', operation_canceled_txbox + '\n')
            text_box.config(state='disabled')
            doc.close()
            return

        ext = "jpg"
        for page in doc:
            pix = page.get_pixmap(matrix=magnify)
            image_file = os.path.join(folder, page_txbox + f"_{str(page.number).zfill(4)}.{ext}")
            pix.save(image_file)
            text_box.insert('end', image_created_txbox + image_file + '\n')

        text_box.insert('end', task_completed_txbox + '\n')
        text_box.see('end')
        doc.close()
        text_box.config(state='disabled')

    except Exception as err:
        mb.showerror(msg_error_tx, str(err))

def quality_changed(event):
    mb.showinfo(quality_select_tx, you_selected_tx + f" {quality_var.get()} dpi!")

label_0 = tk.Label(janela2, text=select_dpi_txlabel, font=('Arial', 12), bg='lightyellow', foreground='orange4')
label_0.pack(pady=0)

quality_var = tk.StringVar()
quality_cb = Combobox(janela2, width=10, font=('Arial', 14), foreground='orange4', textvariable=quality_var)
quality_cb['values'] = ('30', '50', '72', '96', '120', '150', '300', '600')
quality_cb.current(2)
quality_cb.bind('<<ComboboxSelected>>', quality_changed)
quality_cb.pack(pady=10)

tk.Label(janela2, text=attention_res_txlabel_1, font=('Arial', 10), bg='lightyellow', foreground='orange4').pack(pady=0)
tk.Label(janela2, text=attention_res_txlabel_2, font=('Arial', 10), bg='lightyellow', foreground='orange4').pack(pady=0)

selec_convert = tk.Button(janela2, text=select_convert_txbutton, command=converter_imagem, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
selec_convert.pack(pady=10)

# ==================== EXTRAIR PÁGINAS ====================
def extrair_paginas(nome_do_arquivo, pagina_inicial, pagina_final):
    pdf_file = open(nome_do_arquivo, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()

    if pagina_inicial > pagina_final:
        mb.showerror(attention_error_1_tx, attention_error_2_tx)
        pdf_file.close()
        return None

    for i in range(pagina_inicial, pagina_final + 1):
        try:
            page = pdf_reader.pages[i - 1]
            pdf_writer.add_page(page)
        except IndexError:
            mb.showerror(attention_error_1_tx, attention_error_3_tx + f" {nome_do_arquivo}.")
            pdf_file.close()
            return None

    return pdf_writer, pdf_file

nome_do_arquivo = tk.StringVar()

def selecionar_pdf():
    text_box.config(state='normal')
    text_box.delete('1.0', 'end')
    nome_do_arquivo.set(fd.askopenfilename(title=select_pdf_tx, filetypes=[(pdf_filetype, "*.pdf")]))
    caminho = nome_do_arquivo.get()

    if caminho:
        text_box.insert('end', file_selected_txbox + caminho + '\n')
        Select_PDF.config(state='disabled')
        salvar_extracao.config(state='normal')
    else:
        text_box.insert('end', no_pdf_file_selected_txbox + '\n')
        text_box.config(state='disabled')
    text_box.config(state='disabled')

Select_PDF = tk.Button(janela3, text=select_pdf_txbutton, command=selecionar_pdf, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')

def validar_entrada(entrada):
    if entrada == "":
        return True
    try:
        return int(entrada) > 0
    except ValueError:
        return False

vcmd = janela3.register(validar_entrada)

tk.Label(janela3, text=first_page_txlabel, font=('Arial', 14, 'bold'), bg='lightyellow', foreground='orange4').place(relx=0.20, rely=0.4, anchor=tk.E)
pagina_inicial = tk.Entry(janela3, validate="key", validatecommand=(vcmd, '%P'), font=('Arial', 14), foreground='orange4', width=10)
pagina_inicial.place(relx=0.20, rely=0.4, anchor=tk.W)

tk.Label(janela3, text=last_page_txlabel, font=('Arial', 14, 'bold'), bg='lightyellow', foreground='orange4').place(relx=0.80, rely=0.4, anchor=tk.E)
pagina_final = tk.Entry(janela3, validate="key", validatecommand=(vcmd, '%P'), font=('Arial', 14), foreground='orange4', width=10)
pagina_final.place(relx=0.80, rely=0.4, anchor=tk.W)

def salvar_pdf():
    try:
        pag_in = int(pagina_inicial.get())
        pag_fim = int(pagina_final.get())
        resultado = extrair_paginas(nome_do_arquivo.get(), pag_in, pag_fim)

        if resultado is None:
            return

        pdf_writer, pdf_file = resultado

        novo_nome = fd.asksaveasfilename(
            title=save_page_range_txtitle,
            initialfile=initialfile_tx,
            filetypes=[(pdf_filetype, "*.pdf")],
            defaultextension=".pdf"
        )

        if novo_nome:
            if not novo_nome.lower().endswith(".pdf"):
                novo_nome += ".pdf"
            with open(novo_nome, 'wb') as novo_pdf_file:
                pdf_writer.write(novo_pdf_file)
            pdf_file.close()

            text_box.config(state='normal')
            text_box.insert('end', saved_to_txbox + novo_nome + '\n' + task_completed_txbox + '\n')
            text_box.see('end')
            text_box.config(state='disabled')

            salvar_extracao.config(state='disabled')
            Select_PDF.config(state='normal')
            pagina_inicial.delete(0, tk.END)
            pagina_final.delete(0, tk.END)
        else:
            text_box.config(state='normal')
            text_box.delete('1.0', 'end')
            text_box.insert('end', operation_canceled_txbox + '\n')
            text_box.config(state='disabled')
            salvar_extracao.config(state='disabled')
            Select_PDF.config(state='normal')
            pagina_inicial.delete(0, tk.END)
            pagina_final.delete(0, tk.END)
    except ValueError:
        mb.showerror(attention_error_1_tx, attention_error_4_tx)
    except Exception as err:
        mb.showerror(msg_error_tx, f"Ocorreu um erro:\n{err}")

salvar_extracao = tk.Button(janela3, text=save_as_txbutton, command=salvar_pdf, font=("Arial", 14, 'bold'), bg='white', foreground='orange4', state='disabled')

Select_PDF.pack(pady=10)
salvar_extracao.pack(pady=10)

# ==================== AGRUPADOR DE PDFs ====================
def select_files():
    global pdf_files
    text_box.config(state='normal')
    text_box.delete('1.0', 'end')
    files = fd.askopenfilenames(title=select_pdfs_tx, filetypes=[(pdfs_filetype, "*.pdf")])
    if files:
        pdf_files.clear()
        pdf_files.extend(files)
        for file in pdf_files:
            text_box.insert('end', file_selected_txbox + file + "\n")
        select_button.config(state='disabled')
        merge_button.config(state='normal')
    else:
        text_box.insert('end', no_pdfs_files_selected_txbox + '\n')
    text_box.config(state='disabled')

def merge_files():
    global pdf_files
    if not pdf_files:
        return
    merger = PdfMerger()
    for file in pdf_files:
        merger.append(file)

    save_file = fd.asksaveasfilename(
        title=save_merged_file_txtitle,
        initialfile=initialfile_tx,
        filetypes=[(pdf_filetype, "*.pdf")],
        defaultextension=".pdf"
    )

    if save_file:
        if not save_file.lower().endswith(".pdf"):
            save_file += ".pdf"
        merger.write(save_file)
        merger.close()
        text_box.config(state='normal')
        text_box.insert('end', saved_to_txbox + save_file + '\n' + task_completed_txbox + '\n')
        text_box.see('end')
        text_box.config(state='disabled')
        pdf_files.clear()
        merge_button.config(state='disabled')
        select_button.config(state='normal')
    else:
        text_box.config(state='normal')
        text_box.delete('1.0', 'end')
        text_box.insert('end', operation_canceled_txbox + '\n')
        text_box.config(state='disabled')
        merge_button.config(state='disabled')
        select_button.config(state='normal')

select_button = tk.Button(janela4, text=select_pdfs_txbutton, command=select_files, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
select_button.pack(pady=10)

merge_button = tk.Button(janela4, text=merge_pdf_files_txbutton, command=merge_files, state='disabled', font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
merge_button.pack(pady=10)

# ==================== ROTACIONADOR ====================
def select_file():
    global file_path
    text_box.config(state='normal')
    text_box.delete('1.0', 'end')
    file_path = fd.askopenfilename(title=select_pdf_tx, filetypes=[(pdf_filetype, "*.pdf")])
    if file_path:
        text_box.insert('end', file_selected_txbox + file_path + "\n")
        file_button.config(state='disabled')
        rotate_button.config(state='normal')
    else:
        text_box.insert('end', no_pdf_file_selected_txbox + '\n')
    text_box.config(state='disabled')

file_button = tk.Button(janela9, text=select_pdf_txbutton, command=select_file, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
file_button.pack(pady=0)

girar_label = tk.Label(janela9, text=rotate_page_list_txlabel, font=('Arial', 12), bg='lightyellow', foreground='orange4')
girar_label.pack(pady=0)
pages_entry = tk.Entry(janela9, font=('Arial', 12), bg='white', foreground='blue4')
pages_entry.pack(pady=0)

angle_label = tk.Label(janela9, text=rotate_angle_txlabel, font=('Arial', 12), bg='lightyellow', foreground='orange4')
angle_label.pack(pady=0)

angle_var = tk.StringVar()
angle_combobox = Combobox(janela9, textvariable=angle_var, state="readonly", width=10, font=('Arial', 14), foreground='orange4')
angle_combobox["values"] = (angle_90_degrees_tx, angle_180_degrees_tx, angle_270_degrees_tx)
angle_combobox.current(0)
angle_combobox.pack(pady=0)

def rotate_pages():
    global file_path
    pages = pages_entry.get().strip()
    angle_text = angle_var.get()

    if not file_path or not pages:
        text_box.config(state='normal')
        text_box.delete('1.0', 'end')
        text_box.insert('end', rotate_error_tx + '\n')
        text_box.config(state='disabled')
        return

    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        pages_list = []

        for item in pages.split(","):
            item = item.strip()
            if "-" in item:
                start, end = map(int, item.split("-"))
                pages_list.extend(range(start, end + 1))
            elif item.isnumeric():
                pages_list.append(int(item))
            else:
                raise ValueError

        pages_list = list(set(pages_list))

        angle_deg = 90 if angle_text == angle_90_degrees_tx else \
                    180 if angle_text == angle_180_degrees_tx else 270

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            if (i + 1) in pages_list:
                rotated = page.rotate(angle_deg)
                writer.add_page(rotated)
            else:
                writer.add_page(page)

        # Pergunta onde salvar
        save_file = fd.asksaveasfilename(
            title=save_merged_file_txtitle,
            initialfile=initialfile_tx,
            filetypes=[(pdf_filetype, "*.pdf")],
            defaultextension=".pdf"
        )

        if save_file:
            if not save_file.lower().endswith(".pdf"):
                save_file += ".pdf"
            with open(save_file, "wb") as output:
                writer.write(output)

            text_box.config(state='normal')
            text_box.insert('end', saved_to_txbox + save_file + '\n' + task_completed_txbox + '\n')
            text_box.see('end')
            text_box.config(state='disabled')

            file_button.config(state='normal')
            rotate_button.config(state='disabled')
            pages_entry.delete(0, tk.END)
            file_path = ""
        else:
            text_box.config(state='normal')
            text_box.delete('1.0', 'end')
            text_box.insert('end', operation_canceled_txbox + '\n')
            text_box.config(state='disabled')
            file_button.config(state='normal')
            rotate_button.config(state='disabled')
            pages_entry.delete(0, tk.END)
            file_path = ""

    except Exception as err:
        mb.showerror(msg_error_tx, f"Erro na rotação:\n{err}")
        file_button.config(state='normal')
        rotate_button.config(state='disabled')
        pages_entry.delete(0, tk.END)
        file_path = ""

rotate_button = tk.Button(janela9, text=rotate_page_txbutton, command=rotate_pages, state='disabled', font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
rotate_button.pack(pady=10)

# ==================== OCR ====================
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tesseract")

if sys.platform == "win32":
    tesseract = os.path.join(base_dir, "tesseract.exe")
elif sys.platform.startswith("linux"):
    tesseract = os.path.join(base_dir, "tesseract.AppImage")
else:
    tesseract = os.path.join(base_dir, "tesseract")

idiomas = {
    arabic_tx: 'ara', simpl_chinese_tx: 'chi_sim', english_tx: 'eng',
    french_tx: 'fra', greek_tx: 'ell', german_tx: 'frk', hebrew_tx: 'heb',
    hindi_tx: 'hin', italian_tx: 'ita', mathematics_tx: 'equ',
    portuguese_tx: 'por', russian_tx: 'rus', spanish_tx: 'spa', turkish_tx: 'tur'
}

def converter():
    try:
        text_box.config(state='normal')
        text_box.delete('1.0', 'end')

        arquivos = fd.askopenfilenames(
            title=select_images_tx,
            filetypes=(("JPGs", "*.jpg"), ("PNGs", "*.png"), ("GIFs", "*.gif"),
                       ("BMPs", "*.bmp"), (all_txopenfiles, "*.*"))
        )

        if not arquivos:
            text_box.insert('end', no_image_txbox + '\n')
            text_box.config(state='disabled')
            return

        text_box.insert('end', processing_files_txbox + '\n' + please_wait_txbox + '\n')
        destino = fd.askdirectory(title=askdirectory_txtitle)

        if not destino:
            text_box.delete('1.0', 'end')
            text_box.insert('end', operation_canceled_txbox + '\n')
            text_box.config(state='disabled')
            return

        lang_code = idiomas.get(combo.get(), 'por')   # garante código correto

        for arquivo in arquivos:
            text_box.insert('end', file_selected_txbox + arquivo + '\n')
            saida = os.path.join(destino, os.path.splitext(os.path.basename(arquivo))[0])
            subprocess.run([tesseract, arquivo, saida, "-l", lang_code, "pdf"], check=True)
            text_box.insert('end', saved_to_txbox + saida + '.pdf\n')

        text_box.insert('end', task_completed_txbox + '\n')
        text_box.see('end')
        text_box.config(state='disabled')

    except Exception as err:
        mb.showerror(msg_error_tx, f"Erro no OCR:\n{err}")
        text_box.config(state='disabled')

label_0 = tk.Label(janela5, text=img_lang_convert_txlabel, font=('Arial', 12), bg='lightyellow', foreground='orange4')
label_0.pack(pady=0)

combo = Combobox(janela5, width=14, font=('Arial', 14), foreground='orange4', values=list(idiomas.keys()))
combo.set(portuguese_tx)          # texto visível correto
combo.pack(pady=10)

botao_OCR = tk.Button(janela5, text=select_convert_txbutton, command=converter, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
botao_OCR.pack(pady=10)

def abrir_licenca():
    text_box.config(state='normal')
    text_box.delete('1.0', 'end')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "COPYING.txt"), "r", encoding="utf-8") as f:
        text_box.insert("1.0", f.read())
    text_box.config(state='disabled')

texto_licenca = (
    "Esse programa é um software livre: você pode redistribuí-lo e/ou modificá-lo sob os termos "
    "da Licença Pública Geral Affero GNU, conforme publicada pela Free Software Foundation, "
    "tanto a versão 3 da Licença, quanto qualquer versão posterior. Este programa é distribuído "
    "na esperança de que seja útil, mas SEM QUALQUER GARANTIA; sem sequer a garantia implícita "
    "de COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Clique no botão 'Licença' "
    "para ler a Licença Pública Geral Affero GNU."
)

label_0 = tk.Label(
    janela7,
    text=texto_licenca,
    font=('Arial', 12),
    bg='lightyellow',
    fg='orange4',
    justify='center',
    wraplength=500
)

label_0.pack(pady=15, padx=20, fill='x')

janela7.bind('<Configure>', lambda e: label_0.config(wraplength=e.width - 40))

license_button = tk.Button(janela7, text=license_txbutton, command=abrir_licenca, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
license_button.pack(pady=10)

def abrir_sobre():
    text_box.config(state='normal')
    text_box.delete('1.0', 'end')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"), "r", encoding="utf-8") as f:
        text_box.insert("1.0", f.read())
    text_box.config(state='disabled')

label_0 = tk.Label(janela8, text=about_title_txlabel_1, font=('Arial', 12), bg='lightyellow', foreground='orange4')
label_0.pack(pady=0)
label_1 = tk.Label(janela8, text=about_title_txlabel_2, font=('Arial', 12), bg='lightyellow', foreground='orange4')
label_1.pack(pady=0)

about_button = tk.Button(janela8, text=about_txbutton, command=abrir_sobre, font=("Arial", 14, 'bold'), bg='white', foreground='orange4')
about_button.pack(pady=10)

janela.mainloop()