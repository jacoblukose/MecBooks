from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.my
global fl
fl=0
import gridfs
fs = gridfs.GridFS(db)

def upload(val):
	a=fs.put(val)
	b = fs.put(fs.get(a), filename ="one.pdf")
	out=fs.get(b)
	# print out.filename
	# print fs.get(a).read()
	 
def add_book(categoryname,bookname,choicelist,authorname):
	
	
	p=db.get_collection(categoryname)
	p.insert({"bookname" :bookname,"choices" :choicelist,"authorname":authorname})

	
	# db.np.insert({"hello" : "kname"})
	# print "inside func"
	# print type(np)
# def get_country(db,na):
	# return db.na.find_one()


# add_country(db,"network")

def check_book(missing_book):
	#funciton to search if searched book present in database
	categories=db.collection_names()
	for category in categories:
		p=db.get_collection(category)
		l=p.find({"bookname":missing_book})
		for items in l:
			# print "a"
			# print items["bookname"]
			return items["bookname"]


	return 0	 	

def di_collection():
	l=[]
	c=db.collection_names()
	for document in c:
		l.append(document)
		# print l
	return l	

def add_category(missing_category):
	#Function to check if "query" category is already present in database
	categories=db.collection_names(missing_category)
	if missing_category not in categories:
		db.create_collection(missing_category)
		print "collection not present"
		return 1
	else:
		print "Already collection present"
		return 0


def displaybook(query,flag):
	f=0
	c=db.collection_names()
	s=[]
	for document in c:
		if document!="missingbooks":
			p=db.get_collection(document)
			# cursor = db.restaurants.find({"borough": "Manhattan"})
			if flag == 1:
				l=p.find({"bookname":query})
				
				for items in l:
					# print "a"
					s.append(items)
					f=1		
				# print s
			elif flag == 0:
				# print "insi"
				l=p.find({"authorname":query})
				
				for items in l:
					s.append(items)
					# print s
					f=1
			else:
				if document == query:
					l=p.find()

					for items in l:
						# print items
						# print "a"
						s.append(items)
					f=1	
					print s
					# for items in s:
						# print items["bookname"]
	if f == 0:
		s=[]
		return s
		print "not found"
	else:
		return s


def counter(missing_book):
	# print missing_book
	l1=[]
	count=0
	c=db.collection_names()
	if "missingbooks" not in c :
		db.create_collection("missingbooks")	
	s=db.get_collection("missingbooks")
	for items in s.find({"bookname":missing_book}):
		print items
		# print "yoyo"
		count=1
		k=items['_id']
		l=items['countvalue']
		
		
	if count == 0:
		l=0
		s.insert({"bookname" :missing_book,"countvalue" :1})
	else:
		# s.update({ $inc: {countvalue:91}} )
		s.remove({"bookname" :missing_book,"countvalue" :l})  
		print "ssss"
		s.insert({"bookname" :missing_book,"countvalue" :l+1})
		# print missing_book
	if l >= 1 :
		return 1
	else:	
		return 0

def removecategory(query):
	c=db.collection_names()
	# print c
	c1=0
	for temp in c:
		# print temp
		# print query
		if query == temp:
			# print query
			p=db.get_collection(query)
			p.drop()
			c1=1
			break
	if c1:
		return 1
	else:
		return 0
def removebooks(query):
	print query
	print "isnide rempve book function"
	c=db.collection_names()
	for items in c:
		p=db.get_collection(items)
		for items1 in p.distinct("bookname"):
			# print items1
			if query == items1:
				q1 = '\"'
				print q1+query+q1
				p.remove({"bookname":q1+query+q1},1)

def missbooklist(count):
	p=[]
	c=db.get_collection("missingbooks")
	for i in c.find({"countvalue":{ "$gt": 1 }}):
		p.append(i["bookname"])
		print i["bookname"]

	return p