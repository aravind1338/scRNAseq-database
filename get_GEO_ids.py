def main():
	geo_ID_dict = {}
	counter = 0
	with open("test.txt") as file:
		for line in file:
			counter += 1
			if "Series		Accession:" in line:
				terms = line.split(":")
				term_with_geo_ID = terms[1]
				term_with_geo_ID = term_with_geo_ID.strip()
				geo_ID = term_with_geo_ID.split("\t")[0]

				# Add the geo ID to the dictionary without repetition
				if geo_ID not in geo_ID_dict:
					geo_ID_dict[geo_ID] = counter

			elif "Series:" in line:
				terms = line.split(":")
				geo_ID = terms[2]
				geo_ID = geo_ID.rstrip("\n").strip()

				# Add the geo ID to the dictionary without repetition
				if geo_ID not in geo_ID_dict:
					geo_ID_dict[geo_ID] = counter


	"""for key in geo_ID_dict:
		# key is the GEO ID, value happens to be the line number on which it was found
		print (key, geo_ID_dict[key])"""

	with open ("geo_ids.txt", 'w') as f:
		for key in geo_ID_dict:
			f.write(key + "\n")



if __name__ == "__main__":
	main()