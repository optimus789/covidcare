from django.shortcuts import render
from django.http import HttpResponse
from .models import Covidiot
# Create your views here.

def create(request):
    context = {}
    iv = 0
    if request.method == 'POST':
        uname = request.POST.get("uname")  
        fever = request.POST.get("slider")
        cough = request.POST.get("cough")
        lowbreath = request.POST.get("breathlessness")
        smell = request.POST.get("smell")
        appetite = request.POST.get("appetite")
        tired = request.POST.get("tired")
        throat = request.POST.get("throat")
        bodypain = request.POST.get("bodypain")
        invisit = request.POST.get("invisit")
        pubvisit = request.POST.get("pubvisit")
        hivisit = request.POST.get("hivisit")
        xray = request.POST.get("xray")
        ctscan = request.POST.get("ctscan") 
        
        if (xray==""):
            xray=False
        else:
            xray=True


        if (ctscan==""):
            ctscan=False
        else:
            ctscan=True
         
        feverIV = 0.09
        coughIV = 0.09
        lowbreathIV = 0.06
        smellIV = 0.07
        appetiteIV = 0.06
        tiredIV = 0.08
        throatIV = 0.08
        bodypainIV = 0.07
        invisitIV = 0.1
        pubvisitIV = 0.1
        hivisitIV = 0.1
        xrayIV = 0.1
        ctscanIV = 0.1
        fever = int(fever)

        if(int(fever)>96):
            diff = fever-96
            val = diff//2
            iv = iv + feverIV + (val*0.01)
            print("added 0",iv )

        if(cough=="2"):
            iv = iv + coughIV
            print("added 1",iv)

        if(cough=="3"):
            iv = iv + coughIV + 0.04
            print("added 2",iv)

        if(lowbreath=="2"):
            iv = iv + lowbreathIV
            print("added 3",iv)

        if(lowbreath=="3"):
            iv = iv + lowbreathIV + 0.02
            print("added 3",iv)

        if(smell=="on"):
            iv = iv + smellIV         
            print("added 4",iv)

        if(appetite=="on"):
            iv = iv + appetiteIV
            print("added 5",iv)

        if(tired=="on"):
            iv = iv + tiredIV
            print("added 6",iv)

        if(throat=="on"):
            iv = iv + throatIV
            print("added 7",iv)

        if(bodypain=="on"):
            iv = iv + bodypainIV
            print("added 8",iv)
            
        if(invisit=="on"):
            iv = iv + invisitIV                
            print("added 9",iv)

        if(pubvisit=="on"):
            iv = iv + pubvisitIV
            print("added 10",iv)

        if(hivisit=="on"):
            iv = iv + hivisitIV
            print("added 11",iv)

        if(xray):
            iv = iv + xrayIV
            print("added 12",iv)

        if(ctscan):
            iv = iv + ctscanIV 
            print("added 13",iv)

        list1 = []
        list1.append(smell)
        list1.append(appetite)
        list1.append(throat)
        list1.append(tired)
        list1.append(bodypain)
        list1.append(invisit)
        list1.append(pubvisit)

        list1.append(hivisit)
        print("Xray",xray)
        print("Ct scan : ",ctscan)
               
        print(cough)
        print(lowbreath)
        
        for i in range(8):
            if(list1[i] == "on"):
                list1[i]=True
            else:
                list1[i]=False

        smell=list1[0]
        appetite = list1[1]
        throat = list1[2]
        tired = list1[3]
        bodypain = list1[4]
        invisit = list1[5]
        pubvisit = list1[6]
        hivisit = list1[7]
        
        print("Infection Value: ",iv)
        
        p = Covidiot.objects.create(mob=uname, cough=cough,smell=smell, appetite=appetite,breathlessness = lowbreath,  fever=fever, tired=tired,throat=throat, bodypain=bodypain, invisit=invisit, pubvisit=pubvisit, hivisit=hivisit, xray=xray, ctscan=ctscan, iv=iv )
        p.save()
        context = {'result':[uname,fever,cough,iv,tired,throat,bodypain,invisit,pubvisit,hivisit,xray,ctscan,smell,appetite,lowbreath]}
        count = 0
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            count=count+1
            # print(f'Value: {value}') in Python >= 3.7

        print("Count of Post items: ",count )

    return HttpResponse(iv)
    #return render(request, 'covidManager/create.html', context)


