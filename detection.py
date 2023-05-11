from ultralytics import YOLO
import cv2
from tkinter import *
from tkinter import Tk, Canvas

from tkinter.ttk import Button, Label
from PIL import ImageTk, Image
from threading import Thread
import imutils
from imutils.video import VideoStream



window = Tk()
window.geometry("800x500+500+210")
window.title("yolov8")
window.configure(bg="#000000")
# canvas = Canvas(
#     window,
#     bg="#FFFFFF",
#     height=700,
#     width=1200,
#     bd=0,
#     highlightthickness=0,
#     relief="ridge"
# )

label = Label(
    window)
label.place(x=10, y=10)

model = YOLO("yolov8s-seg.pt")
# results = model("0",show=True,stream=True,conf= 0.7, classes=[0, 15, 16] )
# results = model("0",show=True,conf= 0.7, classes=[0, 15, 16] )
#
# def show_frame():
#     cv2.imshow("show", results)
# for result,frame in results:
#      cv2.imshow("show", frame)
rtsp_url = "rtsp://tapoadmin:Khongcomatkhau1@192.168.0.103:554/stream2"
cap = VideoStream(rtsp_url).start()
# results=model(0,show=True,device="0")
# cap=cv2.VideoCapture(0)
# def yolo():
#     frame = cap.read()
#     # print(frame[1].shape)
#     # wight= int(frame[1].shape[1]*1.3)
#     # height= int(frame[1].shape[0]*1.3)
#     # dim=(wight,height)
#     result = model(frame, classes=[0, 15, 16])
#     image = result[0].plot()
#     showimage = cv2.resize(image, (640, 630), interpolation=cv2.INTER_AREA)
#     cv2image = cv2.cvtColor(showimage, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     label.imgtk = imgtk
#     label.configure(image=imgtk)
#     # t2 = Thread(target=yolov8)
#     # t2.start()
#     # t2.join()
#     label.after(1, yolo)
    # canvas.create_image(350, 160, anchor=NW, image=imgtk)
    # show_frame()
    # key = cv2.waitKey(1)
    # if key == ord("q"):
    #     break

    # boxes = result[0].boxes.numpy()
    # for box in boxes:
    #     a = box.conf
# yolo()

def yolov8x():
    frame = cap.read()
    result = model(frame, classes=[0, 15, 16],conf=0.3)
    image = result[0].plot()
    showimage = cv2.resize(image, (780, 480), interpolation=cv2.INTER_AREA)
    cv2image = cv2.cvtColor(showimage, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # img = Image.fromarray(cv2image)
    # imgtk = ImageTk.PhotoImage(image=img)
    # canvas.imgtk = imgtk
    # canvas.create_image(0, 0, image=imgtk)
    label.after(1, yolov8x)
yolov8x()
window.resizable(False, False)
window.mainloop()
