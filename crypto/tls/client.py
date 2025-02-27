import httpx

with httpx.Client(verify='certificate.crt') as cli:
    request = cli.get('http://127.0.0.1:8000')
    print(request.content)