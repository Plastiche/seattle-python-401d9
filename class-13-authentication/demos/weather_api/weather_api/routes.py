from pyramid_restful.routers import ViewSetRouter
from .views.weather_location import WeatherLocationAPIView, LookupAPIView
from .views.auth import AuthAPIView


def includeme(config):
    # config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config, trailing_slash=False)
    # router.register('api/v1/location', WeatherLocationAPIView, 'location', permission='admin')
    router.register('api/v1/location', WeatherLocationAPIView, 'location')
    router.register('api/v1/lookup/{zip_code}', LookupAPIView, 'lookup')
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
