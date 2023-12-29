import cv2
from yolov8 import YOLOv8
import pywt

def detect_objects_in_photo(image_path):
    image = cv2.imread(image_path)
    yolo_model = YOLOv8("./models/best.onnx", conf_thres=0.5, iou_thres=0.5)

    boxes, scores, class_ids = yolo_model(image)
    result_image = yolo_model.draw_detections(image)
    result_path = "./imgs/NoWave/knife1.jpg"
    cv2.imwrite(result_path, result_image)

    return result_path

def detect_objects_in_video(video_path):
    yolo_model = YOLOv8("./models/best.onnx", conf_thres=0.3, iou_thres=0.5)
    video_capture = cv2.VideoCapture(video_path)
    width = int(video_capture.get(3))
    height = int(video_capture.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    result_video_path = "detected_objects_video2.avi"
    out = cv2.VideoWriter(result_video_path, fourcc, 20.0, (width, height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        boxes, scores, class_ids = yolo_model(frame)
        result_frame = yolo_model.draw_detections(frame)
        out.write(result_frame)
    video_capture.release()
    out.release()

    return result_video_path

photo_path = "./imgs/knife.jpg"
detect_objects_in_photo(photo_path)


def detect_objects_in_photo_wavelets(image_path, path_orig):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (640, 640))
    image_orig = cv2.imread(path_orig)
    yolo_model = YOLOv8("./models/best-wave.onnx", conf_thres=0.5, iou_thres=0.5)

    boxes, scores, class_ids = yolo_model(image)
    print(boxes, scores, class_ids)
    result_image = yolo_model.draw_detections(image_orig)
    result_path = "./imgs/Wave/knife4.jpg"
    cv2.imwrite(result_path, result_image)

    return result_path

photo_path_wave = "./imgs/pre/knife4.jpg"
photo_path_orig = "./imgs/knife4.jpg"
detect_objects_in_photo_wavelets(photo_path_wave, photo_path_orig)