from flask import Flask

app = Flask(__name__)

# #######
# Admin Screens
# #######
@app.route("/")
def gibbon_landing():
    return "Gibbon landing"


@app.route("/gibbon404")
def gibbon_404():
    return "Gibbon 404"

# #######
# Break Screens
# #######
@app.route("/on a break")
def on_a_break():
    return "On a break"

# #######
# Gibbon Stats 
# #######

# Top
@app.route("/bluetop")
def blue_top_stat():
    return "Blue top side stats"

@app.route("/redtop")
def red_top_stat():
    return "Red top side stats"

# Jungle
@app.route("/bluejungle")
def blue_jungle_stat():
    return "Blue jungle stats"

@app.route("/redjungle")
def red_jungle_stat():
    return "Red jungle stats"

# Mid
@app.route("/bluemid")
def blue_mid_stat():
    return "Blue mid stats"

@app.route("/redmid")
def red_mid_stat():
    return "Red mid stats"

# Bot
@app.route("/bluebot")
def blue_bot_stat():
    return "Blue bot stats"

@app.route("/redbot")
def red_bot_stat():
    return "Red bot stats"

# Support
@app.route("/bluesupport")
def blue_support_stat():
    return "Blue support stats"

@app.route("/redsupport")
def red_support_stat():
    return "Red support stats"
