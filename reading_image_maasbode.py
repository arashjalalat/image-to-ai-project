from pytesseract import image_to_string
from openai import OpenAI
from dotenv import load_dotenv
import os
import cv2

load_dotenv() # Load .env file
os.environ['OPENAI_API_KEY']

# Image preparation with OpenCV
image = cv2.imread('maasbode.jpg')

# Returns image in grayscale format
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# define the contrast and brightness value
contrast = 1. # Contrast control ( 0 to 127)
brightness = 40. # Brightness control (0-100)

weighted = cv2.addWeighted(gray, contrast, gray, 0, brightness)

cv2.imwrite('result_maasbode.png', weighted)

# Tesseract with custom psm config
custom_psm_config = r'--psm 4'
tesseract_response = image_to_string('result_maasbode.png', config=custom_psm_config)

print(tesseract_response)

# OpenAI with JSON mode
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "Je bent een behulpzame assistent die JSON kan genereren."},
    {"role": "user", "content": f"Kan je een samenvatting geven van de volgende tekst? {tesseract_response}"}
  ],
  
)
print(response.choices[0].message.content)