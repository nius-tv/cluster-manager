docker run \
-v $(pwd):/app \
-v /var/run/docker.sock:/var/run/docker.sock \
-it us.gcr.io/plasmic-artefacts-2/cluster-manager \
bash
