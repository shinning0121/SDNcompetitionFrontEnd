import httplib
import json
 
class StaticFlowPusher(object):
 
    def __init__(self, server):
        self.server = server
 
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
 
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
 
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
 
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
 
pusher = StaticFlowPusher('10.0.2.15')
 
flow1 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=2"
    }
 
flow2 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_2",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=4"
    }

flow3 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_mod_3",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=1"
    }

flow4 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_4",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=1"
    }

flow5 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_5",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=1"
    }

flow6 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_6",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=4"
    }

flow7 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_7",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=2"
    }
 
flow8 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_8",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=4"
    }

flow9 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_mod_9",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=1"
    }

flow10 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_10",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=1"
    }

flow11 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_11",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=1"
    }

flow12 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_12",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=4"
    }

pusher.set(flow1)
pusher.set(flow2)
pusher.set(flow3)
pusher.set(flow4)
pusher.set(flow5)
pusher.set(flow6)
pusher.set(flow7)
pusher.set(flow8)
pusher.set(flow9)
pusher.set(flow10)
pusher.set(flow11)
pusher.set(flow12)
