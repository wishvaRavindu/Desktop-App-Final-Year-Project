import eel
import base64
import pathlib
from project_files.openCamera import VideoCamera

template_folder_path :pathlib.Path = pathlib.Path(__file__).parent
template_folder_path :pathlib.Path = template_folder_path.joinpath('./web')
eel.init(template_folder_path)

#getting data from the js file
@eel.expose()
def openCameraModule():
    print("open camera")
    # openCamera.openCameraFunction()

@eel.expose()
def showDetection():
    print("Show detection")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield frame

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


eel.start('index.html',size=(800,400))