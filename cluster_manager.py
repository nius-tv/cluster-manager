import time
import subprocess

from cluster import Cluster
from config import *
from envsubst import envsubst
from pubsub import PubSub


def check_queued_messages(checks=1):
	num_undelivered_messages = pubsub.num_undelivered_messages()
	print('messages in queue:', num_undelivered_messages)

	if cluster.exists() and num_undelivered_messages == 0:
		print('checks before cluster deletion: {}/{}'.format(checks, MAX_CHECKS))

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
		output_path = '{}/{}.yaml'.format(JOBS_DIR, name)
		cmd = 'docker run \
				-t {image} \
				cat {input_path} \
				> {output_path}'.format(
					image=pod['image'],
					input_path=pod['path'],
					output_path=output_path)
		subprocess.call(['bash', '-c', cmd])

		print('env var substitute')
		env_var_substitute(output_path)


def env_var_substitute(path):
	with open(path) as f:
		data = f.read()

	data = envsubst(data)

	with open(path, 'w') as f:
		f.write(data)


if __name__ == '__main__':
	cluster = Cluster()
	pubsub = PubSub()
	copy_jobs()

	while True:
		print('checking queued messages')		
		check_queued_messages()
		print('checking again in', LOOP_CHECK_TIMEOUT, 'minutes...')
		time.sleep(60 * LOOP_CHECK_TIMEOUT)
