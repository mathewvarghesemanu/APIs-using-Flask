from flask import Flask,jsonify,request
app=Flask(__name__)
stores=[
            {
                'name':'Mak3rspace',
                'items':
                    [
                        {
                            'name':'pen',
                            'cost':10
                        }
                    ]
            }
        ]


#POST /store data:{name}
@app.route('/store',methods=['POST'])
def poststore():
    request_data=request.get_json() 
    new_store={'name':request_data['name'],'items':[]}
    stores.append(new_store)
    return jsonify(new_store)

#POST /store/<string:name>:item
# @app.route('/store/<string:name>/item',methods=['POST'])
# def additem(name):
#     request_data=request.get_json()
#     for obj in stores:
#         if obj['name']==name:
#             new_item={'name':request_data['name'],'cost':request_data['cost']}
#             obj['items'].append(new_item)
#             return jsonify(new_item)
#     return jsonify({'message':'No store found'})


#GET /store
@app.route("/store")
def store():
    return jsonify({'stores':stores})

#GET /store/<string:name>
@app.route("/store/<string:name>")
def storename(name):
    for obj in stores: 
        if name==obj['name']:
            return jsonify(obj)    
        else :
            return jsonify({'name':'store not found'})

#GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def showitem(name):
    for obj in stores: 
        if name==obj['name']:
            return jsonify({'item':obj['items']})    
        else :
            return jsonify({'message':'store not found'})



app.run(port=5000)


