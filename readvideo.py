import cv2
import os


def save_frames_as_images(video_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    frame_count = 0

    # 逐帧读取视频
    while True:
        ret, frame = cap.read()

        # 如果读取帧失败，则结束循环
        if not ret:
            break

        # 构造图像文件名
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")

        # 保存帧为图像文件
        cv2.imwrite(frame_filename, frame)

        # 打印进度信息
        print(f"Saved {frame_filename}")

        frame_count += 1

    # 释放视频捕获对象
    cap.release()
    print("Video processing completed.")

if __name__ == "__main__":

    video_path = 'E:/ProPainter/inputs/video_pre/11.mp4'  # 替换为你的视频文件路径
    output_folder = 'E:/ProPainter/inputs/object_removal/self'  # 替换为你希望保存图像的文件夹路径

    save_frames_as_images(video_path, output_folder)