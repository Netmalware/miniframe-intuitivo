import tkinter as tk


janela = tk.Tk()
janela.title("MiniFrame intuitivo com TKinter - Estudos")
janela.geometry("800x500")
janela.configure(bg="skyblue")


fundo_offset = 0
gravity = 1
velocity_y = 0
ground_level = 400
bola_radius = 15

arrastando = False
offset_x = 0
offset_y = 0


canvas = tk.Canvas(janela, width=800, height=500, bg="skyblue", highlightthickness=0)
canvas.pack(fill="both", expand=True)


campo = canvas.create_rectangle(0, ground_level, 800, 500, fill="green", outline="green")
sol = canvas.create_oval(600, 50, 700, 150, fill="yellow", outline="yellow")
nuvem1 = canvas.create_oval(100, 80, 200, 120, fill="white", outline="white")
nuvem2 = canvas.create_oval(300, 50, 450, 90, fill="white", outline="white")
nuvem3 = canvas.create_oval(500, 100, 620, 140, fill="white", outline="white")


bola_x = 400
bola_y = 100
bola = canvas.create_oval(bola_x - bola_radius, bola_y - bola_radius,
                          bola_x + bola_radius, bola_y + bola_radius,
                          fill="red", outline="black")


def animar():
    global fundo_offset, bola_y, velocity_y

    if not arrastando: 
        velocity_y += gravity
        bola_y += velocity_y

        if bola_y + bola_radius >= ground_level:
            bola_y = ground_level - bola_radius
            velocity_y = -velocity_y * 0.7
            if abs(velocity_y) < 2:
                velocity_y = 0

       
        canvas.coords(bola, bola_x - bola_radius, bola_y - bola_radius,
                             bola_x + bola_radius, bola_y + bola_radius)

  
    fundo_offset -= 2
    if fundo_offset <= -800:
        fundo_offset = 0

    canvas.coords(nuvem1, (100 + fundo_offset) % 800, 80, (200 + fundo_offset) % 800, 120)
    canvas.coords(nuvem2, (300 + fundo_offset) % 800, 50, (450 + fundo_offset) % 800, 90)
    canvas.coords(nuvem3, (500 + fundo_offset) % 800, 100, (620 + fundo_offset) % 800, 140)

    janela.after(20, animar)


def inicio_arraste(event):
    global arrastando, offset_x, offset_y


    mx, my = event.x, event.y

 
    if (bola_x - bola_radius) <= mx <= (bola_x + bola_radius) and (bola_y - bola_radius) <= my <= (bola_y + bola_radius):
        arrastando = True
        offset_x = bola_x - mx
        offset_y = bola_y - my

def durante_arraste(event):
    global bola_x, bola_y

    if arrastando:
        bola_x = event.x + offset_x
        bola_y = event.y + offset_y
        canvas.coords(bola, bola_x - bola_radius, bola_y - bola_radius,
                             bola_x + bola_radius, bola_y + bola_radius)

def fim_arraste(event):
    global arrastando, velocity_y

    if arrastando:
        arrastando = False
        velocity_y = 0  


canvas.bind("<ButtonPress-1>", inicio_arraste)
canvas.bind("<B1-Motion>", durante_arraste)
canvas.bind("<ButtonRelease-1>", fim_arraste)

animar()


janela.mainloop()
