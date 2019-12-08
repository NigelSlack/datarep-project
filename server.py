from flask import Flask, jsonify, request, abort
from projectDAO import projectDAO
import logging

app = Flask(__name__,static_url_path='',static_folder='.')

# ref https://www.scalyr.com/blog/getting-started-quickly-with-flask-logging/
logging.basicConfig(filename='log.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#curl "http://127.0.0.1:5000/project/cd"
@app.route('/project/cd')
def getAllCd():
    results=projectDAO.getAllCd()
    return jsonify(results)

#curl "http://127.0.0.1:5000/project/dvd"
@app.route('/project/dvd')
def getAllDvd():
    results=projectDAO.getAllDvd()
    return jsonify(results)

#curl "http://127.0.0.1:5000/project/cd/1"
@app.route('/project/cd/<int:id>')
def findByIdCd(id):
    app.logger.debug('Body: %s', request.get_data())    
    foundCd=projectDAO.findByIDCd(id)
    return jsonify(foundCd)    

#curl "http://127.0.0.1:5000/project/dvd/1"
@app.route('/project/dvd/<int:id>')
def findByIdDvd(id):
    app.logger.debug('Body: %s', request.get_data())    
    foundDvd=projectDAO.findByIDDvd(id)
    return jsonify(foundDvd)    

# curl -i -H "Content-Type:application/json" -X POST -d "{\"album\":\"New Album\",\"artist\":\"A N Other\",\"price\":1200}" http://127.0.0.1:5000/project/cd
@app.route('/project/cd', methods=['POST'])
def createCd():
    app.logger.debug('Body: %s', request.get_data())
    if not request.json:
        abort(400)
    cd = {
        "album": request.json['album'],
        "artist": request.json['artist'],
        "price": request.json['price']
    }  
    values = (cd['album'],cd['artist'],cd['price'])
    newId = projectDAO.createCd(values)
    cd['id']=newId
    return jsonify(cd) 

# curl -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"New Film\",\"director\":\"A N Other\",\"price\":1200}" http://127.0.0.1:5000/project/dvd
@app.route('/project/dvd', methods=['POST'])
def createDvd():
    app.logger.debug('Body: %s', request.get_data())    
    if not request.json:
        abort(400)
    dvd = {
        "title": request.json['title'],
        "director": request.json['director'],
        "price": request.json['price']
    }  
    values = (dvd['title'],dvd['director'],dvd['price'])
    newId = projectDAO.createDvd(values)
    dvd['id']=newId
    return jsonify(dvd) 

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"album\":\"Another New Album\",\"artist\":\"A N Other\",\"price\":1150}" http://127.0.0.1:5000/project/cd/1
@app.route('/project/cd/<int:id>',methods=['PUT'])
def updateCd(id):
    app.logger.debug('Body: %s', request.get_data())    
    foundCd = projectDAO.findByIDCd(id)
    if not foundCd:
        abort(404)
    if not request.json:
        abort(400)    
    
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        reqJson['price']=int(reqJson['price'])
    if 'album' in reqJson:
        foundCd['album'] = reqJson['album']
    if 'artist' in reqJson:
        foundCd['artist'] = reqJson['artist'] 
    if 'price' in reqJson:
        foundCd['price'] = reqJson['price'] 
    values = (foundCd['album'],foundCd['artist'],foundCd['price'],foundCd['id'])
    projectDAO.updateCd(values)    
    return jsonify(foundCd)  

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"Another New Film\",\"director\":\"A N Other\",\"price\":1150}" http://127.0.0.1:5000/project/dvd/1
@app.route('/project/dvd/<int:id>',methods=['PUT'])
def updateDvd(id):
    app.logger.debug('Body: %s', request.get_data())    
    foundDvd = projectDAO.findByIDDvd(id)
    if not foundDvd:
        abort(404)
    if not request.json:
        abort(400)    
    reqJson = request.json
    reqJson['price']=int(reqJson['price'])
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)   
    if 'title' in reqJson:
        foundDvd['title'] = reqJson['title']
    if 'director' in reqJson:
        foundDvd['director'] = reqJson['director'] 
    if 'price' in reqJson:
        foundDvd['price'] = reqJson['price'] 
    values = (foundDvd['title'],foundDvd['director'],foundDvd['price'],foundDvd['id'])
    projectDAO.updateDvd(values)    
    return jsonify(foundDvd)  

#curl -X DELETE "http://127.0.0.1:5000/project/cd/1"
@app.route('/project/cd/<int:id>',methods=['DELETE'])
def deleteCd(id):
    app.logger.debug('Body: %s', request.get_data())    
    projectDAO.deleteCd(id)  
    return jsonify({"done":True})         

#curl -X DELETE "http://127.0.0.1:5000/project/dvd/1"
@app.route('/project/dvd/<int:id>',methods=['DELETE'])
def deleteDvd(id):
    app.logger.debug('Body: %s', request.get_data())    
    projectDAO.deleteDvd(id)  
    return jsonify({"done":True})         

if __name__ == '__main__':
    app.run(debug=True)    