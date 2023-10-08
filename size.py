import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(file_path)
            except FileNotFoundError:
                pass
    return total_size

current_directory = os.getcwd()
os.chdir(os.path.dirname(current_directory))
file_sizes = []
for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)
    try:
        if os.path.isfile(item_path):
            size_bytes = os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            size_bytes = get_folder_size(item_path)
        if size_bytes >= 1e9:  # 1 GB
            size_str = f"{size_bytes / 1e9:.2f} GB"
        elif size_bytes >= 1e6:  # 1 MB
            size_str = f"{size_bytes / 1e6:.2f} MB"
        elif size_bytes >= 1e3:  # 1 KB
            size_str = f"{size_bytes / 1e3:.2f} KB"
        else:
            size_str = f"{size_bytes} bytes"
        file_sizes.append((item, size_str, size_bytes))
    except PermissionError as e:
        print(f"PermissionError: {e}")

file_sizes.sort(key=lambda x: x[2], reverse=True)
for item, size_str, _ in file_sizes:
    print(f"{item}: {size_str}")

total_size = sum(size for _, _, size in file_sizes)
if total_size >= 1e9:  # 1 GB
    total_size_str = f"{total_size / 1e9:.2f} GB"
elif total_size >= 1e6:  # 1 MB
    total_size_str = f"{total_size / 1e6:.2f} MB"
elif total_size >= 1e3:  # 1 KB
    total_size_str = f"{total_size / 1e3:.2f} KB"
else:
    total_size_str = f"{total_size} bytes"

if current_directory:
    print(f"Total size of current directory '{current_directory}': {total_size_str}")
else:
    print(f"Total size of current directory: {total_size_str}")
    
input("Press Enter to exit...")