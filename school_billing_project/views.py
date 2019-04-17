from django.shortcuts import render

def index(request): 
	return render(request,' school_billing_project/index.html')