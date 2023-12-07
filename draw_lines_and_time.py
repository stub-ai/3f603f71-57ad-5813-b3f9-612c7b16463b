import cv2
from moviepy.editor import VideoFileClip

def draw_lines_and_time(frame, t, fps):
    # Calculate time in seconds
    frame_number = frame.index  # Get the frame number
    t = frame_number / fps  # Calculate time in seconds

    # Draw the lines as before
    cv2.line(frame, (300, 0), (1080, 400), (0, 255, 255), thickness=2)
    cv2.line(frame, (500, 0), (500, 1080), (255, 255, 255), thickness=2)
    cv2.line(frame, (1500, 0), (1200, 1080), (0, 255, 255), thickness=2)

    # Convert time to mm:ss:cc
    milliseconds = int((t % 1) * 100)
    time_str = f'{int(t // 60):02d}:{int(t % 60):02d}:{milliseconds:02d}'

    # Set up text style
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255) # White
    line_type = 2
    position = (frame.shape[1] - 150, 50) # Top right corner

    # Draw time on the frame
    cv2.putText(frame, time_str, position, font, font_scale, font_color, line_type)

    return frame

def process_video(input_video_path, output_video_path, fps):
    clip = VideoFileClip(input_video_path)

    # Modify the line where draw_lines_and_time is called
    # Use 'fl' instead of 'fl_image' to be able to pass the time 't'
    modified_clip = clip.fl(lambda gf, t: draw_lines_and_time(gf(t), t, fps), apply_to=['mask', 'video', 'audio'])
    modified_clip.write_videofile(output_video_path, codec='libx264', fps=fps)

# Video paths
input_video_path = '/Volumes/EuropP25_23/Finales_Sesion_01/3_F_50_FR_SF1_Full Pool.mp4'
output_video_path = '/Volumes/EuropP25_23/Finales_Sesion_01/3_F_50_FR_SF1_Full Pool_ref.mp4'
fps = 50  # Make sure this matches your video's FPS

# Process the video
process_video(input_video_path, output_video_path, fps)