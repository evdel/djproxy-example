from djproxy.views import HttpProxy


# We can use the permission required mixin here
class LocalProxy(HttpProxy):
    base_url = 'http://docs.beta.moneypark.ch/mpre/'
