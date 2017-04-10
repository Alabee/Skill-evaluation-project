from list_display import list_return

def dict_response():
	skills_list = list_return()
	status = {}
	skills_number = len(skills_list)
	counter = 1
	status = {}
	for skill in skills_list:
		if  counter <= skills_number:
			counter += 1
			print("\nPlease answer with 'yes' or 'no'\nTask: %s \nComplete?" % skill)
			raw_feed_back = raw_input('Input feed back:\n')
			feed_back = raw_feed_back.upper()
			status[skill] = feed_back

	return status
