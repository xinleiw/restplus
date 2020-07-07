import json
from flask import Response
from film.constant.error_code_msg import error_dict


def get_error_msg_dict(error_code):
    msg_dict = {"errorCode": error_code, "errorMsg": error_dict.get(error_code)}
    return msg_dict


def get_error_response(error_code):
    resp = Response(json.dumps(get_error_msg_dict(error_code),
                               ensure_ascii=False))
    resp.status_code = 400
    return resp
