from djproxy.views import HttpProxy



class LocalProxy(HttpProxy):
    base_url = 'https://google.com/'