def update(request):
    context = {}
    iv = 0
    if request.method == 'POST':
        #uname = request.POST.get("uname")  
        userid = request.POST.get("id")
        fever = request.POST.get("slider")
        cough = request.POST.get("cough")
        lowbreath = request.POST.get("breathlessness")
        smell = request.POST.get("smell")
        appetite = request.POST.get("appetite")
        tired = request.POST.get("tired")
        throat = request.POST.get("throat")
        bodypain = request.POST.get("bodypain")
        invisit = request.POST.get("invisit")
        pubvisit = request.POST.get("pubvisit")
        hivisit = request.POST.get("hivisit")
        xray = request.POST.get("xray")
        ctscan = request.POST.get("ctscan") 
        
        if (xray==""):
            xray=False
        else:
            xray=True


        if (ctscan==""):
            ctscan=False
        else:
            ctscan=True
         
        feverIV = 0.09
        coughIV = 0.09
        lowbreathIV = 0.06
        smellIV = 0.07
        appetiteIV = 0.06
        tiredIV = 0.08
        throatIV = 0.08
        bodypainIV = 0.07
        invisitIV = 0.1
        pubvisitIV = 0.1
        hivisitIV = 0.1
        xrayIV = 0.1
        ctscanIV = 0.1
        fever = int(fever)

        if(int(fever)>96):
            diff = fever-96
            val = diff//2
            iv = iv + feverIV + (val*0.01)
            print("added 0",iv )

        if(cough=="2"):
            iv = iv + coughIV
            print("added 1",iv)

        if(cough=="3"):
            iv = iv + coughIV + 0.04
            print("added 2",iv)

        if(lowbreath=="2"):
            iv = iv + lowbreathIV
            print("added 3",iv)

        if(lowbreath=="3"):
            iv = iv + lowbreathIV + 0.02
            print("added 3",iv)

        if(smell=="on"):
            iv = iv + smellIV         
            print("added 4",iv)

        if(appetite=="on"):
            iv = iv + appetiteIV
            print("added 5",iv)

        if(tired=="on"):
            iv = iv + tiredIV
            print("added 6",iv)

        if(throat=="on"):
            iv = iv + throatIV
            print("added 7",iv)

        if(bodypain=="on"):
            iv = iv + bodypainIV
            print("added 8",iv)
            
        if(invisit=="on"):
            iv = iv + invisitIV                
            print("added 9",iv)

        if(pubvisit=="on"):
            iv = iv + pubvisitIV
            print("added 10",iv)

        if(hivisit=="on"):
            iv = iv + hivisitIV
            print("added 11",iv)

        if(xray):
            iv = iv + xrayIV
            print("added 12",iv)

        if(ctscan):
            iv = iv + ctscanIV 
            print("added 13",iv)

        list1 = []
        list1.append(smell)
        list1.append(appetite)
        list1.append(throat)
        list1.append(tired)
        list1.append(bodypain)
        list1.append(invisit)
        list1.append(pubvisit)

        list1.append(hivisit)
        print("Xray",xray)
        print("Ct scan : ",ctscan)
               
        print(cough)
        print(lowbreath)
        
        for i in range(8):
            if(list1[i] == "on"):
                list1[i]=True
            else:
                list1[i]=False

        smell=list1[0]
        appetite = list1[1]
        throat = list1[2]
        tired = list1[3]
        bodypain = list1[4]
        invisit = list1[5]
        pubvisit = list1[6]
        hivisit = list1[7]
        
        print("Infection Value: ",iv)
        print("User ID:",userid )
        Covidiot.objects.filter(id=userid).update(cough=cough,smell=smell, appetite=appetite,breathlessness = lowbreath,  fever=fever, tired=tired,throat=throat, bodypain=bodypain, invisit=invisit, pubvisit=pubvisit, hivisit=hivisit, xray=xray, ctscan=ctscan, iv=iv )

        context = {'result':[fever,cough,iv,tired,throat,bodypain,invisit,pubvisit,hivisit,xray,ctscan,smell,appetite,lowbreath]}
        count = 0
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            count=count+1
            # print(f'Value: {value}') in Python >= 3.7

        print("Count of Post items: ",count )

    return HttpResponse(iv)
    #return render(request, 'covidManager/create.html', context)


def updateloc(request):
    result=False
    if request.method == 'POST':
        lat = request.POST.get("lat")
        lon = request.POST.get("lon")
        userid = request.POST.get("userID") 
        if(userid==""):
            userid=0
            result=False
        else:
            print("Lat",lat)
            print("Long",lon)
            print("userid",userid)

            result_out = Covidiot.objects.get(id=userid)

            result_out.lat = lat
            result_out.lon = lon

            result_out.save()

            result=True

    return HttpResponse(result)


def friendloc(request):
    result=False
    if request.method == 'POST':
        userid = request.POST.get("userID")

        result_user = Covidiot.objects.get(id=userid)

        userid_frnd = result_user.friends
        print(userid_frnd)

        userid_frnd_list=userid_frnd.split(",")

        loc = []
        count = 0
        for i in userid_frnd_list:
            frnd = Covidiot.objects.get(id=i)
            latt = frnd.lat
            lonn = frnd.lon
            if(frnd.iv==None or frnd.iv==""):
                iv = str(0)
            else:
                iv = str(frnd.iv)
            count+=1
            if(count==len(userid_frnd_list)):
                loc.append(str(i+","+latt+","+lonn+","+iv ))
            else:
                loc.append(str(i+","+latt+","+lonn+","+iv+","))
            

        
        print("loc: ",loc)
        print("userid",userid)
        context = {'res':[userid_frnd_list,loc]}
            
    return HttpResponse(loc)


