import os, shutil

path = r"C:\Users\Bhuvan\Downloads"  # adjust path
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    ext = ext[1:]  # remove the dot
    if ext == "":
        continue
    folder = os.path.join(path, ext)
    if not os.path.exists(folder):
        os.makedirs(folder)
    shutil.move(os.path.join(path, file), os.path.join(folder, file))

print("Files organized successfully!")
