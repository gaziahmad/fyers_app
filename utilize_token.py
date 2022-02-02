from fyers_api import fyersModel

client_id='F4ZJFEICWT-100'
access_token_valid = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM1MjUyNTEsImV4cCI6MTY0MzU4OTAzMSwibmJmIjoxNjQzNTI1MjUxLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDlqU0RRclNoMWFLblE2MW56VnZxVzlReEptNlRRN0xkRmNScUxvMFgyRVZ2ZXVMQ0tQdWkwbzBwZ29sYzdkSjl0cXR6WFdFMWI3U3puU2g4MXNhS29IQjVVWDVxczdOMm9fOXRZejgzYUpZSjMwdz0iLCJkaXNwbGF5X25hbWUiOiJHQVpJIFNIQU1TSEVSIEFITUFEIiwiZnlfaWQiOiJERzAwMzM5IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6IlkifQ.zqzpO0J4dKxv3Anrs-KaOjBiLYaMCoDCtdCRJk6vkX8'

fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=access_token_valid,log_path='C:/Users/Tasnim/Desktop/fyers_logs')
print('fyers.get_profile',fyers.get_profile())
print('fyers.holdings()',fyers.holdings())
print('fyers.funds()',fyers.funds())
print('fyers.orderbook()',fyers.orderbook())

symbol = {'symbols':'NSE:TATAMOTORS-EQ'}
print(fyers.quotes(symbol))