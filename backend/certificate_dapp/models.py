from django.db import models
from django.http import Http404

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from algosdk.constants import address_len, hash_len, max_asset_decimals, metadata_length
# Algorand SDK functions from the heper.py file
from .helpers import account_balance, account_transactions, passphrase_from_private_key


class Account(models.Model):
    """Base model class for standalone and wallet Algorand accounts."""

    address = models.CharField(max_length=address_len)
    private_key = models.CharField(max_length=address_len + hash_len)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def instance_from_address(cls, address):
        """Return model instance from provided account address."""
        try:
            return cls.objects.get(address=address)
        except ObjectDoesNotExist:
            raise Http404

    def balance(self):
        """Return this instance's balance in microAlgos."""
        return account_balance(self.address)

    @property
    def passphrase(self):
        """Return account's mnemonic."""
        return passphrase_from_private_key(self.private_key)

    def __str__(self):
        """Account's human-readable string representation."""
        return self.address
