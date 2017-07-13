import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

gameChars = "bayonetta,captain,cloud,dedede,diddy,donkey,duckhunt,falco,fox,gamewatch,ganon,gekkouga,ike,kamui,kirby,koopa,koopajr,link,littlemac,lizardon,lucario,lucas,lucina,luigi,mario,mariod,marth,metaknight,mewtwo,murabito,ness,pacman,palutena,peach,pikachu,pikmin,pit,pitb,purin,reflet,robot,rockman,rosetta,roy,ryu,samus,sheik,shulk,sonic,szerosuit,toonlink,wario,wiifit,yoshi,zelda".split(",")
kuroChars = "Bayonetta,Captain%20Falcon,Cloud,King%20Dedede,Diddy%20Kong,Donkey%20Kong,Duck%20Hunt,Falco,Fox,Game%20And%20Watch,Ganondorf,Greninja,Ike,Corrin,Kirby,Bowser,Bowser%20Jr,Link,Little%20Mac,Charizard,Lucario,Lucas,Lucina,Luigi,Mario,Dr.%20Mario,Marth,Meta%20Knight,Mewtwo,Villager,Ness,PAC-MAN,Palutena,Peach,Pikachu,Olimar,Pit,Dark%20Pit,Jigglypuff,Robin,R.O.B,Mega%20Man,Rosalina%20And%20Luma,Roy,Ryu,Samus,Sheik,Shulk,Sonic,Zero%20Suit%20Samus,Toon%20Link,Wario,Wii%20Fit%20Trainer,Yoshi,Zelda".split(",")

gameToKuro = {}
for i in range(len(gameChars)):
    gameToKuro[gameChars[i]] = kuroChars[i]
kuroName = ""
    
ledgejumpActive=[]
ledgejumpFAF=""
ledgerollActive=[]
ledgerollFAF=""
ledgegetupActive=[]
ledgegetupFAF=""
ledgeattackActive=[]
ledgeattackFAF=""
getupFActive = []
getupFFAF=""
getupBActive = []
getupBFAF = ""
getupfrollFActive = []
getupfrollFFAF = ""
getupfrollBActive = []
getupfrollBFAF = ""
getupbrollFActive = []
getupbrollFFAF = ""
getupbrollBActive = []
getupbrollBFAF = ""
    
def getLedgeData(option):
    global ledgejumpActive, ledgejumpFAF, ledgerollActive, ledgerollFAF, ledgegetupActive, ledgegetupFAF, ledgeattackActive, ledgeattackFAF
    if (option == "ledgejump"):
        if (kuroName == "Shulk" or kuroName == "Duck%20Hunt%20Dog"):
            ledgejumpActive = ['1', '15']
            ledgejumpFAF = '16'
        elif (kuroName == "Palutena"):
            ledgejumpActive = ['1', '16']
            ledgejumpFAF = '17'
        else:
            ledgejumpActive = ['1', '12']
            ledgejumpFAF = '13'
        
    elif (option == "ledgeroll"):
        doc = urlopen("http://kuroganehammer.com/Smash4/LedgeRoll")
        soup = BeautifulSoup(doc,"lxml")
        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber1")
        for table in tables:
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                dodgeData.append([ele for ele in cols if ele])
                for d in dodgeData:
                    if (d[1].replace(" ", "%20").lower() == kuroName.lower() or (kuroName == "Duck%20Hunt" and d[1] =="Duck Hunt Dog") or (kuroName == "King%20Dedede" and d[1] == "Dedede") or (kuroName == "Diddy%20Kong" and d[1] == "Diddy") or (kuroName == "Game%20And%20Watch" and d[1] == "Game & Watch") or (kuroName == "R.O.B" and d[1] == "R.O.B.") or (kuroName == "Rosalina%20And%20Luma" and d[1] == "Rosalina") or (kuroName == "Bowser%20Jr" and d[1] == "Bowser Jr.")):
                        ledgerollActive = d[2].split("-")
                        ledgerollFAF = d[3]
    elif (option == "ledgegetup"):
        doc = urlopen("http://kuroganehammer.com/Smash4/LedgeGetup")
        soup = BeautifulSoup(doc,"lxml")
        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber1")
        for table in tables:
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                dodgeData.append([ele for ele in cols if ele])
                for d in dodgeData:
                    if (d[1].replace(" ", "%20").lower() == kuroName.lower() or (kuroName == "Duck%20Hunt" and d[1] =="Duck Hunt Dog") or (kuroName == "King%20Dedede" and d[1] == "Dedede") or (kuroName == "Diddy%20Kong" and d[1] == "Diddy") or (kuroName == "Game%20And%20Watch" and d[1] == "Game & Watch") or (kuroName == "R.O.B" and d[1] == "R.O.B.") or (kuroName == "Rosalina%20And%20Luma" and d[1] == "Rosalina") or (kuroName == "Bowser%20Jr" and d[1] == "Bowser Jr.")):
                        ledgegetupActive = d[2].split("-")
                        ledgegetupFAF = d[3]
        
    elif (option == "ledgeattack"):
        doc = urlopen("http://kuroganehammer.com/Smash4/LedgeAttack")
        soup = BeautifulSoup(doc,"lxml")
        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber1")
        for table in tables:
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                dodgeData.append([ele for ele in cols if ele])
                for d in dodgeData:
                    if (d[1].replace(" ", "%20").lower() == kuroName.lower() or (kuroName == "Duck%20Hunt" and d[1] =="Duck Hunt Dog") or (kuroName == "King%20Dedede" and d[1] == "Dedede") or (kuroName == "Diddy%20Kong" and d[1] == "Diddy") or (kuroName == "Game%20And%20Watch" and d[1] == "Game & Watch") or (kuroName == "R.O.B" and d[1] == "R.O.B.") or (kuroName == "Rosalina%20And%20Luma" and d[1] == "Rosalina") or (kuroName == "Bowser%20Jr" and d[1] == "Bowser Jr.")):
                        ledgeattackActive = d[2][-5:-1].split("-")
                        ledgeattackFAF = d[3]
                    

