from flask import Flask, request, jsonify, blueprints
from sqlalchemy import true
from datetime import datetime 
import cv2
import pickle
import os
from index_image import convert_hash
from index_image import dhash
from pathlib import Path
import tempfile
 
 
app = Flask(__name__)

tree = pickle.loads(open('/home/duyminh/Documents/DACS5/Search_image/vptree.pickle', "rb").read())
hashes = pickle.loads(open('/home/duyminh/Documents/DACS5/Search_image/hash.pickle', "rb").read())

@app.route("/products/searchbyImage",methods=['POST'])
def searchByImage():
     result = []
     if request.method == 'POST':
        uploaded_file = request.files['filename']
        with tempfile.TemporaryDirectory() as td:
            temp_filename = Path(td) / 'uploaded_image_search'
            uploaded_file.save(temp_filename)
            image = cv2.imread(str(temp_filename))
            queryHash = dhash(image)
            queryHash = convert_hash(queryHash)
            results = tree.get_all_in_range(queryHash,20)
            results = sorted(results)
            print(results)
            for i,h in results:
               l ={}
               l = hashes.get(h)
               result.append(l)
            return jsonify(page =1,
                           error= False,
                           products= result)

            
   
if __name__ == "__main__":
    app.run(host='192.168.1.13',port=5000,debug=true)
   
    

