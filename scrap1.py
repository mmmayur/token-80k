import os
import shutil

def copy_only_py_files_flat(src_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.py'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)

                # Rename if there's a name conflict
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(file)
                    i = 1
                    while os.path.exists(os.path.join(dest_dir, f"{base}_{i}{ext}")):
                        i += 1
                    dest_file = os.path.join(dest_dir, f"{base}_{i}{ext}")

                shutil.copy2(src_file, dest_file)
                print(f"📁 Copied: {src_file} -> {dest_file}")



if __name__ == "__main__":
    source_directory = "C:\\Users\\mmmay\\Downloads\\python-main\\python-main"
    destination_directory = "C:\\Users\\mmmay\\Downloads\\token"

    copy_only_py_files_flat(source_directory, destination_directory)
    print("✅ Done copying .py files.")
