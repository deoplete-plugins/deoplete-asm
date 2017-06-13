gen_go_opcode:
	rm -f ./Rplugin/python3/deoplete/sources/opcode.py
	./tools/gen_goopcode.py > ./rplugin/python3/deoplete/sources/opcode.py

docker:
ifeq ($(shell command -v docker 2> /dev/null),)
	$(error no such command: $@)
endif

docker/build: docker
	docker build --rm -t zchee/deoplete-asm -f docker/Dockerfile .

dump_protobuf: docker/build
	docker run --rm zchee/deoplete-asm > rplugin/python3/deoplete/sources/pb/instructions.sdm.pb

.PHONY: gen_go_opcode docker docker/build dump_protobuf
