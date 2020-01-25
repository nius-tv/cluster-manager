import os

CHECK_TIMEOUT = 2 # in minutes
CLUSTER_NAME = os.environ.get('CLUSTER_NAME')
CLUSTER_VERSION = os.environ.get('CLUSTER_VERSION')
COMPUTE_PROJECT_NAME = os.environ.get('COMPUTE_PROJECT_NAME')
GPU_TYPE = os.environ.get('GPU_TYPE')
# Warning: order matters.
INIT_RESOURCES = [
	{
		'image': 'us.gcr.io/plasmic-artefacts-2/generate-jobs-manager',
		'name': 'service-account',
		'path': '/app/service-account.yaml'
	},
	{
		'image': 'us.gcr.io/plasmic-artefacts-2/generate-jobs-manager',
		'name': 'gentle',
		'path': '/app/gentle.yaml'
	},
	{
		'image': 'us.gcr.io/plasmic-artefacts-2/generate-jobs-manager',
		'name': 'jobs-manager',
		'path': '/app/jobs-manager.yaml'
	}
]
JOBS_DIR = '/tmp'
LOOP_CHECK_TIMEOUT = 2 # in minutes
MACHINE_TYPE = os.environ.get('MACHINE_TYPE')
MAX_CHECKS = 5
NUM_GPUS = int(os.environ.get('NUM_GPUS'))
NVIDIA_DEVICE_DAEMON_SET = 'https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml'
WAIT_FOR_PODS = [
	'gentle',
	'jobs-manager'
]
ZONE = os.environ.get('ZONE')
