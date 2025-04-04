#!/usr/bin/env python

import sys

from google.protobuf.compiler.plugin_pb2 import (
    CodeGeneratorResponse,
    CodeGeneratorRequest,
)

if __name__ == "__main__":
    buf = None
    data = b""
    while buf is None or len(buf) > 0:
        buf = sys.stdin.buffer.read(1024)
        data += buf

    request = CodeGeneratorRequest.FromString(data)

    response = CodeGeneratorResponse()  # 1
    generated_file = response.file.add()  # 2
    generated_file.name = "hello_world.txt"  # 3
    generated_file.content = str(request)

    sys.stdout.buffer.write(response.SerializeToString())  # 5
