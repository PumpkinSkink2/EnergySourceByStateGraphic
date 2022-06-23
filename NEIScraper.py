from bs4 import BeautifulSoup

statelist = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']

def maniplist(sourcelist):
	temp_list = []
	for i in sourcelist:

		temp = i
		temp = str(temp).replace('[','')
		temp = temp.replace(']','')
		temp = temp.replace(']','')
		temp = temp.replace("'",'')
		temp = temp.split(',')
		temp_list.append(temp)

	return temp_list

def importHTML(html_file):
	"""imports an html file using BeautifulSoup"""
	with open(html_file, 'r', encoding = 'utf=8') as html_file:
		content = html_file.read()
		soup = BeautifulSoup(content,features="html.parser")
		return(soup)

def slice_List(sourcelist,stepsize):
	"""slices a list(sourcelist) into a stepsize. careful that your stepsize actually divides into the length of the list."""
	sliced_list = []
	listlen = int(round(len(sourcelist)/stepsize))

	for i in range(listlen):
		sliced_list.append(sourcelist[(i*stepsize):((i*stepsize)+stepsize):])
	return(sliced_list)

def getdata(source):
	"""cuts up data for a particular NEI table I wanted to look at"""
	db = source.find('tbody')
	db2 = db.get_text()
	db_list_raw = str(db2).split('\n')
	dud_list = []
	header = []

	length = len(db_list_raw)
	ind = 0

	while ind < length:
		if db_list_raw[ind] == '':
			dud_list.append(ind)
		ind += 1

	b = 0
	while b < len(dud_list):
		db_list_raw.pop((dud_list[b]-b))
		b += 1

	for i in range(10):
		header.append(db_list_raw[i])

	for j in range(10):
		db_list_raw.pop(0)

	db_list = slice_List(db_list_raw,10)

	db_list = maniplist(db_list)

	for i in db_list:
		for j in range(9):
			if '(' in i[j+1]:
				k = i[j+1]
				k = 0
				i[j+1] = k
				# k = i[j+1]
				# k = k.replace('(','-')
				# k = k.replace(')','')
				# i[j+1] = k
	for i in db_list:
		for j in range(9):
			i[j+1] = float((i[j+1]))

	for i in db_list:
		n = 0
		for j in range(9):
			n += int(10*(i[j+1]))
		n = (n/10)
		i.append(n)

	for i in db_list:
		if i[0] not in statelist:
			db_list.remove(i)

	return(db_list, header)



# source = importHTML('StateElectricityGenerationFuelShares.html')
# data = getdata(source)
# print(data)