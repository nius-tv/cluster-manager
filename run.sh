export AUDIO_CODEC=pcm_s16le
export AUDIO_FMT=wav
export CLUSTER_NAME=story-builder
export COMPUTE_PROJECT_NAME=plasmic-compute-256214
export FPS=30
export GENERATED_BUCKET_NAME=generated-stories
export GOOGLE_APPLICATION_CREDENTIALS=/app/service-account.json
export GPU_TYPE=nvidia-tesla-k80
export HTML_CAPTURE_DURATION=30 # screen capture time in seconds
export HTML_CAPTURE_URL=https://storage.googleapis.com/nius-artefacts/news-title/512x1024.html#
export IMG_FMT=png
export LIBRARY_BUCKET_NAME=assets-library
export MACHINE_TYPE=n1-standard-4
export MODELS_BUCKET_NAME=plasmic-models
export PIXEL_FMT=argb
export TEXT_TO_SPEC_SAMPLE_RATE=22050
export TEXT_TO_SPEC_SIGMA=0.666
export TEXT_TO_SPEC_STRENGTH=0.01
export VIDEO_CODEC=qtrle
export VIDEO_FMT=mov

gcloud auth activate-service-account \
	--key-file=$GOOGLE_APPLICATION_CREDENTIALS
gcloud config set core/project $COMPUTE_PROJECT_NAME
gcloud auth configure-docker \
	--quiet

echo '-----------------------------------'
echo 'Launching cluster manager ---------'
echo '-----------------------------------'
python3 cluster_manager.py
