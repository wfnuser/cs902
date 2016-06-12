import Tkinter as tk
class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.frame_Light = tk.Frame(self, background="bisque") 
		self.frame_Light.pack(side="top", fill="both", expand=True) 
		self.light_on = True
		self.canvas = tk.Canvas(self.frame_Light) 
		self.canvas.create_oval(10, 10, 30, 30, fill="yellow", tags="light") 
		self.canvas.pack(side="top", fill="both", expand=True)
#	def draw_light(self):
#			if self.light_on: self.canvas.itemconfig("light", fill="blue")
				#self.light_on = False
#			    self.light_on = False
#				print "on"
#			else:
#				self.canvas.itemconfig("light", fill="red") 
#				self.light_on = True
#				print "of"
#			self.after(1000, self.draw_light)
if __name__ == "__main__": 
	app = App()
#	app.draw_light()
	app.mainloop()
