import null as null
from fyers_api import fyersModel
client_id='F4ZJFEICWT-100'
access_token_valid = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM3NzU5MDgsImV4cCI6MTY0Mzg0ODIwOCwibmJmIjoxNjQzNzc1OTA4LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaC1nZWtmd1NXZzFBbmVMSTZtcGJRdzA4Y0t2eFNUUHdIbXJpQnRnVDVJSmJvTmRkQ0Q3UnB6VmtMbHdkbVFldGl6Sm5LSEJVZlRJcVNUd01ZalVWTzVlYjRzd2xobHk3djVEbmZKV3JySkJFYTRyQT0iLCJkaXNwbGF5X25hbWUiOiJHQVpJIFNIQU1TSEVSIEFITUFEIiwiZnlfaWQiOiJERzAwMzM5IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6IlkifQ.9qJmlK9tUyG_332SUJjroPD-xHS12wqN1NStSqb6L8E'

fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=access_token_valid,log_path='C:/Users/Tasnim/Desktop/fyers_logs')
order_id={
    'symbol':'NSE:ITC-EQ',
    'qty':1,
    'type':2,
    'side':1,
    'productType':'MARGIN',
    'limitPrice':0,
    'stopPrice':0,
    'validity':'DAY',
    'disclosedQty':0,
    'offlineOrder':'False',
    'stopLoss':0,
    'takeProfit':0}
order_id=fyers.place_order(order_id)['id']
if order_id is None:
    print('order not success, mostly because the market is closed now')

print('order_id',order_id)
orders={'id':order_id}
print(fyers.orderbook(orders))