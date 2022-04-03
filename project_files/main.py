import eel
import sys
import pathlib
import upload
import objectDetectionModule

from openCamera import VideoCamera


template_folder_path :pathlib.Path = pathlib.Path(__file__).parent
template_folder_path :pathlib.Path = template_folder_path.joinpath('./web')
eel.init(template_folder_path)

#getting data from the js file
# @eel.expose()
# def openCameraModule():
#     print("open camera")
#     # openCamera.openCameraFunction()
#
# @eel.expose()
# def showDetection():
#     print("Show detection")
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield frame

@eel.expose()
def initateAnomalyDetection():
    print("initate anomaly detection.....")
    objectDetectionModule.initateDetection()

@eel.expose()
def closeDetection():
    print("initiate method")
    objectDetectionModule.exitDetections()
    print("Exit detection..")


# @eel.expose()
# def video_feed():
#     x=VideoCamera()
#     y = gen(x)
#     for each in y:
#         # Convert bytes to base64 encoded str, as we can only pass json to frontend
#         blob = base64.b64encode(each)
#         blob = blob.decode("utf-8")
#         eel.updateImageSrc(blob)()
#         # time.sleep(0.1)


eel.start('index.html',size=(800,400))