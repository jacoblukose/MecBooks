from django.conf.urls import patterns, url
from bloodbank import views
import subprocess
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
 	url(r'^login/$', views.login_new, name='login'),
 	# url(r'^check/$', views.check, name='check'),
 	url(r'^welcome/$', views.welcome, name='welcome'), 
 	url(r'^passchange/$', views.passchange, name='passwordchange'), 
 	url(r'^logout/$', views.logout, name='logout'),  	
 	url(r'^users/$', views.users, name='user_list'),
	url(r'^welcome/find/$', views.find, name='book_upload')  
)



# subprocess.call(['./mini.sh', "clrs"])