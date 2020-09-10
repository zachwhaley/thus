## Cloud Conformity

Install thus as normal. 

## Getting Started

Before using thus, you need to provide credentials and hostnames of your services.
You do this by creating a config file. The file should be placed in `~/.thus/credentials`

    [default]
    CCapikey = <API Key from Cloud Conformity console>
    
This creates a ``default`` profile that has both Deep Security and Smart Check credentials. You can add additional 
profiles for more servers. 

 Next, we need a config file to tell the thus, when using profile `default` what settings we want to use. 
 The file should nbe placed in `~/.thus/config`    
 
    [default]
    CCendpoint = https://us-west-2-api.cloudconformity.com/v1
    
 This is the Cloud Conformity end point to use. Currently there are three. See Cloud Conformity link below for details. 
 
 ## Additional Information
 [Cloud Conformity API documents](https://github.com/cloudconformity/documentation-api)
 