# Extrator de Texto de Imagens 📷✨

Aplicação simples em Python que extrai texto de imagens usando OCR (Reconhecimento Óptico de Caracteres).

## 📋 Descrição

Este projeto permite que você selecione uma imagem do seu computador e extraia todo o texto contido nela. Útil para digitalizar documentos, notas, capturas de tela e muito mais!

## 🚀 Funcionalidades

- Interface gráfica intuitiva
- Suporte para múltiplos formatos de imagem (PNG, JPG, JPEG, BMP)
- Reconhecimento de texto em português
- Extração rápida e eficiente

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Tkinter (interface gráfica)
- Pillow (processamento de imagens)
- Pytesseract (OCR)

## 📦 Instalação

1. Clone este repositório ou faça o download dos arquivos

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Instale o Tesseract OCR no seu sistema:

**Windows:**
- Baixe o instalador em: https://github.com/UB-Mannheim/tesseract/wiki
- Durante a instalação, anote o caminho de instalação
- Adicione o caminho ao PATH do sistema

**Linux (Ubuntu/Debian):**
```bash
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-por
```

**macOS:**
```bash
brew install tesseract
brew install tesseract-lang
```

## ▶️ Como Usar

1. Execute o programa:
```bash
python main.py
```

2. Clique no botão "📁 Escolher Imagem"

3. Selecione a imagem que deseja processar

4. O texto extraído aparecerá na área de texto

## 📝 Observações

- Para melhores resultados, use imagens com texto claro e legível
- Imagens com boa resolução geram melhores extrações
- O idioma padrão é português, mas pode ser alterado no código

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é livre para uso pessoal e educacional.