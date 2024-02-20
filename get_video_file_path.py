import os
import cv2

# Get the directory of the current Python script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to your video file within the 'video' folder
video_file_path = os.path.join(current_directory, 'data', 'roads_-_10812 (720p).mp4')

# Now you can use video_file_path to open your video file
# For example:
video = cv2.VideoCapture(video_file_path)
# Replace 'cv2.VideoCapture()' with the appropriate method for opening your video file

# Example of using video_file_path with cv2.VideoCapture():
import cv2
video = cv2.VideoCapture(video_file_path)
while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
