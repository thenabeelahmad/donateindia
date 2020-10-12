from django.db import connection
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

def addneedy(request):
    if request.method=="POST":
        nam=request.POST['name']
        ag=request.POST['age']
        add=request.POST['address']
        sib=request.POST['siblings']
        fi=request.POST['familyincome']
        myfile = request.FILES['pic']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        fill = fs.url(filename)
        c=connection.cursor()
        c.execute(f"""insert into tbl_needy set name='{nam}',age='{ag}',address='{add}',siblings='{sib}',familyincome='{fi}',
        photo='{fill}' """)
        return redirect('addneedy')
    return render(request,"userpower/addneedy.html")    


def needy(request):
    query=connection.cursor()
    query.execute("select * from tbl_needy ")
    s=query.fetchall()
    return render(request,"userpower/needies.html",{'data':s})