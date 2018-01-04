
from django.conf.urls import url,include
from . import views
urlpatterns = [
url(r'author/', views.authorView.as_view(),name='author'),
url(r'authordetail/(?P<author_id>[0-9]+)',views.authordetail.as_view(),name='authordetail'),
 url(r'bookdetail/(?P<book_id>[0-9]+)',views.bookdetail.as_view(),name='bookdetail'),

url(r'',views.Index.as_view(),name='book'),

]
