
import pprint
import sys
from apiclient.discovery import build
import urllib2
import simplejson
import pprint

# print out.filename


# For this example, the API key is provided as a command-line argument.
# api_key = sys.argv[1]
api_key="AIzaSyBaipdJ_GSGiORY4oS4sEhk5AuEYbeqjOQ"
# The apiclient.discovery.build() function returns an instance of an API service
# object that can be used to make API calls. The object is constructed with
# methods specific to the books API. The arguments provided are:
#   name of the API ('books')
#   version of the API you are using ('v1')
#   API key
service = build('books', 'v1', developerKey=api_key)

# The books API has a volumes().list() method that is used to list books
# given search criteria. Arguments provided are:
#   volumes source ('public')
#   search query ('android')
# The method returns an apiclient.http.HttpRequest object that encapsulates
# all information needed to make the request, but it does not call the API.

def googlebook_search(query):
	request = service.volumes().list(source='public',projection='lite', q=query,maxResults=1)
	# The execute() function on the HttpRequest object actually calls the API.
	# It returns a Python object built from the JSON response. You can print this
	# object or refer to the Books API documentation to determine its structure.
	respon = request.execute()




	#print(response)
	pprint.pprint(respon)
	booksnames=[] #initialisong a list obj in python
	desc=[]
	authorlist=[]
	k='%3A'
	import subprocess
	# Accessing the response like a dict object with an 'items' key returns a list
	# of item objects (books). The item object is a dict object with a 'volumeInfo'
	# key. The volumeInfo object is a dict with keys 'title' and 'authors'.
	# print 'Found %d books:' % len(response['items'])
	for book in respon.get('items', []):
	      # print 'Title: %s, Authors: %s' % ( book['volumeInfo']['title'],book['volumeInfo']['authors'])
	      if(book['volumeInfo']['authors']):
	      	z=0
	      	# print "Er"
	      else:
	      	z=0
	      	# print "Sdf"
	      booksnames.append(book['volumeInfo']['title'])      #list appending in python
	      # print "hola"
	      # # print booksnames
	      # if(book['volumeInfo']['authors']==None):
	      # 	authorlist.append("not available")	
	      authorlist.append(book['volumeInfo']['authors'])  
	      # desc.append(book['volumeInfo']['description'])
	      #print 'hello'
	      #print "Value : %s" %  book.items()
	      #print "Value : %s" %  book.keys()
	
		
	for i,k in enumerate(booksnames): #(for looping iin python )
	  # subprocess.call(['./mini.sh', str(i)])
	  # print booksnames[i],authorlist[i]
	  #print urllib2.quote(i) 


	  return booksnames,authorlist