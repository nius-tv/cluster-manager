docker run \
-v $(pwd)/service-account.json:/app/service-account.json \
-v /var/run/docker.sock:/var/run/docker.sock \
-it us.gcr.io/plasmic-artefacts-2/cluster-manager \
bash
