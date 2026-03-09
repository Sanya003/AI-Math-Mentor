import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text_from_image(uploaded_image):

    # Convert to PIL image
    image = Image.open(uploaded_image)

    # Convert to numpy array
    image_np = np.array(image)

    results = reader.readtext(image_np)

    texts = []
    confidences = []

    for bbox, text, conf in results:
        texts.append(text)
        confidences.append(conf)

    extracted_text = " ".join(texts)

    avg_conf = sum(confidences) / len(confidences) if confidences else 0

    return extracted_text, avg_conf