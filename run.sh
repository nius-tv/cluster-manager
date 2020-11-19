export ARTEFACTS_PROJECT_NAME=plasmic-artefacts-2
export AUDIO_CODEC=pcm_s16le
export AUDIO_FMT=wav
export CLUSTER_NAME=story-builder
export CLUSTER_VERSION=1.16.13-gke.401
export COMPUTE_PROJECT_NAME=plasmic-compute-256214
export FPS=30
export GENERATED_BUCKET_NAME=plasmic-stories
export GOOGLE_APPLICATION_CREDENTIALS=/app/service-account.json
export GPU_TYPE=nvidia-tesla-k80
export HTML_CAPTURE_DURATION=60 # screen capture time in seconds
export HTML_CAPTURE_URL=http://story-overlay.plasmic-compute-256214.appspot.com?story_id=
export IMG_FMT=png
export LIBRARY_BUCKET_NAME=plasmic-library
export MACHINE_TYPE=n1-standard-8
export MODELS_BUCKET_NAME=plasmic-models
export NUM_CPUS=1
export NUM_GPUS=1
export PIXEL_FMT=argb
export TEXT_TO_SPEC_SAMPLE_RATE=22050
export TEXT_TO_SPEC_SIGMA=0.666
export TEXT_TO_SPEC_STRENGTH=0.01
export VIDEO_CODEC=qtrle
export VIDEO_FMT=mov
export ZONE=us-central1-c

gcloud auth activate-service-account \
	--key-file=$GOOGLE_APPLICATION_CREDENTIALS
gcloud config set core/project $COMPUTE_PROJECT_NAME
gcloud auth configure-docker \
	--quiet

echo '-----------------------------------'
echo 'Launching cluster manager ---------'
echo '-----------------------------------'
python3 cluster_manager.py
