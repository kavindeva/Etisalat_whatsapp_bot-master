import json
import re
from flask import request
from flask import Flask, jsonify
from twilio.twiml.messaging_response import MessagingResponse

# Initialize our application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images/'


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/whatsapp/conversation/", methods=['POST'])
def whatsapp_upload():
    response = MessagingResponse()
    if request.method == 'POST':
        if request.form:
            userNewResponse = ["hi", "hello", "hi etisalat", "hello etisalat"]
            print("received data from whatsapp")
            msg = request.form.get('Body')
            print(msg)
            ProfileName = request.form.get("ProfileName")
            PersonNumber = request.form.get("From")
            print(type(msg))
            if msg.lower() in userNewResponse:
                print("Greeting matched")
                data = f"*Hi {ProfileName}*\n*Welcome to Etisalat Bot*\nLet me know what kind of service you needed." \
                       f"\n1. Consumer\n2. Business\n3. Carrier & WholeSale\n4. Group"
                replyData = data
            elif re.findall("consumer", msg.lower()):
                print("second loop")
                data = "Which one would you like to look?\n1.1 Mobile plans\n1.2 TV&Internet\n1.3 Devices"
                replyData = data
            elif re.findall("mobile", msg.lower()):
                print("third loop")
                data = "So, Which one you whould prefer? Prepaid or postpaid"
                replyData = data
            elif re.findall("prepaid", msg.lower()):
                print("Fourth loop")
                data = "*Welcome to Etisalat prepaid services*\n In prepaid service currently " \
                       "we have two kinds of schemes. Please let me know what do you want.\n" \
                       "1. wasel-prepaid-line\n2. wasel-flexi"
                replyData = data
            elif re.findall("wasel prepaid line", msg.lower()):
                print("fifth loop")
                jsonFile = open("Etisalat_schemes.json")
                fileData = json.load(jsonFile)
                schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-prepaid-line"][0]
                print(schemeData)
                data = f"*Here your plan*\n{schemeData}"
                replyData = data
            elif re.findall(r"flexi", msg.lower()):
                print("sixth loop")
                data = "*In wasel-flexi we have three various kinds of flexi plans. Please prefer one below.*\n" \
                       "1GB promo, 2GB promo and 3GB promo.\n*Please select one you want."
                replyData = data
            elif re.findall("1gb promo", msg.lower()):
                print("seventh loop")
                jsonFile = open("Etisalat_schemes.json")
                fileData = json.load(jsonFile)
                schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-flexi"][0]
                print(schemeData)
                data = f"*Here your {schemeData}"
                replyData = data
            elif re.findall("2gb promo", msg.lower()):
                print("eighth loop")
                jsonFile = open("Etisalat_schemes.json")
                fileData = json.load(jsonFile)
                schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-flexi"][1]
                print(schemeData)
                data = f"*Here your {schemeData}"
                replyData = data
            elif re.findall("3gb promo", msg.lower()):
                print("ninth loop")
                jsonFile = open("Etisalat_schemes.json")
                fileData = json.load(jsonFile)
                schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-flexi"][2]
                print(schemeData)
                data = f"*Here your {schemeData}"
                replyData = data
            elif re.findall("postpaid", msg.lower()):
                print("tenth loop")
                data = "*Welcome to Etisalat postpaid services*\n In postpaid service currently " \
                       "we have two kinds of schemes. Please let me know what do you want.\n" \
                       "1. New Freedom and\n2. Freedom"
                replyData = data
            elif re.findall("new freedom", msg.lower()):
                print("condition 11")
                data = "*Here your New Freedom plans*\n1. Unlimited 1 Country Plan 325\n2. Unlimited Calls Plan 600" \
                       "\n3. Plan 200\n4. Plan 125\n5. Unlimited Calls Plan 1200\n*Please select one you want."
                replyData = data
            elif re.findall("freedom", msg.lower()):
                print("condition 12")
                data = "*Here your Freedom plans*\n1. Freedom Plan 1000\n2. Freedom Plan 500\n3. Freedom Plan 100" \
                       "\n4. Freedom Plan 175\n5. Freedom Plan 275\n6. Freedom Plan 225\n*Please select one you want."
                replyData = data
            else:
                replyData = "Invalid keywords!. Please enter complete valid keywords."
            response.message(body=replyData, to=PersonNumber)
    return str(response)


if __name__ == '__main__':
    app.run(debug=True, port=8088)
