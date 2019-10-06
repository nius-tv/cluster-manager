import time
import subprocess

from cluster import Cluster
from config import *
from pubsub import PubSub


def check_queued_messages(checks=1):
	num_undelivered_messages = pubsub.num_undelivered_messages()
	print('messages queued:', num_undelivered_messages)

	if cluster.exists() and num_undelivered_messages == 0:
		print('checks:', checks, '/', MAX_CHECKS)

		if checks < MAX_CHECKS:
			time.sleep(60 * CHECK_TIMEOUT)
			checks += 1
			check_queued_messages(checks)

		elif checks == MAX_CHECKS:
			cluster.delete()

	elif not cluster.exists() and num_undelivered_messages > 0:
		cluster.start()

	else:
		print('nothing to do')


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
		check_queued_messages()
		print('checking again in', LOOP_CHECK_TIMEOUT, 'minutes...')
		time.sleep(60 * LOOP_CHECK_TIMEOUT) # 1 minute
