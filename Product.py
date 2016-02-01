class Product:
	null_set = ["UNK_NAME", "UNK_MAN", "UNK_FAMILY", "UNK_MODEL","UNK_DATE"]
	product_name = null_set[0]
	manufacturer = null_set[1]
	family = null_set[2]
	model = null_set[3]
	announced_date = [4]
	

	def toString(self):
		return self.product_name + " " + self.manufacturer + " " + self.family + " " + self.model + " " + self.announced_date
	def initializeValues(self, json_data):
		product_delimeter = ["product_name", "manufacturer", "family", "model", "announced-date"]
		if product_delimeter[0] in json_data:
			self.product_name = json_data[product_delimeter[0]]
		if product_delimeter[1] in json_data:
			self.manufacturer = json_data[product_delimeter[1]]
		if product_delimeter[2] in json_data:
			self.family = json_data[product_delimeter[2]]
		if product_delimeter[3] in json_data:
			self.model = json_data[product_delimeter[3]]
		if product_delimeter[4] in json_data:
			self.announced_date = json_data[product_delimeter[4]]	
