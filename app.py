from flask import Flask, request, session, redirect

import random
import smtplib

app = Flask(__name__)
app.secret_key = "railway_secret_key"

# YOUR EMAIL
sender_email = "kavimalardhanasekaran@gmail.com"
sender_password = "sptzulamxbhzaipg"


# HOME PAGE

@app.route("/")
def home():

    return '''

<!DOCTYPE html>
<html>

<head>

<title>Railway Booking Portal</title>

<style>

body{
margin:0;
font-family:Arial;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
color:white;
overflow:hidden;
}

body::before{
content:"";
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.65);
z-index:-1;
}

header{
display:flex;
align-items:center;
padding:15px 30px;
background:rgba(0,0,0,0.6);
}

header img{
width:45px;
margin-right:10px;
}

nav{
margin-left:auto;
}

nav a{
color:white;
text-decoration:none;
margin:15px;
font-weight:bold;
}

.hero{
text-align:center;
padding:150px 20px;
}

.hero h1{
font-size:48px;
color:#00ffff;
text-shadow:0 0 20px cyan;
}

button{
padding:14px 25px;
background:#ff6600;
color:white;
border:none;
border-radius:8px;
font-size:18px;
cursor:pointer;
}

button:hover{
background:#ff3300;
transform:scale(1.05);
}

.train{
position:fixed;
bottom:10px;
left:-300px;
font-size:40px;
animation:move 12s linear infinite;
}

@keyframes move{
0%{left:-300px;}
100%{left:110%;}
}

</style>

</head>

<body>

<header>

<img src="https://cdn-icons-png.flaticon.com/512/69/69524.png">

<h2>Mountain Rail Reservation</h2>

<nav>
<a href="/">Home</a>
<a href="/login">Login</a>
</nav>

</header>

<div class="hero">

<h1>🚆 Online Railway Reservation System</h1>

<p>
Book scenic railway journeys easily and securely
</p>

<br>

<button onclick="window.location.href='/login'">
Login To Continue
</button>

</div>

<div class="train">
🚆🚃🚃🚃🚃
</div>

</body>

</html>

'''


# LOGIN PAGE

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        otp = str(random.randint(1000,9999))

        session["otp"] = otp
        session["email"] = email

        try:

            server = smtplib.SMTP("smtp.gmail.com",587)

            server.starttls()

            server.login(sender_email, sender_password)

            message = f"Subject: Railway OTP\n\nYour OTP is {otp}"

            server.sendmail(sender_email,email,message)

            server.quit()

        except:
            print("Mail Sending Failed")

        return redirect("/verify")


    return '''

<!DOCTYPE html>
<html>

<head>

<title>Railway Login</title>

<style>

body{
font-family:Arial;
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
}

body::before{
content:"";
position:absolute;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.6);
}

.card{
width:420px;
padding:30px;
border-radius:15px;
background:rgba(255,255,255,0.15);
backdrop-filter:blur(10px);
text-align:center;
z-index:2;
}

h2{
color:#00ffff;
}

input{
width:100%;
padding:12px;
margin:10px 0;
border:none;
border-radius:8px;
}

button{
width:100%;
padding:12px;
background:#28a745;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

</head>

<body>

<div class="card">

<h2>🚆 Passenger Login</h2>

<form method="POST">

<input type="email" name="email" placeholder="Enter Email ID" required>

<button type="submit">Send OTP</button>

</form>

</div>

</body>

</html>

'''


# OTP PAGE

