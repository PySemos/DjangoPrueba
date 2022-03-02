from django.shortcuts import render

def saludo(request):
	return render(request,"hola.html",{})

def mcm(request,a,b):

	for i in range(max(a,b),a*b+1):
		if i%a==0 and i%b==0:
			return render(request,"mcm.html",{"a":a,"b":b,"mcm":i})
	return render(request,"no_hay_mcm.html",{"a":a,"b":b})