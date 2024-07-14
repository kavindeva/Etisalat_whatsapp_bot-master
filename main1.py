from switchcase import switch
import json
import re
import boto3
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
            print(request.form)
            print("received data from whatsapp")
            msg = request.form.get('Body')
            print(msg)
            ProfileName = request.form.get("ProfileName")
            PersonNumber = request.form.get("From")
            print(type(msg))
            languageCodes = ['ar', 'ta', 'en']
            translate = boto3.client(service_name='translate', region_name='us-east-2', use_ssl=True)

            def response_process(x):
                replyData = None
                userNewResponse = ["hi", "hello", "hi etisalat", "hello etisalat"]
                for case in switch(x.lower(), comp=re.findall):
                    if case in userNewResponse:
                        print("Greeting matched")
                        data = "*Hello! Which language would you prefer?*\n1. Arabic\n2. Tamil\n3. English"
                        replyData = data
                        break
                    if case("consumer"):
                        print("second loop")
                        data = "Which one would you like to look?\n1.1 Mobile plans\n1.2 TV&Internet\n1.3 Devices"
                        replyData = data
                        break
                    if case("mobile"):
                        print("third loop")
                        data = "So, Which one you whould prefer? Prepaid or postpaid"
                        replyData = data
                        break
                    if case("prepaid"):
                        print("Fourth loop")
                        data = "*Welcome to Etisalat prepaid services*\n In prepaid service currently " \
                               "we have two kinds of schemes. Please let me know what do you want.\n" \
                               "1. wasel-prepaid-line\n2. wasel-flexi"
                        replyData = data
                        break
                    if case("wasel line"):
                        print("fifth loop")
                        jsonFile = open("Etisalat_schemes.json")
                        fileData = json.load(jsonFile)
                        schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-prepaid-line"][0]
                        print(schemeData)
                        data = f"*Here your plan*\n{schemeData}"
                        replyData = data
                        break
                    if case(r"flexi"):
                        print("sixth loop")
                        data = "*In wasel-flexi we have three various kinds of flexi plans. Please prefer one " \
                               "below.*\n1GB promo, 2GB promo and 3GB promo.\n*Please select one you want."
                        replyData = data
                        break
                    if case("1gb promo"):
                        print("seventh loop")
                        jsonFile = open("Etisalat_schemes.json")
                        fileData = json.load(jsonFile)
                        schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-flexi"][0]
                        print(schemeData)
                        data = f"*Here your {schemeData}"
                        replyData = data
                        break
                    if case("2gb promo"):
                        print("eighth loop")
                        jsonFile = open("Etisalat_schemes.json")
                        fileData = json.load(jsonFile)
                        schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-flexi"][1]
                        print(schemeData)
                        data = f"*Here your {schemeData}"
                        replyData = data
                        break
                    if case("3gb promo"):
                        print("ninth loop")
                        jsonFile = open("Etisalat_schemes.json")
                        fileData = json.load(jsonFile)
                        schemeData = fileData["consumer"]["mobile_plans"]["plans"]["pre-paid"]["wasel-flexi"][2]
                        print(schemeData)
                        data = f"*Here your {schemeData}"
                        replyData = data
                        break
                    if case("postpaid"):
                        print("tenth loop")
                        data = "*Welcome to Etisalat postpaid services*\n In postpaid service currently " \
                               "we have two kinds of schemes. Please let me know what do you want.\n" \
                               "1. New Freedom and\n2. Freedom"
                        replyData = data
                        break
                    if case("new freedom"):
                        print("condition 11")
                        data = "*Here your New Freedom plans*\n1. Unlimited 1 Country Plan 325\n" \
                               "2. Unlimited Calls Plan 600\n3. Plan 200\n4. Plan 125\n5. Unlimited " \
                               "Calls Plan 1200\n*Please select one you want."
                        replyData = data
                        break
                    if case("freedom"):
                        print("condition 12")
                        data = "*Here your Freedom plans*\n1. Freedom Plan 1000\n2. Freedom Plan 500" \
                               "\n3. Freedom Plan 100\n4. Freedom Plan 175\n5. Freedom Plan 275" \
                               "\n6. Freedom Plan 225\n*Please select one you want."
                        replyData = data
                        break
                    else:
                        replyData = "Invalid keywords!. Please enter complete valid keywords."
                return replyData

            replyData1 = response_process(msg)
            result = translate.translate_text(Text=replyData1, SourceLanguageCode="en", TargetLanguageCode="ar")
            translatedText = result.get('TranslatedText')
            print(result)
            response.message(body=translatedText, to=PersonNumber)
    return str(response)


if __name__ == '__main__':
    app.run(debug=True, port=8088)
