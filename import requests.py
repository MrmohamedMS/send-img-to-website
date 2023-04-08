import requests

# set the URL of the receiving website's 
url = 'https://example.com/receive-image'

# set the path of the image you want to send
image_path = '/path/to/your/image.jpg'

# read the image data as binary and send a POST request to the receiving website
with open(image_path, 'rb') as f:
    image_data = f.read()
    response = requests.post(url, data=image_data)
    
print(response.text)