@app.route("/verify", methods=["GET","POST"])
def verify():

    if request.method == "POST":

        user_otp = request.form["otp"]

        if user_otp == session["otp"]:

            return redirect("/catalogue")

        else:

            return "Invalid OTP"


    return '''

<!DOCTYPE html>
<html>

<head>

<title>Verify OTP</title>

<style>

body{
font-family:Arial;
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
}

body::before{
content:"";
position:absolute;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.6);
}

.card{
width:420px;
padding:30px;
border-radius:15px;
background:rgba(255,255,255,0.15);
backdrop-filter:blur(10px);
text-align:center;
z-index:2;
}

h2{
color:#00ffff;
}

input{
width:100%;
padding:12px;
margin:10px 0;
border:none;
border-radius:8px;
}

button{
width:100%;
padding:12px;
background:#28a745;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

</head>

<body>

<div class="card">

<h2>🔐 Verify OTP</h2>

<form method="POST">

<input type="text" name="otp" placeholder="Enter OTP">

<button type="submit">Verify OTP</button>

</form>

</div>

</body>

</html>

'''


# TRAIN CATALOGUE

@app.route("/catalogue")
def catalogue():

    return '''

<!DOCTYPE html>
<html>

<head>

<title>Train Catalogue</title>

<style>

body{
font-family:Arial;
margin:0;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
color:white;
}

body::before{
content:"";
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.65);
z-index:-1;
}

h1{
text-align:center;
padding-top:20px;
}

.trains{
display:flex;
justify-content:center;
gap:20px;
flex-wrap:wrap;
padding:40px;
}

.card{
width:250px;
background:white;
color:black;
padding:10px;
border-radius:10px;
}

.card img{
width:100%;
border-radius:10px;
}

button{
padding:10px;
width:100%;
background:green;
color:white;
border:none;
border-radius:6px;
cursor:pointer;
}

</style>

</head>

<body>

<h1>🚆 Available Trains</h1>

<div class="trains">

<div class="card">

<img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee">

<h3>Mountain Express</h3>

<p>Chennai → Bangalore</p>

<button onclick="window.location.href='/tracker'">
Select Train
</button>

</div>

<div class="card">

<img src="https://images.unsplash.com/photo-1474487548417-781cb71495f3">

<h3>Royal Coach</h3>

<p>Delhi → Mumbai</p>

<button onclick="window.location.href='/tracker'">
Select Train
</button>

</div>

<div class="card">

<img src="https://images.unsplash.com/photo-1519677100203-a0e668c92439">

<h3>Golden Chariot</h3>

<p>Hyderabad → Goa</p>

<button onclick="window.location.href='/tracker'">
Select Train
</button>

</div>

</div>

</body>

</html>

'''


# ROUTE TRACKER

@app.route("/tracker")
def tracker():

    return '''

<!DOCTYPE html>
<html>

<head>

<title>Railway Route Tracker</title>

<style>

body{
font-family:Arial;
text-align:center;
margin:0;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
color:white;
}

body::before{
content:"";
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.65);
z-index:-1;
}

.map-container{
position:relative;
display:inline-block;
margin-top:20px;
}

.map-container img{
width:700px;
border-radius:10px;
}

.marker{
position:absolute;
width:20px;
height:20px;
background:red;
border:none;
border-radius:50%;
cursor:pointer;
}

#info{
margin-top:20px;
font-size:20px;
font-weight:bold;
color:yellow;
}

button{
margin-top:20px;
padding:12px 20px;
background:green;
color:white;
border:none;
border-radius:6px;
cursor:pointer;
}

</style>

<script>

function showStation(station){

let msg="";

if(station=="chennai")
msg="🚆 Chennai → Bangalore";

else if(station=="bangalore")
msg="🚆 Bangalore → Hyderabad";

else if(station=="hyderabad")
msg="🚆 Hyderabad → Delhi";

else if(station=="delhi")
msg="🚆 Delhi Junction Reached";

document.getElementById("info").innerHTML=msg;

}

</script>

</head>

<body>

<h1>🚆 Railway Route Tracker</h1>

<div class="map-container">

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT9QCch94pAgSVg9qTVRc6HUW9t4oc22q8YA&s">

<button class="marker"
style="left:470px; top:430px;"
onclick="showStation('chennai')"></button>

<button class="marker"
style="left:430px; top:400px;"
onclick="showStation('bangalore')"></button>

<button class="marker"
style="left:420px; top:350px;"
onclick="showStation('hyderabad')"></button>

<button class="marker"
style="left:380px; top:200px;"
onclick="showStation('delhi')"></button>

</div>

<div id="info">
Click a station
</div>

<br>

<button onclick="window.location.href='/reservation'">
Continue Booking
</button>

</body>

</html>

'''


