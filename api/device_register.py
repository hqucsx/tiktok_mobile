import hashlib
import json
import requests
import time
import urllib3
from datetime import date
from .utils.DeviceUtils import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class DeviceRegister:
    
    debug = False

    def __init__(self, gorgon_signer, proxy=None):
        if proxy == "" or proxy is None:
            self.proxies = None
        else:
            self.proxies = { 'https' : 'http://' + proxy, 'http' : 'http://' + proxy }
        self.device = DeviceUtils.create_device()
        self.gorgon_url = gorgon_signer
        self.session = requests.Session()


    def device_register(self):
        ts = time.time()
        ts2 = time.time()
        api_url = 'https://log-va.tiktokv.com/service/2/device_register/?' \
                  + DeviceUtils.device_params_register(self.device, ts, ts2)

        headers = self.get_headers_post(api_url, DeviceUtils.device_params_register(self.device, ts, ts2),
                                        ts, content_type='application/octet-stream;tt-data=a')

        response = self.session.post(api_url, data=DeviceUtils.get_data_register(self.device),
                                     headers=headers, verify=False, proxies=self.proxies).json()

        if self.session.cookies is None:
            return None, None

        self.device.install_id = response['install_id_str']
        self.device.device_id = response['device_id_str']

        if self.debug:
            self.log("[device_register]: " + str(response))

        return self.device, self.session.cookies.get_dict()

    def get_headers_post(self, purl, post_data, ts, content_type='application/x-www-form-urlencoded; charset=UTF-8'):
        cookie = self.get_cookie_string()

        headers = {
            'cookie': cookie,
            'Content-Type': content_type,
            'User-Agent': self.device.ua,
            'X-SS-REQ-TICKET': str(int(round(ts) * 1000)),
            'x-tt-trace-id': self.device.xtttraceid,
            'X-SS-STUB': str(hashlib.md5(post_data.encode()).hexdigest()).upper(),
        }
        gorgon = self.get_gorgon(purl, headers, ts)
        headers['X-Gorgon'] = str(gorgon)
        headers['X-Khronos'] = str(int(ts))
        return headers

    def get_gorgon(self, url, headers, ts):
        data = json.dumps({'url': url, 'headers': headers, 'chr': int(ts) * 1000})
        gorgon = self.session.post(self.gorgon_url, data=data).text
        return gorgon

    def get_cookie_string(self):
        sess_dict = self.session.cookies.get_dict()
        lls = []
        for imn in sess_dict:
            lls.append(str(imn) + '=' + str(sess_dict[imn]))
        return "; ".join(lls).replace("\n", "")

    def log(self, message):
        d = date.today()
        t = datetime.time(datetime.now())
        print('[' + str(d) + ' ' + str(t) + ']: ' + str(message.encode('utf8')))

    def device_params(self, ts):
        return DeviceUtils.device_params(self.device, ts)

    def get_cookies(self):
        return json.dumps(self.session.cookies.get_dict())

    def reset_session(self):
        self.session = requests.Session()