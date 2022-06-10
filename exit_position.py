import null as null
from fyers_api import fyersModel
client_id=open('app_id.txt','r').read()
token=open('token.txt', 'r').read().strip()
fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=token,log_path='C:/Users/Tasnim/Desktop/fyers_logs')

data  = {
     "id":"NSE:ITC-EQ"
   }
fyers.exit_positions(data)
print('position exit')

# orderbook = fyers.orderbook()
# print('orderbook() : ',orderbook)
#
# stock_name = orderbook["orderBook"][0]["description"]
# tradedPrice_for_Stock = orderbook["orderBook"][0]["tradedPrice"]
# stopLoss_price = orderbook["orderBook"][0]["stopPrice"]
#
# print('stock_name',stock_name)
# print('tradedPrice_for_Stock',tradedPrice_for_Stock)
# print('stopLoss_price',stopLoss_price)



