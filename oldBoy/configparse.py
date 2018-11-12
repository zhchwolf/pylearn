import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval':'45',
                     'Compression':'yes',
                     'CompressionLevel':'9'}
config['bitbucket.org'] = {'User': 'hg'}
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini','w') as configfile:
    config.write(configfile)

config.read('example.ini')
print(config.options('bitbucket.org'))
print(config['bitbucket.org']['user'])
print(config.defaults())

for key in config['bitbucket.org']:
    print(key)

config.remove_section('topsecret.server.com')
config.write(open('example.ini','w'))
print(config.has_section('topsecret.server.com'))

config.remove_option('bitbucket.org','user')
config.write(open('example.ini','w'))