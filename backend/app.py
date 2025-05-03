from flask import Flask, request, jsonify, send_file
import cv2
import os
from utils.LSB import LSB
from utils.encryption import crypto
from utils.compressor import compressor
from utils.helpers import gen_functionality, validator

app = Flask(__name__)

# routes: Embed, Extract, (All_messages, Save_message)=>These will need database

@app.route("/Embed", methods=['POST'])
def embed():
    message = request.form.get('message')
    password = request.form.get('password')
    image = request.files.get('image')
    
    #check the number of parameters    
    if len(request.form)+len(request.files) != 3:
        return jsonify({
            'status':'fail',
            'reason':'Invalid Number of Parameters'
        }), 400
    
    #checking the validation of the passed parameters
    if not image or not password or not message:
        return jsonify({
            'status':'fail',
            'reason':'missing parameters'
        }), 400
        
    #checking image type
    if not validator.supported_Type(image):
        return jsonify({
            'status':'fail',
            'reason':'unsupported image type'
        }), 400
        
    saved_image=gen_functionality.image_to_Mat(image)
    if saved_image is None:
        return jsonify({
            'status':'fail',
            'reason':"Unable to load the image from the server"
        }), 400
    
    #checking the number of channels in the image
    if not validator.supported_Number_Of_Channels(saved_image):
        return jsonify({
            'status':'fail',
            'reason':"Image's number of channels are not supported"
        }), 400
        
    #compress the message
    message=compressor.compress(message)
    if not message:
        return jsonify({
            'status':'fail',
            'reason':'Unable to compress the message'
        }), 400
    
    #ecrypt the message
    message=crypto.encrypt(message)
    if not message:
        return jsonify({
            'status':'fail',
            'reason':'Unable to encrypt the message'
        }), 400
    
    #hash the password
    password=crypto.hash_pass(password)
    
    #embeded the data inside the image
    final_image = LSB.embeddedMessage(message, saved_image, password)
    if final_image is None:
        return jsonify({
            'status':'fail',
            'reason':'The Image can not hold the data'
        }), 400
        
    saved_path=gen_functionality.saveMat(final_image, image.filename)

    # Return the file using send_file with the file path directly
    response = send_file(saved_path, mimetype='image/' + image.filename.split('.')[-1].lower(), as_attachment=True, download_name=image.filename)

    return response, 200

@app.route('/Extract', methods=['POST'])
def extract():
    total_param = len(request.form)+len(request.files)
    if total_param != 2:
        return jsonify({
            'status':'fail',
            'reason':'Invalid Number of Parameters'
        }), 400
    image = request.files.get('image')
    password=request.form.get('password')
    if not image or not password:
        return jsonify({
            'status':'fail',
            'reason':'Missing Parameters'
        }), 400
    #check from image type
    if not validator.supported_Type(image):
        return jsonify({
            'status':'fail',
            'reason':'unsupported image type'
        }), 400

    #save image in the server, load the image into np.ndarray object, and remove the saved image
    converted_image=gen_functionality.image_to_Mat(image)
    #! validating the image
    #check from image's number of channels
    if not validator.supported_Number_Of_Channels(converted_image):
        return jsonify({
            'status':'fail',
            'reason':"Image's number of channels are not supported"
        }), 400
    #check if the image holds any data in it
    if not validator.containting_message(converted_image):
        return jsonify({
            'status':'fail',
            'reason':"The Image Does Not Contain Any Message"
        }), 400
    #! Extracting the message
    #extract the compressed, encrypted message along side with hashed password
    extractedMessage, extractedPassword = LSB.extractMessage(converted_image)
    if extractedMessage is None or extractedPassword is None:
        return jsonify({
            'status':'fail',
            'reason':"The Image Does Not Contain Any Message"
        }), 400
    #compute the hash of the passed password, and compare the hashed passed password with the extracted hashed password 
    if crypto.hash_pass(password)!=extractedPassword:
        return jsonify({
            'status':'fail',
            'reason':"Wrong password"
        }), 400
    #decrypt the message
    extractedMessage=crypto.decrypt(extractedMessage)
    #decompress the message
    extractedMessage=compressor.decompress(extractedMessage)
    #return the original message
    return jsonify({
        'status':'success',
        'message':extractedMessage
    })

if __name__=='__main__':
    app.run()
