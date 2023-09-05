import base64


def decodeImage(img_string, file_name):
    imgdata = base64.b64decode(img_string)

    with open("./data/" + file_name, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(cropped_image_path):
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())
