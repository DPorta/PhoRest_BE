from PIL import Image
from io import BytesIO
import base64
import requests

# Convert Image to Base64
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue()).decode('latin-1')
    return img_str

# Convert Base64 to Image
def b64_2_img(data):
    buff = BytesIO(base64.b64decode(data))
    return Image.open(buff)

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content).decode('latin-1')

def get_as_im(url):
    return Image.open(BytesIO(requests.get(url).content))