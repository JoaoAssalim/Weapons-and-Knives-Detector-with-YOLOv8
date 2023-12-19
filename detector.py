from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, QThread, Signal, QCoreApplication, QPoint, Qt

import sqlite3
import sys
import cv2
import pygame
import time

from datetime import datetime
from ultralytics import YOLO
from yolov8 import YOLOv8

from ui.ui_arquivo import Ui_MainWindow
from ui.ui_register import Ui_Register

class VideoCapture:

    def __init__(self, camera):
        self.capture = cv2.VideoCapture(camera)

    def get_frame(self):
        ret, frame = self.capture.read()
        if ret:
            return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def release(self):
        self.capture.release()

class AlarmPlayer(QThread):
    def __init__(self):
        super(AlarmPlayer, self).__init__()

    def run(self):
        pygame.init()
        pygame.mixer.music.load("./assets/snd.mp3")  # Substitua pelo caminho do seu arquivo de áudio
        pygame.mixer.music.play()
        time.sleep(3)
        pygame.mixer.music.stop()
class ObjectDetectionThread(QThread):
    detection_completed = Signal(int, list)

    def __init__(self, index, video_capture, yolo_model):
        super(ObjectDetectionThread, self).__init__()
        self.index = index
        self.video_capture = video_capture
        self.yolo_model = yolo_model
        self.is_running = True
        self.labels = ['weapon', 'weapon']

    def run(self):
        while self.is_running:
            frame = self.video_capture.get_frame()

            if frame is not None:
                boxes, scores, class_ids = self.yolo_model(frame)

                if len(scores) > 0 and len(class_ids) > 0:
                    objects_detected = []

                    for item in range(len(scores)):
                        confidence = scores[item] * 100
                        cls = self.labels[class_ids[item]]

                        objects_detected.append((cls, confidence))
                        #print(f"Local: {self.video_capture} - {cls} - {datetime.strftime(datetime.today().date(), '%Y/%m/%d')} {str(datetime.today().time()).split('.')[0][:-3]}")

                    self.detection_completed.emit(self.index, objects_detected)

    def stop(self):
        self.is_running = False

