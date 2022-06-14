
import cv2
from cv2 import sort
import matplotlib.pyplot as plt
import numpy as np
import vptree 
import os
import imutils as path
import os 
import pickle
import mysql.connector
def dhash(image, hashSize=8):
	# convert the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
	resized = cv2.resize(gray, (hashSize + 1, hashSize))

	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]

	# convert the difference image to a hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def convert_hash(h):
	# convert the hash to NumPy's 64-bit float and then back to
	# Python's built in int
	return int(np.array(h, dtype="float64"))

def hamming(a, b):
	# compute and return the Hamming distance between the integers
	return bin(int(a) ^ int(b)).count("1")
src = '/home/duyminh/Documents/DACS5/storage_product'
imagePaths = os.listdir(src)
hashes = {}
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ecommerce_app")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM product")
myresult = mycursor.fetchall()
 
# for index, tuple in enumerate(myresult):
# 	element_one = tuple[0]
# 	element_two = tuple[1]
# 	print(element_one, element_two)
for(i, results) in enumerate(myresult):
	image = cv2.imread(src +'/'+results[5].split("\\")[1])
	h = dhash(image)
	h = convert_hash(h)
	# update the hashes dictionary
	l = hashes.get(h, {})
	l['id']=results[0]
	l['product_name']=results[1]
	l['price']=results[2]
	l['quatity']=results[3]
	l['supplier']=results[4]
	l['image']=results[5]
	l['category']=results[6]
	hashes[h] = l	
 
points = list(hashes.keys())
tree = vptree.VPTree(points, hamming)
f = open('/home/duyminh/Documents/DACS5/Search_image/vptree.pickle', "wb")
f.write(pickle.dumps(tree))
f.close()
f = open('/home/duyminh/Documents/DACS5/Search_image/hash.pickle', "wb")
f.write(pickle.dumps(hashes))
f.close()
 

 