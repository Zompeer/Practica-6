import tkinter as TK
import threading as TH
import time
class Imagen:
    def __init__(self, x, y, canvas, ruta_imagen):
        self.__x = x
        self.__y = y
        self.__canvas = canvas
        self.__img = TK.PhotoImage(file=ruta_imagen)
        self.__imagen = canvas.create_image(x, y, anchor=TK.NW, image=self.__img)
        self.__ida = False
    def mover_horizontalmente(self):
        while True:
            if not self.__ida:
                if self.__x<500:
                    self.__x+=5
                else:
                    self.__ida = True
            else:
                if self.__x>0:
                    self.__x-=5
                else:
                    self.__ida = False
            self.__canvas.coords(self.__imagen, self.__x, self.__y)
            time.sleep(.01)
    def mover_verticalmente(self):
        while True:
            if not self.__ida:
                if self.__y<250:
                    self.__y+=5
                else:
                    self.__ida = True
            else:
                if self.__y>0:
                    self.__y-=5
                else:
                    self.__ida = False
            self.__canvas.coords(self.__imagen, self.__x, self.__y)
            time.sleep(.01)
    def img(self):
        return self.__imagen
        
raiz = TK.Tk()

canvas = TK.Canvas(raiz, width=1000, height=500)

img = Imagen(0,0, canvas, "homer.gif")
img1 = Imagen(200,200, canvas, "giphy.gif")

thread1 = TH.Thread(target = img.mover_horizontalmente)
thread1.daemon = True
thread1.start()

thread2 = TH.Thread(target = img1.mover_verticalmente)
thread2.daemon = True
thread2.start()

canvas.pack()
TK.mainloop()