
from twilio.rest import Client
from PIL import Image
import cv2
from imutils.io import TempFile
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACdd30234c4c15bbc75f307b121bfc9d80'
auth_token = '998e56b102d3e36d2d8591356aeb8b01'
client = Client(account_sid, auth_token)
def send(image,name):
    tempImg = TempFile(ext = ".jpg")
    #img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "RGB")
    #img.save(tempImg.path)
    
    
    message = client.messages \
              .create(
#                  media_url=[image],
                  from_='whatsapp:+14155238886',
                  body=("*%s* sizi gozleyir" %name),
                  to='whatsapp:+994553541168')

    print(message.sid)
