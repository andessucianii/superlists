from django.conf.urls import url
from lists import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
	#url(r'^$', views.home_page, name='home'),
	url(r'^new$', views.new_list, name='new_list'),
    	url(r'^(\d+)/$', views.view_list, name='view_list'),
	url(r'^(\d+)/add_item$', views.add_item, name='add_item')
	#url(r'^admin/', include(admin.site.urls)),
]
