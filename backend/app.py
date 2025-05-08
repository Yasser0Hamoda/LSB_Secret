from flask import Flask, request, jsonify, send_file
from flask_jwt_extended import JWTManager,create_access_token, jwt_required, get_jwt_identity
from config import ENV_FILE_PATH
from dotenv import load_dotenv
import os
from app.utils.LSB import LSB
from app.utils.encryption import crypto
from app.utils.compressor import compressor
from app.utils.helpers import gen_functionality, validator
from app.db.quereis import queries

load_dotenv(ENV_FILE_PATH)

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')


jwt = JWTManager(app)
# routes: register, login, Embed, Extract, Get_all_messages, Save_message

@app.route('/register', methods=['POST'])
def register():
    if len(request.form) != 3:
        return jsonify({
            'status':'fail',
            'reason':'Invalid Number Of Parameters Parameters'   
        }), 400
        
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    passConfirm = request.form.get('pass_confirm')
    
    if not user_name or not password or not passConfirm:
        return jsonify({
            'status':'fail',
            'reason':'Missing Parameters'   
        }), 400
        
    if password != passConfirm:
        return jsonify({
            'status':'fail',
            'reason':'The Password and The Password Confirmation Do Not Match'
        }), 400
        
    password=password.strip()
    user_name=user_name.strip()
        
    res,msg=queries.add_user(user_name, password)
    if not res:
        return jsonify({
            'status':'fail',
            'reason':msg
        }), 400
        
    return jsonify({
        'status':'success',
        'message':msg
    })

@app.route('/login', methods=['POST'])
def login():
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    
    if len(request.form) != 2:
        return jsonify({
            'status':'fail',
            'reason':'Invalid Number Of Parameters'
        }), 400
        
    if not user_name or not password:
        return jsonify({
            'status':'fail',
            'reason':'Missing Parameters'
        }), 400
        
    user_name=user_name.strip()
    found,msg = queries.get_password(user_name)
    
    if not found:
        return jsonify({
            'status':'fail',
            'reason':msg
        }), 401
    
    if not crypto.hash_pass(password)==msg:
        return jsonify({
            'status':'fail',
            'reason':'Wrong User Name or Password'
        }), 401
    
    success,user_ID = queries.get_user_id(user_name)
    if success:
        return jsonify({
            'status':'success',
            'token': create_access_token(identity=str(user_ID))
        }), 200
        
    return jsonify({
        'status':'fail',
        'reason': 'Can Not Create Token'
    }), 500
        
@app.route("/Embed", methods=['POST'])
@jwt_required()
def embed():
    user_id = get_jwt_identity()
    #check the number of parameters    
    if len(request.form)+len(request.files) != 3:
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: Invalid Number of Parameters')
        return jsonify({
            'status':'fail',
            'reason':'Invalid Number of Parameters'
        }), 400
        
    message = request.form.get('message')
    password = request.form.get('password')
    image = request.files.get('image')
    
    #checking the validation of the passed parameters
    if not image or not password or not message:
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: missing parameters')
        return jsonify({
            'status':'fail',
            'reason':'missing parameters'
        }), 400
        
    #checking image type
    if not validator.supported_Type(image):
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: unsupported image type')
        return jsonify({
            'status':'fail',
            'reason':'unsupported image type'
        }), 400
        
    saved_image=gen_functionality.image_to_Mat(image)
    if saved_image is None:
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: Unable to load the image from the server')
        return jsonify({
            'status':'fail',
            'reason':"Unable to load the image from the server"
        }), 500
    
    #checking the number of channels in the image
    if not validator.supported_Number_Of_Channels(saved_image):
        queries.log_user_action(user_id, 'Embed Message', "The User Tryed to Embed Message but failed Due to: Image's number of channels are not supported")
        return jsonify({
            'status':'fail',
            'reason':"Image's number of channels are not supported"
        }), 400
        
    #compress the message
    message=compressor.compress(message)
    if not message:
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: Unable to compress the message')
        return jsonify({
            'status':'fail',
            'reason':'Unable to compress the message'
        }), 500
    
    #ecrypt the message
    message=crypto.encrypt(message)
    if not message:
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: Unable to encrypt the message')
        return jsonify({
            'status':'fail',
            'reason':'Unable to encrypt the message'
        }), 500
    
    #hash the password
    password=crypto.hash_pass(password)
    
    #embeded the data inside the image
    final_image = LSB.embeddedMessage(message, saved_image, password)
    if final_image is None:
        queries.log_user_action(user_id, 'Embed Message', 'The User Tryed to Embed Message but failed Due to: The Image can not hold the data')
        return jsonify({
            'status':'fail',
            'reason':'The Image can not hold the data'
        }), 400
        
    saved_path=gen_functionality.saveMat(final_image, image.filename)

    # Return the file using send_file with the file path directly
    response = send_file(saved_path, mimetype='image/' + image.filename.split('.')[-1].lower(), as_attachment=True, download_name=image.filename)

    queries.log_user_action(user_id, 'Embed Message', 'The User Embed The Message Successfully Into The Image','sucess')
    
    return response, 200

