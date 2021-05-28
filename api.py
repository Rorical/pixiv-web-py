import requests
import json

class PixivWebApi():
    def __init__(self):
        self.requests = requests.session()
        self.host = "https://www.pixiv.net"
        proxyDict = {"http": "http://localhost:7890", "https": "https://localhost:7890", "ftp": "ftp://localhost:7890"}
        self.requests_kwargs = {"proxies": proxyDict}

    def request(self, method, url, headers={}, params=None, data=None, stream=False):
        url = self.host + url
        if (method == 'GET'):
            return self.requests.get(url, params=params, headers=headers, stream=stream, **self.requests_kwargs)
        elif (method == 'POST'):
            return self.requests.post(url, params=params, data=data, headers=headers, stream=stream, **self.requests_kwargs)
        elif (method == 'DELETE'):
            return self.requests.delete(url, params=params, data=data, headers=headers, stream=stream, **self.requests_kwargs)

    def parseJson(self, json_str):
        return json.loads(json_str)

    def IllustDetail(self, illustId):
        url = '/ajax/illust/%s' % illustId
        r = self.request('GET', url)
        return self.parseJson(r.text)
    
    def IllustPages(self, illustId):
        url = '/ajax/illust/%s/pages' % illustId
        r = self.request('GET', url)
        return self.parseJson(r.text)

    def IllustsRecommend(self, illustId, limit = 30):
        url = '/ajax/illust/%s/recommend/init?limit=%s' % (illustId, limit)
        r = self.request('GET', url)
        return self.parseJson(r.text)
    
    def IllustsDiscovery(self, max = 18, mode = "safe"):
        url = '/ajax/illust/discovery?max=%s&mode=%s' % (max, mode)
        r = self.request('GET', url)
        return self.parseJson(r.text)

    def UserDetail(self, userId):
        url = '/ajax/user/%s' % userId
        r = self.request('GET', url)
        return self.parseJson(r.text)

    def UserIllusts(self, userId):
        url = '/ajax/user/%s/profile/top' % userId
        r = self.request('GET', url)
        return self.parseJson(r.text)

    def UserSpecificIllusts(self, userId, ids):
        url = "/ajax/user/%s/illusts?ids%5B%5D=%s" % (userId, ids)
        r = self.request('GET', url)
        return self.parseJson(r.text)

    def IllustSearch(self, keyword):
        url = '/ajax/search/top/%s' % keyword
        r = self.request('GET', url)
        return self.parseJson(r.text)