# RESERVATION PAGE

@app.route("/reservation", methods=["GET","POST"])
def reservation():

    if request.method == "POST":

        session["name"] = request.form["name"]
        session["from"] = request.form["from"]
        session["to"] = request.form["to"]
        session["date"] = request.form["date"]
        session["seats"] = request.form["seats"]
        session["class"] = request.form["class"]

        return redirect("/payment")


    return '''

<!DOCTYPE html>
<html>

<head>

<title>Train Reservation</title>

<style>

body{
font-family:Arial;
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
}

.card{
width:420px;
padding:30px;
border-radius:15px;
background:rgba(255,255,255,0.15);
backdrop-filter:blur(10px);
text-align:center;
}

input,select{
width:100%;
padding:12px;
margin:10px 0;
border:none;
border-radius:8px;
}

button{
width:100%;
padding:12px;
background:green;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

h2{
color:#00ffff;
}

</style>

</head>

<body>

<div class="card">

<h2>🚆 Reservation Form</h2>

<form method="POST">

<input type="text" name="name" placeholder="Passenger Name" required>

<input type="text" name="from" placeholder="From Station" required>

<input type="text" name="to" placeholder="To Station" required>

<input type="date" name="date" required>

<input type="number" name="seats" placeholder="No of Seats" required>

<select name="class">

<option>Sleeper</option>
<option>AC 3 Tier</option>
<option>AC 2 Tier</option>
<option>First Class</option>

</select>

<button type="submit">
Proceed To Payment
</button>

</form>

</div>

</body>

</html>

'''


# PAYMENT PAGE

@app.route("/payment", methods=["GET","POST"])
def payment():

    if request.method == "POST":

        return redirect("/ticket")


    return '''

<!DOCTYPE html>
<html>

<head>

<title>Payment</title>

<style>

body{
font-family:Arial;
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
}

.card{
width:420px;
padding:30px;
border-radius:15px;
background:white;
text-align:center;
}

input{
width:100%;
padding:12px;
margin:10px 0;
border-radius:8px;
border:1px solid gray;
}

button{
width:100%;
padding:12px;
background:green;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

</head>

<body>

<div class="card">

<h2>💳 Payment Page</h2>

<form method="POST">

<input type="text" placeholder="Card Number" required>

<input type="text" placeholder="Card Holder Name" required>

<input type="password" placeholder="CVV" required>

<button type="submit">
Pay Now
</button>

</form>

</div>

</body>

</html>

'''


# FINAL TICKET PAGE

@app.route("/ticket")
def ticket():

    return f'''

<!DOCTYPE html>
<html>

<head>

<title>Ticket Confirmation</title>

<style>

body{{
font-family:Arial;
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
}}

.ticket{{
width:450px;
padding:30px;
background:white;
border-radius:12px;
text-align:center;
}}

h2{{
color:green;
}}

</style>

</head>

<body>

<div class="ticket">

<h2>🎫 Reservation Confirmed</h2>

<p><b>Passenger:</b> {session["name"]}</p>

<p><b>From:</b> {session["from"]}</p>

<p><b>To:</b> {session["to"]}</p>

<p><b>Date:</b> {session["date"]}</p>

<p><b>Seats:</b> {session["seats"]}</p>

<p><b>Class:</b> {session["class"]}</p>

<h3>🚆 Have a Safe Journey!</h3>

</div>

</body>

</html>

'''


if __name__ == "__main__":
    app.run(debug=True)