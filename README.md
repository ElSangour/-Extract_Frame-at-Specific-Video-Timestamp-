# Extract-Frame-at-Specific-Video-Timestamp
## Video Frame Extractor

Theses two script allows you to extract a specific frame from a video at a given timestamp and the other one allows you to extract all frames from a set of video in a specefic folder in your system.

### Requirements

- Python 3.x
- OpenCV

### Installation

To install OpenCV, you can use pip:

```bash
 pip install opencv-python
```

### Usage

Clone the Repository:
```bash
git clone https://github.com/yourusername/video-frame-extractor.git cd video-frame-extractor
```

Run the Script:
```bash
python extract_frame.py
pyhton extract_frames.py
```
### About extract_frame.py
#### Input the Video Path:

When prompted, enter the path to the video file. This can be an absolute or a relative path.

##### Examples of Paths:

Linux:
- Absolute Path: `/home/username/Videos/video.mp4`
- Relative Path: `../Videos/video.mp4`

Windows:
- Absolute Path: `C:/Users/username/Videos/video.mp4`
- Relative Path: `..\Videos\video.mp4`

macOS:
- Absolute Path: `/Users/username/Videos/video.mp4`
- Relative Path: `../Videos/video.mp4`

#### Enter the Timestamp:

Enter the timestamp in the format hh:mm:ss. For example, 00:02:30 for 2 minutes and 30 seconds.

Example:

bash Give me the path of the video that you want to extract a specific frame from it: /home/username/Videos/video.mp4

Enter timestamp in hh:mm:ss format: 00:02:30


Frame at 00h02m30s.jpg saved successfully as Frame_at_00h02m30s.jpg.

### Notes

- Ensure the video path is correct and the video file is accessible.
- The extracted frame will be saved in the same directory as the script with a filename indicating the timestamp.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
