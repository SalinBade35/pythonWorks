#exercise for banking work

account= [] #empty list

def create_account(name, initial_amount):
    user= {
        'name': name,
        'amount':initial_amount
          }

    account.append(user)  #list ma append garirako xa




    
def get_balance(name):
    for obj in account:
        if obj['name'] == name:
            return obj ['amount']
        else:
            print('user not found')

# def add_balance(name, amount1):
#     for obj in account:
#         if obj['name'] == name:
#             print(obj['name'])
#             obj['amount'] += amount1
#         else:
#             print('user not found')


def checkif(func):
    def referenceFunction(*args, **kwargs):
        for obj in account:
            if obj['amount'] <= 1000:
                print('Amount is less than 1000')
                break
            else:
                func(*args, **kwargs)
    return referenceFunction


@checkif
def add_balance(name, amount1):
    for obj in account:
        if obj['name'] == name:
            amount2= obj["amount"] + amount1
            obj.update({"amount":  amount2})
            obj.get("name")
            print(obj)
            



create_account(name='ram', initial_amount=10000)
# create_account(name='salin', initial_amount=50)
# create_account(name='sampada', initial_amount=2000)
# create_account(name='salina', initial_amount=30)

# add_balance(name='ram', amount1=500)
# add_balance('salin', 5000)
# add_balance('salina', 5000)
add_balance(name='ram', amount1=5000)




# for obj in account:
#     print(obj)
 