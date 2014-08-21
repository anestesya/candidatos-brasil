from webapp2 import Route
import handlers


# Map URLs to handlers
routes = [
    Route('/', handler=handlers.IndexHandler),

    Route('/logout', handler='handlers.AuthHandler:logout', name='logout'),
    Route('/auth/<provider>',  handler='handlers.AuthHandler:_simple_auth', name='auth_login'),
    Route('/auth/<provider>/callback',  handler='handlers.AuthHandler:_auth_callback', name='auth_callback'),

    # api
    Route('/api/inidoneos',  handler=handlers.InidoneosHandler, name='api-inidoneos'),
    Route('/api/inabilitados',  handler=handlers.InabilitadosHandler, name='api-inabilitados'),
]
