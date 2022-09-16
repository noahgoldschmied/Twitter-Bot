#Noah Goldschmied
#June 8th, 2022
#Twitter Bot for learning

import tweepy, time, webbrowser, math, random
from NFL_Team_Class import NFL_Team
from Character_Class import Character


#initializing the API
consumer_key='bCCFXRm3UU7oJHptrGza31Bgl'
consumer_secret='KlexASdT3BMMqa3pV7GmVLqUyycGLvIEqwcertUAMnC1yG6voO'
access_token='1535097172974346250-kAOfeddZUEd1obqg2GV2gh5miWWMuF'
access_token_secret='DFovfB6jbuzpAqtSPYjhtnQaaePzDqOWEIJmkUxQoBjfb'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth)

#def initialize():
niners = NFL_Team("San Francisco 49ers", "49ers.png", "@49ers", "#FTTB", "NFC", "W", 1)
niners_logo = tweepy.models.Media( niners.logo) 
bears = NFL_Team("Chicago Bears", "Bears.png", "@ChicagoBears", "#DaBears", "NFC", "N", 2)
bears_logo = api.media_upload(bears.logo)
bengals = NFL_Team("Cincinnati Bengals", "Bengals.png", "@Bengals", "#RuleTheJungle", "AFC", "N", 3)
bengals_logo = api.media_upload(bengals.logo)
bills = NFL_Team("Buffalo Bills", "Bills.png", "@BuffaloBills", "#BillsMafia", "AFC", "E", 4)
bills_logo = api.media_upload(bills.logo)
broncos = NFL_Team("Denver Broncos", "Broncos.png", "@Broncos", "#BroncosCountry", "AFC", "W", 5)
broncos_logo = api.media_upload(broncos.logo)
browns = NFL_Team("Cleveland Browns", "Browns.png", "@Browns", "#Browns", "AFC", "N", 6)
browns_logo = api.media_upload(browns.logo)
buccaneers = NFL_Team("Tampa Bay Buccaneers", "Buccaneers.png", "@Buccaneers", "#GoBucs", "NFC", "S", 7)
buccaneers_logo = api.media_upload(buccaneers.logo)
cardinals = NFL_Team("Arizona Cardinals", "Cardinals.png", "@AZCardinals", "#AZCardinals", "NFC", "W", 8)
cardinals_logo = api.media_upload(cardinals.logo)
chargers = NFL_Team("Los Angeles Chargers", "Chargers.png", "@chargers", "#BoltUp", "AFC", "W", 9)
chargers_logo = api.media_upload(chargers.logo)
chiefs = NFL_Team("Kansas City Chiefs", "Chiefs.png", "@Chiefs", "#ChiefsKingdom", "AFC", "W", 10)
chiefs_logo = api.media_upload(chiefs.logo)
colts = NFL_Team("Indianapolis Colts", "Colts.png", "@Colts", "#ForTheShoe", "AFC", "S", 11)
colts_logo = api.media_upload(colts.logo)
commanders = NFL_Team("Washington Commanders", "Commanders.png", "@Commanders", "#HTTC", "NFC", "E", 12)
commanders_logo = api.media_upload(commanders.logo)
cowboys = NFL_Team("Dallas Cowboys", "Cowboys.png", "@dallascowboys", "#DallasCowboys", "NFC", "E", 13)
cowboys_logo = api.media_upload(cowboys.logo)
dolphins = NFL_Team("Miami Dolphins", "Dolphins.png", "@MiamiDolphins", "#FinsUp", "AFC", "E", 14)
dolphins_logo = api.media_upload(dolphins.logo)
eagles = NFL_Team("Philadelphia Eagles", "Eagles.png", "@Eagles", "#FlyEaglesFly", "NFC", "E", 15)
eagles_logo = api.media_upload(eagles.logo)
falcons = NFL_Team("Atlanta Falcons", "Falcons.png", "@AtlantaFalcons", "#DirtyBirds", "NFC", "S", 16)
falcons_logo = api.media_upload(falcons.logo)
giants = NFL_Team("New York Giants", "Giants.png", "@Giants", "#TogetherBlue", "NFC", "E", 17)
giants_logo = api.media_upload(giants.logo)
jaguars = NFL_Team("Jacksonville Jaguars", "Jaguars.png", "@Jaguars", "#DUUUVAL", "AFC", "S", 18)
jaguars_logo = api.media_upload(jaguars.logo)
jets = NFL_Team("New York Jets", "Jets.png", "@nyjets", "#TakeFlight", "AFC", "E", 19)
jets_logo = api.media_upload(jets.logo)
lions = NFL_Team("Detroit Lions", "Lions.png", "@Lions", "#OnePride", "NFC", "N", 20)
lions_logo = api.media_upload(lions.logo)
packers = NFL_Team("Green Bay Packers", "Packers.png", "@packers", "#GoPackGo", "NFC", "N", 21)
packers_logo = api.media_upload(packers.logo)
panthers = NFL_Team("Carolina Panthers", "Panthers.png", "@Panthers", "#KeepPounding", "NFC", "S", 22)
panthers_logo = api.media_upload(panthers.logo)
patriots = NFL_Team("New England Patriots", "Patriots.png", "@Patriots", "#ForeverNE", "AFC", "E", 23)
patriots_logo = api.media_upload(patriots.logo)
raiders = NFL_Team("Las Vegas Raiders", "Raiders.png", "@Raiders", "#RaiderNation", "AFC", "W", 24)
raiders_logo = api.media_upload(raiders.logo)
rams = NFL_Team("Los Angeles Rams", "Rams.png", "@RamsNFL", "#RamsHouse", "NFC", "W", 25)
rams_logo = api.media_upload(rams.logo)
ravens = NFL_Team("Baltimore Ravens", "Ravens.png", "@Ravens", "#RavensFlock", "AFC", "N", 26)
ravens_logo = api.media_upload(ravens.logo)
saints = NFL_Team("New Orleans Saints", "Saints.png", "@Saints", "#Saints", "NFC", "S", 27)
saints_logo = api.media_upload(saints.logo)
seahawks = NFL_Team("Seattle Seahawks", "Seahawks.png", "@Seahawks", "#Seahawks", "NFC", "W", 28)
seahawks_logo = api.media_upload(seahawks.logo)
steelers = NFL_Team("Pittsburgh Steelers", "Steelers.png", "@steelers", "#HereWeGo", "AFC", "N", 29)
steelers_logo = api.media_upload(steelers.logo)
texans = NFL_Team("Houston Texans", "Texans.png", "@HoustonTexans", "#WeAreTexans", "AFC", "S", 30)
texans_logo = api.media_upload(texans.logo)
titans = NFL_Team("Tennessee Titans", "Titans.png", "@Titans", "#Titans", "AFC", "S", 31)
titans_logo  = api.media_upload(titans.logo)
vikings = NFL_Team("Minnesota Vikings", "Vikings.png", "@Vikings", "#SKOL", "NFC", "N", 32)
vikings_logo =  api.media_upload(vikings.logo)

