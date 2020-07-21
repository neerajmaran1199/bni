from django.shortcuts import render
from .models import  Country
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, ListView,   UpdateView, DeleteView
# Create your views here.
def HomePage(request):
    post = Country.objects.all()

    context = {
        'posts': post
    }
    return render (request, 'news_app/country.html', context)

class HomeView(ListView):
    model = Country
    template_name = 'news_app/country.html'
    cats = Country.objects.all()
    

   



class CountryCreateView(LoginRequiredMixin,CreateView):
    model = Country
    fields = ['image', 'title', 'content','category', 'date_time']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CountryDetailView(DetailView):
    model = Country

def CategoryView(request, cats):
    category_posts = Country.objects.filter(category=cats)
    return render(request, 'news_app/categories.html', {'cats':cats, 'category_posts':category_posts})    


class CountryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Country
    fields = ['image', 'title', 'content','category', 'date_time']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CountryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Country
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def UserPost(request):
    user = request.user
    list_user_post = Country.objects.filter(author=request.user)
   
    
        
    context = {
        'posts': list_user_post
    }
    

    return render(request, 'news_app/user_post.html', context, { 'user':user})
