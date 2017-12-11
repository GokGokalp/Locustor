'locustor.py'

import time
import schedule
from locustor_config import LocustorConfig
from log_repository import LogRepository
from log_helper import LogHelper

def job():
    'Locustor is a simple scheduled worker which sends Locust logs to InfluxDB.'
    log_output = LogHelper().parse_log_to_json(LocustorConfig.LOCUST_CSV_LOG_FILE_PATH)
    LogRepository().add_log(log_output)

schedule.every(LocustorConfig.DELAY_IN_SEC).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
