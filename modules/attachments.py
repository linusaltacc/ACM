import base64
import os
from apiclient import errors

from gmail import *
from modules.ocr import *

def get_attachment_data(mime_data):
  try:
        ocr_data = ""
        for part in mime_data.walk():  # iterate through mime data
            if part.get_content_type() == "image/png": # get content type == image 
                if part.get_filename() != None:  # get filename from mime
                    filename = part.get_filename()
                attachment_data = part.get_payload()  # get attachment data from mime
                file_data = base64.urlsafe_b64decode(attachment_data.encode('UTF-8'))  #decode
                path = ''.join(['./temp/', filename])  #save
                with open(path,'wb') as f:
                    f.write(file_data)
                f.close()
                # return text from image attachments
                import cv2  # for opening file
                import pytesseract  # ocr module 
                img = cv2.imread(path)
                ocr = pytesseract.image_to_string(img) 
                ocr_data+=ocr
                os.remove(path)  # remove files once ocr finished
        return ocr_data        
  except errors.HttpError as error:
        print('An error occurred: ', error)
# msg_id = get_message_id(service,user_id)[0]['id']
# print(get_attachment_data(mime_data))
