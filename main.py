from flask import Flask, request, jsonify, url_for
from PIL import Image
from classifier import clasiffier_CNN_predict
from gfp_gan_api import predict_gfpgan_image
from image_functions import b64_2_img, im_2_b64, get_as_base64

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route('/getfilename', methods=['POST'])
def show_file_name():
    # get image filename
    get_file_img = request.files['filename']

    file_name = secure_filename(get_file_img.filename)

    full_file_name = "." + url_for("static", filename="images/" + file_name)

    #save PIL object filename attribute
    get_file_img.save(full_file_name)

    #open file as a PIL object and resize
    imgPILresized = Image.open(get_file_img).resize((512, 512))

    #Convert Image to b64
    img_b64 = im_2_b64(imgPILresized)

    #Enviar PIL Object al clasificador
    result_casiffier = clasiffier_CNN_predict(imgPILresized)

    #Enviar filename to gfp-gan
    predicted_gfpgan_image_url = predict_gfpgan_image(full_file_name)

    #convert url_gfp_gan_output to base64
    base64_predicted = get_as_base64(predicted_gfpgan_image_url)


    return jsonify({'status': 'base64 recibida correctamente', 'base64': img_b64, 'imageResult': result_casiffier, 'GFP-GAN': base64_predicted})


@app.route('/')
def index():
    return jsonify({"Test":"Hola"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
