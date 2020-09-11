from DeepSecurity import *
if __name__ == '__main__':
    #Make a config object with the values for the service.
    config = Config()
    config.api_key="<API KEY>"
    config.host="https://dsm.example.com:4119/api"
    config.verify_ssl=False
    connection = Connection(config=config)

    #Create an object for what your after
    dsComputers = Computers(config=config, connection=connection)
    #Return a listing of all computers
    d = dsComputers.list(expand="Interfaces,webreputation")
    print(d)
    #Create a search object per API spec
    search = {
        'maxItems': 1,
        'searchCriteria': [{
            'idValue': 1,
            'idTest': 'greater-than-or-equal'
        }]
    }
    #Search by id, let the SDK do auto-paging
    c = dsComputers.search(payload=search)
    print(c)

