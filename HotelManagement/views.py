from email import message_from_file
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from.models import Log_In_ID, Data,Food, Query, Invoice 
from django.contrib import messages


def Home(request):
    return render(request, "Home.html")

def Aboutpage(request):
    return render(request, "About.html")

def LogInpage(request):
    return render(request, "Login.html")

def booking(request):
    return render(request, "booking.html")

def savedata(request):
  n=''
  if request.method == "POST":
    if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('address') and request.POST.get('pincode') :
        data = Data()
        data.name = request.POST.get('name')
        data.mobile= request.POST.get('mobile')
        data.email = request.POST.get('email')
        data.address = request.POST.get('address')
        data.pincode = request.POST.get('pincode')
        # data.check_in = request.POST.get('check_in')
        # data.check_out = request.POST.get('check_out')
        # data.room_1 = request.POST.get('room_1')
        # data.doublebed = request.POST.get('doublebed')
        # data.room_2 = request.POST.get('room_2')
        data.save()
        n= 'Save Data In Database'
        return render(request, 'booking.html')
    else:
        return render(request, 'booking.html')


def contactpage(request):
    # if request.method == "POST":
    #     if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('message'):
    #       data = Query()
    #       data.name = request.POST.get('name')
    #       data.email= request.POST.get('email')
    #       data.subject = request.POST.get('subject')
    #       data.message = request.POST.get('message')
    #       data.save()
    #       return HttpResponse('form submit')
    # else:
        return render(request,'contact.html')

def Servicepage(request):
    return render(request, "service.html")


def Roomspage(request):
    return render(request, "rooms.html")


def Dashboardpage(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password  = request.POST['Password']
        data = Log_In_ID.objects.get(id=1)
        uname = data.Username
        pw = data.Password
        if username == uname and password == pw:
            return render(request, 'dashboard.html')
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))


def orderlist(request):
    n=''
    if request.method == "POST":
         if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('address') and request.POST.get('pincode')  and request.POST.get('idproof')  and request.POST.get('idnumber') and request.POST.get('check_in') and request.POST.get('check_out'):
            obj = Data()
            obj.name = request.POST.get('name')   
            obj.mobile = request.POST.get('mobile')   
            obj.email = request.POST.get('email')   
            obj.address = request.POST.get('address')   
            obj.pincode = request.POST.get('pincode')   
            obj.idproof = request.POST.get('idproof')   
            obj.idnumber = request.POST.get('idnumber')   
            obj.check_in = request.POST.get('check_in')   
            obj.check_out = request.POST.get('check_out')  
            obj.save()  
            info= Data.objects.all()
            return render(request, 'orderlist.html',{'obj':info})
    else:
        info= Data.objects.all()
        return render(request, 'orderlist.html',{'obj':info})
       

def foodlist(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('time') and request.POST.get('item') and request.POST.get('quantity'):
            data = Food()
            data.name = request.POST.get('name')
            data.mobile= request.POST.get('mobile')
            data.time = request.POST.get('time')
            data.item = request.POST.get('item')
            data.quantity = request.POST.get('quantity')
            data.save()
            info= Food.objects.all()
            return render(request, 'food.html',{'data':info})
    else:
        info= Food.objects.all()
        return render(request, 'food.html',{'data':info})


def billinglist(request):
    return render(request, "billinglist.html")


# def billingt(request):
#     n=''
#     if request.method == "POST":
#          if request.POST.get('name') and request.POST.get('address') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('room_price')  and request.POST.get('room_quantity')  and request.POST.get('food_price') and request.POST.get('food_quantity') and request.POST.get('discount') and request.POST.get('gst') and request.POST.get('total'):
#             obj = Invoice()
#             obj.name = request.POST.get('name')   
#             obj.address = request.POST.get('address')   
#             obj.mobile = request.POST.get('mobile')   
#             obj.email = request.POST.get('email')   
#             obj.room_price = request.POST.get('room_price')   
#             obj.room_quantity = request.POST.get('room_quantity')   
#             obj.food_price = request.POST.get('food_price')   
#             obj.food_quantity = request.POST.get('food_quantity')   
#             obj.discount = request.POST.get('discount')   
#             obj.gst = request.POST.get('gst')  
#             obj.total = request.POST.get('total')  
#             obj.save()  
#             info= Invoice.objects.all()
#             return render(request, 'billinglist.html',{'obj':info})
    # else:
    #     info= Data.objects.all()
    #     return render(request, 'billinglist.html',{'obj':info})
    

# def displayfood(request):
#      info= Food.objects.all()
#      return render(request, 'food.html',{'data':info})

def Querypage(request):
    info= Query.objects.all()
    return render(request, 'Query.html',{'data':info})

def Foodpage(request):
    return render(request, "food.html")

def display(request):
   return render(request, 'display.html',)



def Updaterecord(request):
   updatr_id = Data.objects.get(id=id)
   template = loader.get_template('update.html')
   return render(request, 'display.html',)













    