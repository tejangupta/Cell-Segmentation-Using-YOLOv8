from flask import Flask, render_template, request, Response, jsonify
from flask_cors import CORS, cross_origin
from cellSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
import os
import shutil

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")

        opencodedbase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        shutil.rmtree("runs")
    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=80)  # For AZURE
