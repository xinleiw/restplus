from flask import Blueprint
from flask_restplus import Api
from film.modules.proxy import views as proxy
from film.modules.QR_code import views as qr_code

api_blu = Blueprint("test", __name__, url_prefix="/test")
api = Api(api_blu, version="1.0", title="OpenApi", description="The Open Api Service")

api.add_resource(proxy.HelloWorld, "/hello")
api.add_resource(qr_code.GenerateQR, "/QR")

