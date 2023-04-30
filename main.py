from flask import Flask, request, jsonify
from PIL import Image
from classifier import clasiffier_CNN_predict
import tensorflow as tf
import io
import base64
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.config.set_visible_devices([],'GPU')

app = Flask(__name__)

@app.route('/getbase64', methods=['POST'])
def show_base64():
    # Decodificar la cadena de base64 a una imagen
    base64img = request.form['imageb64']

    decoded_string = base64.b64decode(base64img)



    #Convertir imagen a PIL Object
    imageBW = Image.open(io.BytesIO(decoded_string))
    imageBWresized = imageBW.resize((512, 512))

    #Enviar PIL Object al clasificador
    result_casiffier = clasiffier_CNN_predict(imageBWresized)

    # Codificar la imagen en base64 nuevamente
    bufferedImg = io.BytesIO()
    imageBWresized.save(bufferedImg, format="JPEG")
    base64BW = base64.b64encode(bufferedImg.getvalue()).decode('latin-1')

    return jsonify({'status': 'base64 recibida correctamente', 'base64P': base64BW, 'imageResult': result_casiffier})

@app.route('/')
def index():
    return jsonify({"Test":"Hola"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
