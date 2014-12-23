import os

from waterbutler.core import metadata


class BaseCloudFilesMetadata:

    @property
    def provider(self):
        return 'cloudfiles'


class CloudFilesFileMetadata(BaseCloudFilesMetadata, metadata.BaseFileMetadata):

    @property
    def name(self):
        return os.path.split(self.raw['name'])[1]

    @property
    def path(self):
        return self.raw['name']

    @property
    def size(self):
        return self.raw['bytes']

    @property
    def modified(self):
        return self.raw['last_modified']

    @property
    def content_type(self):
        return self.raw['content_type']


class CloudFilesHeaderMetadata(BaseCloudFilesMetadata, metadata.BaseFileMetadata):

    def __init__(self, raw, path):
        super().__init__(raw)
        self._path = path

    @property
    def name(self):
        return os.path.split(self._path)[1]

    @property
    def path(self):
        return self._path

    @property
    def size(self):
        return int(self.raw['Content-Length'])

    @property
    def modified(self):
        return self.raw['Last-Modified']

    @property
    def content_type(self):
        return self.raw['Content-Type']


class CloudFilesFolderMetadata(BaseCloudFilesMetadata, metadata.BaseFolderMetadata):

    @property
    def name(self):
        return os.path.split(self.raw['subdir'].rstrip('/'))[1]

    @property
    def path(self):
        return self.raw['subdir']
