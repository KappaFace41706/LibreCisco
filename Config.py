
# This is the global settting for whole service.
# Setup will seperated into serveral part by sub-service.
class Config:
    
    #########################################################################
    #                              THREADES                                 #
    #########################################################################

    OUTPUT = {
        'LOG': {
            'LEVEL': 'INFO',
            'FOLDER': './logs',
            'SIZE_PER_FILE': 20*1024*1024,
            'MAX_BACKUP_COUNT': 10
        }
    }

    STATUS_MANAGER = {}

    #########################################################################
    #                              PROCESSES                                #
    #########################################################################

    # Redis for cross-machine process communication.
    REDIS_MANAGER = {
        'ADDRESS': ('redis-15525.c17.us-east-1-4.ec2.cloud.redislabs.com', 15525),
        'PASSWORD': 'LibCisco'
    }
    
    # LIB CISCO: control core
    LIB_CISCO = {}

    # LIB SERVER: control client side such as JLibCisco-cli to access with which ip and port.
    LIB_SERVER = {
        'HOST': '127.0.0.1',
        'PORT' : 25534
    }

    # SWITCH MANAGER: control
    SWITCH_MANAGER = {
        # Temporary database to store the data synced from remote database.
        #   Use sqlite3 to get good IO speed.
        'TEMP_DATABASE': {
            'path': './temp.sqlite'
        },
        # Default login for switch when not username / password can use.
        'DEFAULT_USERNAME' : 'LibServer',
        'DEFAULT_PASSWORD' : 'HoorayYunnet',
        # If both static and database field are set, manager would merge two field's available switch.
        # Static record devices to connect,
        #   if none, just set 'STATIC': None,
        'STATIC': [
            #{ 'host': 'xxx.xxx.xxx.xxx' },
            #{ 'host': 'xxx.xxx.xxx.xxx', 'username': 'username', 'password': 'password' },
        ],
        # Dynamically connect to database to load record. 
        #   if none, just set 'DATABASE': None,
        #   For specified where stores device infor: 
        #      use mongodb, need to use collection field: 'colname': '<COLLECTION_NAME>',
        #      use mysql, need to use table field: 'tabname': '<TABLE_NAME>',
        'DATABASE' : {
            'type': 'mongodb',
            'uri': 'mongodb://libcisco:libcisco@ds155130.mlab.com:55130/libcisco-testmongo',
            'dbName': 'libcisco-testmongo',
            'switchColName': 'switch',
            'ipColName': 'ip'
        },
        # For any api interface to connect to get device info like RESTful framework.
        #   if none, just set 'API': None
        #   Besure API does have right POST url to response data correctly.
        #   Ref: Wiki url for api proviode to LibCisco server.
        'API': {
            'url': 'http://<host>:<port>/api/switch/',
            'method': 'POST',
            'content-type': 'application/json'
        }
    }

    SCHEDULE_MANAGER = {
        'TEMP_DATABASE': {
            'path': './temp.sqlite'
        }
    }
