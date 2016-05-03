#welcome to views page -django 

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from bloodbank.forms import *
#from login.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
#from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from bloodbank.models import *
from django.template import Context, Template
import subprocess
from django.http import HttpResponse
from mongoscript import *
from test import *
from django.contrib.auth.decorators import login_required
from googlebooks import *
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
import urllib2


# 2 variables declared outside all functions : used for global purposes.
global_query_variable=None
author_name=None
global curr_user
# global val
# val=[]
# global idn
# index funxtion servers starting of page 
def index(request): 
	#proxy = urllib2.ProxyHandler({'https':'http://mec:mec@192.168.0.4:3128'})
	# auth = urllib2.HTTPBasicAuthHandler()
	# opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	# urllib2.install_opener(opener)
	# url='https://www.google.com/search?complete=0&num=5&hl=en&complete=0&site=webhp&source=hp&q=network%20pdf&start=0'
	# req = urllib2.Request(url)
	# req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	# response = urllib2.urlopen(req)
	# # response = json.load(response)
	# response=response.read()
	# print response
	# print "he"
	# return HttpResponse(response)
	return render(request,'bloodbank/boot.html',)


def welcome(request):
 # global idn
 if 'idn' in request.session:	
	if request.method == 'GET' and request.session['idn']==request.session.session_key:
		m1=[]
		# print "inside get"
		# print request.session['id']
		m1=missbooklist(2)
		print m1
		m="POPULAR MISSING BOOKS"	
		context={'list2':m1,'list':m}
		
		return render(request,'bloodbank/search.html',context)
	else:
		if "addcat_submit_button" in request.POST:
			form=search_addcat_form(request.POST)
			p=request.POST.get('categoryname')
		
			
			
			if(add_category(p)):
				m="Searched book category you wish to add is beig added "
				context={'comment':m}		
				return render(request,'bloodbank/test.html',context)
				o=9
			else:
				m="Searched bookcategory you wish to add already present "
				context={'comment':m}		
				return render(request,'bloodbank/test.html',context)
				# return HttpResponse("Searched bookcategory you wish to add already present ")

		elif "uploadfile" in request.POST:
			 #print request.FILES
			 #form=fileupload(request.POST,request.FILES)
			 f=request.FILES['myfile']
			 # print f
			 upload(f)
			 # with open('/home/jake/django-user/mysit/bloodbank/a.txt','wb+') as destination:
				# for chunks in form.chunks():
				# destination.write(f.read())
		elif "remcategorynameat_submit_button" in request.POST:
			temp1=request.POST.get('remcategoryname')
			temp=removecategory(temp1)
			if temp:
				m="BOok category removed "
				context={'comment':m}		
				return render(request,'bloodbank/test.html',context)
			else:
				m="No such book category exists "
				context={'comment':m}		
				return render(request,'bloodbank/test.html',context)
		elif "rembook_submit_button" in request.POST:
			global p
			global global_query_variable
			global author_name
			temp1=request.POST.get('rembookname')	
			gb_bookname,gb_authorname=googlebook_search(temp1)
			global_query_variable=gb_bookname[0]
			removebooks(global_query_variable)
			return HttpResponse("REMOVE BOOK")
		else: 
			print "local"
			print request.POST
			form=search_addbook_form(request.POST)
			if form.is_valid():
				query=form.cleaned_data['bookname']
				  
				global p
				global global_query_variable
				global author_name
				
				gb_bookname,gb_authorname=googlebook_search(query)
				 #search query in google books
				
				global_query_variable=gb_bookname[0]
				
				p=check_book(global_query_variable)
				
				# print gb_bookname[0],gb_authorname[0][0]
				# global_query_variable=query
				author_name=gb_authorname[0][0]
				
				if(p):
					global_query_variable=None
					# print "inside dis"
					# print p
					return HttpResponse("Searched book %s already present " % p)
				else:
					# print str(query)
					# s=[]
					# s=di_collection()
					# context={'list':s[1:]}
					# if request.method == 'POST':
					# 	print "hello2"

					subprocess.call(['./mini.sh', str(query)])
					# 	# return HttpResponse("Searched book missing to be added")
					# 	return render(request,'bloodbank/drop.html',context)
					# 	# subprocess.call(['ls'])
					# else:
					# 	print "hello"
					return HttpResponseRedirect('/bloodbank/welcome/find')
			
			m="LANDED ON WRONG PAGE"
			context={'comment':m}		
			return render(request,'bloodbank/test.html',context)
			# return HttpResponse("Welcome to MEc bloodbank site")
	print "Dddddff"
 else:
	# print request.session['id']
	m="Not valid session "
	context={'comment':m}		
	return render(request,'bloodbank/test.html',context)
	# return HttpResponse("not valid sesison")

