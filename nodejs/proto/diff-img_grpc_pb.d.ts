// package: Diff
// file: diff-img.proto

import * as grpc from '@grpc/grpc-js';
import * as diff_img_pb from './diff-img_pb';

interface IDiffImgService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  getDiff: IDiffImgService_IgetDiff;
}

interface IDiffImgService_IgetDiff extends grpc.MethodDefinition<diff_img_pb.DiffRequest, diff_img_pb.DiffResponse> {
  path: '/Diff.DiffImg/getDiff'
  requestStream: false
  responseStream: false
  requestSerialize: grpc.serialize<diff_img_pb.DiffRequest>;
  requestDeserialize: grpc.deserialize<diff_img_pb.DiffRequest>;
  responseSerialize: grpc.serialize<diff_img_pb.DiffResponse>;
  responseDeserialize: grpc.deserialize<diff_img_pb.DiffResponse>;
}

export const DiffImgService: IDiffImgService;
export interface IDiffImgServer extends grpc.UntypedServiceImplementation {
  getDiff: grpc.handleUnaryCall<diff_img_pb.DiffRequest, diff_img_pb.DiffResponse>;
}

export interface IDiffImgClient {
  getDiff(request: diff_img_pb.DiffRequest, callback: (error: grpc.ServiceError | null, response: diff_img_pb.DiffResponse) => void): grpc.ClientUnaryCall;
  getDiff(request: diff_img_pb.DiffRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: diff_img_pb.DiffResponse) => void): grpc.ClientUnaryCall;
  getDiff(request: diff_img_pb.DiffRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: diff_img_pb.DiffResponse) => void): grpc.ClientUnaryCall;
}

export class DiffImgClient extends grpc.Client implements IDiffImgClient {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: Partial<grpc.ClientOptions>);
  public getDiff(request: diff_img_pb.DiffRequest, callback: (error: grpc.ServiceError | null, response: diff_img_pb.DiffResponse) => void): grpc.ClientUnaryCall;
  public getDiff(request: diff_img_pb.DiffRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: diff_img_pb.DiffResponse) => void): grpc.ClientUnaryCall;
  public getDiff(request: diff_img_pb.DiffRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: diff_img_pb.DiffResponse) => void): grpc.ClientUnaryCall;
}

