import numpy
import torch
import cv2


# cap = cv2.VideoCapture(0)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')
# img = cv2.imread(r'C:\Users\dangm\Desktop\NCKH\pytorch_project\giaodien\build\anh1.jpg',1)
# results = model(img)
# detetion = model(img)
# results = detetion.pandas().xyxy[0].to_dict(orient = "record")
# x=results
# x = numpy.array(results)
# print(x)

# detection = yolo_model(cap)
#
# results = detection.pandas().xyxy[0].to_dict(orient = "record")
# x = numpy.array(results)
# print(x)
#
# for result in results:
#     confidence = result['confident']
#     name = result['name']
#     clas = result['class']

MARGIN=10
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
color1 = (0, 0 , 255)
thickness = 1
# while True:
#     success, img = cap.read()
#     detection = model(img)
#     results = detection.pandas().xyxy[0].to_dict(orient = "records")
#     x = numpy.array(results)
#     #print(x)
#
#     for result in results:
#         #confidence = result['confident']
#         name = result['name']
#         clas = result['class']
#         x1 = int(result['xmin'])
#         y1 = int(result['ymin'])
#         x2 = int(result['xmax'])
#         y2 = int(result['ymax'])
#         cv2.putText(img, name, (x1+3, y1-10), font, fontScale, color1, thickness, cv2.LINE_AA)
#         cv2.rectangle(img, (x1, y1), (x2, y2), color, 4)
#
#     cv2.imshow('yolo',img)
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break

