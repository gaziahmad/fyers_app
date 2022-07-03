from fyers_api.websocket import ws
from fyers_api import fyersModel
from playsound import playsound

client_id='F4ZJFEICWT-100'
token=open('token.txt', 'r').read().strip()
access_token = client_id+":"+token
data_type = 'symbolData'
# symbol = ['NSE:TATAMOTORS-EQ','NSE:ITC-EQ']
symbol = ['NSE:ITC-EQ']

# stopLoss_price = 220
last_profit = 0
# managing_stoploss = 22022

stopLoss_price = input("Enter the  {} stock stopLoss_price = ".format(symbol[0]))
managing_stoploss = stopLoss_price


def custom_message(ticks):
    global last_price
    global current_order_price
    global stopLoss_price
    global profit
    global last_profit
    global managing_stoploss

    try:
        print('')
        # print('symbol = ', ticks.response[0]['symbol'], ' last_price = ',

        #       ticks.response[0]['ltp'])
        last_price = ticks.response[0]['ltp']

        ## logic for trailing stoploss

        fyers = fyersModel.FyersModel(client_id='F4ZJFEICWT-100', token=token)

        orderbook = fyers.orderbook()
        # print('orderbook() : ', orderbook)

        stock_name = orderbook["orderBook"][0]["description"]
        tradedPrice_for_Stock = orderbook["orderBook"][0]["tradedPrice"]
        side = orderbook["orderBook"][0]["side"]
        # stopLoss_price = orderbook["orderBook"][0]["stopPrice"]

        if(side == 1):
            print('stock_name', stock_name)
            print('tradedPrice= ' + str(tradedPrice_for_Stock) + '  last_price= '+ str(last_price))
            print('original SL= ' + str(stopLoss_price) + '  New SL= '+ str(managing_stoploss))

            # print('new_stopLoss_price', managing_stoploss)

            # print('last_price', last_price)265

            if(last_price > tradedPrice_for_Stock):
                profit = last_price - tradedPrice_for_Stock

            # print('last_profit', last_profit) 265

            if (profit > 0):
                if(last_profit < profit):
                    print('profit', profit)
                    last_profit = profit
                    managing_stoploss = stopLoss_price + profit
                    # print('original SL= ' + 266 + ' New SL=' + )
            else:
                print('loss', - (profit))

            condition_for_selling = last_price - managing_stoploss
            print('condition_for_selling', condition_for_selling)
            if(managing_stoploss >= last_price ):
                order_id = {
                    'symbol': 'NSE:ITC-EQ',
                    'qty': 10,
                    'type': 2,
                    'side': -1,
                    'productType': 'CNC',
                    'limitPrice': 0,
                    'stopPrice': 0,
                    'validity': 'DAY',
                    'disclosedQty': 0,
                    'offlineOrder': 'False',
                    'stopLoss': 0,
                    'takeProfit': 0}
                order_id = fyers.place_order(order_id)['id']
                if order_id is None:
                    print('order not successfull, mostly because the market is closed now')

                print('order_id', order_id)
                orders = {'id': order_id}
                # print(fyers.orderbook(orders))
                playsound('loss.mp3')
                print('equity sold at : ',last_price)

    except Exception as e:
        # print("Exception is handled here, no need to worry, chill !!")
        print(e)


ws.FyersSocket.websocket_data = custom_message
fs = ws.FyersSocket(access_token, data_type,symbol)
fs.subscribe()
