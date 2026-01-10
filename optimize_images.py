from PIL import Image
import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            file_path = os.path.join(root, file)
            img = Image.open(file_path)
            file_name, ext = os.path.splitext(file_path)
            new_file_path = file_name + '.webp'
            img.save(new_file_path, 'webp')
          