#def signup(request):
#template = loader.get_template('bloodbank/index.html')
#return HttpResponse("Welcome , to mec bloodbank ONLINE PORTAL ")
#return render(request,'bloodbank/index.html',)
link=[]
def passchange(request):
	# return HttpResponse("welcome to password changing")
	if request.method == 'GET':

		return render(request,'bloodbank/passchange.html')
	else:
		# form=pass_change(request.POST)

		global curr_user
		# print curr_userI
		user=curr_user
		print user
		print user.password
		temp=request.POST['passold']
		# password = user.cleaned_data.get('password', None)
		if check_password(temp, user.password):
			 print 'user password matches default password'
			 if request.POST['passnew1'] and request.POST['passnew2'] and request.POST['passnew1'] == request.POST['passnew2']:

				 u=User.objects.get(username__exact=user)
				 print request.POST['passnew1']
				 u.set_password(request.POST['passnew1'])
				 u.save()
				 print u.password
		else:
			m="Default password wrong "
			context={'comment':m}		
			return render(request,'bloodbank/test.html',context)

		


def find(request):
	if request.method == 'GET':
		form=categoryform()
		s=[]
		s=di_collection()
		link=links()
		print links
		# print link[2]
		form.fields['choices'].choices = [(x,x) for x in link]
		context={'list':s[1:],'list2':form}
		return render(request,'bloodbank/drop.html',context)
	else:
		
		form=categoryform(request.POST)
		# print request.POST
		l=[]
		l=request.POST.getlist('choices')
		s=request.POST.get('categoryname')
		# print p
		global global_query_variable
		global author_name
		add_book(s,global_query_variable,l,author_name)
		global_query_variable=None
		author_name=None
		# if form.is_valid():
		# print "SDf"
		# print form.cleaned_data['categoryname']
		# print form.cleaned_data['choices']
	
		# print form.get('choices')
		# for item in form.cleaned_data['choices']:
			# print item

		# add_collection(catname)
		m="The book has been added"
		context={'comment':m}		
		return render(request,'bloodbank/test.html',context)
		# return HttpResponse()

def logout(request):
	del request.session['idn']
	m="You have been logged out"
	context={'comment':m}		
	return render(request,'bloodbank/test.html',context)
	# return HttpResponse()

#@csrf_protect
def signup(request):    
	if request.method == 'GET':
#print 'ddd'
		return render(request,'bloodbank/rick.html',)
	else:								# If the form has been submitted...
		print request.POST
		form=CForm(request.POST) # A form bound to the POST data
		# print "ddd"
		try:
			if form.is_valid():		       
				print "ddd"
				c =Customer()
				print form.clean_password2
				if form.clean_password2()==0:
					m="Password mismatch "
					context={'comment':m}		
					return render(request,'bloodbank/test.html',context)
					# return HttpResponse("Password mismatch")
				else:
					c.password=form.cleaned_data['pass1']
					p= User.objects.create_user(
				username=form.cleaned_data['firstname'],
				first_name=form.cleaned_data['firstname'],
				password=form.cleaned_data['pass1'],
				last_name=form.cleaned_data['lastname'])
					# c.age=form.cleaned_data['age']
					# ;c.email=form.cleaned_data['email']
					c.user=p
					c.save()
					return HttpResponseRedirect('/bloodbank/login')
			else:
					return HttpResponse("Fields missing")
		except IntegrityError as e:
			m="Username already exists"
			context={'comment':m}		
			return render(request,'bloodbank/test.html',context)

			# return HttpResponse()
			#return render_to_response("signup.html",{"message": e.message})


