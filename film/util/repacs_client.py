import os
import requests
from film import logger


class Repacs(object):
    def __init__(self):
        self.url = os.environ.get("REPACS_URL", default="http://192.168.109.92:3333")

    def get_study_info(self, study_iuid):
        try:
            study_resp = requests.get(F"{self.url}/studies/{study_iuid}", timeout=5)
            study_resp.raise_for_status()
            return study_resp.json()
        except Exception as e:
            logger.error(F"{study_iuid}请求repacs study出错: {e}")
            return None

    def get_series_info(self, series_iuid):
        try:
            series_resp = requests.get(F"{self.url}/series/{series_iuid}", timeout=5)
            series_resp.raise_for_status()
            return series_resp.json()
        except Exception as e:
            logger.error(F"{series_iuid}请求repacs series出错: {e}")
            return None

    def get_series_task(self, series_iuid):
        try:
            task_resp = requests.get(F"{self.url}/series/{series_iuid}/tasks", timeout=5)
            task_resp.raise_for_status()
            return task_resp.json()
        except Exception as e:
            logger.error(F"{series_iuid}请求task类型错误: {e}")
            return None

    def get_task_result(self, series_iuid, task_type):
        try:
            result_resp = requests.get(F"{self.url}/series/{series_iuid}/predict/{task_type}", timeout=5)
            result_resp.raise_for_status()
            return result_resp.json()
        except Exception as e:
            logger.error(F"{series_iuid}请求result结果错误: {e}")
            return None
