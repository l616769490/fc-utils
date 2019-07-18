import jwt
from jwt.exceptions import DecodeError
import time

class JwtUtils(object):
    """docstring for JwtUtils"""
    def __init__(self):
        super(JwtUtils, self).__init__()
        
    def encode(self, payload, priv_key):
        ''' 加密
        :param payload:有效载荷
        :param priv_key:私钥
        '''
        encoded = jwt.encode(payload, priv_key, algorithm='RS256')
        return str(encoded, encoding='utf-8')

    def decode(self, encoded_str, pub_key):
        ''' 解密
        :param encoded_str:加密后的文件
        :param pub_key:公钥
        '''
        try:
            info = jwt.decode(encoded_str, pub_key, algorithm='RS256')
            return {'message':'success', 'data':{'decode_str':info}}
        except DecodeError as e:
            return {'message':'fail', 'data':{'msg':'签名错误'}}

    def timeLaterForDay(self, day = 30):
        """ 生成签名过期时间，默认一个月
        """
        return int(time.time() + 3600 * 24 * day)

    def timeLaterForHour(self, hour = 0.5):
        """ 生成签名过期时间，默认半小时
        """
        return int(time.time() + 3600 * hour)

__jwt_utils = JwtUtils()
encode = __jwt_utils.encode
decode = __jwt_utils.decode
timelateForDay = __jwt_utils.timeLaterForDay
timelaterForHour = __jwt_utils.timeLaterForHour