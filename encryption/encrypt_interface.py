from base64 import b64decode, b64encode
import hashlib
import datetime
import json


class EncryptInterface:

    def __init__(self, name='', password=''):
        self.time = self._get_now_time()
        self.salt = {}
        self.name = name
        self.password = password
    
    def get_token(self):
        self.salt['time'] = self.time
        self.salt['name'] = self.name
        self.salt['password'] = self.password
        self.salt = b64encode(json.dumps(self.salt).encode('utf-8')).decode()
        sha512 = hashlib.sha512()
        sha512.update(self.salt.encode('utf-8'))
        return sha512.hexdigest()

    def _get_now_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

if __name__=='__main__':
    a = EncryptInterface('admin', 'admin123')
    print(a.get_token())