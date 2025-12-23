from flask import Flask, render_template, request, redirect
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract\tesseract.exe"

#init the application
app=Flask(__name__,static_url_path="/static")

#creating get method with "/" routing
@app.route("/")
def index():
    return render_template("index.html")

#creating post method with "/" routing
@app.route("/", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    if file:
        #save the upload image
        image_path = "static/uploads/" + file.filename
        #perform OCR using Tesseract
        extracted_text = perform_ocr(image_path)
        return render_template("index.html",extracted_text=extracted_text, image_path=image_path)

def perform_ocr(image_path):
    #open the image using pillow
    image = Image.open(image_path)
    #now we are going to perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

#main function
if __name__=="__main__":
    app.run(debug=True)