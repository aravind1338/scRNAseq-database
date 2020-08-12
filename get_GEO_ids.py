def main():
	geo_ID_dict = {}
	counter = 0
	with open("gds_result.txt") as file:
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
				
				# Cases where the sample belongs to two different studies
				geo_ID = geo_ID.split(" ")
				if len(geo_ID) > 1:
					# more than one study
					for ID in geo_ID:
						# Add the geo ID to the dictionary without repetition
						if ID not in geo_ID_dict:
							geo_ID_dict[geo_ID] = counter

				else:
					# Add the geo ID to the dictionary without repetition
					if geo_ID[0] not in geo_ID_dict:
						geo_ID_dict[geo_ID] = counter


			if counter % 10000 == 0:
				print ("Finished %d lines" % counter)


	# Write GEO ID's to text file
	
	with open ("geo_ids.txt", 'w') as f:
		for key in geo_ID_dict:
			f.write(key + "\n")



if __name__ == "__main__":
	main()