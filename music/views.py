# # from django.http import Http404
# # from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from .models import Album

# def index(request):
# 	all_album = Album.objects.all()
# 	context = {
# 		'all_album' : all_album
# 	}
# 	return render(request,'music/index.html',context)

# def detail(request,Album_id):
# 	# try:
# 	# 	album = Album.objects.get(pk=Album_id)
# 	# except Album.DoesNotExist:
# 	# 	raise Http404("Album does not exist")
# 	#    -------OR-------------#
# 	album = get_object_or_404(Album, pk = Album_id)
# 	return render(request,'music/detail.html',{'album' : album})

# def favourite(request,Album_id):
# 	album = get_object_or_404(Album, pk = Album_id)
# 	try:
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError,Song.DoesNotExist):
# 		return render(request,'music/detail.html',{
# 			'album' : album,
# 			'error_message': 'You have not selected a valid song',
# 			})
# 	else:
# 		selected_song.is_favourite= True
# 		selected_song.save()
# 		return render(request,'music/detail.html',{'album' : album})

# ---------------------------------------------------------------------------------------

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_album'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_logo', 'album_title']

class UpdateCreate(UpdateView):
	model = Album
	fields = ['artist', 'album_logo', 'album_title']

class DeleteCreate(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			#not saving it to the data so that we
			# can do what we want with the data
			user = form.save(commit=False)
			#we are going to clean or nomalize the data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#authentication
			user = authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('music:index')

		return render(request,self.template_name,{'form':form})


# class ProductListView(ListView):
#     queryset = Product.objects.all()
#     template_name = "products/list.html"
#
#     # def get_context_data(self, *args, **kwargs):
#     #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
#     #     print(context)
#     #     return context
#
#
# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list': queryset
#     }
# return render(request, "products/list.html", context)
#
#
# class ProductDetailView(DetailView):
#     queryset = Product.objects.all()
#     template_name = "products/detail.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         print(context)
#         # context['abc'] = 123
#         return context
#
#
# def product_detail_view(request, pk=None, *args, **kwargs):
#     #instance = Product.objects.get(pk=pk) #id
#     instance = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': instance
#     }
# return render(request, "products/detail.html", context)





