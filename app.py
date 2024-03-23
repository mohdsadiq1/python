from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_origin_ip_reverse():
    # Get the origin IP address from the request headers
    origin_ip = request.remote_addr

    # Split the IP address into octets and reverse them
    reversed_ip = '.'.join(reversed(origin_ip.split('.')))

    # Return the reversed IP address as a response
    return reversed_ip

if __name__ == '__main__':
    app.run(debug=True)
