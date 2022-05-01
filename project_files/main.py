import base64

import eel
import pathlib
import cv2
import sys
import logging
import upload
import time
from openCamera import VideoCamera


def gen(camera,closeWindow):
    while True:

        if closeWindow:
            break

        frame = camera.get_frame()
        yield frame

    cv2.destroyAllWindows()
    time.sleep(5)
    # upload.main()
    sys.exit()


@eel.expose()
def closeDetection():
    print("the window should close now1")
    video_feed(True)

    # calling the main method for start uploading the frames into the cloud after detection is completed
    # upload.main()


@eel.expose()
def video_feed(closeWindow):
    x = VideoCamera()
    y = gen(x,closeWindow)

    for each in y:
        # Convert bytes to base64 encoded str, as we can only pass json to frontend
        blob = base64.b64encode(each)
        blob = blob.decode("utf-8")
        eel.updateImageSrc(blob)()
        # time.sleep(0.1)


def start_app():
    # Start the server
    try:
        template_folder_path: pathlib.Path = pathlib.Path(__file__).parent
        template_folder_path: pathlib.Path = template_folder_path.joinpath('./web')
        eel.init(template_folder_path)
        start_html_page = "index.html"
        logging.info("App Started")

        eel.start(start_html_page, port=8080, size=(900, 700))

    except Exception as e:
        err_msg = 'Could not launch a local server'
        logging.error('{}\n{}'.format(err_msg, e.args))
        # show_error(title='Failed to initialise server', msg=err_msg)
        logging.info('Closing App')
        sys.exit()


if __name__ == "__main__":
    start_app()

