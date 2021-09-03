"use strict";
exports.__esModule = true;
var messages = require("./proto/diff-img_pb");
var services = require("./proto/diff-img_grpc_pb");
var grpc = require("grpc");
function main() {
    var channel = grpc.credentials.createInsecure();
    var client = new services.DiffImgClient("127.0.0.1:5000", 
    // @ts-ignore
    channel);
    var req = new messages.DiffRequest();
    req.setFirst("nodejs/imgs/bbb-1.png");
    req.setSecond("nodejs/imgs/bbb-2.png");
    client.getDiff(req, function (err, res) {
        if (!err) {
            console.log('nodejs:client copyed', res);
        }
        else {
            console.log('err', err.message);
        }
    });
}
main();
