import tkinter as tk

lives = 3

root = tk.Tk() #abre a janela Tkinter e atribiui o nome de root
frame = tk.Frame(root) # abre a janela Frame com nome da variavel frame
canvas = tk.Canvas(frame, width = 600, height = 400, bg = '#aaaaff') # abre a janela canvas com as especificações de largura, altura e cor

frame.pack() # empacota a janela de frame no root
canvas.pack() # empacota a janela de canvas dentro do frame e do root

root.title('Janela do Jogo') # da nome a janela do root

root.mainloop() # mantem a janela aberta em loop.