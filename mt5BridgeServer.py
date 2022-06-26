from flask import Flask, request
import MetaTrader5 as mt5
api = Flask(__name__)


@api.route('/mt5', methods=['GET'])
def testMethod():
    return {"message": "success"}, 200


@api.route('/mt5', methods=['POST'])
def callMethods():
    try:
        if not request.is_json:
            return {
                'message': "Incorrect data"
            }, 404
        data = request.get_json()
        print("data", data)
        methodName = data['methodName']
        args = None
        if ('args' in data):
            args = data['args']
        objectToUse = mt5
        print("Attempt to call mt5.", methodName, "with", args)
        if not hasattr(objectToUse, methodName):
            return {
                'message': "Method does not exist"
            }, 404
        else:
            method = getattr(objectToUse, methodName)
            methodResult = None
            if isinstance(args, list):
                methodResult = method(*args)
            elif isinstance(args, dict):
                methodResult = method(**args)
            else:
                methodResult = method()
        print("methodResult ", methodResult)
        return {'data': methodResult}, 200

    except Exception as e:
        print("Error :", e)
        return {'message': "Something went wrong"}, 500


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=5001)
