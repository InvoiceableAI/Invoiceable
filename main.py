print('Importing modules...')
import flask
import os
from flask import Flask, render_template, request, session, redirect, url_for
from waitress import serve
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
import uuid
import tempfile
from PIL import Image
from transformers import pipeline
print('Starting pipeline...')
nlp = pipeline("document-question-answering", model="impira/layoutlm-document-qa")
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'tiff'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# https://mtyurt.net/post/2019/multipage-pdf-to-jpeg-image-in-python.html

def convert_pdf(file_path, output_path):
    # save temp image files in temp dir, delete them after we are finished
    with tempfile.TemporaryDirectory() as temp_dir:

        # convert pdf to multiple image
        images = convert_from_path(file_path, output_folder=temp_dir)

        # save images to temporary directory
        temp_images = []
        for i in range(len(images)):
            image_path = f'{temp_dir}/{i}.jpg'
            images[i].save(image_path, 'JPEG')
            temp_images.append(image_path)

        # read images into pillow.Image
        imgs = list(map(Image.open, temp_images))

    # find minimum width of images
    min_img_width = min(i.width for i in imgs)

    # find total height of all images
    total_height = 0
    for i, img in enumerate(imgs):
        total_height += imgs[i].height

    # create new image object with width and total height
    merged_image = Image.new(imgs[0].mode, (min_img_width, total_height))

    # paste images together one by one
    y = 0
    for img in imgs:
        merged_image.paste(img, (0, y))
        y += img.height

    # save merged image
    merged_image.save(output_path)

    return output_path
###
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/invoice', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        formdata = request.form
    else:
        formdata = request.args
    if request.method == 'POST':
        question = formdata['question']
        # check if the post request has the file part
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file and allowed_file(file.filename):
            fileid = str(uuid.uuid4())
            ext = str(file.filename.rsplit('.', 1)[1].lower())
            if (ext == 'pdf'):
                file.save(os.path.join('uploads', fileid + '.pdf'))
                filename = secure_filename(fileid + '.png')
                convert_pdf('uploads/' + fileid + '.pdf', 'uploads/' + filename)
                os.remove('uploads/' + fileid + '.pdf')
            else:
                filename = fileid + '.' + ext
                filename = secure_filename(filename)
                file.save(os.path.join('uploads', filename))
            answers = nlp('uploads/' + filename, question)
            if len(answers) == 0:
                os.remove(os.path.join(os.getcwd(), 'uploads/' + filename))
                return 'Sorry, I can\'t find the answer for that question. Please try again with a different document.'
            answer = answers[0]
            os.remove(os.path.join(os.getcwd(), 'uploads/' + filename))
            return 'I am ' + str(answer['score'] * 100) + '% sure that the answer is: ' + str(answer['answer']) + '.'
# {'score': 0.9943977, 'answer': 'us-001', 'start': 15, 'end': 15}

#            return redirect(url_for('upload', name=filename))

print('Server started!')
serve(app, host='0.0.0.0', port=2717)