def getGetupData(getupOption):
    global getupFActive, getupFFAF, getupBActive, getupBFAF, getupfrollFActive, getupfrollFFAF, getupfrollBActive, getupfrollBFAF, getupbrollFActive, getupbrollFFAF, getupbrollBActive, getupbrollBFAF
    if (getupOption in {"getupF", "getupB"}):
        if (kuroName == "Wii%20Fit%20Trainer"):
            getupFFAF = '29'
        else:
            getupFFAF = '30'
        getupFActive = ['1', '22']
        getupBActive = ['1', '22']
        getupBFAF = '30'
    elif (getupOption in {"getupfrollF", "getupfrollB"}):
        doc = urlopen("http://kuroganehammer.com/Smash4/GetUpForwardRoll")
        soup = BeautifulSoup(doc,"lxml")
        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber1")
        tableNum = 0
        for table in tables:
            tableNum = tableNum + 1
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            notEveryoneElse1 = False
            notEveryoneElse2 = False
            
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                dodgeData.append([ele for ele in cols if ele])
                for d in dodgeData:
                    if (d[1].replace(" ", "%20").lower() == kuroName.lower() or (kuroName == "Duck%20Hunt" and d[1] =="Duck Hunt Dog") or (kuroName == "King%20Dedede" and d[1] == "Dedede") or (kuroName == "Diddy%20Kong" and d[1] == "Diddy") or (kuroName == "Game%20And%20Watch" and d[1] == "Game & Watch") or (kuroName == "R.O.B" and d[1] == "R.O.B.") or (kuroName == "Rosalina%20And%20Luma" and d[1] == "Rosalina") or (kuroName == "Bowser%20Jr" and d[1] == "Bowser Jr.")):
                        if (tableNum == 1):
                            getupfrollBActive = d[2].split("-") 
                            getupfrollBFAF = d[3]
                            notEveryoneElse1 = True
                        if (tableNum == 2):
                            getupfrollFActive = d[2].split("-") 
                            getupfrollFFAF = d[3]
                            notEveryoneElse2 = True
                if (tableNum == 1 and notEveryoneElse1 == False):
                    getupfrollBActive = ['1', '22']
                    getupfrollBFAF = '36'
                if (tableNum == 2 and notEveryoneElse2 == False):
                    getupfrollFActive = ['1', '22']
                    getupfrollFFAF = '36'

    elif (getupOption in {"getupbrollF", "getupbrollB"}):
        doc = urlopen("http://kuroganehammer.com/Smash4/GetUpBackRoll")
        soup = BeautifulSoup(doc,"lxml")
        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber1")
        tableNum = 0
        for table in tables:
            tableNum = tableNum + 1
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            notEveryoneElse1 = False
            notEveryoneElse2 = False
            
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                dodgeData.append([ele for ele in cols if ele])
                for d in dodgeData:
                    if (d[1].replace(" ", "%20").lower() == kuroName.lower() or (kuroName == "Duck%20Hunt" and d[1] =="Duck Hunt Dog") or (kuroName == "King%20Dedede" and d[1] == "Dedede") or (kuroName == "Diddy%20Kong" and d[1] == "Diddy") or (kuroName == "Game%20And%20Watch" and d[1] == "Mr. Game & Watch") or (kuroName == "R.O.B" and d[1] == "R.O.B.") or (kuroName == "Rosalina%20And%20Luma" and d[1] == "Rosalina") or (kuroName == "Bowser%20Jr" and d[1] == "Bowser Jr.")):
                        if (tableNum == 1):
                            getupbrollBActive = d[2].split("-") 
                            getupbrollBFAF = d[3]
                            notEveryoneElse1 = True
                        if (tableNum == 2):
                            getupbrollFActive = d[2].split("-") 
                            getupbrollFFAF = d[3]
                            notEveryoneElse2 = True
                if (tableNum == 1 and notEveryoneElse1 == False):
                    getupbrollBActive = ['1', '22']
                    getupbrollBFAF = '36'
                if (tableNum == 2 and notEveryoneElse2 == False):
                    getupbrollFActive = ['1', '22']
                    getupbrollFFAF = '36'                    
                        
def main():
        if (len(sys.argv) != 2):
            print("Needs one argument: gameChar name")
            exit()
        charName = sys.argv[1]

        global kuroName
        kuroName = gameToKuro[charName]

        doc = urlopen("http://kuroganehammer.com/Smash4/{}".format(gameToKuro[charName]))
        soup = BeautifulSoup(doc,"lxml")
        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber1") 
        for table in tables:
            table_bodies = table.find_all('tbody')
            for table_body in table_bodies:
                rows = table_body.find_all('tr')

                for row in rows:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    dodgeData.append([ele for ele in cols if ele])

        #print(dodgeData)
        spotdodgeActive = dodgeData[len(dodgeData)-4][0].split("-")
        spotdodgeFAF = dodgeData[len(dodgeData)-4][1]
        frollActive = dodgeData[len(dodgeData)-3][0].split("-")
        frollFAF = dodgeData[len(dodgeData)-3][1]
        brollActive = dodgeData[len(dodgeData)-2][0].split("-")
        brollFAF = dodgeData[len(dodgeData)-2][1]
        airdodgeActive = dodgeData[len(dodgeData)-1][0].split("-")
        airdodgeFAF = dodgeData[len(dodgeData)-1][1]
        if (charName == "bayonetta"):
            spotdodgeActive[1] = spotdodgeActive[1].split(" ")[0]
            frollActive[1] = frollActive[1].split(" ")[0]
            brollActive[1] = brollActive[1].split(" ")[0]
            airdodgeActive[1] = airdodgeActive[1].split(" ")[0]
            
        print(spotdodgeActive[0], spotdodgeActive[1], "spotdodgeActive", sep='\t')
        print(spotdodgeFAF, "spotdodgeFAF", sep='\t')
        print(frollActive[0], frollActive[1], "frollActive", sep='\t')
        print(frollFAF, "frollFAF", sep='\t')
        print(brollActive[0], brollActive[1], "brollActive", sep='\t')
        print(brollFAF, "brollFAF", sep='\t')
        print(airdodgeActive[0], airdodgeActive[1], "airdodgeActive", sep='\t')
        print(airdodgeFAF, "airdodgeFAF", sep='\t')

        jumpsquat = dodgeData[5][3][0]
        lightLanding = dodgeData[6][3][0]
        hardLanding = dodgeData[7][3][0]
        
        getLedgeData("ledgejump")
        getLedgeData("ledgeroll")
        getLedgeData("ledgegetup")
        getLedgeData("ledgeattack")
        print(ledgejumpActive[0], ledgejumpActive[1], "ledgejumpActive", sep='\t')
        print(ledgejumpFAF, "ledgejumpFAF", sep='\t')
        print(ledgerollActive[0], ledgerollActive[1], "ledgerollActive", sep='\t')
        print(ledgerollFAF, "ledgerollFAF", sep='\t')
        print(ledgegetupActive[0], ledgegetupActive[1], "ledgegetupActive", sep='\t')
        print(ledgegetupFAF, "ledgegetupFAF", sep='\t')
        print(ledgeattackActive[0], ledgeattackActive[1], "ledgeattackActive", sep='\t')
        print(ledgeattackFAF, "ledgeattackFAF", sep='\t')

        dodgeData = []
        tables = soup.find_all('table', id="AutoNumber2")
        for table in tables:
            table_bodies = table.find_all('tbody')
            for table_body in table_bodies:
                rows = table_body.find_all('tr')
            
                for row in rows:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    dodgeData.append([ele for ele in cols if ele])

        landingLag = [dodgeData[i][-2:-1][0] for i in range(len(dodgeData)) if dodgeData[i][-2:-1][0] != '-']
        landingAirN = landingLag[0]
        landingAirF = landingLag[1]
        landingAirB = landingLag[2]
        landingAirHi = landingLag[3] if (charName != "rockman") else 0
        landingAirLw = landingLag[4] if (charName != "rockman") else landingLag[3]
        landingAirZ = landingLag[5] if (len(landingLag) == 6) else 0

        print(jumpsquat, "jumpsquat", sep="\t")
        print(lightLanding, "lightLanding", sep='\t')
        print(hardLanding, "hardLanding", sep='\t')
        
        print(landingAirN, "landingAirN", sep="\t")
        print(landingAirF, "landingAirF", sep="\t")
        print(landingAirB, "landingAirB", sep="\t")
        print(landingAirHi, "landingAirHi", sep="\t")
        print(landingAirLw, "landingAirLw", sep="\t")
        print(landingAirZ, "landingAirZ", sep="\t")

        getGetupData("getupF")
        getGetupData("getupfrollF")
        getGetupData("getupbrollF")
        print(getupFActive[0], getupFActive[1], "getupFActive", sep="\t")
        print(getupFFAF, "getupFFAF", sep="\t")
        print(getupBActive[0], getupBActive[1], "getupBActive", sep="\t")
        print(getupBFAF, "getupBFAF", sep="\t")
        print(getupfrollFActive[0], getupfrollFActive[1], "getupfrollFActive", sep="\t")
        print(getupfrollFFAF, "getupfrollFFAF", sep="\t")
        print(getupfrollBActive[0], getupfrollBActive[1], "getupfrollBActive", sep="\t")
        print(getupfrollBFAF, "getupfrollBFAF", sep="\t")
        print(getupbrollFActive[0], getupbrollFActive[1], "getupbrollFActive", sep="\t")
        print(getupbrollFFAF, "getupbrollFFAF", sep="\t")
        print(getupbrollBActive[0], getupbrollBActive[1], "getupbrollBActive", sep="\t")
        print(getupbrollBFAF, "getupbrollBFAF", sep="\t")

        passiveActive = ['1', '20']
        passiveFAF = '27'
        passiveFActive = ['1', '20']
        passiveFFAF = '41'
        passiveBActive = ['1', '20']
        passiveBFAF = '41'
        if (charName in {"duckhunt","pacman"}):
            passiveFAF = '26'
            passiveFFAF = '40'
            passiveBFAF = '40'
        if (charName == "rockman"):
            passiveFFAF = '40'
            passiveBFAF = '40'
        if (charName == "littlemac"):
            passiveBFAF = '40'

        print(passiveActive[0], passiveActive[1], "passiveActive", sep="\t")
        print(passiveFAF, "passiveFAF", sep="\t")
        print(passiveFActive[0], passiveFActive[1], "getupBActive", sep="\t")
        print(passiveFFAF, "passiveFFAF", sep="\t")
        print(passiveBActive[0], passiveBActive[1], "passiveBActive", sep="\t")
        print(passiveBFAF, "passiveBFAF", sep="\t")

main()

