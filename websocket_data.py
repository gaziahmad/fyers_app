from fyers_api.websocket import ws
client_id='F4ZJFEICWT-100'
access_token_valid = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM0NzYzOTcsImV4cCI6MTY0MzUwMjYxNywibmJmIjoxNjQzNDc2Mzk3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDlYV3ROaU5vUTlCWVlmTG1pS2lXdkx1WmQwM0psMFhkY3JuTy1uQzU5Zk5hbGtZZUZpcGV2aXloM3NZeWVkQ0JMdVphczFINUlZb2hoemdhWnV0R0ZVaUlpNXFCUGhMU0c4V3JhSm5rU2ZoNVh0bz0iLCJkaXNwbGF5X25hbWUiOiJHQVpJIFNIQU1TSEVSIEFITUFEIiwiZnlfaWQiOiJERzAwMzM5IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6IlkifQ.EQA-h6x47DGati2FhQIEcVt7uubtaI7LkrQfaJWUFGQ'
access_token = client_id+":"+access_token_valid
data_type = 'symbolData'
symbol = ['NSE:TATAMOTORS-EQ','NSE:ITC-EQ']
def custom_message(ticks):
    print(ticks.response)

ws.FyersSocket.websocket_data = custom_message
fs = ws.FyersSocket(access_token, data_type,symbol)
fs.subscribe()