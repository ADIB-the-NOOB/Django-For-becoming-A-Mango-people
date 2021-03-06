from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Post
# Create your views here.
from django.views import View
from .forms import ContactForm,PostForm

class ContactView(View):
    form_class = ContactForm
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse("Success")
        return render(request, self.template_name, {'form': form})        

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactForm()
    
    return render(request,"contact.html",{'form':form})

def PostView(request):
    post = Post.objects.all()
    return render(request,'firstapp/postview.html',{'post': post})

def postcreate(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
    else:
        form = PostForm()
    return render(request,'firstapp/postcreate.html',{'form':form})