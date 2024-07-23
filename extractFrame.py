import cv2

def extract_frame_from_video(video_path, timestamp):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error: Could not open video.")
        return

    fps = video.get(cv2.CAP_PROP_FPS)

    timestamp_list = timestamp.split(":")
    hh, mm, ss = timestamp_list
    timestamp_list_floats = [float(i) for i in timestamp_list]
    h, m, s = timestamp_list_floats

    frame_nb = h * 3600 * fps + m * 60 * fps + s * fps

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_nb)
    success, frame = video.read()

    if success:
        frame_filename = f'Frame_at_{hh}h{mm}m{ss}s.jpg'
        cv2.imwrite(frame_filename, frame)
        print(f"Frame at {hh}:{mm}:{ss} saved successfully as {frame_filename}.")
    else:
        print("Failed to extract frame.")

if __name__ == "__main__":
    video_path = input("Give me the path of the video that you want to extract a specific frame from it:\n")
    timestamp = input("Enter timestamp in hh:mm:ss format:\n")
    extract_frame_from_video(video_path, timestamp)
