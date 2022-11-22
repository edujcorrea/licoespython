import tkinter as tkinter

Class Game(tk.Frame):
	def  __init__(self, master):
		super(Game, self).__init__(master)
		self.lives = 3
		self.width = 610
		self.height = 400
		self.canvas = tk.Canvas(self, bg='#aaaaff',
			width=self.width,
			height=self.height)
		slef.canvas.pack()
		slef.pack()

if __name__ == '__main__':
	root = tk.Tk()
	root.title(' Janela do Jogo!')
	game = Game(root)
	game.mainloop()
