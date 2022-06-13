from brownie import network, accounts


LOCAL_CHAINS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_CHAINS:
        return accounts[0]
    
    else:
        accounts.load(input("wallet name:"))
        return accounts[0]
