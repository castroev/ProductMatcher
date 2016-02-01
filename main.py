from Product import Product
from Feature_Extractor import Feature_Extractor
import json

product_file = "products.txt"
listing_file = "listings.txt"
scan_product_f = open(product_file)
scan_listing_f = open(listing_file)
scan_product_sentinel = True
product_list = []

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

feature = Feature_Extractor()
for product in product_list:
	feature.processProduct(product)
feature.complete_preprocessing();
'''
#Plotting data analysis
feature.plot(10,feature.tags_pname)
feature.plot(20,feature.tags_manfact)
feature.plot(30,feature.tags_fam)
feature.plot(40,feature.tags_model)
feature.plot(50,feature.tags_date)
feature.draw()
'''
#scanner close
scan_product_f.close()
scan_listing_f.close()

