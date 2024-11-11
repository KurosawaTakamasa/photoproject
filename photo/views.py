from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
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