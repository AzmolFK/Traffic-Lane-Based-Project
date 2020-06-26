from twilio.rest import Client

account_sid = 'ACb8db5eda469c18adfa5ad2bd1979d423' # Found on Twilio Console Dashboard
auth_token = '341ab29333f69814042aa8a425410f5f' # Found on Twilio Console Dashboard

myPhone = '+8801521200380' # Phone number you used to verify your Twilio account
TwilioNumber = '+12055399996' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)

client.messages.create(
  to=myPhone,
  from_=TwilioNumber,
  body='Dear Faed, You have been penalized for breaking the traffic rules. Your vehicle no is 2399422.   ' + u'\U0001f680')
