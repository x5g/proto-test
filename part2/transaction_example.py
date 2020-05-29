import transaction_pb2

PB_FILE_PATH = 'transaction.pb'
JSON_FILE_PATH = 'transaction.json'

transaction = transaction_pb2.CompletedTransaction()
money = transaction.amount
money.currency_code = transaction_pb2.CURRENCY_USD
money.value = 200
credit_account = transaction.credit_account
credit_account.accountType = transaction_pb2.PAYTM_WALLET
credit_account.account_identifier = '9898989898'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(transaction.SerializeToString())
f.close()

# 读addressbook
transaction = transaction_pb2.CompletedTransaction()
f = open(PB_FILE_PATH, "rb")
transaction.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(transaction)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

