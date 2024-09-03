from PIL import Image

def resize(target_dir_path, holding_dir_path, file_path, size_mult):
    # print(dir_path + "\\" + file_path)
    try:
        image = Image.open(target_dir_path + "\\" + file_path)
        width, height = image.size
        new_width = round(width * size_mult)
        new_height = round(height * size_mult)
        new_image = image.resize((new_width, new_height))
        new_image.save(holding_dir_path + "\\" + file_path)
        print("Resized: " + file_path)
    except:
        print("Ran into an error, sorry :(")