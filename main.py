from flask import Flask, request, jsonify
from PIL import Image
import io
import base64

app = Flask(__name__)

# Definir una función para convertir la imagen a blanco y negro


def convert_to_bw(image_file):
    img = Image.open(image_file)
    img = img.convert('L')
    # Guardar la imagen en un buffer
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG')
    # Retornar la imagen procesada como string
    bw_img_raw = buffer.getvalue()
    bw_img_str = bw_img_raw.decode('latin-1')
    return bw_img_str


@app.route('/restoreImage', methods=['POST'])
def convert_image():
    image_file = request.files['image']
    bw_image = convert_to_bw(image_file)
    # print(bw_image_str)
    return jsonify({'status': 'imagen recibida correctamente', 'processed': bw_image})


@app.route('/getbase64', methods=['POST'])
def show_base64():
    # Decodificar la cadena de base64 a una imagen
    base64img = request.form['imageb64']
    # print("11111111111111 BASE 64 RECEIVED->", base64img)
    decoded_string = base64.b64decode(base64img)
    # print("22222222222222 BASE 64 Decoded ->", decoded_string)
    # Convertir la imagen a escala de grises
    imageBW = Image.open(io.BytesIO(decoded_string)).convert('L')
    # print("333333333333 Image BW CODE->", imageBW)
    # Codificar la imagen en base64 nuevamente
    bufferedImg = io.BytesIO()
    imageBW.save(bufferedImg, format="JPEG")
    base64BW = base64.b64encode(bufferedImg.getvalue()).decode('latin-1')
    # print("4444444444444 imagep b64->", base64BW)
    return jsonify({'status': 'base64 recibida correctamente', 'base64': base64img, 'base64P': base64BW})
    # return jsonify({'status': 'base64 recibida correctamente', 'base64': base64img})

@app.route('/')
def index():
    return jsonify({"Test":"Hola"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
