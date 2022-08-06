import pyrebase

def saveAnomalyLocations(rawlocation_data):
  #connecting to the firbase db
  firebaseConfig={
    'apiKey': "AIzaSyDa9913OZkNZCcuRy6T_fpTbaB-lAR3-so",
    'authDomain': "anomaly-location-data.firebaseapp.com",
    'databaseURL': "https://anomaly-location-data-default-rtdb.firebaseio.com/",
    'projectId': "anomaly-location-data",
    'storageBucket': "anomaly-location-data.appspot.com",
    'messagingSenderId': "999492609246",
    'appId': "1:999492609246:web:068b15e94e42b25b924e4f"
  }

  # configuring
  firebase = pyrebase.initialize_app(firebaseConfig)
  #accessing the real-time db
  db = firebase.database()

  #settingdata
  latitude_value = float(rawlocation_data[0])
  longitudinal_value = float(rawlocation_data[1])

  #sending data
  locValue = [{"latitude": latitude_value, "longitude": longitudinal_value}, ]
  db.push(locValue)
import pyrebase

def saveAnomalyLocations(rawlocation_data):
  #connecting to the firbase db
  firebaseConfig={
    'apiKey': "AIzaSyDa9913OZkNZCcuRy6T_fpTbaB-lAR3-so",
    'authDomain': "anomaly-location-data.firebaseapp.com",
    'databaseURL': "https://anomaly-location-data-default-rtdb.firebaseio.com/",
    'projectId': "anomaly-location-data",
    'storageBucket': "anomaly-location-data.appspot.com",
    'messagingSenderId': "999492609246",
    'appId': "1:999492609246:web:068b15e94e42b25b924e4f"
  }

  # configuring
  firebase = pyrebase.initialize_app(firebaseConfig)
  #accessing the real-time db
  db = firebase.database()

  #settingdata
  latitude_value = float(rawlocation_data[0])
  longitudinal_value = float(rawlocation_data[1])

  #sending data
  locValue = [{"latitude": latitude_value, "longitude": longitudinal_value}, ]
  db.push(locValue)
