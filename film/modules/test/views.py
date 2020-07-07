from flask_restplus import Resource, Namespace
from film.util.error_msg_util import get_error_response
from film.constant.error_code_msg import ErrorCodeMsg

ns = Namespace("test", description="test")


class HelloWorld(Resource):
    @ns.doc(params={"test": "test"})
    def get(self):
        return "hello world"
