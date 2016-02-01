import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Feature_Extractor:
	tag_set = ["PNAME", "MANFACT", "FAM", "MODEL", "DATE"]
	tags_pname = []
	tags_manfact = []
	tags_fam = []
	tags_model = []
	tags_date = []
	
	'''
	Extract tags from the Product properties.
	Invokes hashing of product property to the appropriate tag_tuple list for statistical calculation.
	@param product : Product.py instance
	'''
	def processProduct(self, product):
		print product.null_set
		if product.product_name not in product.null_set:
			self.tags_pname.append(self.hashContents(product.product_name))
		if product.manufacturer not in product.null_set:
			self.tags_manfact.append(self.hashContents(product.manufacturer))
		if product.family not in product.null_set:
			self.tags_fam.append(self.hashContents(product.family))
		if product.model not in product.null_set:
			self.tags_model.append(self.hashContents(product.model))
		if product.announced_date not in product.null_set:
			self.tags_date.append(self.hashContents(product.announced_date))
	'''
	Hashes the character value.
	@param argVal : String
	@Return : int
	'''
	def hashContents(self, argVal):
		counter = 1
		hashSum = 0
		for char in argVal:
			hashSum += ord(char) * counter
			counter += 1
		testStr = "hashed %d" % hashSum 
		print testStr
		return hashSum

	def plot(self, y_offset, list):
		
		for val in list:
			plt.plot([val], [y_offset], 'ro')
			plt.ylabel("tag")
			plt.xlabel("values")
		
	def draw(self):
		plt.show()
