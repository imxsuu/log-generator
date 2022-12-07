image_name=faker

tag=v2.0.0

repository_url=10.0.0.255:5000
project_name=gedge-platform

dev-env:
	set-git
build:
	build-docker

#### dev-env ####
set-git:
	git config --local commit.template .gitmessage.txt


#### docker #####
build-docker:
	docker build -f Dockerfile -t $(image_name):$(tag) .

run-docker:
	docker run -it -d --shm-size=8G --init --name $(image_name) $(image_name):$(tag) -p 9000:19000

exec-docker:
	docker exec -it $(image_name) /bin/bash

rm-docker:
	docker stop $(image_name) && docker rm $(image_name)
#################


#### image management ####
push-image:
	docker tag $(image_name):$(tag) $(repository_url)/$(project_name)/$(image_name):$(tag)
	docker push $(repository_url)/$(project_name)/$(image_name):$(tag)
