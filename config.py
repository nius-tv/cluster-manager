import os

CHECK_TIMEOUT = 2 # in minutes
CLUSTER_NAME = os.environ.get('CLUSTER_NAME')
GPU_TYPE = os.environ.get('GPU_TYPE')
# Warning: order matters.
INIT_RESOURCES = [
	{
		'image': 'us.gcr.io/plasmic/generate-jobs-manager',
		'name': 'service-account',
		'path': '/app/service-account.yaml'
	},
	{
		'image': 'us.gcr.io/plasmic/generate-jobs-manager',
		'name': 'redis',
		'path': '/app/redis.yaml'
	},
	{
		'image': 'us.gcr.io/plasmic/generate-jobs-manager',
		'name': 'gentle',
		'path': '/app/gentle.yaml'
	},
	{
		'image': 'us.gcr.io/plasmic/generate-jobs-manager',
		'name': 'jobs-manager',
		'path': '/app/jobs-manager.yaml'
	}
]
JOBS_DIR = '/tmp'
LOOP_CHECK_TIMEOUT = 2 # in minutes
NVIDIA_DEVICE_DAEMON_SET = 'https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml'
MACHINE_TYPE = 'n1-standard-4'
MAX_CHECKS = 5
PROJECT_NAME = 'plasmic-artefacts'
WAIT_FOR_PODS = [
	'gentle',
	'jobs-manager'
]
ZONE = 'us-central1-c'
