# protoc-gen-grpc --js_out=import_style=commonjs:. --grpc_out=. -I=. proto/diff-img.proto
protoc-gen-grpc-ts --ts_out=./proto --proto_path ./proto proto/diff-img.proto