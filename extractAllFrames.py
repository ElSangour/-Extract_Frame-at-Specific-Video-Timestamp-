import os
import cv2

def extract_all_frames_from_video(video_path, output_folder):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Error: Could not open video {video_path}.")
        return

    video_name = os.path.basename(video_path).split('.')[0]
    os.makedirs(output_folder, exist_ok=True)
    
    frame_count = 0
    success, frame = video.read()
    
    while success:
        frame_filename = os.path.join(output_folder, f'{video_name}_frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
        success, frame = video.read()
    
    print(f"Extracted {frame_count} frames from {video_path} to {output_folder}.")

def extract_frames_from_folder(input_folder, output_folder):
    for video_file in os.listdir(input_folder):
        video_path = os.path.join(input_folder, video_file)
        extract_all_frames_from_video(video_path, output_folder)

if __name__ == "__main__":
    base_path = "/yourpath"
    output_base_path = "/yourdesiredoutputpath"
    
    vol_videos_folder = os.path.join(base_path, "vol")
    non_vol_videos_folder = os.path.join(base_path, "nonVol")
    
  extract_frames_from_folder(vol_videos_folder, vol_images_folder)
