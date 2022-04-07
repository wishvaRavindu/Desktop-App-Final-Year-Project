import base64

import eel
import pathlib
# import upload
from openCamera import VideoCamera

template_folder_path :pathlib.Path = pathlib.Path(__file__).parent
template_folder_path :pathlib.Path = template_folder_path.joinpath('./web')
eel.init(template_folder_path)


window_Closed = False

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
def gen(camera):
    while True:
        print("times of call")
        if window_Closed:
            break
        frame = camera.get_frame()
        yield frame

@eel.expose()
def closeDetection():
    window_Closed = True
    exit_video = VideoCamera()
    exit_video.__del__()

@eel.expose()
def video_feed():
    x=VideoCamera()
    y = gen(x)
    for each in y:
        # Convert bytes to base64 encoded str, as we can only pass json to frontend
        blob = base64.b64encode(each)
        blob = blob.decode("utf-8")
        eel.updateImageSrc(blob)()
        # time.sleep(0.1)


eel.start('index.html',size=(900,700))