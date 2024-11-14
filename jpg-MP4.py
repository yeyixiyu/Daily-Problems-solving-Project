from moviepy.editor import ImageSequenceClip
import os

def create_video_from_images(image_folder, output_video_path, fps=30):
    """
    将图片文件夹中的图片合成视频

    :param image_folder: 图片所在的文件夹路径
    :param output_video_path: 输出视频文件的路径
    :param fps: 视频的帧率（每秒显示的帧数），默认为24
    """
    # 确保图片文件夹存在
    if not os.path.isdir(image_folder):
        raise FileNotFoundError(f"指定的图片文件夹不存在: {image_folder}")

    # 获取图片文件夹中的所有图片文件名
    image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if
                   img.endswith(('.png', '.jpg', '.jpeg'))]

    # 确保至少有一张图片
    if not image_files:
        raise FileNotFoundError(f"在文件夹 {image_folder} 中没有找到任何图片文件。")

    # 创建视频剪辑
    clip = ImageSequenceClip(image_files, fps=fps)

    # 写入视频文件
    clip.write_videofile(output_video_path, codec='libx264')

if __name__ == "__main__":
    # 示例用法
    image_folder = 'E:/ProPainter/inputs/video_pre/self'  # 替换为你的图片文件夹路径
    output_video_path = 'E:/ProPainter/inputs/1.mp4'  # 替换为你希望输出的视频文件路径
    fps = 30  # 你可以根据需要调整帧率

    create_video_from_images(image_folder, output_video_path, fps)