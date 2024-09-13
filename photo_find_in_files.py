import os
import shutil


def merge_images(src_folder, dest_folder, record_file):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: {dest_folder}")

    with open(record_file, 'w', encoding='utf-8') as f:
        found_files = False
        for root, dirs, files in os.walk(src_folder):
            print(f"Scanning directory: {root}")  # 调试信息
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    found_files = True
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_folder, file)
                    try:
                        if os.path.exists(src_path):
                            shutil.copy(src_path, dest_path)
                            relative_path = os.path.relpath(root, src_folder)
                            f.write(f"{file} : {relative_path}\n")
                            print(f"Moved: {file} from {root} to {dest_path}")
                        else:
                            print(f"File not found during move: {src_path}")
                    except Exception as e:
                        print(f"Error moving {file} from {root} to {dest_path}: {e}")
        if not found_files:
            print("No image files found in the source folder.")


# 使用示例
src_folder = r"C:\Users\yuesen\Desktop\weiman"  # 源文件夹路径
dest_folder = 'C:\\Users\\yuesen\\Desktop\\destination_folder'  # 目标文件夹路径
record_file = 'C:\\Users\\yuesen\\Desktop\\record_file.txt'  # 记录文件路径

merge_images(src_folder, dest_folder, record_file)
