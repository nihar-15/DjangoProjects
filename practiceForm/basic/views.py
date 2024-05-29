from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect




def welcomePage(request):

##    author={
  ###      'name': request.POST.get('output')
            
    ###}


    return render(request,"WelcomePage.html")



def registerPage(request):
    output={}
    try:
        name=request.POST['first']
        lastname=request.POST['last']
        print( name ," ",lastname)
        output={
            'fullname':name+lastname
        }
        
        ## yeh value url mein dikhayegi 
        ##url='/?output={}'.format(output)
        ##method 1 to reedirect page
        ### return HttpResponseRedirect(url)
        ## method 2

        ### in the argument ,we can pass either url obj or the path of the page where we nt to redirect
        ##return redirect('/')
    
    except:
        pass    
    return render(request,'register.html',output)        


def AboutMe(request):
     return render(request,'AboutMe.html')


def ContactPage(request):
    contact_details={
    'phno':["98987654321","98987654322","97865434210"],
    'email':["tulipfestival@gmail.com","enquiry.tulipfestival@gmail.com"],

    }
   

    return render(request,'contact.html',contact_details)


def thank(request):
    return render(request,"Thankyou.html")






