__version__ = '0.2.0'

from .http_utils import (
    getData, getDataForJson, getDataForStr, FCHttpUtils
)
from .jwt_utils import (
    encode, decode, timelateForDay, timelaterForHour
)
from .oss_utils import (
    ShanghaiOSS, HangzhouOSS, QingdaoOSS, BeijingOSS, ZhangjiakouOSS, HuhehaoteOSS, ShenzhenOSS, ChengduOSS, HongkongOSS
)
from .pwd_utils import (
    createPwd, createSalt
)