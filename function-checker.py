#!/usr/bin/python3.4

if __name__ == "__main__":
	import argparse, csv


	def isFunction(relation):
		"""
		Returns True if parameter relation represents a function
		and False if it does not represent a function
		"""
		if len(relation) < 2:
			return False
		else:
			for key in relation.keys():
				if len(relation[key]) > 1:
					return False
		return True

	# parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", help="read data from csv file")
	args = parser.parse_args()

	# read data from csv file
	with open(args.filename, newline='') as csvfile:
		relation_reader = csv.reader(csvfile, delimiter=",")

		# build a relation using a dictionary
		try:
			relation = {}
			for row in relation_reader:
				if float(row[0]) not in relation.keys():
					relation[float(row[0])] = []
					relation[float(row[0])].append(float(row[1]))
				else:
					if float(row[1]) not in relation[float(row[0])]:
						relation[float(row[0])].append(float(row[1]))


			# output domain and range
			print("Domain\t\tRange")
			for domain_element in relation.keys():
				if len(relation[domain_element]) > 1:
					for item in range(len(relation[domain_element])):
						print("{domain_element}\t\t{range_element}".format(domain_element=domain_element, 
							range_element=relation[domain_element][item]))
				else:
					print("{domain_element}\t\t{range_element}".format(domain_element=domain_element, range_element=relation[domain_element][0]))


			# check if relation is a function
			if isFunction(relation):
				print("This relation represents a function.")
			else:
				print("This relation does not represent a function.")
		except ValueError as e:
			print(e)
			quit()
