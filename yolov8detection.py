from ultralytics import YOLO
import cv2
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import torch

from PIL import Image, ImageTk

window = Tk()
window.geometry("900x506")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 506,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


lmain = Label(canvas)
lmain.place()


modelyolov8 = YOLO(r"C:\Users\dangm\Desktop\NCKH\pytorch_project\build\yolov8s-seg.pt")
capyolo8 = cv2.VideoCapture(0)


def video():
    _, frame = capyolo8.read()
    results = modelyolov8(frame)
    annotated_frame = results[0].plot()
    cv2image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video)

video()
window.resizable(False, False)
window.mainloop()