#initializing the characters
AaronJudge=Character("Aaron Judge", "aaronJudge.jfif", "Judge")
AaronJudge_photo = api.media_upload(AaronJudge.photo)
Perry=Character("Perry the Platypus", "agentP.png", "Agent P")
Perry_photo = api.media_upload(Perry.photo)
Albon=Character("Alex Albon", "albon.png", "Albono")
Albon_photo = api.media_upload(Albon.photo)
Kirk=Character("Alejandro Kirk", "AlejandroKirk.jfif", "Kirk")
Kirk_photo = api.media_upload(Kirk.photo)
Alonso=Character("Fernando Alonso", "Alonso.png", "Nando")
Alonso_photo = api.media_upload(Alonso.photo)
Auston=Character("Auston Matthews", "Auston.png", "Auston")
Auston_photo = api.media_upload(Auston.photo)
Biden=Character("Joe Biden", "biden.jfif", "President Biden")
Biden_photo = api.media_upload(Biden.photo)
BlackWidow=Character("Black Widow", "black widow.jfif", "Natalia")
BlackWidow_photo = api.media_upload(BlackWidow.photo)
BlakeLively=Character("Blake Lively", "blake lively.jfif", "Blake")
BlakeLively_photo = api.media_upload(BlakeLively.photo)
Bichette=Character("Bo Bichette", "boBichette.jfif", "Bo Flows")
Bichette_photo = api.media_upload(Bichette.photo)
Bokoblin=Character("Bokoblin", "bokoblin.jfif", "Boko")
Bokoblin_photo = api.media_upload(Bokoblin.photo)
Boo=Character("Boo", "boo.jfif", "Boo")
Boo_photo = api.media_upload(Boo.photo)
Bottas=Character("Valtteri Bottas", "Bottas.png", "Bottas")
Bottas_photo = api.media_upload(Bottas.photo)
BowserJr=Character("Bowser Jr", "bowser jr.jfif", "Bowser Jr")
BowserJr_photo = api.media_upload(BowserJr.photo)
Bowser=Character("Bowser", "bowser.jfif", "Bowser")
Bowser_photo = api.media_upload(Bowser.photo)
Brian=Character("Brian Griffin", "BrianGriffin.png", "Brian")
Brian_photo = api.media_upload(Brian.photo)
Bryce=Character("Bryce Harper", "bryceHarper.jfif", "Bryce")
Bryce_photo = api.media_upload(Bryce.photo)
Bugs=Character("Bugs Bunny", "BugsBunny.jfif", "Bugs")
Bugs_photo = api.media_upload(Bugs.photo)
Bill=Character("Bullet Bill", "bullet bill.jfif", "Bill")
Bill_photo = api.media_upload(Bill.photo)
Ganon=Character("Calamity Ganon", "calam ganon.jfif", "Ganon")
Ganon_photo = api.media_upload(Ganon.photo)
Cap=Character("Captain America", "cap.jfif", "Cap")
Cap_photo = api.media_upload(Cap.photo)
Carlos=Character("Carlos Sainz Jr.", "CarlosSainz.png", "the Smooth Operator")
Carlos_photo = api.media_upload(Carlos.photo)
Chance=Character("Chance the Rapper", "Chance.jfif", "Chance")
Chance_photo = api.media_upload(Chance.photo)
Charles=Character("Charles Leclerc", "charles.png", "Charles")
Charles_photo = api.media_upload(Charles.photo)
Charli=Character("Charli D'Amelio", "charli damelio.jfif", "Charli")
Charli_photo = api.media_upload(Charli.photo)
Checo=Character("Sergio Perez", "Checo.png", "Checo")
Checo_photo = api.media_upload(Checo.photo)
Chris=Character("Chris Griffin", "chris griffin.png", "Chris")
Chris_photo = api.media_upload(Chris.photo)
Mcdavid=Character("Connor McDavid", "connor mcdavid.jfif", "McJesus")
Mcdavid_photo = api.media_upload(Mcdavid.photo)
Consuela=Character("Consuela", "consuela.jfif", "Consuela")
Consuela_photo = api.media_upload(Consuela.photo)
Daisy=Character("Princess Daisy", "daisy.jfif", "Daisy")
Daisy_photo = api.media_upload(Daisy.photo)
Deadpool=Character("Deadpool", "deadpool.jfif", "Deadpool")
Deadpool_photo = api.media_upload(Deadpool.photo)
DK=Character("Donkey Kong", "DonkeyKong.jfif", "DK")
DK_photo = api.media_upload(DK.photo)
Dora=Character("Dora the Explorer", "Dora.png", "Dora")
Dora_photo = api.media_upload(Dora.photo)
Drake=Character("Drake", "drake.jfif", "Drizzy")
Drake_photo = api.media_upload(Drake.photo)
Dua=Character("Dua Lipa", "dua lipa.jfif", "Dua")
Dua_photo = api.media_upload(Dua.photo)
Fox=Character("Adam Fox", "Fox.png", "Foxy")
Fox_photo = api.media_upload(Fox.photo)
Gasly=Character("Pierre Gasly", "gasly.png", "Gasly")
Gasly_photo = api.media_upload(Gasly.photo)
GR=Character("George Russell", "GeorgeRussell.png", "GR63")
GR_photo = api.media_upload(GR.photo)
Springer=Character("George Springer", "georgeSpringer.jfif", "Springer")
Springer_photo = api.media_upload(Springer.photo)
Goldschmidt=Character("Paul Goldschmidt", "Goldschmidt.jfif", "Goldy")
Goldschmidt_photo = api.media_upload(Goldschmidt.photo)
Goomba=Character("Goomba", "Goomba.png", "Goomba")
Goomba_photo = api.media_upload(Goomba.photo)
Goron=Character("Goron", "goron.jfif", "Goron")
Goron_photo = api.media_upload(Goron.photo)
Fieri=Character("Guy Fieri", "Guy Fieri.jfif", "Mayor of Flavourtown")
Fieri_photo = api.media_upload(Fieri.photo)
Hawkeye=Character("Hawkeye", "hawkeye.jfif", "Clint")
Hawkeye_photo = api.media_upload(Hawkeye.photo)
Hedman=Character("Victor Hedman", "Hedman.png", "Hedman")
Hedman_photo = api.media_upload(Hedman.photo)
Huby=Character("Jonathan Huberdeau", "Huby.png", "Huby")
Huby_photo = api.media_upload(Huby.photo)
Hulk=Character("Hulk", "hulk.jfif", "Bruce")
Hulk_photo = api.media_upload(Hulk.photo)
IMan=Character("Iron Man", "iron man.jfif", "Tony")
IMan_photo = api.media_upload(IMan.photo)
Jack=Character("Jack Harlow", "jack harlow.jfif", "Jack")
Jack_photo = api.media_upload(Jack.photo)
JakePaul=Character("Jake Paul", "jake paul.jfif", "Jake")
JakePaul_photo = api.media_upload(JakePaul.photo)
JayZ=Character("Jay-Z", "jayz.jfif", "HOV")
JayZ_photo = api.media_upload(JayZ.photo)
JCole=Character("J-Cole", "JCole.jfif", "J-Cole")
JCole_photo = api.media_upload(JCole.photo)
Johnny=Character("Johnny Gaudreau", "JohnnyGaudreau.png", "Johnny Hockey")
Johnny_photo = api.media_upload(Johnny.photo)
Josi=Character("Roman Josi", "Josi.png", "Josi")
Josi_photo = api.media_upload(Josi.photo)
JRam=Character("Jose Ramirez", "JRam.jfif", "J-Ram")
JRam_photo = api.media_upload(JRam.photo)
Trudeau=Character("Justin Trudeau", "justinTrudeau.jfif", "the Prime Minister")
Trudeau_photo = api.media_upload(Trudeau.photo)
Kanye=Character("Kanye", "kanye.jfif", "Ye")
Kanye_photo = api.media_upload(Kanye.photo)
Ketchup=Character("Ketchup", "ketchup.jfif", "Ketchup")
Ketchup_photo = api.media_upload(Ketchup.photo)
Khloe=Character("Khloe Kardashian", "khloe kardashian.jfif", "Khloe")
Khloe_photo = api.media_upload(Khloe.photo)
Kim=Character("Kim Kardashian", "kim k.jfif", "Kim")
Kim_photo = api.media_upload(Kim.photo)
Kirill=Character("Kirill Kaprizov", "Kirill.png", "Kirill the Thrill")
Kirill_photo = api.media_upload(Kirill.photo)
KMag=Character("Kevin Magnussen", "KMag.png", "K-Mag")
KMag_photo = api.media_upload(KMag.photo)
Kylie=Character("Kylie Jenner", "kylie.jfif", "Kylie")
Kylie_photo = api.media_upload(Kylie.photo)
Lance=Character("Lance Stroll", "lance.png", "Sir Lancelot")
Lance_photo = api.media_upload(Lance.photo)
Lando=Character("Lando Norris", "Lando.png", "Lando")
Lando_photo = api.media_upload(Lando.photo)
Latifi=Character("Nicholas Latifi", "latifi.png", "Goatifi")
Latifi_photo = api.media_upload(Latifi.photo)
Lebron=Character("Lebron James", "lebron.jfif", "Lebron")
Lebron_photo = api.media_upload(Lebron.photo)
Messi=Character("Leo Messi", "LeoMessi.jfif", "Messi")
Messi_photo = api.media_upload(Messi.photo)
Drai=Character("Leon Draisaitl", "LeonDrai.png", "Drai")
Drai_photo = api.media_upload(Drai.photo)
Lewis=Character("Sir Lewis Hamilton", "Lewis.png", "Lewis")
Lewis_photo = api.media_upload(Lewis.photo)
Link=Character("Link", "link.jfif", "Link")
Link_photo = api.media_upload(Link.photo)
Lois=Character("Lois Griffin", "LoisGriffin.jfif", "Lois")
Lois_photo = api.media_upload(Lois.photo)
Lep=Character("Lucky the Leprechaun", "luckyLep.jfif", "Lucky")
Lep_photo = api.media_upload(Lep.photo)
Luigi=Character("Luigi", "luigi.jfif", "Luigi")
Luigi_photo = api.media_upload(Luigi.photo)
Makar=Character("Cale Makar", "Makar.png", "Cale")
Makar_photo = api.media_upload(Makar.photo)
Machado=Character("Manny Machado", "mannyMachado.jfif", "Manny")
Machado_photo = api.media_upload(Machado.photo)
Mario=Character("Mario", "mario.jfif", "Mario")
Mario_photo = api.media_upload(Mario.photo)
Marner=Character("Mitch Marner", "Marner.png", "Marner")
Marner_photo = api.media_upload(Marner.photo)
Mayo=Character("Mayo", "mayo.jfif", "Mayo")
Mayo_photo = api.media_upload(Mayo.photo)
Mbappe=Character("Kylian Mbappe", "mbappe.jfif", "Mbappe")
Mbappe_photo = api.media_upload(Mbappe.photo)
Meg=Character("Meg Griffin", "meg griffin.jfif", "Meg")
Meg_photo = api.media_upload(Meg.photo)
MJ=Character("Michael Jordan", "michaelJordan.jfif", "MJ")
MJ_photo = api.media_upload(MJ.photo)
Mick=Character("Mick Schumacher", "mick.png", "Mick")
Mick_photo = api.media_upload(Mick.photo)
Mickey=Character("Mickey Mouse", "MickeyMouse.png", "Mickey")
Mickey_photo = api.media_upload(Mickey.photo)
Trout=Character("Mike Trout", "mikeTrout.jfif", "Trout")
Trout_photo = api.media_upload(Trout.photo)
Moblin=Character("Moblin", "moblin.jfif", "Moblin")
Moblin_photo = api.media_upload(Moblin.photo)
Mookie=Character("Mookie Betts", "mookieBetts.jfif", "Mookie")
Mookie_photo = api.media_upload(Mookie.photo)
Mustard=Character("Mustard", "mustard.jfif", "Mustard")
Mustard_photo = api.media_upload(Mustard.photo)
Neymar=Character("Neymar", "neymar.jfif", "Ney")
Neymar_photo = api.media_upload(Neymar.photo)
Ocon=Character("Esteban Ocon", "Ocon.png", "Ocon")
Ocon_photo = api.media_upload(Ocon.photo)
Peach=Character("Princess Peach", "peach.jfif", "Peach")
Peach_photo = api.media_upload(Peach.photo)
Peter=Character("Peter Griffin", "PeterGriffin.jfif", "Peter")
Peter_photo = api.media_upload(Peter.photo)
Phineas=Character("Phineas Fletcher", "phineas.png", "Phineas")
Phineas_photo = api.media_upload(Phineas.photo)
Quagmire=Character("Glenn Quagmire", "quagmire.jfif", "Quagmire")
Quagmire_photo = api.media_upload(Quagmire.photo)
Relish=Character("Relish", "relish.jfif", "Relish")
Relish_photo = api.media_upload(Relish.photo)
Revali=Character("Revali", "revali.jfif", "Revali")
Revali_photo = api.media_upload(Revali.photo)
Ric=Character("Daniel Ricciardo", "Ricciardo.png", "Danny Ric")
Ric_photo = api.media_upload(Ric.photo)
Rih=Character("Rihanna", "rih.jfif", "Rihanna")
Rih_photo = api.media_upload(Rih.photo)
Ronaldo=Character("Cristiano Ronaldo", "ronaldo.jfif", "SUIIII")
Ronaldo_photo = api.media_upload(Ronaldo.photo)
Rosalina=Character("Rosalina", "Rosalina.jfif", "Rosalina")
Rosalina_photo = api.media_upload(Rosalina.photo)
Reyn=Character("Ryan Reynolds", "ryan reynolds.jfif", "Ryan")
Reyn_photo = api.media_upload(Reyn.photo)
Shohei=Character("Shohei Ohtani", "Shohei.jfif", "Shohei")
Shohei_photo = api.media_upload(Shohei.photo)
Sidemen=Character("The Sidemen", "sidemen.jfif", "The Sidemen")
Sidemen_photo = api.media_upload(Sidemen.photo)
Sidon=Character("Sidon", "sidon.jfif", "Sidon")
Sidon_photo = api.media_upload(Sidon.photo)
Pete=Character("Pete Davidson", "skete.jfif", "Skete")
Pete_photo = api.media_upload(Pete.photo)
Sonic=Character("Sonic", "Sonic.jfif", "Sonic")
Sonic_photo = api.media_upload(Sonic.photo)
Spiderman=Character("Spiderman", "spiderman.jfif", "Spidey")
Spiderman_photo = api.media_upload(Spiderman.photo)
Spongebob=Character("Spongebob Squarepants", "Spongebob.png", "Spongebob")
Spongebob_photo = api.media_upload(Spongebob.photo)
Stamkos=Character("Steven Stamkos", "Stamkos.png", "Stammer")
Stamkos_photo = api.media_upload(Stamkos.photo)
Stewie=Character("Stewie Griffin", "StewieGriffin.png", "Stewie")
Stewie_photo = api.media_upload(Stewie.photo)
Thor=Character("Thor", "thor.jfif", "Thor")
Thor_photo = api.media_upload(Thor.photo)
Toad=Character("Toad", "Toad.jfif", "Toad")
Toad_photo = api.media_upload(Toad.photo)
TomH=Character("Tom Holland", "tommy h.jfif", "Tom")
TomH_photo = api.media_upload(TomH.photo)
Tony=Character("Tony the Tiger", "tony the tiger.jfif", "Tony")
Tony_photo = api.media_upload(Tony.photo)
Toucan=Character("Toucan Sam", "toucan sam.jfif", "Sam")
Toucan_photo = api.media_upload(Toucan.photo)
Trump=Character("Donald Trump", "Trump.jfif", "President Trump")
Trump_photo = api.media_upload(Trump.photo)
Tupac=Character("Tupac Shakur", "Tupac.jfif", "Pac")
Tupac_photo = api.media_upload(Tupac.photo)
Tyler=Character("Tyler the Creator", "tylerCreator.jfif", "Tyler")
Tyler_photo = api.media_upload(Tyler.photo)
Uzi=Character("Lil Uzi Vert", "Uzi.jfif", "Uzi")
Uzi_photo = api.media_upload(Uzi.photo)
Max=Character("Max Verstappen", "verstappen.png", "Max")
Max_photo = api.media_upload(Max.photo)
Seb=Character("Sebastian Vettel", "vettel.png", "Seb")
Seb_photo = api.media_upload(Seb.photo)
Vladdy=Character("Vladimir Guerrero Jr.", "vladdy.jfif", "Vladdy")
Vladdy_photo = api.media_upload(Vladdy.photo)
Yoshi=Character("Yoshi", "yoshi.jfif", "Yoshi")
Yoshi_photo = api.media_upload(Yoshi.photo)
Yuki=Character("Yuki Tsunoda", "Yuki Tsunoda.png", "Yuki")
Yuki_photo = api.media_upload(Yuki.photo)
Zendaya=Character("Zendaya", "zendaya.jfif", "Zendaya")
Zendaya_photo = api.media_upload(Zendaya.photo)
Zhou=Character("Zhou Guanyu", "zhouGuanyu.png", "Zhou")
Zhou_photo = api.media_upload(Zhou.photo)
    
