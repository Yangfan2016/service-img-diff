protoc-gen-grpc --js_out=import_style=commonjs:. --grpc_out=. -I=. proto/diff-img.proto
protoc-gen-grpc-ts --ts_out=grpc_js:./proto --proto_path ./proto ./proto/diff-img.proto

# # Path to this plugin, Note this must be an abolsute path on Windows (see #15)
# PROTOC_GEN_TS_PATH="./node_modules/.bin/protoc-gen-ts"

# # Path to the grpc_node_plugin
# PROTOC_GEN_GRPC_PATH="./node_modules/.bin/grpc_tools_node_protoc_plugin"

# # Directory to write generated code to (.js and .d.ts files)
# OUT_DIR="./proto"
# protoc \
#     --plugin="protoc-gen-ts=${PROTOC_GEN_TS_PATH}" \
#     --plugin=protoc-gen-grpc=${PROTOC_GEN_GRPC_PATH} \
#     --js_out="import_style=commonjs,binary:${OUT_DIR}" \
#     --ts_out="service=grpc-node,mode=grpc-js:${OUT_DIR}"\
#     --grpc_out="grpc_js:${OUT_DIR}"\
#     diff-img.proto