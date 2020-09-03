##SmartCheck
Install thus as normal. 

## Getting Started
Before using thus, you need to provide credentials and hostnames of your services.
You do this by creating a config file. The file should be placed in `~/.thus/credentials`

    [default]
    SCUser = administrator
    SCPassword =  MySuperPassword   
    
This creates a ``default`` profile that has both Deep Security and Smart Check credentials. You can add additional 
profiles for more servers. 

 Next, we need a config file to tell the thus, when using profile `default` what settings we want to use. 
 The file should nbe placed in `~/.thus/config`    
 
    [default]
    SCHost = https://mySmartCheck.example.com:443
    SCverifyssl = False

**Note** The `/api` should **not** be appended to the end of the URL. 

## Using both Deep Security and Smartheck in the configuration
To add Deep Security credentials and configuration to same section, `[default]` you need only to append the values. 

For the credentials file in  `~/.thus/credentials`

    [default]
    DSMapikey = F16564D5-492A-F167-5472-2CEDA60E12D7:GDwCvBV2kV7FjSVuYJXdEqeeeu0WKlls3/sqwu+HEXM=
    SCUser = administrator
    SCPassword =  MySuperPassword   
    
For the configuration file in  `~/.thus/config`    
    
    [default]
    DSMhost = https://mydsm.example.com:443/api
    DSMverifyssl = False
    SCHost = https://mySmartCheck.example.com:443
    SCverifyssl = False