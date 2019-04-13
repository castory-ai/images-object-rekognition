import boto3
from pprint import pprint
import image_helpers as ih

client = boto3.client('rekognition')
img_path = 'images/socket-background.jpg'
img_bytes = ih.get_image_from_file(img_path)
rek_resp = client.detect_labels(Image={'Bytes': img_bytes})

pprint(rek_resp)

print('Here is what I see in the image:\n')
for label in rek_resp['Labels']:
    print(label['Name'])
