import time
import subprocess

from cluster import Cluster
from config import *
from pubsub import PubSub


def check_subscriptions(checks=0):
	if pubsub.num_undelivered_messages() == 0:
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
		cmd = 'gcloud docker -- run \
				-t {image} \
				cat {path} \
				>> {job_dir}/{name}.yaml'.format(
					image=pod['image'],
					path=pod['path'],
					job_dir=JOBS_DIR,
					name=pod['name'])
		subprocess.call(['bash', '-c', cmd])


if __name__ == '__main__':
	cluster = Cluster()
	pubsub = PubSub()

	while True:
		check_subscriptions()
		time.sleep(60 * 1) # 1 minute
