from fyers_api import fyersModel
from fyers_api import accessToken
session = accessToken.SessionModel(client_id='F4ZJFEICWT-100',
                                   secret_key='VX8949YAT8', redirect_uri='https://myapi.fyers.in/docs/',
                                   response_type='code', grant_type='authorization_code')
print(session.generate_authcode())
#the auth code below we need to paste from the redirectURL
auth_code = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NTU3MTU0NDMsImV4cCI6MTY1NTc0NTQ0MywibmJmIjoxNjU1NzE0ODQzLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJERzAwMzM5Iiwibm9uY2UiOiIiLCJhcHBfaWQiOiJGNFpKRkVJQ1dUIiwidXVpZCI6ImU1NGE4NWRhNThmMjRlOTVhMzE0MDRmNjUyZGMyNjI3IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.jST0xr5Zd_B9kyF6dM5G8bTMjk7my9Vt0BTkO-olZG8'
session.set_token(auth_code)
response = session.generate_token()
print(response)
access_token = response["access_token"]
print('access_token',access_token)
token_file = open("token.txt", "w")
token_file.write(access_token)

# access_token_valid = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM3NzU5MDgsImV4cCI6MTY0Mzg0ODIwOCwibmJmIjoxNjQzNzc1OTA4LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaC1nZWtmd1NXZzFBbmVMSTZtcGJRdzA4Y0t2eFNUUHdIbXJpQnRnVDVJSmJvTmRkQ0Q3UnB6VmtMbHdkbVFldGl6Sm5LSEJVZlRJcVNUd01ZalVWTzVlYjRzd2xobHk3djVEbmZKV3JySkJFYTRyQT0iLCJkaXNwbGF5X25hbWUiOiJHQVpJIFNIQU1TSEVSIEFITUFEIiwiZnlfaWQiOiJERzAwMzM5IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6IlkifQ.9qJmlK9tUyG_332SUJjroPD-xHS12wqN1NStSqb6L8E'
