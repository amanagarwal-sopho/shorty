from django.shortcuts import render
from .models import URLEntry
from .forms import URLForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def redirect_url(request,code):
    
    try :
        if URLEntry.objects.get(code=code):
            url = URLEntry.objects.get(code=code).url
            return HttpResponseRedirect(url)
    except URLEntry.DoesNotExist:
        return HttpResponse('No such code exists')
        
def index(request):
    
    done = False
    code = '' 
    if request.method == 'POST':
        url_form = URLForm(data=request.POST)
        if url_form.is_valid():
            done = True
            url = url_form.save()
            url = url.create_code()
            code = url.code
        else :
            print(url_form.errors)
    
    else :
        url_form = URLForm()

    return render(request,'shorturl/index.html',{'url_form' : url_form, 'done' : done , 'code': code})
            
    
    
