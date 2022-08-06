import socket, traceback


def calculateGPSValue(locationData):
    gpsFloat = float(locationData)
    gpsDeg = int(gpsFloat / 100)
    gpsMin = gpsFloat - gpsDeg * 100
    convertedValue = gpsDeg + (gpsMin / 60)

    return "{:.6f}".format(convertedValue)

def findGPSLocation():
    #needs to be altered
    host = '192.168.8.139'
    port = 5555
    finalList = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((host, port))

    print("connected....")

    while True:
        try:
            # address sents the IP address details while the message sents the GPS details
            message, address = s.recvfrom(8192)
            value = message.decode('utf8').replace(" ", "").split(",")
            # the values are taken from GNRMC
            print("data collected....", value)
            if value[0] == '$GNRMC' and value[2] == "A":
                # converting the latitude co-ordinates ddmm.mmmm to decimal degree(dd)
                latitudeInitialValue = value[3]
                longitudinalInitialValue = value[5]
                if value[4] == "S":
                    latitudeInitialValue = -latitudeInitialValue

                latitudeValue = calculateGPSValue(latitudeInitialValue)

                # converting the longitude co-ordinates ddmm.mmmm to decimal degree(dd)
                if value[6] == "W":
                    longitudinalInitialValue = -longitudinalInitialValue

                longitudinalValue = calculateGPSValue(longitudinalInitialValue)

            print("data collected....",value)
            if value[0] == "$GNGGA":
                finalList.append(latitudeValue)
                finalList.append(longitudinalValue)
                print("data saved......")
                return finalList

        except (KeyboardInterrupt, SystemExit):
            print("killing the system")
            # raise
        except:
            traceback.print_exc()


tracking = findGPSLocation()
print("value - ",tracking)
import socket, traceback


def calculateGPSValue(locationData):
    gpsFloat = float(locationData)
    gpsDeg = int(gpsFloat / 100)
    gpsMin = gpsFloat - gpsDeg * 100
    convertedValue = gpsDeg + (gpsMin / 60)

    return "{:.6f}".format(convertedValue)

def findGPSLocation():
    #needs to be altered
    host = '192.168.8.139'
    port = 5555
    finalList = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((host, port))

    print("connected....")

    while True:
        try:
            # address sents the IP address details while the message sents the GPS details
            message, address = s.recvfrom(8192)
            value = message.decode('utf8').replace(" ", "").split(",")
            # the values are taken from GNRMC
            print("data collected....", value)
            if value[0] == '$GNRMC' and value[2] == "A":
                # converting the latitude co-ordinates ddmm.mmmm to decimal degree(dd)
                latitudeInitialValue = value[3]
                longitudinalInitialValue = value[5]
                if value[4] == "S":
                    latitudeInitialValue = -latitudeInitialValue

                latitudeValue = calculateGPSValue(latitudeInitialValue)

                # converting the longitude co-ordinates ddmm.mmmm to decimal degree(dd)
                if value[6] == "W":
                    longitudinalInitialValue = -longitudinalInitialValue

                longitudinalValue = calculateGPSValue(longitudinalInitialValue)

            print("data collected....",value)
            if value[0] == "$GNGGA":
                finalList.append(latitudeValue)
                finalList.append(longitudinalValue)
                print("data saved......")
                return finalList

        except (KeyboardInterrupt, SystemExit):
            print("killing the system")
            # raise
        except:
            traceback.print_exc()


tracking = findGPSLocation()
print("value - ",tracking)
