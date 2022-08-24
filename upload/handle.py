def handle_uploaded_file(f):
    with open('/tmp/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            destination.write("\r\n\r\n")
