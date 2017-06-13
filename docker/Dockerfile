FROM openjdk:8
LABEL maintainer "zchee <https://github.com/zchee>"

ARG INTEL_PDF_URL=https://software.intel.com/sites/default/files/managed/39/c5/325462-sdm-vol-1-2abcd-3abcd.pdf

RUN set -eux \
	&& echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list \
	&& curl https://bazel.build/bazel-release.pub.gpg | apt-key add - \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends --no-install-suggests \
		file \
		bazel \
	\
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& curl -LO $INTEL_PDF_URL \
	\
	&& git clone https://github.com/google/exegesis \
	\
	&& cd exegesis \
	# why external/com_github_glog_glog/configure is Permission denied?
	&& bazel run //exegesis/tools:parse_intel_sdm -c opt -- --exegesis_input_spec=/325462-sdm-vol-1-2abcd-3abcd.pdf --exegesis_output_file_base=$PWD/instructions --exegesis_transforms=default || chmod +x bazel-exegesis/external/com_github_glog_glog/configure \
	# re run after the chmod
	&& bazel run //exegesis/tools:parse_intel_sdm -c opt -- --exegesis_input_spec=/325462-sdm-vol-1-2abcd-3abcd.pdf --exegesis_output_file_base=$PWD/instructions --exegesis_transforms=default

CMD ["cat", "/exegesis/instructions_0.sdm.pb"]
