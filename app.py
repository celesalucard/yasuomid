from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import requests
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        gameid = request.form['gameid']
        return redirect(url_for('matchanal',idgame = gameid))
    else:
        return render_template('index.html')


@app.route('/matchanal/<idgame>', methods=['GET'])
def matchanal(idgame):
    match_id = idgame
    
    urlmatch = "https://yasapi.herokuapp.com/match/matches_info?match_id=" + str(match_id)
    urlparty = "https://yasapi.herokuapp.com/match/participant?match_id=" + str(match_id)
    
    
    matchdata = requests.get(urlmatch)
    partydata = requests.get(urlparty)
    
    
    #memasukan data ke masing2 variabel agar mudah dipakai
    
    #dari urlmatch
    durasi = matchdata.json()['gameDuration'] #int
    gameId = matchdata.json()['gameId'] #int
    gameMode = matchdata.json()['gameMode'] #string
    gameType = matchdata.json()['gameType'] #string
    gameVersion = matchdata.json()['gameVersion'] #string
    mapId = matchdata.json()['mapId'] #int
    teamWin = matchdata.json()['teamWin'] #int , 1 berarti tim 1 menang, 2 berarti tim 2 menang
    bans = matchdata.json()['bans'] #list
    
    
    #dari partydata (team 1= p1-p5, team 2=p6-p10)
    
    #player 1
    summonerName1 = partydata.json()[0]['summonerName'] #string
    championId1 = partydata.json()[0]['championId'] #int
    kills1 = partydata.json()[0]['kills'] #int
    deaths1 = partydata.json()[0]['deaths'] #int
    assists1 = partydata.json()[0]['assists'] #int
    
    #player 2
    summonerName2 = partydata.json()[1]['summonerName'] #string
    championId2 = partydata.json()[1]['championId'] #int
    kills2 = partydata.json()[1]['kills'] #int
    deaths2 = partydata.json()[1]['deaths'] #int
    assists2 = partydata.json()[1]['assists'] #int
    
    #player 3
    summonerName3 = partydata.json()[2]['summonerName'] #string
    championId3 = partydata.json()[2]['championId'] #int
    kills3 = partydata.json()[2]['kills'] #int
    deaths3 = partydata.json()[2]['deaths'] #int
    assists3 = partydata.json()[2]['assists'] #int
    
    #player 4
    summonerName4 = partydata.json()[3]['summonerName'] #string
    championId4 = partydata.json()[3]['championId'] #int
    kills4 = partydata.json()[3]['kills'] #int
    deaths4 = partydata.json()[3]['deaths'] #int
    assists4 = partydata.json()[3]['assists'] #int
    
    #player 5
    summonerName5 = partydata.json()[4]['summonerName'] #string
    championId5 = partydata.json()[4]['championId'] #int
    kills5 = partydata.json()[4]['kills'] #int
    deaths5 = partydata.json()[4]['deaths'] #int
    assists5 = partydata.json()[4]['assists'] #int
    
    #player 6
    summonerName6 = partydata.json()[5]['summonerName'] #string
    championId6 = partydata.json()[5]['championId'] #int
    kills6 = partydata.json()[5]['kills'] #int
    deaths6 = partydata.json()[5]['deaths'] #int
    assists6 = partydata.json()[5]['assists'] #int
    
    #player 7
    summonerName7 = partydata.json()[6]['summonerName'] #string
    championId7 = partydata.json()[6]['championId'] #int
    kills7 = partydata.json()[6]['kills'] #int
    deaths7 = partydata.json()[6]['deaths'] #int
    assists7 = partydata.json()[6]['assists'] #int
    
    #player 8
    summonerName8 = partydata.json()[7]['summonerName'] #string
    championId8 = partydata.json()[7]['championId'] #int
    kills8 = partydata.json()[7]['kills'] #int
    deaths8 = partydata.json()[7]['deaths'] #int
    assists8 = partydata.json()[7]['assists'] #int
    
    #player 9
    summonerName9 = partydata.json()[8]['summonerName'] #string
    championId9 = partydata.json()[8]['championId'] #int
    kills9 = partydata.json()[8]['kills'] #int
    deaths9 = partydata.json()[8]['deaths'] #int
    assists9 = partydata.json()[8]['assists'] #int
    
    #player 10
    summonerName10 = partydata.json()[9]['summonerName'] #string
    championId10 = partydata.json()[9]['championId'] #int
    kills10 = partydata.json()[9]['kills'] #int
    deaths10 = partydata.json()[9]['deaths'] #int
    assists10 = partydata.json()[9]['assists'] #int
    
    
    #untuk tes apakah terintegrasi
    y = " durasi: " + str(durasi) + "\n id game: " + str(gameId) + "\n gameMode: " + gameMode + "\n gameType: " + gameType + "\n gameVersion: " +gameVersion + "\n mapId: " + str(mapId) + "\n teamWin: " + str(teamWin)
    return str(y)
    
    
    
    
    #return render_template('yasuomid.html',)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)