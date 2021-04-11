from flask import Flask, jsonify, request
from admin_panel import Administrator
from markupsafe import escape
from panel_server import serve
import os

app = Flask(__name__)

admin = Administrator()

@app.route('/', methods=['GET'])
def root_route():
    return jsonify({
        'message': 'Welcome to the Admin Panel!',
    })


@app.route('/register', methods=['POST'])
def register():
    # admin = Administrator()
    result = admin.register(
        cid=request.json['cid'],
        info=request.json['info']
    )
    return jsonify({'message': result.message})

@app.route('/update', methods=['PUT'])
def update():
    # admin = Administrator()
    result = admin.update(
        cid=request.json['cid'],
        info=request.json['info']
    )
    return jsonify({'message': result.message})

@app.route('/client/<cid>', methods=['GET'])
def get(cid):
    # admin = Administrator()
    result = admin.get(cid=escape(cid))
    return jsonify({'message': result.message})

@app.route('/client/<cid>', methods=['DELETE'])
def delete(cid):
    # admin = Administrator()
    result = admin.delete(cid=escape(cid))
    return jsonify({'message': result.message})

def main():
    admin_panel_server = os.fork()
    if admin_panel_server == 0:
        return serve()
    app.run(debug=True)

if __name__ == '__main__':
    exit(main())
