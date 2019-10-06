import time
import subprocess

from cluster import Cluster
from config import *
from pubsub import PubSub


def check_subscriptions(checks=0):
	num_undelivered_messages = pubsub.num_undelivered_messages()
	print('messages queued:', num_undelivered_messages)

	if num_undelivered_messages == 0:
		print('checks:', checks, '/', MAX_CHECKS)

		if checks < MAX_CHECKS:
			time.sleep(60 * CHECK_TIMEOUT)
			checks += 1
			check_subscriptions(checks)

		elif checks == MAX_CHECKS:
			cluster.delete()

	elif not cluster.exists():
		cluster.start()


def copy_jobs():
	for pod in INIT_PODS:
		name = pod['name']
		print('copying pod yaml:', name)
		cmd = 'docker run \
				-t {image} \
				cat {path} \
				>> {job_dir}/{name}.yaml'.format(
					image=pod['image'],
					path=pod['path'],
					job_dir=JOBS_DIR,
					name=name)
		subprocess.call(['bash', '-c', cmd])


if __name__ == '__main__':
	cluster = Cluster()
	pubsub = PubSub()
	copy_jobs()

	while True:
		print('checking queued messages')		
		check_subscriptions()
		time.sleep(60) # 1 minute
