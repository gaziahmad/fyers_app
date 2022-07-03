from fyers_api import fyersModel
client_id='F4ZJFEICWT-100'
token=open('token.txt', 'r').read().strip()

fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=token)
# print('fyers.get_profile',fyers.get_profile())
# print('fyers.holdings()',fyers.holdings())
# print('fyers.funds()',fyers.funds())
print('fyers.holdings()',fyers.holdings())

symbol = {'symbols':'NSE:ITC-EQ'}
# print(fyers.quotes(symbol))