def addfriend(request):
    result = False
    
    if request.method == 'POST':
        fid = request.POST.get("friendID")
        userid = request.POST.get("userID") 

        print("friend id:",fid)
        print("user id:",userid)

        result_in = Covidiot.objects.get(id=fid)#client
        result_out = Covidiot.objects.get(id=userid)#host

        p_in = result_in.pending_in
        p_out = result_out.pending_out

        result_frnd = result_in.friends
        main_flag = True
        if(result_frnd!=None):
            res_frd_list=result_frnd.split(",")
            
            for i in res_frd_list:
                if(i==userid):
                    main_flag=False

        if(main_flag==True):
            print("P_out:", p_out)
            if(p_in==None):
                p_in=""

            if(p_out==None):
                p_out=""

            print("P_in:", p_in)
            
            flag1 = True
            flag2 = True    
            p_in_list=p_in.split(',')

            for i in p_in_list:
                if(i == userid):
                    flag1=False
                

            p_out_list=p_out.split(',')
            
            for i in p_out_list:
                if(i == fid):
                    flag2=False
                        

            if(result != None and flag1==True):
                if(p_in==""):
                    result_in.pending_in = str(userid)
                else:
                    result_in.pending_in = str(p_in+','+userid)
                
                result_in.save()
            
            if(result != None and flag2==True):
                if(p_out==""):
                    result_out.pending_out = str(fid)
                else:
                    result_out.pending_out = str(p_out+','+fid)
                
                result_out.save()

            result=True
            
    print("Result: ",result)
    return HttpResponse(result)

def notify(request):
    list1=[]
    friend=""
    if request.method == 'POST':
        userid = request.POST.get("userID")
        print(userid)  
        result_in = Covidiot.objects.get(id=userid)
        p_in = result_in.pending_in
        print(p_in)
        p_in_list = p_in.split(",")
        print(p_in_list)
        friend = p_in_list[0]
    print("Pending Requests: ",list1)
    return HttpResponse(friend)

def accept(request):

    if request.method == 'POST':
        userid = request.POST.get("userID")
        fid = request.POST.get("friendID") 
         
        result_frnd = Covidiot.objects.get(id=userid)
        result_out = Covidiot.objects.get(id=fid)

        result_out_frnd = result_out.friends
        

        if(result_out_frnd==None or result_out_frnd == ""):
            result_out.friends = str(userid)
        else:
            result_out.friends = str(result_out_frnd+','+userid)

        result_out.save()
        r_frnd = result_frnd.friends 
        
        p_in = result_frnd.pending_in 
        p_in_list = p_in.split(",")
        p_in_list.remove(fid)
        p = ""
        for i in p_in_list:
            if(i != ","):
                p =p + i + ","
        result_frnd.pending_in = str(p)
        result_frnd.save()
        print(p_in_list)
        if(r_frnd==None or r_frnd == ""):
            result_frnd.friends = str(fid)
        else:
            result_frnd.friends = str(r_frnd+','+fid)
        
        result_frnd.save()

        result_out_p_out = result_out.pending_out

        result_out_p_out_list = result_out_p_out.split(",")

        result_out_p_out_list.remove(userid)
        p = ""
        
        for i in result_out_p_out_list:
            if(i != ","):
                p = p + i + ","

        result_out.pending_out = str(p)
        result_out.save()

    return HttpResponse("Friend Added")

    
def reject(request):
    if request.method == 'POST':
        userid = request.POST.get("userID")
        fid = request.POST.get("friendID")  
        result_frnd = Covidiot.objects.get(id=userid)
        result_out = Covidiot.objects.get(id=fid)
        r_frnd = result_frnd.friends 
        p_in = result_frnd.pending_in 
        p_in_list = p_in.split(",")
        p_in_list.remove(fid)
        p = ""
        for i in p_in_list:
            if(i != ","):
                p =p + i + ","
        result_frnd.pending_in = str(p)
        result_frnd.save()

        r_out = result_out.friends 
        p_out = result_out.pending_out 
        p_out_list = p_out.split(",")
        p_out_list.remove(userid)
        p = ""
        for i in p_out_list:
            if(i != ","):
                p =p + i + ","
        result_out.pending_out = str(p)
        result_out.save()

        print(p_in_list)
        print(p_out_list)
          
    return HttpResponse("Friend Denied")        


