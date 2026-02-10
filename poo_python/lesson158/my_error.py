class BankErrorAgency(Exception):
    ...

class BankErrorClient(Exception):
    ...

class BankErrorAccount(Exception):
    ...

def raise_agency():
    error_ = BankErrorAgency('Esta agencia não pertence a este banco')
    raise error_

def raise_client():
    error_ = BankErrorClient('Este cliente não pertence a este banco')
    raise error_

def raise_account():
    error_ = BankErrorAccount('Esta conta não pertence a este banco')
    raise error_