from contracts.dmag import DMagContract


def get_contract(name=None):
    """return the contract identified by name

    returns a Contract instance

    TODO: for now, this functino returns a DMagContract()
    """
    return DMagContract()
