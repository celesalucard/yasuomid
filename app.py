from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST','GET'])
def input():
    if request.method == 'POST':
      gameid = request.form['gameid']
      return redirect(url_for('matchanal',idgame = gameid))
    else:
      gameid = request.args.get('gameid')
      return redirect(url_for('matchanal',idgame = gameid))

    

@app.route('/matchanal/<idgame>', methods=['GET'])
def matchanal(idgame):
    match_id = idgame
    
    urlmatch = "https://yasapi.herokuapp.com/match/matches_info?match_id=" + str(match_id)
    urlparty = "https://yasapi.herokuapp.com/match/participant?match_id=" + str(match_id)
    
    
    matchdata = requests.get(urlmatch)
    partydata = requests.get(urlparty)
    
    
    #memasukan data ke masing2 variabel agar mudah dipakai
    
    #dari urlmatch
    durasi = matchdata.json()['gameDuration']
    gameId = matchdata.json()['gameId']
    gameMode = matchdata.json()['gameMode']
    gameType = matchdata.json()['gameType']
    gameVersion = matchdata.json()['gameVersion']
    mapId = matchdata.json()['mapId']
    teamWin = matchdata.json()['teamWin']
    bans = matchdata.json()['bans']
    
    
    
    
    
    y = " durasi: " + str(durasi) + "\n id game: " + str(gameId) + "\n gameMode: " + gameMode + "\n gameType: " + gameType + "\n gameVersion: " +gameVersion + "\n mapId: " + str(mapId) + "\n teamWin: " + str(teamWin)
    return str(y)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)