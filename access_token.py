from fyers_api import fyersModel
from fyers_api import accessToken
session = accessToken.SessionModel(client_id='F4ZJFEICWT-100',
                                   secret_key='VX8949YAT8', redirect_uri='https://myapi.fyers.in/docs/',
                                   response_type='code', grant_type='authorization_code')
print(session.generate_authcode())
#the auth code below we need to paste from the redirectURL
auth_code = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NDM0NzYzNzQsImV4cCI6MTY0MzUwNjM3NCwibmJmIjoxNjQzNDc1Nzc0LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJERzAwMzM5Iiwibm9uY2UiOiIiLCJhcHBfaWQiOiJGNFpKRkVJQ1dUIiwidXVpZCI6Ijg3M2U0ZDhiZWYwODQxNDdhZmY3NTcxYzJlYjMwZmZmIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.3---n9pKn6HvXBTsloVnv_cuIc77aJGNTBnQDwWvlpk'
session.set_token(auth_code)
response = session.generate_token()
print(response)
access_token = response["access_token"]
print('access_token',access_token)
access_token_valid = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM0NzYzOTcsImV4cCI6MTY0MzUwMjYxNywibmJmIjoxNjQzNDc2Mzk3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDlYV3ROaU5vUTlCWVlmTG1pS2lXdkx1WmQwM0psMFhkY3JuTy1uQzU5Zk5hbGtZZUZpcGV2aXloM3NZeWVkQ0JMdVphczFINUlZb2hoemdhWnV0R0ZVaUlpNXFCUGhMU0c4V3JhSm5rU2ZoNVh0bz0iLCJkaXNwbGF5X25hbWUiOiJHQVpJIFNIQU1TSEVSIEFITUFEIiwiZnlfaWQiOiJERzAwMzM5IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6IlkifQ.EQA-h6x47DGati2FhQIEcVt7uubtaI7LkrQfaJWUFGQ'
