## Examples 

Get a list of computers from Deep Security: 

    thus deepsecurity computers list

Get a list of computers from Deep Security with only two expand values: 

    thus deepsecurity computers list expand=interfaces,webreputation

Search Computers using thus's auto-paging to find all computer ID's greater than 0, getting 100 at a time from the server.
    
    thus deepsecurity computers search payload='{ "maxItems": 100, "searchCriteria": [{"idValue": 0, "idTest":"greater-than-or-equal" }] }'

Search Computers using thus's auto-paging to find all computer ID's greater than 0, getting 100 at a time from the server, returning only ec2VirtualMachineSummary data.
    
    thus deepsecurity computers search payload='{ "maxItems": 100, "searchCriteria": [{"idValue": 0, "idTest":"greater-than-or-equal" }] }' expand=ec2VirtualMachineSummary

Search Computers using thus's auto-paging to find all computer ID's greater than 0, getting 100 at a time from the server, returning only ec2VirtualMachineSummary,azureVMVirtualMachineSummary,gcpVirtualMachineSummary  data.
    
    thus deepsecurity computers search payload='{ "maxItems": 100, "searchCriteria": [{"idValue": 0, "idTest":"greater-than-or-equal" }] }' expand=ec2VirtualMachineSummary,azureVMVirtualMachineSummary,gcpVirtualMachineSummary


Get a list of polices from Deep Security: 

    thus deepsecurity policies list

Search all polices for ones which name contains "Windows": 

    thus deepsecurity policies search payload='{ "searchCriteria": [ {"fieldName":"name", "stringValue":"%Windows%", "stringTest":"equal","stringWildcards":true  }] }'
    
Get a list of scans from Smart Check 

    thus smartcheck scans list
 