def team_generator(): #bare logic to get the random team for the draft. 32 decisions being made. 5 embeded statements. DONT DO IF YOU DONT HAVE TO LOL its PAIN
    team_number = random.randint(1,32)
    print (team_number)
    if team_number <= 16:
        if team_number<=8:
            if team_number<=4:
                if team_number<=2:
                    if team_number==1:
                        team = niners
                        logo = niners_logo
                    else:
                        team = bears
                        logo = bears_logo
                else:
                    if team_number==3:
                        team = bengals
                        logo = bengals_logo
                    else:
                        team = bills
                        logo = bills_logo
            else:
                if 6>=team_number>4:
                    if team_number==5:
                        team = broncos
                        logo = broncos_logo
                    else:
                        team = browns
                        logo = browns_logo
                else:
                    if team_number==7:
                        team = buccaneers
                        logo = buccaneers_logo
                    else:
                        team = cardinals
                        logo = cardinals_logo
        else:
            if 12>=team_number>8:
                if 10>=team_number>8:
                    if team_number==9:
                        team = chargers
                        logo = chargers_logo
                    else:
                        team = chiefs
                        logo = chiefs_logo
                else:
                    if team_number==11:
                        team = colts
                        logo = colts_logo
                    else:
                        team = commanders
                        logo = commanders_logo
            else:
                if 14>=team_number>12:
                    if team_number==13:
                        team = cowboys
                        logo = cowboys_logo
                    else:
                        team = dolphins
                        logo = dolphins_logo
                else:
                    if team_number==15:
                        team = eagles
                        logo = eagles_logo
                    else:
                        team = falcons
                        logo = falcons_logo
    else:
        if 24>=team_number>16:
            if 20>=team_number>16:
                if 18>=team_number>16:
                    if team_number==17:
                        team = giants
                        logo = giants_logo
                    else:
                        team = jaguars
                        logo = jaguars_logo
                else:
                    if team_number==19:
                        team = jets
                        logo = jets_logo
                    else:
                        team = lions
                        logo = lions_logo
            else:
                if 22>=team_number>20:
                    if team_number==21:
                        team = packers
                        logo = packers_logo
                    else:
                        team = panthers
                        logo = panthers_logo
                else:
                    if team_number==23:
                        team = patriots
                        logo = patriots_logo
                    else:
                        team = raiders
                        logo = raiders_logo
        else:
            if 28>=team_number>24:
                if 26>=team_number>24:
                    if team_number==25:
                        team = rams
                        logo = rams_logo
                    else:
                        team = ravens
                        logo = ravens_logo
                else:
                    if team_number==27:
                        team = saints
                        logo = saints_logo
                    else:
                        team = seahawks
                        logo = seahawks_logo
            else:
                if 30>=team_number>28:
                    if team_number==29:
                        team = steelers
                        logo = steelers_logo
                    else:
                        team = texans
                        logo = texans_logo
                else:
                    if team_number==31:
                        team = titans
                        logo = titans_logo
                    else:
                        team = vikings
                        logo = vikings_logo
    return team,logo
                        
