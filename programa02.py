from asyncio import events
from ctypes import sizeof
import io
from optparse import Values
import os
from re import S
from tkinter import CENTER
from turtle import width
import PySimpleGUI as sg
from PIL import Image
import requests
from io import BytesIO
import urllib
from io import StringIO
from urllib.request import urlretrieve

def main():
    cont = 0
    # Layout da janela
    layout = [
        [sg.Image(key="-IMAGE-", size = (500,500))],
        [
            sg.Text("Arquivo de Imagem"),
            sg.Input(size=(25,1), key = "-FILE-"),
            sg.FileBrowse(file_types = [("JPEG (*.jpg)", "*.jpg"), ("Todos os arquivos", "*.*")]),
            sg.Button("Carregar Imagem"),
        ],
        [
            sg.Text("Nome do arquivo"),
            sg.Input(size=(10,1), key = "-FILENAME-"),
            sg.Text("Formato"),
            sg.Combo(["png", "jpeg", "jpg"], key="-COMBO-"),
            sg.Button("Salvar como Original"),
            sg.Button("Salvar como Thumbnail"),
            sg.Button("Salvar com Qualidade Reduzida"),

        ],
        [
            sg.Text("Largura"),
            sg.Input(size=(6,1), key = "-WIDTH-"),
            sg.Text("Altura"),
            sg.Input(size=(6,1), key = "-HEIGHT-")
        ],
        [
            sg.Text("Insira um endereço WEB"),
            sg.Input(size=(25,1), key = "-FILENAMEWEB-"),
            sg.Button("Salvar imagem WEB"),
            sg.Button("Mostrar WEB")
        ]
    ]

    # Crio nossa janela
    window = sg.Window("Visualizador de Imagem", layout = layout)
    
    # Looping principal
    while True:
        event, value = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        if event == "Carregar Imagem":
            arquivo = value['-FILE-']
            if os.path.exists(arquivo):
                image = Image.open(arquivo)
                image.thumbnail((500,500))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue(), size = (500, 500))

        # Se clicarmos no botão de salvar thumbnail
        if event == "Salvar como Thumbnail":
            # Pegamos o arquivo que selecionamos, através da caixa de texto
            arquivo = value['-FILE-']
            # Pego o nome que colocamos para o arquivo através da caixa de texto
            nome_arquivo = value["-FILENAME-"]
            # Adiciono 1 no contador. Serve para poder salvar vários arquivos.
            cont += 1
            # Se o caminho for verdadeiro
            if os.path.exists(arquivo):
                # Abro a imagem
                image2 = Image.open(arquivo)
                # Tranformo ela em 75, 75
                image2.thumbnail((75,75))
                # Salvo ela, e renomeio com o nome que colocamos
                image2.save(nome_arquivo+str(cont)+".jpg")
                # Confirmação visual de que foi salvo
                sg.popup("Imagem salva!")
            

        if event == "Salvar com Qualidade Reduzida":
            arquivo = value['-FILE-']
            nome_arquivo = value["-FILENAME-"]
            cont += 1
            if os.path.exists(arquivo):
                image3 = Image.open(arquivo)
                image3.save(nome_arquivo+str(cont)+".jpg", optimize = True, quality = 1)
                sg.popup("Imagem salva!")

        if event == "Salvar imagem WEB":
            urlv = value["-FILENAMEWEB-"]
            nome_arquivo = value["-FILENAME-"]
            cont += 1
            url = urlv
            urlretrieve(url, "imagem"+str(cont)+'.jpg')         
            image4 = Image.open("imagem"+str(cont)+'.jpg')
            image4.save(nome_arquivo+str(cont)+".jpg")
            sg.popup("Imagem salva!")
        
        if event == "Mostrar WEB":
            urlv = value["-FILENAMEWEB-"]
            url = urlv
            urlretrieve(url, "imagem"+str(cont)+'.jpg')
            image4 = Image.open("imagem"+str(cont)+'.jpg')
            bio = io.BytesIO()
            image4.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue(), size = (500, 500))

        if event == "Salvar como Original":
            arquivo = value['-FILE-']
            nome_arquivo = value["-FILENAME-"]
            formato = value["-COMBO-"]
            tamanho = (int(value['-WIDTH-']), int(value['-HEIGHT-']))
            cont += 1
            if os.path.exists(arquivo):
                image5 = Image.open(arquivo)
                image5 = image5.resize(tamanho)
                image5.save(nome_arquivo+str(cont)+"."+formato)
                sg.popup("Imagem salva!")

    window.close()

if __name__ == "__main__":
    main()

"""

                
"""