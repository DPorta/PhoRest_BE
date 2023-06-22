from dotenv import load_dotenv
load_dotenv()
import replicate

def predict_image_inpainting(filename):

    output = replicate.run(
        "microsoft/bringing-old-photos-back-to-life:c75db81db6cbd809d93cc3b7e7a088a351a3349c9fa02b6d393e35e0d51ba799",
        input={"image": open(filename, "rb"), "HR":True, "with_scratch": True}
    )

    return output