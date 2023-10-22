import os
import csv, json
import w3storage
from flask import Flask, flash, render_template as render, redirect, request

with open("/home/gabriel/prog/json_config/gobchainboard.json") as config_file:
    sec_config = json.load(config_file)

app = Flask(__name__, static_url_path='/static')
app.secret_key = sec_config['SECRET_KEY']

ALLFILES = [
    'bafybeify4liulrj65tt2mnnig2whhbqp642frhyqvrswj75e6hwqp5cffa',
    'bafybeigd4p2qnarbcna5jpxcmhpkcsnnsaysalqxmxqid224ibqm3lshvq'
]

@app.route('/', methods=['GET', 'POST'])
def home():

    return render("home.html", title="Home")


@app.route('/loadFile', methods=['GET', 'POST'])
def loadFile():
    allInstr = []
    if request.method == "POST":

        filefrom = "/home/gabriel/prog/ETH/speed/challenge-1-decentralized-staking-main/packages/hardhat/contracts/"
        
        # Connect to web3_storage
        if request.method == "POST":
            fileinn = request.files.get("fileinn")
            namefile = fileinn.filename

            # Connect to web3_storage
            w3 = w3storage.API(token=sec_config['API_TOKEN'])
            some_uploads = w3.user_uploads(size=25)

            contrato_cid = w3.post_upload((filefrom + namefile, 'contract'))

            ALLFILES.append(contrato_cid)

            print(contrato_cid)
            return redirect("listFiles")

    return render("loadFile.html", title="LoadFile")


@app.route('/listFiles', methods=['GET', 'POST'])
def listFiles():
    filesList = ALLFILES

    return render("allFiles.html", title="Files List", filesList=filesList)


if __name__ == '__main__':
    #app.run(debug=True, host="<ip address>", port=8080)
    app.run(debug=True, host="localhost", port=5000)

