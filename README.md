# Image to AI project

This project extracts text from an image with the Optical Character Recognition (OCR) engine Tesseract and uses OpenAI to interpret the text for different purposes. Before the text extraction the image is preprocessed with OpenCV to improve the text extraction process.

## Getting Started

### Installation

```sh
git clone git@github.com:arashjalalat/image-to-ai-project.git
cd image-to-ai-project
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Env file
Create an .env file in the root of the project and put your [OpenAI key](https://platform.openai.com/account/api-keys) in the file, e.g.: OPENAI_API_KEY=<your_key>

## Running the example

To run the program, use:

```sh
python3 reading_image_newton.py
python3 reading_image_maasbode.py
```

## Built With

- [Python](https://www.python.org/) - Programming language used
- [OpenCV](https://opencv.org/) - Open source computer vision library
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- OpenAI
