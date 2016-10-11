from django.shortcuts import render,render_to_response, redirect
from django.template import RequestContext
from django.utils import translation
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from news.models import *
from django import forms
from django.views.generic import TemplateView
import json






def base_index(req=None):
    data = {
        'html_lang':req.get_full_path()[1:3], 
        'url':req.get_full_path()[4:],
        'contact': Contact.objects.all(),
        'category_menu': Category.objects.all().order_by('id',)
    }
    data.update(csrf(req))
    return data






def test(request):
    rend_it = base_index(req=request)
    rend_it['news'] = News.objects.all()
    rend_it['menu'] = Menu.objects.all()
    return render_to_response('perde.html',rend_it, context_instance=RequestContext(request))


def index(request):
    rend_it = base_index(req=request)
    rend_it['slider'] = Slider.objects.filter(status=True)
    rend_it['news'] = News.objects.all()
    rend_it['teams'] = Teams.objects.all()
    arr = []
    for x in rend_it['slider']:
        arr.append('/media/'+str(x.image))
    rend_it['data'] = json.dumps(arr) 
    return render_to_response('index.html',rend_it, context_instance=RequestContext(request))



def Draw_prroject(request):
    rend_it = base_index(req=request)
    return render_to_response('service_drowing_project.html',rend_it, context_instance=RequestContext(request))

def Product_delivery(request):
    rend_it = base_index(req=request)
    return render_to_response('product-delivery.html',rend_it, context_instance=RequestContext(request))


def Reference(request):
    rend_it = base_index(req=request)
    return render_to_response('references.html', rend_it, context_instance=RequestContext(request))

def Teams_view(request):
    rend_it = base_index(req=request)
    return render_to_response('teams.html', rend_it, context_instance=RequestContext(request))



def Collections(request):
    rend_it = base_index(req=request)
    rend_it['kategory'] = Category.objects.all().order_by('id')
    return render_to_response('collections.html', rend_it , context_instance=RequestContext(request))



def Collection_menu(request,name):
    rend_it = base_index(req=request) 
    try:
        tipi = Category.objects.get(text_en=name.replace('-',' ')) 
        data = Collection.objects.filter(types=tipi)
        rend_it['name'] = tipi.text
        rend_it['data'] = data
        return render_to_response('collection-single.html', rend_it, context_instance=RequestContext(request))
    except:
        return HttpResponse('Page not found')
     




def about(request):
    rend_it = base_index(req=request)
    rend_it['menu'] = Menu.objects.all()
    rend_it['url'] = request.get_full_path()[4:]
    return render_to_response('about.html',rend_it, context_instance=RequestContext(request))

def news(request):
    rend_it = base_index(req=request)
    rend_it['menu'] = Menu.objects.all()
    news_list = News.objects.all()
    paginator = Paginator(news_list, 1)
    page = request.GET.get('page')
    try:
        rend_it['news'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rend_it['news'] = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rend_it['news'] = paginator.page(paginator.num_pages)
    rend_it['url'] = request.get_full_path()[4:]
    rend_it['image_list'] = rend_it['news'][0].images.all()
    return render_to_response('news.html',rend_it, context_instance=RequestContext(request))



def news_single(request, slug):
    rend_it = base_index(req=request)
    try:
        rend_it['data'] = News.objects.get(id=forms.IntegerField().clean(slug[-2:]))
        rend_it['image_list'] = rend_it['data'].images.all()
        return render_to_response('news-single.html', rend_it, context_instance=RequestContext(request))

    except:
        return redirect('/error')


def service_drawing_project(request):
    rend_it = base_index(req=request)
    rend_it['slider'] = Slider.objects.filter(status=True)
    return render_to_response('contact.html', rend_it, context_instance=RequestContext(request))



def contact(request):
    rend_it=base_index(req=request)
    rend_it['slider'] = Slider.objects.filter(status=True)
    return render_to_response('contact.html', rend_it, context_instance=RequestContext(request))


        

def set_language(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return response
