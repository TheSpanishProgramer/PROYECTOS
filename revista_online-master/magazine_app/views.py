from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator
from .models import MagazineApp
from .forms import StoryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 


# Create your views here.
def index(request):
    return render(request, "index.html", {})

def magazine_view(request):
    return render(request, "magazine.html", {})

def contact_view(request): #Views de contacto
    my_context = {
        "my_text": "Este es el mail de contacto: ",
        "my_mail": "test@mail.com"
    }
    return render(request, "contact.html", my_context)

def story_detail_view(request): #Views del detalle de cada obra
    obj = MagazineApp.objects.all()
    context = {
        'object': obj
    }
    return render(request, "magazine/story_detail.html", context)

def story_list_view(request): #Views del listado de obras
    obj = MagazineApp.objects.all()
    paginator = Paginator(obj, 3)
    page = request.GET.get('pg')
    obj = paginator.get_page(page)
    
    return render(request, "magazine/story_list.html", {'object': obj})

@login_required
def story_create_view(request): #Views del apartado para enviar una obra
    form = StoryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.manage = request.user
        instance.save()
        form = StoryForm()
    context = {
        'form': form
    }
    return render(request, "magazine/story_create.html", context)

@login_required
def your_story_list_view(request): #Views del listado de obras del usuario
    obj = MagazineApp.objects.filter(manage=request.User)
    paginator = Paginator(obj, 3)
    page = request.GET.get('pg')
    obj = paginator.get_page(page)
    
    return render(request, "magazine/your_story_list.html", {'object': obj})
    