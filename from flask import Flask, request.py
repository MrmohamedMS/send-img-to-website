from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['image']
    image_data = image_file.read()

    # call the Python code that sends the image to the other website
    send_image_to_other_website(image_data)

    return 'Image uploaded successfully'

if __name__ == '__main__':
    app.run()
