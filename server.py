import grpc
import pingpong_pb2 
import pingpong_pb2_grpc
from concurrent import futures # it will run a threadpool executer
import time
import threading



class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
    def __init__(self, *args, **kwargs):
        self.counter = 0; # variable counter to count
        self.lastPrintTime = time.time() # variable lastPrintTime to get time

    def ping(self, request, context): # rpc ping method described in .proto file 
        self.counter += 1; #increase counter
        if(self.counter > 10000): # if counter value > 10000
            print("10000 calls in %3f seconds" % (time.time() - self.lastPrintTime))
            self.lastPrintTime = time.time()
            self.counter = 0;
        return pingpong_pb2.Pong(count=request.count + 1) # return count value increased by 1

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers= 100))
    pingpong_pb2_grpc.add_PingPongServiceServicer_to_server(Listener() , server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("server on: Threads %i" %(threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)

if __name__ == "__main__":
    serve()