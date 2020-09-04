import json
from DeepSecurity import *
if __name__ == '__main__':
    config = Config()
    config.api_key="E07564D5-492A-F167-8472-1CEDA60E12D7:GDwCVBV1kV4FjsVuYjXdEqeeeu0WKlls3/sQwU+HEXM="
    config.host="https://ec2-34-220-194-214.us-west-2.compute.amazonaws.com:443/api"
    config.verify_ssl=False
    connection = Connection(config=config)

    ds = Computers(config=config, connection=connection)
    search = {
        'maxItems': 1,
        'searchCriteria': {
            'idValue': 1,
            'idTest': 'equal'
        }
    }
    d = ds.list(expand="Interfaces,webreputation")
    c = ds.searchComputer(payload=search)
    print(c)

