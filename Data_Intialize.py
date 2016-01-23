from Product import Product
from Feature_Extractor import Feature_Extractor
import json

product_file = "products.txt"
listing_file = "listings.txt"
scan_product_f = open(product_file)
scan_listing_f = open(listing_file)
scan_product_sentinel = True
product_list = []
product_delimeter = ["product_name", "manufacturer", "family", "model", "announced-date"]

#LOOP INVARIANT:
#products.txt has unread products
while True:
	argData = scan_product_f.readline()
	if not argData:
		break # reached EOF
	json_data = json.loads(argData)
	tempProduct = Product()
	tempProduct.initializeValues(json_data)	
	product_list.append(tempProduct)
	print tempProduct.toString()
feature = Feature_Extractor()
feature.draw()

#scanner close
scan_product_f.close()
scan_listing_f.close()

