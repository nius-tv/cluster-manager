export GCS_BUCKET_NAME=plasmic-generated
export REDIS_HOST=memstore-redis
export REDIS_INSTANCE_NAME=plasmic-generate
export REDIS_PORT=6379
export REGION=us-central1
export TEXT_TO_SPEC_SAMPLE_RATE=22050
export TEXT_TO_SPEC_SIGMA=0.666
export TEXT_TO_SPEC_STRENGTH=0.01
# Warning: keep this command last,
# because it requires $CLUSTER_NAME and $REGION value.
export REDIS_IP=$(gcloud redis instances list \
	--filter "name:$REDIS_INSTANCE_NAME" \
	--format "value(HOST)" \
	--region $REGION)

python3 cluster_manager.py
