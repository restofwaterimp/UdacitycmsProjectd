import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'EQogul.gJY-g7bc.m~yCN1TV5v10m_-282'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage1234'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'mBy+WA3D+tbw6wG9k2S9P0ytepKg+mOhVnuhce79MXhtVgFGU7tgZxBvSWPzb0pCx92sRvqORv+LBd4igUFosw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsproject2.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsproject2db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cms_admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Maidream0925'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # CLIENT_SECRET is client secret value
    CLIENT_SECRET = "EQogul.gJY-g7bc.m~yCN1TV5v10m_-282"
    #CLIENT_SECRET = "_Vyh5XIsGcPfkp0eT3Km8043cpP_xR~t_0"
    #CLIENT_SECRET = "RQ1DV1y2B22ros~xMlAESOVO.Zq.1~OBll"
    
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    #AUTHORITY = "https://login.microsoftonline.com/cmsTenant"

    #Application client ID
    CLIENT_ID = "f14213e5-f176-4187-b3bf-9a2f72ffec61"
  

    #REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/home"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session