class RegisterCameraWindow(QMainWindow, Ui_Register):
    
    def __init__(self, main_window):
        super(RegisterCameraWindow, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.main_window = main_window  # Store the reference to the MainWindow instance

        self.close_button.clicked.connect(self.on_close_button_clicked)
        self.min_sf.clicked.connect(self.on_minimize_button_clicked)
        self.register_2.clicked.connect(self.on_register_camera)

    def on_close_button_clicked(self):
        self.close()

    def on_minimize_button_clicked(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def on_register_camera(self):
        local = self.local_name.text()
        ip = self.camera_ip.text()

        # Update the database
        bd = sqlite3.connect('cameras.db')
        cursor = bd.cursor()
        cursor.execute('INSERT INTO registered_cameras (local, ip) VALUES (?, ?)', (local, ip))
        bd.commit()
        bd.close()

        self.main_window.handle_camera_registered()

        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    main2yolo_begin_sgl = Signal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.yolov8_detector = YOLOv8("./models/best.onnx", conf_thres=0.3, iou_thres=0.5)
        self.yolo_enabled = False

        self.bd = sqlite3.connect('cameras.db')
        self.bd.execute('CREATE TABLE IF NOT EXISTS registered_cameras (id INTEGER PRIMARY KEY, local TEXT, ip TEXT)')
        self.bd.close()

        self.cameras = []
        self.locais = []
        self.log_cameras = []
        self.activatedCameras = []
        self.indexCamera = 0
        self.alarm_playing = False
        self.alarm_player = AlarmPlayer()

        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.load_registered_cameras()

        self.dragging = False
        self.offset = QPoint()

        if len(self.cameras) > 0:
            self.local_info.setText(f"Local de identificação: {self.locais[self.indexCamera]}")
        else:
            self.local_info.setText(f"Local de identificação: Sem Local")

        self.close_button.clicked.connect(self.on_close_button_clicked)
        self.min_sf.clicked.connect(self.on_minimize_button_clicked)
        self.next_btn.clicked.connect(self.next_camera)
        self.prev_btn.clicked.connect(self.previous_camera)
        self.add_camera.clicked.connect(self.open_register_camera)

        if len(self.activatedCameras) > 0:
            self.video_capture = self.activatedCameras[self.indexCamera]
        else:
            self.video_capture = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33) 

        self.threads = []
        for index, video_capture in enumerate(self.activatedCameras):
            thread = ObjectDetectionThread(index, video_capture, self.yolov8_detector)
            thread.detection_completed.connect(self.handle_detection_result)
            self.threads.append(thread)
            thread.start()

    def handle_camera_registered(self):
        # Atualizar as listas e a interface do usuário
        self.load_registered_cameras()

        self.update_camera_threads()

    def update_camera_threads(self):
        # Atualizar as threads de detecção com as câmeras recém-ativadas
        for index, video_capture in enumerate(self.activatedCameras):
            if index >= len(self.threads):
                thread = ObjectDetectionThread(index, video_capture, self.yolov8_detector)
                thread.detection_completed.connect(self.handle_detection_result)
                self.threads.append(thread)
                thread.start()

    def load_registered_cameras(self):
        self.bd = sqlite3.connect('cameras.db')
        cursor = self.bd.cursor()
        cursor.execute('SELECT * FROM registered_cameras')
        data = cursor.fetchall()
        self.bd.close()

        self.cameras = [int(camera[2]) if camera[2].isdigit() else camera[2] for camera in data]
        self.locais = [camera[1] for camera in data]

        if len(self.cameras) > len(self.activatedCameras):
            for e, cam in enumerate(self.cameras):
                if e >= len(self.activatedCameras):
                    self.activatedCameras.append(VideoCapture(cam))
                    self.log_cameras.append([])

        if len(self.activatedCameras) == 1:
            self.indexCamera = 0
            self.video_capture = self.activatedCameras[self.indexCamera]
            self.local_info.setText(f"Local de identificação: {self.locais[self.indexCamera]}")
        
    def update_frame(self):
        if self.video_capture:
            frame = self.video_capture.get_frame()

            if frame is not None:
                # Update object localizer
                boxes, scores, class_ids = self.yolov8_detector(frame)
                combined_img = self.yolov8_detector.draw_detections(frame)

                # Display the image with detections
                height, width, channel = combined_img.shape
                bytes_per_line = 3 * width
                q_image = QImage(combined_img.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)
                self.video.setPixmap(pixmap)
            else:
                self.video.setPixmap(QPixmap())
                self.local_info.setText("Local de identificação: Sem Local")
                self.log.setPlainText("")
        else:
            self.video.setPixmap(QPixmap())
            self.local_info.setText("Local de identificação: Sem Local")
            self.log.setPlainText("")

    def next_camera(self):
        if len(self.activatedCameras) > 0:
            if self.indexCamera == len(self.activatedCameras) - 1:
                self.indexCamera = 0
            else:
                self.indexCamera += 1

            next_camera = self.activatedCameras[self.indexCamera]
            if isinstance(next_camera, VideoCapture):
                self.video_capture = next_camera
                self.local_info.setText(f"Local de identificação: {self.locais[self.indexCamera]}")
                current_log = ''.join(self.log_cameras[self.indexCamera])
                self.log.setPlainText(current_log)
            else:
                self.video_capture = None
                self.local_info.setText("Local de identificação: Sem Local")
                self.log.setPlainText("")
        else:
            self.video_capture = None
            self.local_info.setText("Local de identificação: Sem Local")
            self.log.setPlainText("")

    def previous_camera(self):
        if len(self.activatedCameras) > 0:
            if self.indexCamera <= 0:
                self.indexCamera = len(self.activatedCameras) - 1
            else:
                self.indexCamera -= 1

            prev_camera = self.activatedCameras[self.indexCamera]
            if isinstance(prev_camera, VideoCapture):
                self.video_capture = prev_camera
                self.local_info.setText(f"Local de identificação: {self.locais[self.indexCamera]}")
                current_log = ''.join(self.log_cameras[self.indexCamera])
                self.log.setPlainText(current_log)
            else:
                self.video_capture = None
                self.local_info.setText("Local de identificação: Sem Local")
                self.log.setPlainText("")
        else:
            self.video_capture = None
            self.local_info.setText("Local de identificação: Sem Local")
            self.log.setPlainText("")

    def play_alarm(self):
        if not self.alarm_playing:
            self.alarm_playing = True
            self.alarm_player.start()
            self.alarm_player.finished.connect(self.handle_alarm_finished)
    
    def handle_alarm_finished(self):
        self.alarm_playing = False

    def handle_detection_result(self, index, objects_detected):
        if objects_detected:
            log_text = f"Objects are detected: "
            for obj in objects_detected:
                log_text += obj[0] + ', '
            
            log_text = log_text[:-2] + f" - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
            self.log_cameras[index].append(log_text)
            self.indexCamera = index
            self.video_capture = self.activatedCameras[self.indexCamera]
            self.local_info.setText(f"Local de identificação: {self.locais[self.indexCamera]}")

            current_log = ''.join(self.log_cameras[self.indexCamera])
            self.log.setPlainText(current_log)

            scroll_bar = self.log.verticalScrollBar()
            scroll_bar.setValue(scroll_bar.maximum())
            
            # Chame play_alarm apenas se um alarme não estiver em andamento
            if not self.alarm_playing:
                self.play_alarm()

    def on_close_button_clicked(self):
        for thread in self.threads:
            thread.stop()

        for thread in self.threads:
            thread.wait()

        for video_capture in self.activatedCameras:
            video_capture.release()

        try:
            QCoreApplication.quit()
        except Exception as e:
            pass

    def on_minimize_button_clicked(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def open_register_camera(self):
        self.register_window = RegisterCameraWindow(self)

        self.register_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = MainWindow()
    Home.show()
    sys.exit(app.exec())