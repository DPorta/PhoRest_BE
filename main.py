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
    base64img = request.form['imageb64']
    print("BASE 64 ->", base64)
    decoded_string = base64.b64decode(base64img)
    image = Image.open(io.BytesIO(decoded_string)).convert('L')
    image.show()
    return jsonify({'status': 'base64 recibida correctamente', 'base64': base64img})


if __name__ == '__main__':
    app.run(debug=False)