def rand_pick():
    pick= str(random.randint(1,259))
    if pick.endswith('1') and not (pick=="11" or pick=="111" or pick=="211"):
        ending="st"
    elif pick.endswith('2') and not (pick=="12" or pick=="112" or pick=="212"):
        ending="nd"
    elif pick.endswith('3') and not (pick=="13" or pick=="113" or pick=="213"):
        ending="rd"
    else:
        ending="th"
    good_pick=pick+ending
    print(good_pick)
    return good_pick

def rand_school():
    team_number = random.randint(1,32)
    if team_number <= 16:
        if team_number<=8:
            if team_number<=4:
                if team_number<=2:
                    if team_number==1:
                        team = "@GeorgiaFootball"
                    else:
                        team = "@AlabamaFTBL"
                else:
                    if team_number==3:
                        team = "@UMichFootball"
                    else:
                        team = "@GoBearcatsFB"
            else:
                if 6>=team_number>4:
                    if team_number==5:
                        team = "@OhioStateFB"
                    else:
                        team = "@BUFootball"
                else:
                    if team_number==7:
                        team = "@CowboyFB"
                    else:
                        team = "@NDFootball"
        else:
            if 12>=team_number>8:
                if 10>=team_number>8:
                    if team_number==9:
                        team = "@MSU_Football"
                    else:
                        team = "@OU_Football"
                else:
                    if team_number==11:
                        team = "@Utah_Football"
                    else:
                        team = "@OleMissFB"
            else:
                if 14>=team_number>12:
                    if team_number==13:
                        team = "@Pitt_FB"
                    else:
                        team = "@UHCougarFB"
                else:
                    if team_number==15:
                        team = "@WakeFB"
                    else:
                        team = "@ClemsonFB"
    else:
        if 24>=team_number>16:
            if 20>=team_number>16:
                if 18>=team_number>16:
                    if team_number==17:
                        team = "@RaginCajunsFB"
                    else:
                        team = "@PackFootball"
                else:
                    if team_number==19:
                        team = "@UKFootball"
                    else:
                        team = "@RazorbackFB"
            else:
                if 22>=team_number>20:
                    if team_number==21:
                        team = "@oregonfootball"
                    else:
                        team = "@BYUfootball"
                else:
                    if team_number==23:
                        team = "@BadgerFootball"
                    else:
                        team = "@USUFootball"
        else:
            if 28>=team_number>24:
                if 26>=team_number>24:
                    if team_number==25:
                        team = "@HawkeyeFootball"
                    else:
                        team = "@AztecFB"
                else:
                    if team_number==27:
                        team = "@UTSAFTBL"
                    else:
                        team = "@AggieFootball"
            else:
                if 30>=team_number>28:
                    if team_number==29:
                        team = "@CoastalFootball"
                    else:
                        team = "@BoilerFootball"
                else:
                    if team_number==31:
                        team = "@PennStateFball"
                    else:
                        team = "@FresnoStateFB"
    print(team)
    return team

