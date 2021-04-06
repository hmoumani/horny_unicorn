import string
import random

# in the_bank.py
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount
    def give(self, amount):
        self.value -= amount

    # in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def is_valide(self, account, amount, is_sender=False):
        if type(account) == int or type(account) == str:
            elem = [elem for elem in self.account if elem.id == account or elem.name == account]
            if len(elem) != 1:
                return False
            elem = elem[0]
        else:
            return False
        attrs = dir(elem)
        if (is_sender and elem.value < amount) or len(attrs) % 2 == 0 or any([e[0] == 'b' for e in attrs]) or (not any([e.startswith('zip') or e.startswith('addr') for e in attrs])) or (not all([e in attrs for e in ['name', 'id', 'value']])):
            return False
        return elem

        

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        sender = self.is_valide(origin, amount, True)
        receiver = self.is_valide(dest, amount)
        if amount < 0 or not sender or not receiver:
            return False
        sender.give(amount)
        receiver.transfer(amount)
        return True
        


    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        if type(account) == int or type(account) == str:
            elem = [elem for elem in self.account if elem.id == account or elem.name == account]
            if len(elem) != 1:
                return False
            elem = elem[0]
        else:
            return False
        for attr in dir(elem):
            if attr[0] == 'b':
                delattr(elem, attr)
        if not any([e.startswith('zip') or e.startswith('addr') for e in dir(elem)]):
            setattr(elem, 'zip_safe', '')
        if not hasattr(elem, 'name'):
            setattr(elem, 'name', 'default')
        if not hasattr(elem, 'id'):
            setattr(elem, 'id', Account.ID_COUNT)
            account.ID_COUNT += 1
        if not hasattr(elem, 'value'):
            setattr(elem, 'value', 0)
        if len(dict(elem) %2 == 0):
            setattr(elem, ''.join(random.choices(string.ascii_uppercase , k=5)))
            

acc = Account('houssam', value=0, zip_check=10)
acc1 = Account('test', value=0, zip_check=10)
acc.transfer(8000)
bank = Bank()

bank.add(acc)
bank.add(acc1)

print(bank.transfer(acc, acc1, 150))

print(bank.transfer('houssam', 2, 150))

acc2 = Account('lol', value=0)
bank.add(acc2)

print(bank.transfer('houssam', 'lol', 150))


acc3 = Account('lol1', value=0, zip_check=0 , bambolzed=42)
bank.add(acc3)

print(bank.transfer('houssam', 'lol1', 150))