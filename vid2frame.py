import cv2
import os

# Create a directory to save frames
output_directory = "frames"
os.makedirs(output_directory, exist_ok=True)

# Open the video file
video_path = "your_video.mp4"  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_count = 0

# Loop through the frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Save the frame as an image
    frame_filename = os.path.join(output_directory, f"frame_{frame_count:04d}.png")
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

    # Display the frame (optional)
    cv2.imshow("Frame", frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

print(f"Saved {frame_count} frames to {output_directory}")
