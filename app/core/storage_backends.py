from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = 'studentitystatic'
    account_key = os.environ.get('AZURE_STORAGE_KEY')
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'studentitystatic' 
    account_key = os.environ.get('AZURE_STORAGE_KEY') 
    azure_container = 'static'
    expiration_secs = None