#!/bin/bash -xe

if [ ${#GITHUB_TOKEN} -eq 0 ]; then
	echo "WARNING: \$GITHUB_TOKEN is not set!"
fi

function build() {
	cd /tmp
	git clone https://${GITHUB_TOKEN}@github.com/phuslu/gfwlist

	cd gfwlist

	curl https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt | \
	python parse.py >gfwlist.txt
}

function release() {
	git add * && \
	git commit -m "[skip ci] update gfwlist" && \
	git push origin master -f
}

build
release
