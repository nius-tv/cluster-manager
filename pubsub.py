import json
import time

from config import *
from google.cloud import monitoring_v3
from google.protobuf.json_format import MessageToJson


class PubSub(object):

	def __init__(self):
		self.client = monitoring_v3.MetricServiceClient()
		self.project_path = self.client.project_path(PROJECT_NAME)

	def num_undelivered_messages(self):
		interval = monitoring_v3.types.TimeInterval()
		now = time.time()
		interval.end_time.seconds = int(now)
		# Data is sampled every 60 seconds.
		# After sampling, data is not visible for up to 120 seconds.
		# For more info visit https://cloud.google.com/monitoring/api/metrics_gcp.
		interval.start_time.seconds = int(now - 300) # magic number

		results = self.client.list_time_series(
			self.project_path,
			'metric.type="pubsub.googleapis.com/subscription/num_undelivered_messages"',
			interval,
			monitoring_v3.enums.ListTimeSeriesRequest.TimeSeriesView.FULL)

		count = 0
		for result in results:
			result = MessageToJson(result)
			result = json.loads(result)
			# "points" is a time series list. We are only interested on the first
			# element on the list.
			count += int(result['points'][0]['value']['int64Value'])

		return count
