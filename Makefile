docker:
ifeq ($(shell command -v docker 2> /dev/null),)
	$(error no such command: $@)
endif

docker/build: docker
	docker build --rm -t zchee/deoplete-asm -f dockerfiles/Dockerfile .

dump_protobuf: docker/build
	docker run --rm zchee/deoplete-asm > rplugin/python3/deoplete/sources/pb/instructions.sdm.pb

.PHONY: docker docker/build dump_protobuf
