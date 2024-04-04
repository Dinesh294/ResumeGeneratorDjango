from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.



def accept_data(request):

    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("past_exp","")
        skills = request.POST.get("skill","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,
                          degree=degree,school=school,
                          university=university,
                          previous_work= previous_work,skills=skills)
        profile.save()

    return render(request,'index.html',{})



def resume(request,id):
    profile = Profile.objects.get(pk=id)

    template = loader.get_template('resume.html')
    html = template.render({'profile':profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    config = pdfkit.configuration(wkhtmltopdf=r'D:\CodingProject\Django\ResumeGeneratorDjango\project_library\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response 
    # return render(request,'resume.html',{'profile':profile})



def list_users(request):
    profile = Profile.objects.all()
    return render(request,'listuser.html',{'profile':profile})






