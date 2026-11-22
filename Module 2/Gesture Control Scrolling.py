import cv2
import mediapipe as mp
import pyautogui
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
SCROLL_SPEED = 300
SCROLL_DELAY = 1
CAM_WIDTH, CAM_HEIGHT = 640, 480
def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if landmarks.landmarks[tip].y < landmarks.landmarks[tip - 2].y:
            fingers.append(1)
    thumb_tip = mp_hands.HandLandmark.THUMB_TIP
    thumb_ip = mp_hands.HandLandmark.THUMB_IP
    if (handedness == 'Right' and landmarks.landmarks[thumb_tip].x > landmarks.landmarks[thumb_ip].x) or (handedness == 'Left' and landmarks.landmarks[thumb_tip].x < landmarks.landmarks[thumb_ip].x):
        fingers.append(1)
    return "scroll_up" if sum(fingers) == 5 else "scroll_down" if sum(fingers) == 0 else "no_scroll"
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)
last_scroll_time = p_time = 0
print ("Gesture Scroll Control Active\nOpen palm: Scroll Up\nFist: Scroll Down\nPress 'q' to exit")
while cap.isOpened():
    success, img = cap.read()
    if not success: break
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
    results = hands.process(img)
    gesture, handedness = "no_scroll", None
    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            handedness = hand_handedness.classification[0].label
            gesture = detect_gesture(hand_landmarks, handedness)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        if (time.time() - last_scroll_time) > SCROLL_DELAY:
            if gesture == "scroll_down":
                pyautogui.scroll(-SCROLL_SPEED)
                last_scroll_time = time.time()