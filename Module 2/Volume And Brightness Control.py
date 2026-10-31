import cv2, numpy as np, mediapipe as mp, screen_brightness_control as sbc
from pynput import keyboard
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP
try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, 'GetDefaultOutputDevice') else AudioUtilities.GetSpeakers()
    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volctl.GetVolumeRange()[:2]
except Exception as e:
    print (f"Pycaw error: {e}"); exit()
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error opening video stream or file")
    exit()
WIN = "Volume and Brightness Control"; cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1); h, w = img.shape[:2]
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
