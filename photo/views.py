from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from .models import PhotoPost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = 'post_photo.html'
    success_url  = reverse_lazy('photo:post_done')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PhotoSuccessView(TemplateView):
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 6
    
    def get_queryset(self):
        category_id = self.kwargs['category']
        records = PhotoPost.objects.filter(
            category = category_id).order_by('-posted_at')
        return records

class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 6
    
    def get_queryset(self):
        user_id = self.kwargs['user']
        records = PhotoPost.objects.filter(
            user = user_id).order_by('-posted_at')
        return records

class PhotoDetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost
    
class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 6
    
    def get_queryset(self):
        records = PhotoPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        return records