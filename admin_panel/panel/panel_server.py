# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import admin_panel_pb2
import admin_panel_pb2_grpc
from hashtable.hashtable import HashTable


class AdminPanel(admin_panel_pb2_grpc.AdminPanelServicer):

    def __init__(self, hash_table=HashTable()):
        self.hash_table = hash_table

    def InsertClient(self, request, context):
        result = self.hash_table.set(request.cid, request.value)
        self.hash_table.structure()
        response = {'message': result}
        return admin_panel_pb2.Response(**response)

    def UpdateClient(self, request, context):
        result = self.hash_table.update(request.cid, request.value)
        self.hash_table.structure()
        response = {'message': result}
        return admin_panel_pb2.Response(**response)

    def GetClient(self, request, context):
        result = self.hash_table.get(request.cid)
        self.hash_table.structure()
        response = {'message': result}
        return admin_panel_pb2.Response(**response)

    def DeleteClient(self, request, context):
        result = self.hash_table.delete(request.cid)
        self.hash_table.structure()
        response = {'message': result}
        return admin_panel_pb2.Response(**response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_panel_pb2_grpc.add_AdminPanelServicer_to_server(AdminPanel(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
