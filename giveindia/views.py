from django.shortcuts import render
from django.db import connection

def home(request):
    if request.method=="POST":
        nam=request.POST['name']
        m=request.POST['mail']
        ms=request.POST['msg']
        c=connection.cursor()
        c.execute(f"""insert into tbl_contact set name='{nam}',
        mail='{m}',msg='{ms}' """)
    return render(request,"home.html")    

def about(request):
	return render(request,"about.html")


def donate(request):
	return render(request,"donate.html")

