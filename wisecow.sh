#!/usr/bin/env bash

SRVPORT=4499

prerequisites() {
    command -v cowsay >/dev/null 2>&1 &&
    command -v fortune >/dev/null 2>&1 ||
    { echo "Install prerequisites."; exit 1; }
}

main() {
    prerequisites
    echo "Wisdom served over TLS on port=$SRVPORT..."

    socat OPENSSL-LISTEN:$SRVPORT,reuseaddr,cert=/app/certs/wisecow.crt,key=/app/certs/wisecow.key,verify=0,fork SYSTEM:"bash -c '
        # read first line of HTTP request (avoid blocking)
        read request_line
        # generate fortune + cowsay
        response=\$(fortune | cowsay)
        # send full HTTP response with headers
        printf \"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n<pre>%s</pre>\r\n\"\"\$response\"
     done
   '"
}

main




