from django.shortcuts import render,redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from home.models import *
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

	
def index(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        email=data.get('email')
        user=certificate.objects.filter(student_email=email)
        if user.exists():
            return redirect('/pdf_view/')
        else:
           return redirect('/index/')
    user=certificate.objects.all()
    return render(request,'index.html',context={'data':user})



def pdf(request):
	if request.method=="POST":
		data=request.POST
		username=data.get('username')
		email=data.get('email')
		user=certificate.objects.get(student_email=email).student_name
		if user.exists():
			return render(request,'pdf_template.html',context={'data':user})
		else:
			pass
		return render(request,'pdf_template.html',context={'data':user})
	return render(request,'pdf_template.html')

def register(request):
	if request.method=="POST":
		data=request.POST
		username=data.get('username')
		email=data.get('email')
		user=certificate.objects.filter(student_email=email)
		if user.exists():
			print("user already")
		else:
			certificate.objects.create(
				student_name=username,
				student_email=email
			)
		return redirect('/regis/')
	return render(request,'registration.html')

def fake(request):
	return render(request,'fake.html')
def pdf_data(request):
	data=certificate.objects.all()
	if request.GET.get('username'):
		name=request.GET.get('username')
		data=data.filter(student_name=name)
		if data:
			pass
		else:
			print('no user')
	return render(request,'test.html',context={'data':data})

		