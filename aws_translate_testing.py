import boto3

# translate = boto3.client(service_name='translate', region_name='us-east-2', use_ssl=True)
#
# result = translate.translate_text(Text="Hello, World", SourceLanguageCode="en", TargetLanguageCode="ar")
# print('TranslatedText: ' + result.get('TranslatedText'))
# print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
# print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
text = "marhaban masa' alkhayr"

print('Calling DetectDominantLanguage')
results = comprehend.detect_dominant_language(Text=text)
print(results)
print(results["Languages"][0]["LanguageCode"])
resutls1 = results["Languages"][0]["LanguageCode"]
print(type(resutls1))
print("End of DetectDominantLanguage\n")
