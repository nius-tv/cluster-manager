export AUDIO_CODEC=pcm_s16le
export CLUSTER_NAME=story-builder
export FPS=30
export GENERATED_BUCKET_NAME=generated-stories
export GOOGLE_APPLICATION_CREDENTIALS=/app/service-account.json
export GPU_TYPE=nvidia-tesla-k80
export LIBRARY_BUCKET_NAME=assets-library
export MACHINE_TYPE=n1-standard-4
export PIXEL_FMT=argb
export PROJECT_NAME=plasmic-artefacts-2
export REDIS_HOST=memstore-redis
export REDIS_INSTANCE_NAME=story-builder
export REDIS_PORT=6379
export REDIS_REGION=us-central1
export TEXT_TO_SPEC_SAMPLE_RATE=22050
export TEXT_TO_SPEC_SIGMA=0.666
export TEXT_TO_SPEC_STRENGTH=0.01
export VIDEO_CODEC=qtrle
export VIDEO_FMT=mov

gcloud auth activate-service-account \
	--key-file=$GOOGLE_APPLICATION_CREDENTIALS
gcloud config set core/project $PROJECT_NAME
gcloud auth configure-docker \
	--quiet

# Warning: be careful about moving this line of code,
# because it requires $CLUSTER_NAME and $REDIS_REGION values.
export REDIS_IP=$(gcloud redis instances list \
	--filter "name:$REDIS_INSTANCE_NAME" \
	--format "value(HOST)" \
	--region $REDIS_REGION)
echo 'Redis IP:' $REDIS_IP

echo '-----------------------------------'
echo 'Launching cluster manager ---------'
echo '-----------------------------------'
python3 cluster_manager.py
