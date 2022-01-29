# import sys
# import webbrowser
# from fyers_api import accessToken
# client_id='F4ZJFEICWT-100',
# secret_key='VX8949YAT8',
# appSession = accessToken.SessionModel(client_id,secret_key)
# response = appSession.generate_authcode()
# print('response',response)

# if response["code"] != 200:
#   print(response)
#   sys.exit()
#
# auth_code = response["data"]["authorization_code"]
# print('auth_code',auth_code)
# appSession.set_token(auth_code)
#
# generateTokenUrl = appSession.generate_token()
# print('generateTokenUrl',generateTokenUrl)
#
# webbrowser.open(generateTokenUrl,new=1)