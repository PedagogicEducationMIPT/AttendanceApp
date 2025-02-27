create-private-key-crt-pair:
	openssl genpkey -algorithm RSA -out private.key
	openssl req -x509 \
		-key private.key \
		-out certificate.crt \
		-days 365 \
		-subj "/CN=127.0.0.1" \
		-addext "subjectAltName=IP:127.0.0.1" \
		-nodes

show-cert:
	openssl x509  -in certificate.crt -text

download-cert:
	openssl s_client \
		-connect 127.0.0.1:8000 \
		-showcerts </dev/null 2>/dev/null | openssl x509 -text -noout
	