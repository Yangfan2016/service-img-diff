import * as messages from "./proto/diff-img_pb";
import * as services from "./proto/diff-img_grpc_pb";
import grpc from "@grpc/grpc-js";


function main() {
    const channel = grpc.credentials.createInsecure();
    const client = new services.DiffImgClient("127.0.0.1:5000", channel);
    const req = new messages.DiffRequest();
    req.setFirst("nodejs/imgs/bbb-1.png");
    req.setSecond("nodejs/imgs/bbb-2.png");
    client.getDiff(req, (err, res) => {
        if (!err) {
            console.log('nodejs:client copyed', res)
        } else {
            console.log('err', err.message);
        }
    })
}

main()