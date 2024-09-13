import os
import shutil


def restore_folders(record_file, images_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    with open(record_file, 'r', encoding='utf-8') as f:
        for line in f:
            file, original_path = line.strip().split(' : ')
            src_path = os.path.join(images_folder, file)
            dest_path = os.path.join(output_folder, original_path, file)
            try:
                if os.path.exists(src_path):
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy(src_path, dest_path)
                    print(f"Copied: {file} from {src_path} to {dest_path}")
                else:
                    print(f"Source file not found: {src_path}")
            except Exception as e:
                print(f"Error copying {file} from {src_path} to {dest_path}: {e}")


# 使用示例
record_file = r"C:\Users\yuesen\Desktop\record_file.txt"  # 记录文件路径
images_folder = r"D:\edgedownload\weiman_download"  # 包含所有图片的文件夹路径
output_folder = r"C:\Users\yuesen\Desktop\weiman1111"  # 输出文件夹路径

restore_folders(record_file, images_folder, output_folder)
