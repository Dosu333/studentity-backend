from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = 'studentitystatic' # Must be replaced by your <storage_account_name>
    account_key = os.environ.get('AZURE_STORAGE_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'studentitystatic' # Must be replaced by your storage_account_name
    account_key = os.environ.get('AZURE_STORAGE_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
