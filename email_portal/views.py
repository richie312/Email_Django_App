from django.shortcuts import render, get_object_or_404
from django.http import Http404
import json
import yagmail
import urllib.request
import os

# Create your views here.


from .models import CompanyEmail1
from .forms import ApplicationModelForm

def user_form(request):
	form = ApplicationModelForm(request.POST or None)
	if form.is_valid():
		form.save()
	template_name = "user_form.html"
	context = {'form': form}
	return render(request,template_name,context)



def Sendmail(request):
    form = ApplicationModelForm(request.POST or None)
    if form.is_valid():
        form.save(commit = False)
    passw = request.POST.get('Password')
    main_dir = os.getcwd()
    yagmail.register("richie.chatterjee31@gmail.com", passw)
    yag = yagmail.SMTP("richie.chatterjee31@gmail.com", passw,host="smtp.gmail.com")
    image_folder = os.path.join(main_dir,'images')
    template_folder = os.path.join(main_dir,'templates')
    if request.POST.get('file') == '':
        html_msg = [yagmail.inline(os.path.join(image_folder,"profile2.jpg")),os.path.join(template_folder,"links.html"),main_dir + "/docs/Resume.pdf"]
    else:
        html_msg = [yagmail.inline(os.path.join(image_folder,"profile2.jpg")),os.path.join(template_folder,"links.html"),request.FILES.get('file')]   
    Company = form.cleaned_data['company_name']
    Location = form.cleaned_data['location']
    email = form.cleaned_data['email_address']        
    Subject_line = request.POST.get('Subject')
    if Subject_line == "":
    	default_subject = "Aritra_Chatterjee_Resume_DataScience_Python_Developer"
    else:
    	default_subject = Subject_line
    template_name = 'user_form.html'
    yag.send(email, default_subject, html_msg)
    context = {"form": form}
    return render(request, template_name, context)


