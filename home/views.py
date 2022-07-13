from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Address, Select

from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import SignupForm, SelectForm, AddressForm

def mmdv(request):
    selectmodeldisplay = Select.objects.all()
    addressmodeldisplay = Address.objects.all()
    return render(request, "home/select_list.html", {"select": selectmodeldisplay, "address":addressmodeldisplay})
    

def pdf_report_create(request):
    all_invoices = Select.objects.all()
    address = Address.objects.all()
    address = Address.objects.all()
    template_path = 'home/pdfReport.html'
    context = {'all_invoices': all_invoices, 'address': address, 'address': address}  
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="pdfReport.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response  
            
def address(request):
    submitted = False
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect('/address?submitted=True')       
    else:
        form = AddressForm()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'home/address.html', {'form': form, 'submitted': submitted})


def select(request):
    submitted = False
    if request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            form.save()            
        return HttpResponseRedirect('/select?submitted=True')                    
    else:
        form = SelectForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home/select.html', {'form': form, 'submitted': submitted})

def list(request):
    all_invoices = Select.objects.all()
    if request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_bound and form.is_valid():
            form.save()                        
            all_invoices = [select for select in all_invoices]
    else:
        form = SelectForm()
    return render(request, 'home/select.html', {'form' : form, 'all_invoices': all_invoices})


def index(request):
    return render(request, 'base.html')


def signup(request):
    submitted = False
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False
        return HttpResponseRedirect('/signup?submitted=True')
    else:
        form = SignupForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/signup.html', {'form': form, 'submitted': submitted})


def logout(request):   
    return render(request, 'home/logout.html')



