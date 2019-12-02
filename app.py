from flask import Flask, request, jsonify, render_template
import requests
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index.html', title='Yasuomid - LOL Analysis App')

@app.route('/matchanal', methods=['GET'])
def show():
    if 'match_id' in request.args:
        match_id = int(request.args['match_id'])
    else:
        return "Error: No match field provided. Please specify an match."
    
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