@app.route('/Extract', methods=['POST'])
@jwt_required()
def extract():
    user_id = get_jwt_identity()
    total_param = len(request.form)+len(request.files)
    if total_param != 2:
        queries.log_user_action(user_id, 'Extract Message', 'The User Tryed to Extract Message but failed Due to: Invalid Number of Parameters')
        return jsonify({
            'status':'fail',
            'reason':'Invalid Number of Parameters'
        }), 400
    image = request.files.get('image')
    password=request.form.get('password')
    if not image or not password:
        queries.log_user_action(user_id, 'Extract Message', 'The User Tryed to Extract Message but failed Due to: Missing Parameters')
        return jsonify({
            'status':'fail',
            'reason':'Missing Parameters'
        }), 400
    #check from image type
    if not validator.supported_Type(image):
        queries.log_user_action(user_id, 'Extract Message', 'The User Tryed to Extract Message but failed Due to: unsupported image type')
        return jsonify({
            'status':'fail',
            'reason':'unsupported image type'
        }), 400

    #save image in the server, load the image into np.ndarray object, and remove the saved image
    converted_image=gen_functionality.image_to_Mat(image)
    #! validating the image
    #check from image's number of channels
    if not validator.supported_Number_Of_Channels(converted_image):
        queries.log_user_action(user_id, 'Extract Message', "The User Tryed to Extract Message but failed Due to: Image's number of channels are not supported")
        return jsonify({
            'status':'fail',
            'reason':"Image's number of channels are not supported"
        }), 400
    #check if the image holds any data in it
    if not validator.containting_message(converted_image):
        queries.log_user_action(user_id, 'Extract Message', 'The User Tryed to Extract Message but failed Due to: The Image Does Not Contain Any Message')
        return jsonify({
            'status':'fail',
            'reason':"The Image Does Not Contain Any Message"
        }), 400
    #! Extracting the message
    #extract the compressed, encrypted message along side with hashed password
    extractedMessage, extractedPassword = LSB.extractMessage(converted_image)
    if extractedMessage is None or extractedPassword is None:
        queries.log_user_action(user_id, 'Extract Message', 'The User Tryed to Extract Message but failed Due to: The Image Does Not Contain Any Message')
        return jsonify({
            'status':'fail',
            'reason':"The Image Does Not Contain Any Message"
        }), 400
    #compute the hash of the passed password, and compare the hashed passed password with the extracted hashed password 
    if crypto.hash_pass(password)!=extractedPassword:
        queries.log_user_action(user_id, 'Extract Message', 'The User Tryed to Extract Message but failed Due to: Wrong password')
        return jsonify({
            'status':'fail',
            'reason':"Wrong password"
        }), 400
    #decrypt the message
    extractedMessage=crypto.decrypt(extractedMessage)
    #decompress the message
    extractedMessage=compressor.decompress(extractedMessage)
    #return the original message
    queries.log_user_action(user_id, 'Extract Message', 'The User Extracted The Message Successfully From The Image')
    return jsonify({
        'status':'success',
        'message':extractedMessage
    })

if __name__=='__main__':
    app.run()