def rand_pos():
    team_number = random.randint(1,32)
    if team_number <= 16:
        if team_number<=8:
            if team_number<=4:
                if team_number<=2:
                    if team_number==1:
                        team = "QB"
                    else:
                        team = "QB"
                else:
                    if team_number==3:
                        team = "LB"
                    else:
                        team = "RB"
            else:
                if 6>=team_number>4:
                    if team_number==5:
                        team = "RB"
                    else:
                        team = "RB"
                else:
                    if team_number==7:
                        team = "RB"
                    else:
                        team = "FB"
        else:
            if 12>=team_number>8:
                if 10>=team_number>8:
                    if team_number==9:
                        team = "WR"
                    else:
                        team = "WR"
                else:
                    if team_number==11:
                        team = "WR"
                    else:
                        team = "LB"
            else:
                if 14>=team_number>12:
                    if team_number==13:
                        team = "TE"
                    else:
                        team = "TE"
                else:
                    if team_number==15:
                        team = "OT"
                    else:
                        team = "OT"
    else:
        if 24>=team_number>16:
            if 20>=team_number>16:
                if 18>=team_number>16:
                    if team_number==17:
                        team = "OT"
                    else:
                        team = "LB"
                else:
                    if team_number==19:
                        team = "IOL"
                    else:
                        team = "IOL"
            else:
                if 22>=team_number>20:
                    if team_number==21:
                        team = "CB"
                    else:
                        team = "CB"
                else:
                    if team_number==23:
                        team = "CB"
                    else:
                        team = "S"
        else:
            if 28>=team_number>24:
                if 26>=team_number>24:
                    if team_number==25:
                        team = "S"
                    else:
                        team = "K"
                else:
                    if team_number==27:
                        team = "P"
                    else:
                        team = "DE"
            else:
                if 30>=team_number>28:
                    if team_number==29:
                        team = "DE"
                    else:
                        team = "IDL"
                else:
                    if team_number==31:
                        team = "IDL"
                    else:
                        team = "LB"
    print(team)
    return team

