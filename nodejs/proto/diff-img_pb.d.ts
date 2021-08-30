// package: Diff
// file: diff-img.proto

import * as jspb from 'google-protobuf';

export class DiffRequest extends jspb.Message {
  getFirst(): string;
  setFirst(value: string): void;

  getSecond(): string;
  setSecond(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DiffRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DiffRequest): DiffRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DiffRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DiffRequest;
  static deserializeBinaryFromReader(message: DiffRequest, reader: jspb.BinaryReader): DiffRequest;
}

export namespace DiffRequest {
  export type AsObject = {
    first: string,
    second: string,
  }
}

export class DiffResponse extends jspb.Message {
  getRes(): string;
  setRes(value: string): void;

  getSsim(): number;
  setSsim(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DiffResponse.AsObject;
  static toObject(includeInstance: boolean, msg: DiffResponse): DiffResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DiffResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DiffResponse;
  static deserializeBinaryFromReader(message: DiffResponse, reader: jspb.BinaryReader): DiffResponse;
}

export namespace DiffResponse {
  export type AsObject = {
    res: string,
    ssim: number,
  }
}

