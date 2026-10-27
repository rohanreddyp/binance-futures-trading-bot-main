from bot.client import client

try:
    print("Server Time:")
    print(client.futures_time())

    print("\nAccount:")
    print(client.futures_account())

except Exception as e:
    print(type(e).__name__)
    print(e)