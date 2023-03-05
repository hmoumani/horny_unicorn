import string
import random

# in the_bank.py
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount
    
def is_valid(account):
    if len(dir(account)) % 2 == 0: # an even number of attributes,
        return False
    if any(attr.startswith('b') for attr in dir(account)): # an attribute starting with b
        return False
    if not any(attr.startswith('zip') or attr.startswith('addr') for attr in dir(account)): # no attribute starting with zip or addr
        return False
    if not hasattr(account, 'value') or not hasattr(account, 'name') or not hasattr(account, 'id'): # no attribute name, id and value,
        return False
    if not isinstance(account.name, str): # • name not being a string,
        return False
    if not isinstance(account.id, int): # • id not being an int,
        return False
    if not isinstance(account.value, float) and not isinstance(account.value, int): # • value not being an int or a float.
        return False
    return True
# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        if any(new_account.name == account.name for account in self.accounts):
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, (float, int)):
            return False
        if amount < 0:
            return False
        origin_account = next((account for account in self.accounts if account.name == origin), None)
        dest_account = next((account for account in self.accounts if account.name == dest), None)
        if origin_account is None or dest_account is None:
            return False
        if origin_account.value < amount:
            return False
        if not is_valid(origin_account) or not is_valid(dest_account):
            return False
        if origin_account == dest_account:
            return True
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True
        
    def __try_fix_account(self, account):
        """ try to fix account if corrupted
        @account: Account() account to fix
        @return True if success, False if an error occured
        """
        if len(dir(account)) % 2 == 0: # fix even number of attributes,
            while len(dir(account)) % 2 == 0:
                setattr(account, ''.join(random.choices(string.ascii_uppercase, k=4)), 0)
        for attr in dir(account): # fix attribute starting with b
            if attr.startswith('b'):
                delattr(account, attr)
        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in dir(account)): # fix no attribute starting with zip or addr
            setattr(account, 'zip' + ''.join(random.choices(string.ascii_uppercase, k=4)), 0)
        if not hasattr(account, 'value'):
            setattr(account, 'value', 0)
        if not hasattr(account, 'name'):
            setattr(account, 'name', '')
        if not hasattr(account, 'id'): # no attribute name, id and value,
            setattr(account, 'id', 0)
        if not isinstance(account.name, str): # • name not being a string,
            account.name = str(account.name)
        if not isinstance(account.id, int): # id not being an int
            _id = 0
            ids = [account.id for account in self.accounts]
            while _id in ids:
                account.id += 1
            account.id = _id
        if not isinstance(account.value, float) and not isinstance(account.value, int): # • value not being an int or a float.
            account.value = float(account.value)

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = next((account for account in self.accounts if account.name == name), None)
        if account is None:
            return False
        if is_valid(account):
            return True
        while is_valid(account) is False:
            try:
                self.__try_fix_account(account)
            except Exception as e:
                return False
        return True
