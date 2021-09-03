# -*- coding: utf-8 -*-
from proto import diff_img_pb2 as messages
from proto import diff_img_pb2_grpc as services
import grpc
from concurrent import futures
from diff import diffImg

outdir="diff-results"
port="5000"
remote_address="0.0.0.0:{}".format(port)

class DiffImg(services.DiffImgServicer):
    def getDiff(self, request):
        res,ssim=diffImg(request.first,request.second,outdir)
        return messages.DiffResponse(res=res,ssim=ssim)

def main():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_DiffImgServicer_to_server(DiffImg,server)
    server.add_insecure_port(remote_address)
    server.start()
    print("py:diff-image-server is running... at {}",remote_address)
    server.wait_for_termination()
    return


if __name__=="__main__":
    main()