# Hand_gesture_CV

A real-time computer vision project that allows users to control their system using hand gestures — like switching tabs, adjusting volume, and changing brightness — through the webcam using MediaPipe and OpenCV

#🚀 Features:
🖐 Hand tracking using MediaPipe
✌️ Peace sign → Switch browser tabs
👍 Thumbs up → Increase system volume
🖐 Open palm → Increase screen brightness
🤟 3 fingers up → Decrease brightness
Real-time gesture detection via webcam
Easy to extend for more gestures

#🧰 Tech Stack
1.Python 3
2.OpenCV
3.MediaPipe
4.pynput – for keyboard and volume control
5.screen_brightness_control – for brightness control

How It Works:
*Uses MediaPipe Hands to extract 21 hand landmarks.
*Analyzes finger positions to classify gestures.
*Triggers corresponding system actions using pynput and screen_brightness_control.

Gestures & Actions
👍 Thumbs Up -	Volume Up
✌️ Peace Sign	 - Switch Tab
🖐 Open Palm	- Brightness Up
🤟 3 Fingers Up	- Brightness Down

Acknowledgements
MediaPipe by Google
OpenCV
pynput
