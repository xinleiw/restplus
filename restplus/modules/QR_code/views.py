from flask import send_file
from film.lib import generate_QR
from flask_restplus import Resource, Namespace
from film.util.error_msg_util import get_error_response
from film.constant.error_code_msg import ErrorCodeMsg

ns = Namespace("qr", description="Generate QR code")


class GenerateQR(Resource):
    @ns.doc(params={"study_iuid": "study_iuid"})
    def get(self, study_iuid):
        url = F"www.baidu.com"
        qr_img = generate_QR.create_qr(url)
        return send_file(qr_img, mimetype='image/png')
