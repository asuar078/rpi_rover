from __future__ import print_function
import sys
import socketserver
import json
import time
from motor_controller import controller, mock_controller

# global reference to controller
mc = mock_controller.MockController()


class UDPHandler(socketserver.BaseRequestHandler):
    """
    The UDP RequestHandler for the server. We pass this to the
    server instance, don't directly initialize this class. The
    server instance will call it each time it needs.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, *args):
        """Pass along any arguments to our parent."""
        self.mc = mc
        print("creating UDP server")
        # print("args: " + str(args))
        socketserver.BaseRequestHandler.__init__(self, *args)

    def handle(self):
        """
        Overrides BaseRequestHandler.handle() to process requests.
        self.request is a tuple == (data socket, client socket)
        """
        data = self.request[0].strip()
        # socket = self.request[1]

        # print what we received from client
        print("{} wrote:".format(self.client_address[0]))
        # print(data)
        string_data = str(data, 'utf-8')
        print(string_data)
        loaded_json = json.loads(string_data)

        left_angle = loaded_json['left_angle']
        left_strength = loaded_json['left_strength']

        # print("left angle: " + str(left_angle) + ", strength: " + str(left_strength))

        right_angle = loaded_json['right_angle']
        right_strength = loaded_json['right_strength']

        # print("right angle: " + str(right_angle) + ", strength: " + str(right_strength))

        self.mc.left_motors(left_angle, left_strength)
        self.mc.right_motors(right_angle, right_strength)

        # send back in upper case
        # socket.sendto(data.upper(), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9090

    print("setting up motor controller")
    # mc = controller.Controller()

    # Create server instance
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)

    try:
        print("Serving on port {}. CTRL-c to end...".format(PORT))
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server shutting down...")
        sys.exit()
