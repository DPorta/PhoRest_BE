from dotenv import load_dotenv
load_dotenv()
import replicate

def predict_gfpgan_image(filename):

    output = replicate.run(
        "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3",
        input={"img": open(filename, "rb")}
    )

    #print(output)
    return output