def login_new(request):
	if request.method == 'GET':
		return render(request,'bloodbank/login.html',)
	else:
		# print request.POST
		

		if "yoyo" in request.POST:
			form=searchbookform(request.POST)
			flag2=-1
			if form.is_valid():
				option=form.cleaned_data['yoyi']
				searchquery=form.cleaned_data['queryname']
				if option != "categories":
					
					gb_bookname,gb_authorname=googlebook_search(searchquery)
				else:
					o=0
				m=[]
				print m
				print "identification"
				
				if option == "authorname":
					# print "SDf"
					searchquery=gb_authorname[0][0]
					# print searchquery
					flag2=0
					m=displaybook(searchquery,0)
					# print m	
				elif option == "bookname":
					flag2=1
					searchquery=gb_bookname[0]
					print searchquery
					print "inside booksearch"
					m=displaybook(searchquery,1) 
				else:
					m=displaybook(searchquery,2)
					# return HttpResponse("category search")
				pp=[]
				p1=[]
				p2=[]
				if m==[]:
					print "isnide m=[]"
				else:
					print "inside m!=[]"

					for items in m:
						# print items
						# print "inside func for displaybook"
						# print items
						pp.append(items['choices'])
						p1.append(items['bookname'])
						p2.append(items['authorname'])
						# print pp
				
				if pp == [] and flag2==1:
					
					# print "inside"
					temp2=counter(searchquery)
					if temp2!= 0:
						# global val
						# val.append(temp2)
						# print val
						m="Searched book will be added shortly"
						context={'comment':m}		
						return render(request,'bloodbank/test.html',context)
						# return HttpResponse("Searched book will be added shortly")
					else:
						m="Searched book missing"
						context={'comment':m}		
						return render(request,'bloodbank/test.html',context)
						# return HttpResponse("Searched book missing")
				else:
					context={'list':pp,'list2':p1,'list3':p2}
					# print "LL"
					return render(request,'bloodbank/disp.html',context) 

			# print "hihi"
			return HttpResponse("hooolahhhh vada mone")
		else:
			form=Lform(request.POST)
			# print request.POST
			# print request.session.session_key
			# print request.session.session_key
			
			if form.is_valid():
				username = form.cleaned_data['firstname']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				
				# print "insrde login"

				request.session['idn']=request.session.session_key
				
				if user is not None :
					if user.is_active:
						# request.session.set_expiry(0)
						print request.session['idn']
						# print user.objects.all()
						login(request,user)
						global curr_user
						curr_user=user
						# print "user foudn"
						# print request.user.last_name
					return HttpResponseRedirect('/bloodbank/welcome')
				else:
					m="INVALID username - password combination"
					context={'comment':m}		
					return render(request,'bloodbank/test.html',context)
					# return HttpResponse()
			else:
				m="Fields missing"
				context={'comment':m}		
				return render(request,'bloodbank/test.html',context)
					
				# return HttpResponse("Fields missing")
def users(request):
	p=User.objects.all()
	#print p
	template = Template("My name is {{ my_name }}.")
	context = Context({"my_name": "Adrian"})
	template.render(context)
	print template
	return HttpResponse("List")








# def check(request):
# 	from m1 import *
# 	db = get_db() 
# 	add_country(db,"hihi")
# 	print get_country(db)


# 	return HttpResponse("Welcome to MEc mongo bloodbank site")


	