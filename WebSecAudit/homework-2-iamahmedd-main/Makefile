UPLOAD_URL=http://35.188.254.156/upload


.PHONY: test
default: test get_curl


get_curl:
	@which curl >/dev/null 2>/dev/null || sudo apt-get install -y curl

test: get_curl
	@zip -qr /tmp/project.zip part1-xss part2-sqli part3-cmd
	@curl -s -F filename=upload.zip -F "file=@/tmp/project.zip" $(UPLOAD_URL)
	@rm /tmp/project.zip

