CHECK_TIMEOUT = 2 # in minutes
CLUSTER_NAME = 'plasmic-generate'
GPU_TYPE = 'nvidia-tesla-p100'
INIT_PODS = [
	'gentle',
	'init-story'
]
JOBS_DIR = '/jobs'
MACHINE_TYPE = 'n1-standard-4'
MAX_CHECKS = 5
PROJECT_NAME = 'plasmic-artefacts'
ZONE = 'us-central1-c'
