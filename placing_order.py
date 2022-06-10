from fyers_api import fyersModel

client_id = open('app_id.txt', 'r').read()
token = open('token.txt', 'r').read().strip()
fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=token)

symbol = input("Enter the stock symbol")
qty = input("Enter the stock quantity")
typeNumber = input("Enter the stock type number")
side = input("Enter the stock side")
productType = input("Enter the stock productType")
limitPrice = input("Enter the stock limitPrice")
stopPrice = input("Enter the stock stopPrice")
validity = input("Enter the stock validity")
disclosedQty = input("Enter the stock disclosedQty")
offlineOrder = input("Enter the stock offlineOrder")
stopLoss = input("Enter the stock stopLoss")
takeProfit = input("Enter the stock takeProfit")


order_id = {
    'symbol': symbol,
    'qty': qty,
    'type': typeNumber,
    'side': side,
    'productType': productType,
    'limitPrice': limitPrice,
    'stopPrice': stopPrice,
    'validity': validity,
    'disclosedQty': disclosedQty,
    'offlineOrder': offlineOrder,
    'stopLoss': stopLoss,
    'takeProfit': takeProfit}

# order_id={
#     'symbol':'NSE:ZOMATO-EQ',
#     'qty':1,
#     'type':2,
#     'side':1,
#     'productType':'CNC',
#     'limitPrice':0,
#     'stopPrice':0,
#     'validity':'DAY',
#     'disclosedQty':0,
#     'offlineOrder':'False',
#     'stopLoss':0,
#     'takeProfit':0}
order_id = fyers.place_order(order_id)['id']
if order_id is None:
    print('order not successfull, mostly because the market is closed now')

print('order_id', order_id)
orders = {'id': order_id}
print(fyers.orderbook(orders))