from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit  import CreateView
from django.views.generic import TemplateView
from twilio.twiml.messaging_response import MessagingResponse
from sbin.models import User,Bin

# Find these values at https://twilio.com/user/account
account_sid = "ACaa8017dfbe4f80f07395fabc4c83f1c5"
auth_token = "e77ace335eb745593033dafd3f5cff02"
client = Client(account_sid, auth_token)

class Sendmess(CreateView):
    def post(self,request,*args,**kwargs):
        client.api.account.messages.create(
            to="+919003768929",
            from_="+19193283318",
            body="Testing django twilio!")
        return HttpResponse("Hello, world. You're at the polls index.")
    def get(self,request,*args,**kwargs):
        client.api.account.messages.create(
            to="+919003768929",
            from_="+19193283318",
            body="Testing django twilio!")
        return HttpResponse("Hello World. You are at polls index")

class Home(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')

class login(TemplateView):
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        pid = request.POST["uname"]
        passwd = request.POST["psw"]
        user = User.objects.all().filter(Idd=str(pid))
        if (user):
            binID = user[0].Binn.bin_ID
            if (binID==passwd):
                return redirect("http://127.0.0.1:8000/sbin/details/%s/%s" %(pid,passwd))
            else:
                error="Invalid password"
        else:
            error="Invalid Username!!"
        return render(request,'login.html',{'error':error,})
    def get(self,request,*args,**kwargs):
        return render(request,'login.html',)

class Details(TemplateView):
    def get(self,request,PID,Bin):
        print (PID,Bin)
        user = User.objects.all().filter(Idd=str(PID))[0]
        return render(request,'PersonalView.html',{'pid':PID,'name':user.Name,'ph':user.Ph_no,'email':user.email,
                                                   'bid':user.Binn.bin_ID,'lastC':user.Binn.Last_cleaned})