def rand_char():
    team_number=random.randint(1,126)
    if team_number<=64:  
        if team_number<=32:
            if team_number <= 16:
                if team_number<=8:
                    if team_number<=4:
                        if team_number<=2:
                            if team_number==1:
                                team = AaronJudge
                                logo = AaronJudge_photo
                            else:
                                team = Perry
                                logo = Perry_photo
                        else:
                            if team_number==3:
                                team = Albon
                                logo = Albon_photo
                            else:
                                team = Kirk
                                logo = Kirk_photo
                    else:
                        if 6>=team_number>4:
                            if team_number==5:
                                team = Alonso
                                logo = Alonso_photo
                            else:
                                team = Auston
                                logo = Auston_photo
                        else:
                            if team_number==7:
                                team = Biden
                                logo = Biden_photo
                            else:
                                team = BlackWidow
                                logo = BlackWidow_photo
                else:
                    if 12>=team_number>8:
                        if 10>=team_number>8:
                            if team_number==9:
                                team = BlakeLively
                                logo = BlakeLively_photo
                            else:
                                team = Bichette
                                logo = Bichette_photo
                        else:
                            if team_number==11:
                                team = Bokoblin
                                logo = Bokoblin_photo
                            else:
                                team = Boo
                                logo = Boo_photo
                    else:
                        if 14>=team_number>12:
                            if team_number==13:
                                team = Bottas
                                logo = Bottas_photo
                            else:
                                team = BowserJr
                                logo = BowserJr_photo
                        else:
                            if team_number==15:
                                team = Bowser
                                logo = Bowser_photo
                            else:
                                team = Brian
                                logo = Brian_photo
            else:
                if 24>=team_number>16:
                    if 20>=team_number>16:
                        if 18>=team_number>16:
                            if team_number==17:
                                team = Bryce
                                logo = Bryce_photo
                            else:
                                team = Bugs
                                logo = Bugs_photo
                        else:
                            if team_number==19:
                                team = Bill
                                logo = Bill_photo
                            else:
                                team = Ganon
                                logo = Ganon_photo
                    else:
                        if 22>=team_number>20:
                            if team_number==21:
                                team = Cap
                                logo = Cap_photo
                            else:
                                team = Carlos
                                logo = Carlos_photo
                        else:
                            if team_number==23:
                                team = Chance
                                logo = Chance_photo
                            else:
                                team = Charles
                                logo = Charles_photo
                else:
                    if 28>=team_number>24:
                        if 26>=team_number>24:
                            if team_number==25:
                                team = Charli
                                logo = Charli_photo
                            else:
                                team = Checo
                                logo = Checo_photo
                        else:
                            if team_number==27:
                                team = Chris
                                logo = Chris_photo
                            else:
                                team = Mcdavid
                                logo = Mcdavid_photo
                    else:
                        if 30>=team_number>28:
                            if team_number==29:
                                team = Consuela
                                logo = Consuela_photo
                            else:
                                team = Daisy
                                logo = Daisy_photo
                        else:
                            if team_number==31:
                                team = Deadpool
                                logo = Deadpool_photo
                            else:
                                team = DK
                                logo = DK_photo
        else:
            if 48>=team_number > 32:
                if team_number<=40:
                    if team_number<=36:
                        if team_number<=34:
                            if team_number==33:
                                team = Dora
                                logo = Dora_photo
                            else:
                                team = Drake
                                logo = Drake_photo
                        else:
                            if team_number==35:
                                team = Dua
                                logo = Dua_photo
                            else:
                                team = Fox
                                logo = Fox_photo
                    else:
                        if 38>=team_number>36:
                            if team_number==37:
                                team = Gasly
                                logo = Gasly_photo
                            else:
                                team = GR
                                logo = GR_photo
                        else:
                            if team_number==39:
                                team = Springer
                                logo = Springer_photo
                            else:
                                team = Goldschmidt
                                logo = Goldschmidt_photo
                else:
                    if 44>=team_number>40:
                        if 42>=team_number>40:
                            if team_number==41:
                                team = Goomba
                                logo = Goomba_photo
                            else:
                                team = Goron
                                logo = Goron_photo
                        else:
                            if team_number==43:
                                team = Fieri
                                logo = Fieri_photo
                            else:
                                team = Hawkeye
                                logo = Hawkeye_photo
                    else:
                        if 46>=team_number>44:
                            if team_number==45:
                                team = Hedman
                                logo = Hedman_photo
                            else:
                                team = Huby
                                logo = Huby_photo
                        else:
                            if team_number==47:
                                team = Hulk
                                logo = Hulk_photo
                            else:
                                team = IMan
                                logo = IMan_photo
            else:
                if 64>=team_number>48:
                    if 56>=team_number>48:
                        if 52>=team_number>48:
                            if team_number==49:
                                team = Jack
                                logo = Jack_photo
                            else:
                                team = JakePaul
                                logo = JakePaul_photo
                        else:
                            if team_number==51:
                                team = JayZ
                                logo = JayZ_photo
                            else:
                                team = JCole
                                logo = JCole_photo
                    else:
                        if 54>=team_number>52:
                            if team_number==53:
                                team = Johnny
                                logo = Johnny_photo
                            else:
                                team = Josi
                                logo = Josi_photo
                        else:
                            if team_number==55:
                                team = JRam
                                logo = JRam_photo
                            else:
                                team = Trudeau
                                logo = Trudeau_photo
                else:
                    if 60>=team_number>56:
                        if 58>=team_number>56:
                            if team_number==57:
                                team = Kanye
                                logo = Kanye_photo
                            else:
                                team = Ketchup
                                logo = Ketchup_photo
                        else:
                            if team_number==59:
                                team = Khloe
                                logo = Khloe_photo
                            else:
                                team = Kim
                                logo = Kim_photo
                    else:
                        if 62>=team_number>60:
                            if team_number==61:
                                team = Kirill
                                logo = Kirill_photo
                            else:
                                team = KMag
                                logo = KMag_photo
                        else:
                            if team_number==63:
                                team = Kylie
                                logo = Kylie_photo
                            else:
                                team = Lance
                                logo = Lance_photo
    else:
        if 96>=team_number>64:
            if team_number <=80:
                if team_number<=72:
                    if team_number<=68:
                        if team_number<=66:
                            if team_number==65:
                                team = Lando
                                logo = Lando_photo
                            else:
                                team = Latifi
                                logo = Latifi_photo
                        else:
                            if team_number==67:
                                team = Lebron
                                logo = Lebron_photo
                            else:
                                team = Messi
                                logo = Messi_photo
                    else:
                        if 70>=team_number>68:
                            if team_number==69:
                                team = Drai
                                logo = Drai_photo
                            else:
                                team = Lewis
                                logo = Lewis_photo
                        else:
                            if team_number==71:
                                team = Link
                                logo = Link_photo
                            else:
                                team = Lois
                                logo = Lois_photo
                else:
                    if 76>=team_number>72:
                        if 74>=team_number>72:
                            if team_number==73:
                                team = Lep
                                logo = Lep_photo
                            else:
                                team = Luigi
                                logo = Luigi_photo
                        else:
                            if team_number==75:
                                team = Makar
                                logo = Makar_photo
                            else:
                                team = Machado
                                logo = Machado_photo
                    else:
                        if 78>=team_number>76:
                            if team_number==77:
                                team = Mario
                                logo = Mario_photo
                            else:
                                team = Marner
                                logo = Marner_photo
                        else:
                            if team_number==79:
                                team = Mayo
                                logo = Mayo_photo
                            else:
                                team = Mbappe
                                logo = Mbappe_photo
            else:
                if 88>=team_number>80:
                    if 84>=team_number>80:
                        if 82>=team_number>80:
                            if team_number==81:
                                team = Meg
                                logo = Meg_photo
                            else:
                                team = MJ
                                logo = MJ_photo
                        else:
                            if team_number==83:
                                team = Mick
                                logo = Mick_photo
                            else:
                                team = Mickey
                                logo = Mickey_photo
                    else:
                        if 86>=team_number>84:
                            if team_number==85:
                                team = Trout
                                logo = Trout_photo
                            else:
                                team = Moblin
                                logo = Moblin_photo
                        else:
                            if team_number==87:
                                team = Mookie
                                logo = Mookie_photo
                            else:
                                team = Mustard
                                logo = Mustard_photo
                else:
                    if 92>=team_number>88:
                        if 92>=team_number>88:
                            if team_number==89:
                                team = Neymar
                                logo = Neymar_photo
                            else:
                                team = Ocon
                                logo = Ocon_photo
                        else:
                            if team_number==91:
                                team = Peach
                                logo = Peach_photo
                            else:
                                team = Peter
                                logo = Peter_photo
                    else:
                        if 94>=team_number>92:
                            if team_number==93:
                                team = Phineas
                                logo = Phineas_photo
                            else:
                                team = Quagmire
                                logo = Quagmire_photo
                        else:
                            if team_number==95:
                                team = Relish
                                logo = Relish_photo
                            else:
                                team = Revali
                                logo = Revali_photo
        else:
            if 112>=team_number > 96:
                if team_number<=104:
                    if team_number<=100:
                        if team_number<=98:
                            if team_number==97:
                                team = Ric
                                logo = Ric_photo
                            else:
                                team = Rih
                                logo = Rih_photo
                        else:
                            if team_number==99:
                                team = Ronaldo
                                logo = Ronaldo_photo
                            else:
                                team = Rosalina
                                logo = Rosalina_photo
                    else:
                        if 102>=team_number>100:
                            if team_number==101:
                                team = Reyn
                                logo = Reyn_photo
                            else:
                                team = Shohei
                                logo = Shohei_photo
                        else:
                            if team_number==103:
                                team = Sidemen
                                logo = Sidemen_photo
                            else:
                                team = Sidon
                                logo = Sidon_photo
                else:
                    if 108>=team_number>104:
                        if 106>=team_number>104:
                            if team_number==105:
                                team = Pete
                                logo = Pete_photo
                            else:
                                team = Sonic
                                logo = Sonic_photo
                        else:
                            if team_number==107:
                                team = Spiderman
                                logo = Spiderman_photo
                            else:
                                team = Spongebob
                                logo = Spongebob_photo
                    else:
                        if 110>=team_number>108:
                            if team_number==109:
                                team = Stamkos
                                logo = Stamkos_photo
                            else:
                                team = Stewie
                                logo = Stewie_photo
                        else:
                            if team_number==111:
                                team = Thor
                                logo = Thor_photo
                            else:
                                team = Toad
                                logo = Toad_photo
            else:
                if 126>=team_number>112:
                    if 120>=team_number>112:
                        if 116>=team_number>112:
                            if team_number==113:
                                team = TomH
                                logo = TomH_photo
                            else:
                                team = Tony
                                logo = Tony_photo
                        else:
                            if team_number==115:
                                team = Toucan
                                logo = Toucan_photo
                            else:
                                team = Trump
                                logo = Trump_photo
                    else:
                        if 118>=team_number>116:
                            if team_number==117:
                                team = Tupac
                                logo = Tupac_photo
                            else:
                                team = Tyler
                                logo = Tyler_photo
                        else:
                            if team_number==119:
                                team = Uzi
                                logo = Uzi_photo
                            else:
                                team = Max
                                logo = Max_photo
                else:
                    if 124>=team_number>120:
                        if 122>=team_number>120:
                            if team_number==121:
                                team = Seb
                                logo = Seb_photo
                            else:
                                team = Vladdy
                                logo = Vladdy_photo
                        else:
                            if team_number==123:
                                team = Yoshi
                                logo = Yoshi_photo
                            else:
                                team = Yuki
                                logo = Yuki_photo
                    else:
                        if 126>=team_number>124:
                            if team_number==125:
                                team = Zendaya
                                logo = Zendaya_photo
                            else:
                                team = Zhou
                                logo = Zhou_photo
                        
    return team, logo
    
    
                        
def posting(team,logo, good_pick, school, position, char, photo):
    text = "With the "+good_pick+" pick in the NFL Draft, the "+ team.twitter +" select " +char.name+", the "+position+" out of " +school+". Congratulations to the "+ team.hashtag +" fanbase and "+char.short
    new_status = api.update_status(text, media_ids=[logo.media_id_string, photo.media_id_string])

def main():
    while True:
        team,logo = team_generator()
        good_pick = rand_pick()
        school = rand_school()
        position = rand_pos()
        char, photo = rand_char()
        posting(team,logo, good_pick, school, position, char, photo)
        time.sleep(900)
