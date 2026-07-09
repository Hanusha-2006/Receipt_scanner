import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr import ocr_predict
from parser import parse_receipt

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 

def after_request(response):
    response.headers["Access-Control-Allow-Origin"]  = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

@app.route('/scan', methods=['POST', 'OPTIONS'])
def receipt_process():
    
    if request.method == 'OPTIONS':
        return jsonify({}), 200  
    
    if 'image' not in request.files:
        return jsonify({"error: No image if found upload the image "}), 400
    
    receipt = request.files['image']
    
    # Temporarily saving the image 
    image_path = "temp_save.jpg"
    receipt.save(image_path)
    
    #ocr processing the image
    text = ocr_predict(image_path)
    #parsing the text
    receipt_data = parse_receipt(text)
    
    os.remove(image_path)
    
    
    return jsonify(receipt_data)
    
    

# def print_receipt_data(receipt_data):
#     print("==========Receipt Summery ==========")
#     print(f"Store Name: {receipt_data['store_name']}")
#     print(f"Date: {receipt_data['date']}")
#     print(f"Time: {receipt_data['time']}")
#     print(f"Subtotal: {receipt_data['subtotal']}")
#     print(f"Total: {receipt_data['total']}")
#     print(f"Tax: {receipt_data['tax']}")
#     print()
    
    
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")