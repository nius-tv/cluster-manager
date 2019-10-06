CHECK_TIMEOUT = 2 # in minutes
CLUSTER_NAME = 'plasmic-generate'
GPU_TYPE = 'nvidia-tesla-p100'
INIT_PODS = [
	{
		'image': 'us.gcr.io/plasmic/generate-jobs-manager',
		'name': 'gentle',
		'path': '/app/gentle.yaml'
	},
	{
		'image': 'us.gcr.io/plasmic/generate-jobs-manager',
		'name': 'init-story',
		'path': '/app/init-story.yaml'
	}
]
JOBS_DIR = '/tmp'
LOOP_CHECK_TIMEOUT = 5 # in minutes
MACHINE_TYPE = 'n1-standard-4'
MAX_CHECKS = 5
PROJECT_NAME = 'plasmic-artefacts'
ZONE = 'us-central1-c'
