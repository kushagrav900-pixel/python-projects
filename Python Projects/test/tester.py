import tkinter as tk
import math

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

cx, cy = 200, 200      # Center
radius = 120

for i in range(10):
    angle = math.radians(180 * i / 9)  # 0° to 180°
    x = cx + radius * math.cos(angle)
    y = cy - radius * math.sin(angle)

    b = tk.Button(root, text=str(i))
    canvas.create_window(x, y, window=b)

root.mainloop()
