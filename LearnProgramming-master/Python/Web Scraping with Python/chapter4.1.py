from twitter import *

Consumer_Key = "30aGv0p27w0WuKrR1gf29A"
Consumer_Secret = "vy5YzgctHbO8aYR30cUiKi0r9r2VYLv7kpj49sliHpA"
Access_Token = "10759922-O2GJ0rIEPqJ3gZ4NJU7GC8q8lIkENj2MO7RugmnNM"
Access_Token_Secret = "G5fpMUhUqv11LEoh5Wtrr9am7KcDHd2HJCVK93GloLVgm"

t = Twitter(auth=OAuth(Access_Token, Access_Token_Secret, Consumer_Key, Consumer_Secret))

update = t.statuses.update(status="tweet by python")
print(update)
