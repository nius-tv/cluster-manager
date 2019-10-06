import json
import subprocess
import time

from config import *


class Cluster(object):

	def _cluster_exists(self):
		cmd = 'gcloud container clusters list \
				--filter name={cluster_name} \
				--zone {zone}'.format(
					cluster_name=CLUSTER_NAME,
					zone=ZONE)
		output = subprocess.check_output(['bash', '-c', cmd])
		output = json.loads(output)
		return len(output) > 0

	def _connect_to_cluster(self):
		cmd = 'gcloud container clusters get-credentials {cluster_name} \
				--project {project_name} \
				--zone {zone}'.format(
					cluster_name=CLUSTER_NAME,
					project_name=PROJECT_NAME,
					zone=ZONE)
		subprocess.call(['bash', '-c', cmd])

	def _create_cluster(self):
		cmd = 'gcloud container clusters create {cluster_name} \
				--accelerator type={gpu_type},count=1 \
				--cluster-ipv4-cidr 10.0.0.0/14 \
				--cluster-version 1.14.6-gke.1 \
				--enable-ip-alias \
				--enable-kubernetes-alpha \
				--num-nodes 1 \
				--machine-type {machine_type} \
				--services-ipv4-cidr 10.4.0.0/19 \
				--scopes default,storage-full \
				--quiet \
				--zone {zone}'.format(
					cluster_name=CLUSTER_NAME,
					gpu_type=GPU_TYPE,
					machine_type=MACHINE_TYPE,
					zone=ZONE)
		subprocess.call(['bash', '-c', cmd])

	def _start_pod(self, name):
		cmd = 'kubectl apply -f {}/{}.yaml'.format(JOBS_DIR, name)
		subprocess.call(['bash', '-c', cmd])

		self._wait_for_pod(name)

	def _wait_for_pod(self, name):
		while True:
			print('waiting for pod:', name)
			cmd = 'kubectl get pods \
					--selector app={} \
					-o jsonpath="{.items[*].status.phase}"'.format(name)
			output = subprocess.check_output(['bash', '-c', cmd])

			if output.lower() == 'running':
				break
			if output.lower() == 'error':
				raise
			time.sleep(5)

	def delete(self):
		cmd = 'gcloud container clusters delete {cluster_name} \
				--zone {zone}'.format(
					cluster_name=CLUSTER_NAME,
					zone=ZONE)
		subprocess.call(['bash', '-c', cmd])

	def start(self):
		self._create_cluster()
		self._connect_to_cluster()
		for pod in INIT_PODS:
			self._start_pod(pod)
