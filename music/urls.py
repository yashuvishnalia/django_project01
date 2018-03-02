from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	# #/music/
	# path('',views.index, name='index'),
	# #/music/714
	# path('<Album_id>/',views.detail, name='detail'),
	# #/music/Album_id/favourite
	# path('<Album_id>/favourite/',views.favourite, name='favourite'),
	#/music/
	path('',views.IndexView.as_view(), name='index'),
	path('register/', views.UserFormView.as_view(), name='register'),
	#/music/714
	path('<pk>/',views.DetailView.as_view(), name='detail'),
	
	path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
	path('album/<pk>/', views.UpdateCreate.as_view(), name='album-update'),
	path('album/<pk>/delete/', views.DeleteCreate.as_view(), name='album-delete'),

	]