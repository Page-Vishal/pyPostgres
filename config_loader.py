import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    db_config = {
        'hostname': config['pgsql']['hostname'],
        'database': config['pgsql']['database'],
        'username': config['pgsql']['username'],
        'password': config['pgsql']['password'],
        'port': config['pgsql']['port']
    }
    return db_config