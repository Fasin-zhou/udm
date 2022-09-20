import base64
from Crypto.Cipher import AES
from Crypto import Random
import random
import string


class EncryptAes:

    def __init__(self,pwd):
        '''
        CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
        '''
        self.key = self._check_key('deshangyunxing12')
        self.pwd = pwd
        self.BS = 16
        self.mode = AES.MODE_CBC
        self.random_string = self._get_random_string(self.BS - len(pwd.encode()) % self.BS)
        self.pad = lambda s: s + self.random_string
        self.unpad = lambda s: (s[: -(self.BS - len(pwd.encode()) % self.BS)])

    def _check_key(self, key):
        '''
        检测key的长度是否为16,24或者32bytes的长度
        '''
        try:
            if isinstance(key, bytes):
                assert len(key) in [16, 24, 32]
                return key
            elif isinstance(key, str):
                assert len(key.encode()) in [16, 24, 32]
                return key.encode()
            else:
                raise Exception(f'密钥必须为str或bytes,不能为{type(key)}')
        except AssertionError:
            print('输入的长度不正确')

    def _get_random_string(self,str_len):
        return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(str_len))

    def check_data(self, data):
        '''
        检测加密的数据类型
        '''
        if isinstance(data, int):
            data = str(data)
        elif isinstance(data, bytes):
            data = data.decode()
        elif isinstance(data, str):
            pass
        else:
            raise Exception(f'加密的数据必须为str或bytes,不能为{type(data)}')
        return data

    def encrypt(self):
        self.pwd = self.check_data(self.pwd)
        self.pwd = self.pad(self.pwd).encode()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, self.mode, iv)
        return base64.b64encode(iv + cipher.encrypt(self.pwd)).decode()

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:self.BS]
        cipher = AES.new(self.key, self.mode, iv)
        return self.unpad(cipher.decrypt(enc[self.BS:]).decode())


if __name__ == "__main__":
    df = 'a12312312'
    aes = EncryptAes(df)
    df1 = aes.encrypt()
    df2 = aes.decrypt(df1)
    print(df1,df2)