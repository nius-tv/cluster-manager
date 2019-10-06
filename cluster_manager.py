import time

from cluster import Cluster
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


if __name__ == '__main__':
	cluster = Cluster()
	pubsub = PubSub()

	while True:
		check_subscriptions()
		time.sleep(60 * 1) # 1 minute
