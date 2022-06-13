from brownie import config, network, NonceAcademy
from scripts.utils import get_account




def deploy_nonce_academy():

    account = get_account()


    nonce_academy_contract = NonceAcademy.deploy({'from': account}, publish_source=config["networks"][network.show_active()]["verify"])
    
    print("Contract Deployed at: {}".format(nonce_academy_contract.address))
    return nonce_academy_contract



def main():
    deploy_nonce_academy()
