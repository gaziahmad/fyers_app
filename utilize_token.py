from fyers_api import fyersModel

client_id='F4ZJFEICWT-100'
access_token_valid = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM0NzYzOTcsImV4cCI6MTY0MzUwMjYxNywibmJmIjoxNjQzNDc2Mzk3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDlYV3ROaU5vUTlCWVlmTG1pS2lXdkx1WmQwM0psMFhkY3JuTy1uQzU5Zk5hbGtZZUZpcGV2aXloM3NZeWVkQ0JMdVphczFINUlZb2hoemdhWnV0R0ZVaUlpNXFCUGhMU0c4V3JhSm5rU2ZoNVh0bz0iLCJkaXNwbGF5X25hbWUiOiJHQVpJIFNIQU1TSEVSIEFITUFEIiwiZnlfaWQiOiJERzAwMzM5IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6IlkifQ.EQA-h6x47DGati2FhQIEcVt7uubtaI7LkrQfaJWUFGQ'

fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=access_token_valid,log_path='C:/Users/Tasnim/Desktop/fyers_logs')
print('fyers.get_profile',fyers.get_profile())
print('fyers.holdings()',fyers.holdings())
print('fyers.funds()',fyers.funds())
print('fyers.orderbook()',fyers.orderbook())

symbol = {'symbols':'NSE:TATAMOTORS-EQ'}
print(fyers.quotes(symbol))