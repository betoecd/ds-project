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

from __future__ import print_function
import logging

import grpc

import admin_panel_pb2
import admin_panel_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = admin_panel_pb2_grpc.AdminPanelStub(channel)
        response = []
        response.append(stub.InsertClient(
            admin_panel_pb2.RequestValue(cid='beto', value='mago dos códigos')))
        response.append(stub.InsertClient(
            admin_panel_pb2.RequestValue(cid='beto2', value='mago dos códigos 2')))
        response.append(stub.UpdateClient(
            admin_panel_pb2.RequestValue(cid='beto3', value='mago dos códigos')))
        response.append(stub.UpdateClient(
            admin_panel_pb2.RequestValue(cid='beto2', value='mago dos códigos II')))
        response.append(stub.GetClient(
            admin_panel_pb2.Request(cid='beto3')))
        response.append(stub.GetClient(
            admin_panel_pb2.Request(cid='beto2')))
        response.append(stub.DeleteClient(
            admin_panel_pb2.Request(cid='beto3')))
        response.append(stub.DeleteClient(
            admin_panel_pb2.Request(cid='beto')))

    for r in response:
        print(r)

    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
