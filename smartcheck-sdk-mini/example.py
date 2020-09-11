from SmartCheck import *
if __name__ == '__main__':
    #Make a config object with the values for the service.
    config = Config()
    config.username = "administrator"
    config.password = "<Password>"
    config.host="<host>"
    config.verify_ssl=False
    connection = Connection(config=config)

    regs = Registries(config=config, connection=connection)
    r = regs.list()
    print(r)
    ScanObs = Scans(config=config, connection=connection)
    s = ScanObs.list()
    print(s)


