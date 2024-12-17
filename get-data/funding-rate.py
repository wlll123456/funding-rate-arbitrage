from binance.client import Client
import json


# 从 secret.txt 读取 API 密钥
def load_api_keys():
    with open('./funding-rate-arbitrage/secret.txt', 'r') as f:
        keys = {}
        for line in f:
            key, value = line.strip().split('=')
            keys[key] = value
    return keys['api_key'], keys['api_secret']

# 获取 API 密钥
api_key, api_secret = load_api_keys()

# 创建现货客户端
client = Client(api_key, api_secret)


def get_spot_order_book(symbol, limit=5):
    """
    获取现货的订单簿数据
    :param symbol: 交易对，例如 'BTCUSDT'
    :param limit: 返回的订单数量，默认 5
    :return: 订单簿数据
    """
    order_book = client.get_order_book(symbol=symbol, limit=limit)
    print(f"现货订单簿 ({symbol}):")
    print(json.dumps(order_book, indent=2))
    return order_book

def get_futures_order_book(symbol, limit=5):
    """
    获取合约的订单簿数据
    :param symbol: 交易对，例如 'BTCUSDT'
    :param limit: 返回的订单数量，默认 5
    :return: 订单簿数据
    """
    order_book = client.futures_order_book(symbol=symbol, limit=limit)
    print(f"合约订单簿 ({symbol}):")
    print(json.dumps(order_book, indent=2))
    return order_book

def get_futures_funding_rate(symbol, limit=5):
    """
    获取合约的资金费率
    :param symbol: 交易对，例如 'BTCUSDT'
    :return: 资金费率数据
    """
    funding_rate = client.futures_funding_rate(symbol=symbol, limit=limit)
    print(f"合约资金费率 ({symbol}):")
    print(json.dumps(funding_rate, indent=2))
    return funding_rate

# 示例调用
spot_order_book = get_spot_order_book('BTCUSDT')
futures_order_book = get_futures_order_book('BTCUSDT')
funding_rate = get_futures_funding_rate('BTCUSDT')