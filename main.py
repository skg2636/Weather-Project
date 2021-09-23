
from flask import Flask, render_template, request
import time
from database_task import insertUserDetails, checkUser, userLogin
from password_task import validatePassword, encryptPassword
from sendOTP import generateOTP, sendOTP
from weather_details import fetch_weather_details


app = Flask(__name__)

user_data = dict.fromkeys(['name', 'email', 'password', 'address', 'gender', 'otp'], None)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/afterregister/', methods=['GET', 'POST'])
def afterregister():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        email = request.form.get('email_id')
        password = request.form.get('password1')
        password2 = request.form.get('password2')
        name = request.form.get('user_name')
        address = request.form.get('user_address')
        gender = request.form.get('gender')
        result, msg = validatePassword(password, password2)
        checkuser = checkUser(email)
        if result:
            if checkuser == "New User":

                otp = generateOTP(6)
                result, msg = sendOTP(email, otp)
                if result:
                    user_data['name'] = name
                    user_data['email'] = email
                    user_data['password'] = encryptPassword(password)
                    user_data['address'] = address
                    user_data['gender'] = gender
                    user_data['otp'] = otp
                    return render_template('OTPverification.html', email=email)

                else:
                    return render_template('signup.html', msg=msg)
            else:
                return render_template('signup.html', msg=checkuser)





        else:
            return render_template('signup.html', msg=msg)


@app.route('/verifyotp/', methods=['GET', 'POST'])
def verifyOTP():
    if request.method == 'GET':
        return render_template('OTPverification.html')
    else:
        print(user_data)
        input_otp = request.form.get('OTP')
        if user_data['otp'] == input_otp:
            result, msg = insertUserDetails(user_data)
            if result:
                return render_template('developerpage.html')
            else:
                return render_template('OTPverification.html', msg=msg, email=user_data['email'])
        else:
            return render_template('OTPverification.html', msg="WRONG OTP")


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/afterlogin/', methods=['GET', 'POST'])
def afterlogin():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email_id')
        password = request.form.get('password')
        result, msg = userLogin(email, password)
        if result:
            return render_template('developerpage.html')
        else:
            return render_template('login.html', msg=msg)


@app.route('/developerpage/')
def developerpage():
    return render_template('developerpage.html')


@app.route('/getWeather/', methods=['GET','POST'])
def getWeather():
    if request.method == 'GET':
        return render_template('developerpage.html')
    else:
        city_name = request.form.get('city_name')
        data = fetch_weather_details(city_name)
        if data['cod'] == 200:
            t = time.localtime(data['sys']['sunset'])
            sunset = f"{t[3]}:{t[4]}:{t[5]}"
            t = time.localtime(data['sys']['sunrise'])
            sunrise = f"{t[3]}:{t[4]}:{t[5]}"
            data['sys']['sunset'] = sunset
            data['sys']['sunrise']= sunrise
            t = time.localtime(data['dt'])
            updated_time= time.asctime(t)
            return render_template('developerpage.html', data = data,updated_time=updated_time)
        else:
            return render_template('developerpage.html',msg="City Not Found")


app.run(debug=True)
