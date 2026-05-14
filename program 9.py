from flask import Flask, request, session, redirect

import random
import smtplib

app = Flask(__name__)
app.secret_key = "railway_secret_key"


sender_email = "kavimalardhanasekaran@gmail.com"
sender_password = "mbel yucg njjl wdeu"


@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        otp = str(random.randint(1000,9999))

        session["otp"] = otp
        session["email"] = email

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: Railway OTP\n\nYour OTP is {otp}"

        server.sendmail(sender_email,email,message)

        server.quit()

        return redirect("/verify")


    return """

<!DOCTYPE html>
<html>

<head>

<title>Railway Reservation Login</title>

<style>

body{
font-family:Arial;
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:url("https://images.unsplash.com/photo-1474487548417-781cb71495f3") no-repeat center/cover;
overflow:hidden;
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
backdrop-filter:blur(12px);
box-shadow:0 0 25px black;
text-align:center;
z-index:2;
}

h2{
color:#00eaff;
}

input{
width:100%;
padding:12px;
margin:10px 0;
border-radius:8px;
border:none;
}

button{
width:100%;
padding:12px;
background:#28a745;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
font-size:16px;
}

button:hover{
background:#1e7e34;
}

.trainTrack{
position:absolute;
bottom:0;
left:-300px;
font-size:40px;
animation:trainMove 14s linear infinite;
}

@keyframes trainMove{
0%{left:-300px;}
100%{left:110%;}
}

</style>

</head>

<body>

<div class="card">

<h2>🚆 Railway Login</h2>

<form method="POST">

<input type="email" name="email" placeholder="Enter Email ID" required>

<button type="submit">Send OTP</button>

</form>

</div>

<div class="trainTrack">
🚆🚃🚃🚃🚃
</div>

</body>
</html>

"""


@app.route("/verify", methods=["GET","POST"])
def verify():

    if request.method == "POST":

        user_otp = request.form["otp"]

        if user_otp == session["otp"]:
            return redirect("/reservation")

        return "Invalid OTP"


    return """

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
backdrop-filter:blur(12px);
box-shadow:0 0 25px black;
text-align:center;
}

h2{
color:#00eaff;
}

input{
width:100%;
padding:12px;
margin:10px 0;
border-radius:8px;
border:none;
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

<h2>Enter OTP</h2>

<form method="POST">

<input type="text" name="otp" placeholder="Enter OTP">

<button type="submit">Verify OTP</button>

</form>

</div>

</body>
</html>

"""


@app.route("/reservation", methods=["GET","POST"])
def reservation():

    if request.method == "POST":

        name = request.form["name"]
        from_station = request.form["from"]
        to_station = request.form["to"]
        seats = request.form["seats"]
        travel_class = request.form["class"]

        return f"""

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
background:white;
padding:30px;
border-radius:10px;
width:420px;
text-align:center;
}}

</style>

</head>

<body>

<div class="ticket">

<h2>🎫 Reservation Confirmed</h2>

<p><b>Passenger:</b> {name}</p>
<p><b>From:</b> {from_station}</p>
<p><b>To:</b> {to_station}</p>
<p><b>Seats:</b> {seats}</p>
<p><b>Class:</b> {travel_class}</p>

<h3>🚆 Have a Safe Journey!</h3>

</div>

</body>
</html>

"""


    return """

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
backdrop-filter:blur(12px);
text-align:center;
}

input,select{
width:100%;
padding:12px;
margin:10px 0;
border-radius:8px;
border:none;
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

<h2>🚆 Train Reservation</h2>

<form method="POST">

<input type="text" name="name" placeholder="Passenger Name">

<input type="text" name="from" placeholder="From Station">

<input type="text" name="to" placeholder="To Station">

<input type="number" name="seats" placeholder="No of Seats">

<select name="class">
<option>Sleeper</option>
<option>AC 3 Tier</option>
<option>AC 2 Tier</option>
<option>First Class</option>
</select>

<button type="submit">Confirm Reservation</button>

</form>

</div>

</body>
</html>

"""


if __name__ == "__main__":
    app.run(debug=True)