import pytesseract
from PIL import Image
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# funcao pra abrir e processar a imagem
def abrir_imagem():
    arquivo = filedialog.askopenfilename(
        title="Escolha a imagem",
        filetypes=[("Arquivos de imagem", "*.png *.jpg *.jpeg *.bmp")]
    )

    if arquivo == "":
        return

    try:
        # abrindo a imagem
        img = Image.open(arquivo)
        
        # extraindo o texto
        texto_extraido = pytesseract.image_to_string(img, lang="por")

        # limpando a caixa de texto antes de inserir
        area_texto.delete("1.0", END)
        
        # colocando o texto extraido na caixa
        area_texto.insert("1.0", texto_extraido)

    except Exception as erro:
        messagebox.showerror("Erro!", f"Não foi possível processar a imagem:\n{erro}")

# criando a janela principal
root = Tk()
root.title("Extrator de Texto de Imagens")
root.geometry("700x450")

# botao para selecionar imagem
btn_selecionar = Button(
    root,
    text="📁 Escolher Imagem",
    command=abrir_imagem,
    font=("Arial", 11)
)
btn_selecionar.pack(pady=15)

# area onde o texto vai aparecer
area_texto = Text(root, wrap=WORD, font=("Courier", 10))
area_texto.pack(expand=True, fill=BOTH, padx=15, pady=10)

# rodando a aplicacao
root.mainloop()