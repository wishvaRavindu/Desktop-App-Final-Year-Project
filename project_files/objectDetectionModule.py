# this is the working file
import cv2 as cv
import time
import math
from pynput.keyboard import Key, Controller

frame_name = "detection_frame"


# converting the box values into pixel values.
def convert(img_size, box):
    (x_min, y_min) = (box[0], box[1])
    (w, h) = (box[2], box[3])
    x_max = x_min + w
    y_max = y_min + h

    x_center = float((x_min + x_max)) / 2 / img_size[1]
    y_center = float((y_min + y_max)) / 2 / img_size[0]

    w = float((x_max - x_min)) / img_size[1]
    h = float((y_max - y_min)) / img_size[0]

    x_center = round(x_center, 6)
    y_center = round(y_center, 6)
    w = round(w, 6)
    h = round(h, 6)

    return [x_center, y_center, w, h]


# def kalman_filter_prediction(cx,cy):
#     # Load Kalman filter to predict the trajectory
#     kf = KalmanFilter()
#     predict = kf.predict(cx,cy)
#
#     #predicting for another 2 steps
#     for i in range(2):
#         predict = kf.predict(predict[0],predict[1])
#
#     return predict

def write_to_txt(list_of_detection, frame_counter):
    f = open("./frames/Frame" + str(frame_counter) + ".txt", "a")
    for x in list_of_detection:
        separator = ","
        x = separator.join(map(str, x))
        # b = ' '.join(str(x).split(','))
        f.write(str(x) + "\n")
    f.close()
    list_of_detection.clear()


def get_frame(frame):
    ret, jpeg = cv.imencode('.jpg', frame)
    return jpeg.tobytes()


def exitDetections():
    keyboard = Controller()
    key = 'q'
    keyboard.press(key)

    keyboard.release(key)
    print("hello world")


def initateDetection():
    global label, color, cap, out
    frame_counter = 0
    anomaly_tracker = 0
    list_of_detection = []
    center_point_previous_point = []
    object_tracker = {}
    Conf_threshold = 0.6
    NMS_threshold = 0.4
    COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),
              (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    with open('obj.names', 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]

    weights_path = "./weights-file/yolov4-custom_3000.weights"
    net = cv.dnn.readNet(weights_path, './config-file/yolov4-custom.cfg')

    net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
    model = cv.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

    cap = cv.VideoCapture("./test_videos/test6.mp4")
    frame_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

    fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
    # cap.set(cv.CAP_PROP_FPS, 7)
    dim = (int(frame_width), int(frame_height))
    out = cv.VideoWriter('OutputVideo3.avi', fourcc, 30.0, dim)
    starting_time = time.time()

    while cap.isOpened():
        try:
            ret, frame = cap.read()
            height, width, _ = frame.shape
            result = frame[100:360, 120:640]
            frame_counter += 1
            if ret == False:
                break

            center_point = []

            frame = cv.resize(result, dim, interpolation=cv.INTER_AREA)
            frame_without_boxes = result
            classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)
            for (classid, score, box) in zip(classes, scores, boxes):
                color = COLORS[int(classid) % len(COLORS)]
                label = "%s : %f" % (class_name[classid], score)
                # getting the box values
                (x, y, w, h) = box
                # getting the center point of the boxes
                cx = int((x + x + w) / 2)
                cy = int((y + y + h) / 2)
                center_point.append((cx, cy))
                # adding the bounding box
                cv.rectangle(frame, box, color, 1)

                # kalman_filter_prediction_result = kalman_filter_prediction(cx,cy)

                if score > 0.6 and classid == 0:
                    # scale to pixel values
                    bb = convert((width, height), box)
                    bb.insert(0, classid)
                    list_of_detection.append(bb)
                    # the images will be saved into the frames folder
                    cv.imwrite('./frames/Frame' + str(frame_counter) + '.jpg', frame_without_boxes)

            # only at the start we compare the previouse and current framw
            if frame_counter <= 2:
                for point in center_point:
                    for point2 in center_point_previous_point:
                        distance = math.hypot(point2[0] - point[0], point2[1] - point[1])

                        if distance < 20:
                            object_tracker[anomaly_tracker] = point
                            anomaly_tracker += 1
            else:
                object_tracker_copy = object_tracker.copy()
                center_point_copy = center_point.copy()

                for anomaly_objects_id, point2 in object_tracker_copy.items():
                    anomaly_object_exist = False
                    for point in center_point_copy:
                        distance = math.hypot(point2[0] - point[0], point2[1] - point[1])
                        # updating the anomaly position
                        if distance < 20:
                            object_tracker[anomaly_objects_id] = point
                            anomaly_object_exist = True
                            if point in center_point:
                                center_point.remove(point)
                            continue

                    # remove the ids
                    if not anomaly_object_exist:
                        # get the location from this position where the id of the tracker will be removed
                        object_tracker.pop(anomaly_objects_id)

                # add new ids
                for point in center_point:
                    object_tracker[anomaly_tracker] = point
                    anomaly_tracker += 1

            for anomaly_id, point in object_tracker.items():
                display_text = label + ' (' + str(anomaly_id) + ')'
                cv.putText(frame, display_text, (point[0], point[1] - 7),
                           cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1)

            # writing to the file
            if len(list_of_detection) != 0:
                write_to_txt(list_of_detection, frame_counter)

            endingTime = time.time() - starting_time
            fps = frame_counter / endingTime
            # print(fps)
            cv.line(frame, (18, 43), (140, 43), (0, 0, 0), 27)
            cv.putText(frame, f'FPS: {round(fps, 2)}', (20, 50),
                       cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)
            cv.imshow('frame', frame)
            out.write(frame)

            # saves each frame will detection is being done

            # center point previous frame location
            center_point_previous_point = center_point.copy()
            if cv.waitKey(1) == ord('q'):
                print("the break command")
                break

        except KeyboardInterrupt:
            break

    cap.release()
    out.release()
    cv.destroyWindow(frame_name)

    # upload_project.main()
