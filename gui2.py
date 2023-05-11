# Khai bao thu vien
import PIL
from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, ttk, PhotoImage
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from threading import Thread
from ultralytics import YOLO
from yolov5 import *
from imutils.video import VideoStream

#Tao duong dan den thu muc luu anh va khoi chay model yolo
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Apphoctap\Code\Allcode\Giaodien\Main\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
modelyolov8 = YOLO("yolov8s-seg.pt")

#Khai bao bien dieu khien
stop = None
start = None
waitz=None

# Cac ham dieu khien nut nhan
def start_process():
    global stop
    global start
    stop = 0
    start = 1
    print("Start")
    if chosenet_cb.get() == 'None':
        video()
    if chosenet_cb.get() == 'YOLO V5':
        yolov5det()
    if chosenet_cb.get() == 'YOLO V8':
        print("yolov8")
        wait()
        print(waitz)
        wind()

#Khoi tao giao dien
def stop_dectect():
    global stop
    global start
    stop = 1
    start = 0


window = Tk()
window.geometry("1200x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    600.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    65.0,
    65.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=53.0,
    y=150.0,
    width=310.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=start_process,
    relief="flat"
)
button_2.place(
    x=53.0,
    y=285.0,
    width=310.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=stop_dectect,
    relief="flat"
)
button_3.place(
    x=53.0,
    y=360.0,
    width=310.0,
    height=60.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    692.0,
    80.0,
    image=image_image_3
)

# Tab
tab_control = ttk.Notebook(window, width=315, height=200)
tab_control.pack(expand=True)
tab_control.place(x=53,y=460)
tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_1, text='Wellcome')
tab_control.add(tab_2, text='Guide')
tab_control.add(tab_3, text='Info')

lbl1 = Label(tab_1)
ipimglb = Image.open(r'C:\Users\ngokh\Desktop\willdel\Main\build\assets\frame1\image_4.png')
img1 = ImageTk.PhotoImage(ipimglb)
lbl1.place(x=0, y=0)
lbl1.configure(image=img1)
lbl2 = Label(tab_2)
lbl2.place(x=0, y=0)
ipimglb2 = Image.open(r'C:\Users\ngokh\Desktop\willdel\Main\build\assets\frame1\image_5.png')
img2 = ImageTk.PhotoImage(ipimglb2)
lbl2.place(x=0, y=0)
lbl2.configure(image=img2)
lbl3 = Label(tab_3)
lbl3.place(x=0, y=0)
ipimglb3 = Image.open(r'C:\Users\ngokh\Desktop\willdel\Main\build\assets\frame1\image_6.png')
img3 = ImageTk.PhotoImage(ipimglb3)
lbl3.place(x=0, y=0)
lbl3.configure(image=img3)

# create a combobox
selected_net = tk.StringVar()
chosenet_cb = ttk.Combobox(window, font="Times 30", textvariable=selected_net, width=14)
chosenet_cb['values'] = ['None', 'YOLO V5', 'YOLO V8']
chosenet_cb['state'] = 'readonly'
chosenet_cb.current(0)
chosenet_cb.place(y=220, x=55)


# Thong bao khi chon mang nhan dien
def net_changed(event):
    showinfo(
        title='Result',
        message=f'You selected {selected_net.get()}!'
    )

chosenet_cb.bind('<<ComboboxSelected>>', net_changed)

# Lay hinh anh tu camera
rtsp_url = "rtsp://tapoadmin:Khongcomatkhau1@192.168.0.101:554/stream2"
cap = VideoStream(rtsp_url).start()


# Normal
def video():
    image = cap.read()
    image = cv2.resize(image, (820, 520))
    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = PIL.ImageTk.PhotoImage(image=img)
    canvas.imgtk = imgtk
    canvas.create_image(373, 160, anchor=NW, image=imgtk)
    if stop == 1 and start == 0:
        return
    window.after(1, video)


# YOLO V5
def yolov5det():
    image = cap.read()

    def yolov5t():
        detection = model(image)
        results = detection.pandas().xyxy[0].to_dict(orient="records")
        x = numpy.array(results)
        for result in results:
            # confidence = result['confident']
            name = result['name']
            clas = result['class']
            x1 = int(result['xmin'])
            y1 = int(result['ymin'])
            x2 = int(result['xmax'])
            y2 = int(result['ymax'])
            cv2.putText(image, name, (x1 + 3, y1 - 10), font, fontScale, color1, thickness, cv2.LINE_AA)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 4)
    t1 = Thread(target=yolov5t)
    t1.start()
    t1.join()
    showimage = cv2.resize(image, (820, 520))
    cv2image = cv2.cvtColor(showimage, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    canvas.imgtk = imgtk
    canvas.create_image(373, 160, anchor=NW, image=imgtk)
    if stop == 1 and start == 0:
        return
    window.after(1, yolov5det)


# YOLO V8
yolowin = ''

def wind():
    global yolowin
    global waitz
    yolowin = Toplevel(window)
    yolowin.geometry("820x520")
    yolowin.title("Instance segmentation")
    yolowin.resizable(False, False)

    btn2 = Button(yolowin, text="Close me",
                  command=windetroy )
    btn2.place(x=400, y=480)
    label = Label(yolowin)
    label.place(x=0, y=0)
    print(waitz)
    if waitz==1:
        # global yolowin
        def yolov8dect():
            _, frame = cap.read()
            result = modelyolov8(frame,classes=[0, 15, 16])
            showimage = result[0].plot()
            resized = cv2.resize(showimage, (820, 520))
            cv2image = cv2 .cvtColor(resized, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
            label.after(1, yolov8dect())
        yolov8dect()

def wait():
    global waitz
    waitz=1
    print(waitz)

def windetroy():
    global waitz
    waitz=0
    print(waitz)
    yolowin.destroy()



window.resizable(False, False)
window.mainloop()
