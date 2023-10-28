from hume import HumeBatchClient
from hume.models.config import FaceConfig
import time
from pprint import pprint

client = HumeBatchClient("a8EPV7v5TGkfRLncB6gTrgtwOgKzqIeoF0v75IDuSal6Ucig")
urls = ["https://as2.ftcdn.net/v2/jpg/00/88/53/89/1000_F_88538986_5Bi4eJ667pocsO3BIlbN4fHKz8yUFSuA.jpg  "]
config = FaceConfig()
job = client.submit_job(urls, [config])

status = job.get_status()
print(f"Job status: {status}")
time.sleep(3)
details = job.get_details()
run_time_ms = details.get_run_time_ms()
print(f"Job ran for {run_time_ms} milliseconds")

predictions = job.get_predictions()
pprint(predictions)