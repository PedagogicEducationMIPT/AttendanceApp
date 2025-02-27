create-private-key-crt-pair:
	openssl genpkey -algorithm RSA -out private.key
	openssl req -x509 \
		-key private.key \
		-out certificate.crt \
		-days 365 \
		-subj "/CN=127.0.0.1" \
		-addext "subjectAltName=IP:127.0.0.1" \
		-nodes

decode:
	