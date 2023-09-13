import cv2

# Function to dehaze a single frame (you should use your own dehazing function)
def dehaze_frame(frame):
    # Your dehazing code here
    return dehazed_frame

# Input video file path
input_video_path = 'input_video.mp4'

# Output video file path
output_video_path = 'output_video.mp4'

# Open the input video file
cap = cv2.VideoCapture(input_video_path)

# Get the video's width, height, and frames per second (fps)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# Define the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object to write the output video
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Process each frame in the input video
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Break the loop if we've reached the end of the video

    # Dehaze the frame using your dehazing function
    dehazed_frame = dehaze_frame(frame)  # Replace with your dehazing code

    # Write the dehazed frame to the output video
    out.write(dehazed_frame)

# Release video objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
