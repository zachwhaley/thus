from CloudConformity import *
def ReadCFNTemplate(fileName):
    output=""
    with open(fileName, 'r') as f:
        output = f.read()
    return output
if __name__ == '__main__':
    config = Config()
    config.api_key="<API KEY>"
    #Put in your correct endpoint
    config.host="https://us-west-2-api.cloudconformity.com/v1"
    connection = Connection(config=config)

    CCAccounts = Accounts(config=config, connection=connection)
    accounts = CCAccounts.list()
    print(accounts)
    templateToScan = {
        'data': {
            "attributes": {
                "type": "cloudformation-template",
                "contents": ReadCFNTemplate("My_Template.yaml")
            }
        }
    }
    scanner = TemplateScanner(config=config, connection=connection)
    results = scanner.Scan(payload=templateToScan)
    print(results)
