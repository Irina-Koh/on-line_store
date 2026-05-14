from blog.models import BlogPost
from django.http import request
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class BlogListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return super().get_queryset().filter(is_published=False)


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image']
    success_url = reverse_lazy('blog:blogpost_list')


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image']
    success_url = reverse_lazy('blog:blogpost_list')

    def get_success_url(self):
        return reverse('blog:blogpost_detail', args=[self.kwargs.get('pk')])



class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')

