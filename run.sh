export GCS_BUCKET_NAME=plasmic-generated
export GOOGLE_APPLICATION_CREDENTIALS=/app/service-account.json
export PROJECT_NAME=plasmic-artefacts
export REDIS_HOST=memstore-redis
export REDIS_INSTANCE_NAME=plasmic-generate
export REDIS_PORT=6379
export REGION=us-central1
export TEXT_TO_SPEC_SAMPLE_RATE=22050
export TEXT_TO_SPEC_SIGMA=0.666
export TEXT_TO_SPEC_STRENGTH=0.01

gcloud auth activate-service-account \
	--key-file=$GOOGLE_APPLICATION_CREDENTIALS
gcloud config set core/project $PROJECT_NAME
gcloud auth configure-docker \
	--quiet

# Warning: be careful about moving this line of code,
# because it requires $CLUSTER_NAME and $REGION values.
export REDIS_IP=$(gcloud redis instances list \
	--filter "name:$REDIS_INSTANCE_NAME" \
	--format "value(HOST)" \
	--region $REGION)
echo 'Redis IP:' $REDIS_IP

echo '-----------------------------------'
echo 'Launching cluster manager ---------'
echo '-----------------------------------'
python3 cluster_manager.py
