from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_email = request.POST['email']
		message_subject = request.POST['subject']
		message = request.POST['message']

		#send an email
		send_mail(
			message_name, #subject
			message, #message
			message_email, # from email
			['sammymunywoki44@gmail.com'], # To email
			)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

	
def about(request):
	return render(request, 'about.html', {})

def blogs(request):
	return render(request, 'blog_single.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def department(request):
	return render(request, 'department.html', {})

def doctor(request):
	return render(request, 'doctor.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def appointment(request):
	if request.method == "POST":
		first_name = request.POST['firstname']
		last_name  = request.POST['lastname']
		address  = request.POST['address']
		appointment = request.POST['appointment']
		date       = request.POST['date']
		phone       = request.POST['phone']
		time      = request.POST['time']

		
		

		#send an email
		#send_mail(
			#'appointment Request'
		 	#message, #message
		 	#message_email, # from email
		 	#['sammymunywoki44@gmail.com'], # To email
		 #	)
		return render(request, 'appointment.html', {
			'first_name': first_name,
			'last_name': last_name,
			'address': address,
			'appointment': appointment,
			'date': date,
			'phone': phone,
			'time': time})
	else:
		return render(request, 'home.html', {})







