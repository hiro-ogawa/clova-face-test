run: venv sample_images/Girl.jpg sample_images/Lenna.jpg
	$(VENV)/python clova_face.py

sample_images/Girl.jpg:
	mkdir -p sample_images
	wget http://www.ess.ic.kanagawa-it.ac.jp/std_img/colorimage/Girl.jpg -P sample_images

sample_images/Lenna.jpg:
	mkdir -p sample_images
	wget http://www.ess.ic.kanagawa-it.ac.jp/std_img/colorimage/Lenna.jpg -P sample_images

clean: clean-venv
	rm -rf sample_images

# https://github.com/sio/Makefile.venv
include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv
