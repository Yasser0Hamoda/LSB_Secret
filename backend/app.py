from flask import Flask, request, jsonify, send_file
import cv2
import os
from utils.LSB import LSB
from utils.encryption import crypto
from utils.compressor import compressor
from config import RESULT_IMAGE_FOLDER_PATH, SUPPORTED_IMAGE_TYPES

app = Flask(__name__)

# routes: Embed, Extract, (All_messages, Save_message)=>These will need database

def remove_image(image_path:str):
    if os.path.exists(image_path):
        os.remove(image_path)

@app.route("/Embed", methods=['POST'])
def embed():
    message = request.form.get('message')
    password = request.form.get('password')
    image = request.files.get('image')
    
    #checking the validation of the passed parameters
    if not image or not password or not message:
        return jsonify({
            'status':'fail',
            'reason':'missing parameters'
        }), 400
        
    #checking image type
    if image.filename.split('.')[-1] not in SUPPORTED_IMAGE_TYPES:
        return jsonify({
            'status':'fail',
            'reason':'unsupported image type'
        }), 400
        
    image_path=RESULT_IMAGE_FOLDER_PATH+image.filename
    image.save(image_path)
    saved_image=cv2.imread(image_path)
    if saved_image is None:
        return jsonify({
            'status':'fail',
            'reason':"Unable to load the image from the server"
        }), 400
        
    
    #checking the number of channels in the image
    if saved_image.shape[2] != 3:
        remove_image(image_path)
        return jsonify({
            'status':'fail',
            'reason':"Image's number of channels are not supported"
        }), 400
        
    #compress the message
    message=compressor.compress(message)
    if not message:
        remove_image(image_path)
        return jsonify({
            'status':'fail',
            'reason':'Unable to compress the message'
        }), 400
    
    #ecrypt the message
    message=crypto.encrypt(message)
    if not message:
        remove_image(image_path)
        return jsonify({
            'status':'fail',
            'reason':'Unable to encrypt the message'
        }), 400
    
    #hash the password
    password=crypto.hash_pass(password)
    
    #embeded the data inside the image
    final_image = LSB.embeddedMessage(message, saved_image, password)
    if final_image is None:
        remove_image(image_path)
        return jsonify({
            'status':'fail',
            'reason':'The Image can not hold the data'
        }), 400
        
    cv2.imwrite(image_path, final_image)

    # Return the file using send_file with the file path directly
    response = send_file(image_path, mimetype='image/' + image.filename.split('.')[-1].lower(), as_attachment=True, download_name=image.filename)

    # After sending the file, remove the image from disk
    # remove_image(image_path)
    
    return response, 200
 
if __name__=='__main__':
    app.run()
