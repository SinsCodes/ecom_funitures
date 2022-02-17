# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import customer_regform, sofa_form, dining_form, bed_form, armchair_form
from .models import Customer_Reg, Admin_Reg, Ecom_Chair, Ecom_Dining, Ecom_Bed, Ecom_Armchairs


def index(request):
    return render(request,'index.html')

def index_list(request):
    return render(request,'index_list.html')

def pro_page(request):

    return render(request,'productpage.html')

def index_base(request):

    return render(request,'indexbase.html')

def sofa_list(request):
    obj=sofa_form()
    return render (request,'sofa/sofalist.html',{'form':obj})

def add_sofa(request):

    if request.method =='POST' and request.FILES['image']:
        upload_file = request.FILES['image']
        up_name = upload_file.name
        file = FileSystemStorage()
        fdata=file.save(up_name,upload_file)
        upload_url=file.url(fdata)
        name1=request.POST.get('name')
        price1=request.POST.get('price')
        category1=request.POST.get('category')
        discount1=request.POST.get('discount')
        obj=Ecom_Chair(name=name1,price=price1,category=category1,discount=discount1,image=upload_url)

        obj.save()
    obj=sofa_form()
    return render(request,'sofa/sofalist.html',{'form':obj})


def view_sofa(request):

    obj = Ecom_Chair.objects.all()

    return render(request, 'sofa/viewsofa.html', {'form': obj})

def detail_sofa(request):

    if request.method == 'POST':
        print('one')
        sid=request.POST.get('nid')
        print(sid)

        obj = Ecom_Chair.objects.get(id=request.POST.get('nid'))

        return render(request,'sofa/sofadetail.html',{'details':obj})

def dining_create(request):
    obj=dining_form()
    return render (request,'dining table/dininglist.html',{'form':obj})

def dining_list(request):

    if request.method=='POST' and request.FILES['image']:
        upload_file=request.FILES['image']
        upload_name=upload_file.name
        file=FileSystemStorage()
        fdata=file.save(upload_name,upload_file)
        upload_url=file.url(fdata)
        n1=request.POST.get('name')
        p1=request.POST.get('price')
        d1=request.POST.get('discount')
        c1=request.POST.get('category')
        obj=Ecom_Dining(name=n1,price=p1,discount=d1,category=c1,image=upload_url)
        obj.save()
    obj = dining_form()
    return render(request,'dining table/dininglist.html',{'form':obj})

def view_dining(request):

    obj=Ecom_Dining.objects.all()
    return render(request,'dining table/viewdining.html',{'form':obj})

def armchair_create(request):
    obj=armchair_form()
    return render (request,'armchairs/armchairlist.html',{'form':obj})

def armchair_list(request):
    if request.method == 'POST' and request.FILES['image']:
        upload_file = request.FILES['image']
        upload_name = upload_file.name
        file = FileSystemStorage()
        fdata = file.save(upload_name, upload_file)
        upload_url = file.url(fdata)
        n1 = request.POST.get('name')
        p1 = request.POST.get('price')
        d1 = request.POST.get('discount')
        c1 = request.POST.get('category')
        obj = Ecom_Armchairs(name=n1, price=p1, discount=d1, category=c1, image=upload_url)
        obj.save()
    obj = armchair_form()
    return render(request,'armchairs/armchairlist.html',{'form':obj})

def view_armchair(request):

    obj=Ecom_Armchairs.objects.all()
    return render(request,'armchairs/viewarmchair.html',{'form':obj})

def create_bed(request):
    obj=bed_form()
    return render(request,'bed/bedlist.html',{'form':obj})

def bed_list(request):

    if request.method=='POST' and request.FILES['image']:
        upload_file = request.FILES['image']
        up_name = upload_file.name
        file = FileSystemStorage()
        fdata = file.save(up_name, upload_file)
        upload_url = file.url(fdata)
        n1=request.POST.get('name')
        p1=request.POST.get('price')
        d1=request.POST.get('discount')
        c1=request.POST.get('category')
        obj=Ecom_Bed(name=n1,price=p1,discount=d1,category=c1,image=upload_url)
        obj.save()
    obj=bed_form()
    return render(request,'bed/bedlist.html',{'form':obj})


def view_bed(request):

    obj=Ecom_Bed.objects.all()
    return render(request,'bed/view_bed.html',{'form':obj})

def cus_regform(request):
    obj=customer_regform()

    return render(request,'registration.html',{'form':obj})

def cus_reg(request):

    if request.method == 'POST':
        obj=customer_regform(request.POST)
        if obj.is_valid():
            obj.save()
    return cus_regform(request)


def admin_reg(request):
    if request.method =='POST':

        obj=Admin_Reg(username=request.POST.get('uname'),
                      email=request.POST.get('email'),
                      password=request.POST.get('pword'))

        obj.save()

        return render(request,'admin/adminreg.html')
    return render(request,'admin/adminreg.html')


def login(request):

    if request.method == 'POST':

        utype=request.POST.get('utype')
        user=request.POST.get('uname')
        pd=request.POST.get('pword')

        if utype == 'Admin':

            try:

                if Admin_Reg.objects.get(username=user)is not None:
                    a=Admin_Reg.objects.get(username=user)
                    if pd == a.password:
                        request.session['sid']=a.username
                        return redirect('/index_list/')
                    else:
                        return HttpResponse('incorrectpassword')

            except:
                return render(request,'index.html',{'msg':'username doesnot exist'})


        else:

            try:

                if Customer_Reg.objects.get(username=user) is not None:

                    b=Customer_Reg.objects.get(username=user)
                    if pd == b.password:
                        request.session['sid']=b.username
                        return render(request,'registration.html')

                    else:
                        return HttpResponse ('incorrect password')

            except:

                return render(request,'index_list.html',{'msg':'username doesnot exist'})
