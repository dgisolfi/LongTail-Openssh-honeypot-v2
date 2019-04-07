# Daniel Gisolfi

IMAGE=ssh_honeypot
CONTAINER=ssh_honeypot

build:
	@docker build -t $(IMAGE) .

run: build
	@docker run -it --rm --name $(CONTAINER) -p22:22 $(IMAGE)

dev: build
	@docker run -it --rm --name $(CONTAINER) -p22:22 -v${PWD}/src/test:/usr/local/source/openssh/openssh-22/test $(IMAGE)