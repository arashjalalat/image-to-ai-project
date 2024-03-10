from pytesseract import image_to_string
from openai import OpenAI
from dotenv import load_dotenv
import os
import cv2

load_dotenv() # Load .env file
os.environ['OPENAI_API_KEY']

# Image preparation with OpenCV
image = cv2.imread('newtonphilosophy.jpg')

# Returns image in grayscale format
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary image
th, dst = cv2.threshold(gray,180,255,cv2.THRESH_BINARY)

cv2.imwrite('result_newtonphilosophy.png', dst)

# Tesseract with custom psm config
custom_psm_config = r'--psm 4'
tesseract_response = image_to_string('result_newtonphilosophy.png', config=custom_psm_config)

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