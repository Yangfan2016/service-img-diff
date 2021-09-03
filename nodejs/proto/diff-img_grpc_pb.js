// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var proto_diff$img_pb = require('../proto/diff-img_pb.js');

function serialize_Diff_DiffRequest(arg) {
  if (!(arg instanceof proto_diff$img_pb.DiffRequest)) {
    throw new Error('Expected argument of type Diff.DiffRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_Diff_DiffRequest(buffer_arg) {
  return proto_diff$img_pb.DiffRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_Diff_DiffResponse(arg) {
  if (!(arg instanceof proto_diff$img_pb.DiffResponse)) {
    throw new Error('Expected argument of type Diff.DiffResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_Diff_DiffResponse(buffer_arg) {
  return proto_diff$img_pb.DiffResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var DiffImgService = exports.DiffImgService = {
  getDiff: {
    path: '/Diff.DiffImg/getDiff',
    requestStream: false,
    responseStream: false,
    requestType: proto_diff$img_pb.DiffRequest,
    responseType: proto_diff$img_pb.DiffResponse,
    requestSerialize: serialize_Diff_DiffRequest,
    requestDeserialize: deserialize_Diff_DiffRequest,
    responseSerialize: serialize_Diff_DiffResponse,
    responseDeserialize: deserialize_Diff_DiffResponse,
  },
};

exports.DiffImgClient = grpc.makeGenericClientConstructor(DiffImgService);
