import random
import string
from dataclasses import dataclass, field

from banking.account import Account


@dataclass
class Bank:
    accounts: dict[str, Account] = field(default_factory=dict)
    # field() gives you fine-grained control over individual fields in a dataclass, for cases where a simple default value isn't enough.
    # Because mutable defaults (lists, dicts, sets) are shared across all instances in regular Python. default_factory creates a fresh one for each instance.
    #This is because dataclass field defaults are initialized at the class level under the hood

    def create_account(self, name: str) -> Account:
        number = "".join(random.choices(string.digits, k=12))
        account = Account(name, number)
        self.accounts[number] = account
        return account

    def get_account(self, account_number: str) -> Account:
        return self.accounts[account_number]
