import time
import subprocess

from cluster import Cluster
from config import *
from envsubst import envsubst
from pubsub import PubSub


def check_queued_messages(checks=1):
	num_undelivered_messages = pubsub.num_undelivered_messages()
	print('\nmessages in queue:', num_undelivered_messages)

	num_jobs_running = 0
	if cluster.exists():
		num_jobs_running = cluster.num_jobs_running()
	print('number of jobs running:', num_jobs_running)

	if cluster.exists() and num_undelivered_messages == 0 and num_jobs_running == 0:
		print('checks before cluster deletion: {}/{}'.format(checks, MAX_CHECKS))

		if checks < MAX_CHECKS:
			print('next check will be in:', CHECK_TIMEOUT, 'minutes...')
			time.sleep(60 * CHECK_TIMEOUT)
			checks += 1
			check_queued_messages(checks)

		elif checks == MAX_CHECKS:
			cluster.delete()

	elif not cluster.exists() and num_undelivered_messages > 0:
		cluster.start()
		print('cluster is ready')


def copy_resources():
	for resource in INIT_RESOURCES:
		name = resource['name']
		image = resource['image']
		print('\ncopying resource yaml:', name)

		print('pulling latest docker image')
		cmd = 'docker pull {}'.format(image)
		subprocess.call(['bash', '-c', cmd])

		# Copy resource yaml
		output_path = '{}/{}.yaml'.format(JOBS_DIR, name)
		cmd = 'docker run \
				-t {image} \
				cat {input_path} \
				> {output_path}'.format(
					image=image,
					input_path=resource['path'],
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
	copy_resources()

	while True:	
		check_queued_messages()
		print('checking again in', LOOP_CHECK_TIMEOUT, 'minutes...')
		time.sleep(60 * LOOP_CHECK_TIMEOUT)
