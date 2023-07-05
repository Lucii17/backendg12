"""desarrollar backend"""
from flask import Flask ,jsonify ,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
"""a partir de este objeto se crea la conexion a la BD, modelos y manipula la misma """

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/crud_aa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#modelo BS

class Aire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    imagen = db.Column(db.String(400))
    precio = db.Column(db.Float())
    stock = db.Column(db.Integer)
    marca = db.Column(db.String(50))

    def __init__(self, nombre, imagen, precio, stock, marca):
        self.nombre = nombre
        self.imagen = imagen
        self.precio = precio
        self.stock = stock
        self.marca = marca

#se pueden crear todas las tablas que se quiera acá abajo

with app.app_context():
    db.create_all()  #acá se crea la tabla

class AireSchema(ma.Schema):
    class Meta:
        fields= ('id', 'nombre','imagen','precio', 'stock', 'marca')

aire_schema=AireSchema()
aires_schema=AireSchema(many=True)

@app.route('/aires', methods=['GET'])
def get_aires():
    aires = Aire.query.all()
    resultado = aires_schema.dump (aires)
    return jsonify(resultado)

@app.route('/aires/<id>', methods=['GET'])
def get_aire(id):
    aire = Aire.query.get(id)
    return aire_schema.jsonify(aire)

@app.route('/aires/<id>', methods=['DELETE'])
def delete_aire(id):
    aire=Aire.query.get(id)
    db.session.delete (aire)
    db.session.commit()
    return aire_schema.jsonify(aire)

@app.route('/aires', methods=['POST'])
def created_aire():
    nombre = request.json['nombre']
    imagen = request.json['imagen']
    precio = request.json['precio']
    stock = request.json['stock']
    marca = request.json['marca']
    nuevo_aire = Aire (nombre, imagen, precio, stock, marca)
    db.session.add(nuevo_aire)
    db.session.commit()
    return aire_schema.jsonify(nuevo_aire)

@app.route('/aires/<id>', methods=['PUT'])
def update_aire(id):
    aire = Aire.query.get(id)
    nombre = request.json['nombre']
    imagen = request.json['imagen']
    precio = request.json['precio']
    stock = request.json['stock']
    marca = request.json['marca']

    aire.nombre = nombre
    aire.imagen = imagen
    aire.precio = precio
    aire.stock = stock
    aire.marca = marca

    db.session.commit() #guarda los datos en la bd
    return aire_schema.jsonify(aire)
#pablo
class Lavarropa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    precio = db.Column(db.Float())
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, marca, precio, stock, imagen):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

with app.app_context():
    db.create_all()

class LavarropaSchema(ma.Schema):
    class Meta:
        fields =('id', 'nombre', 'marca', 'precio', 'stock', 'imagen')

lavarropa_schema=LavarropaSchema()
lavarropas_schema=LavarropaSchema(many=True)

@app.route('/lavarropas', methods=['GET'])
def get_lavarropas():
    lavarropas = Lavarropa.query.all()
    resultado = lavarropas_schema.dump(lavarropas)
    return jsonify(resultado)

@app.route('/lavarropas/<id>', methods=['GET'])
def get_lavarropa(id):
    lavarropa=Lavarropa.query.get(id)
    return lavarropa_schema.jsonify(lavarropa)

@app.route('/lavarropas/<id>', methods=['DELETE'])
def delete_lavarropa(id):
    lavarropa=Lavarropa.query.get(id)
    db.session.delete(lavarropa)
    db.session.commit()
    return lavarropa_schema.jsonify(lavarropa)

@app.route('/lavarropas' , methods=['POST'])
def create_lavarropa():
    nombre = request.json['nombre']
    marca = request.json['marca']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    nuevo_lavarropa = Lavarropa(nombre, marca, precio, stock, imagen)
    db.session.add(nuevo_lavarropa)
    db.session.commit()
    return lavarropa_schema.jsonify(nuevo_lavarropa)

@app.route('/lavarropas/<id>', methods=['PUT'])
def update_lavarropa(id):
    lavarropa = Lavarropa.query.get(id)

    nombre = request.json['nombre']
    marca = request.json['marca']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']

    lavarropa.nombre = nombre
    lavarropa.marca = marca
    lavarropa.precio = precio
    lavarropa.stock = stock
    lavarropa.imagen = imagen

    db.session.commit()
    return lavarropa_schema.jsonify(lavarropa)   
#Braian
class Television (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    precio = db.Column(db.Float())
    stock = db.Column(db.Integer())
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, marca, precio, stock, imagen):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

with app.app_context():
    db.create_all() # Se crea TODAS la tabla que se definieron


# Creo una instancia de Marshmallow
class TelevisionSchema(ma.Schema):
    class Meta:
        fields=('id','nombre', 'marca', 'precio', 'stock', 'imagen')


television_schema=TelevisionSchema()            # El objeto television_schema es para traer un producto
lista_televisiones_schema=TelevisionSchema(many=True)  # El objeto lista_televisiones_schema es para traer multiples registros de producto


# Creo los endPoind

# Lista de Televisiones
@app.route('/television', methods=['GET'])
def getTelevision():
    tv = Television.query.all()
    listaTv = lista_televisiones_schema.dump(tv)
    return jsonify(listaTv)

# Get por ID 
@app.route('/television/<id>', methods=['GET'])
def getByIdTelevision(id):
    tv = Television.query.get(id)
    return television_schema.jsonify(tv) # retorna el JSON de una TV recibida


# DELETE Borro una TV por ID
@app.route('/television/<id>', methods=['DELETE'])
def DeleteByIdTelevision(id):
    tv = Television.query.get(id)
    db.session.delete(tv)
    db.session.commit()  # persiste los datos en la base de datos
    return television_schema.jsonify(tv)

# POST creo uns TV
@app.route('/television', methods=['POST'])
def createTelevision():
    nombre = request.json['nombre']
    marca = request.json['marca']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    nueva_tv = Television(nombre, marca, precio, stock, imagen)
    db.session.add(nueva_tv)
    db.session.commit()
    return television_schema.jsonify(nueva_tv)
    
# PUT actualiso los campos de la TV 
@app.route('/television/<id>', methods=['PUT'])
def updataTelevisionid(id):
    tv = Television.query.get(id)

    nombre = request.json['nombre']
    marca = request.json['marca']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']

    tv.nombre = nombre
    tv.marca = marca
    tv.precio = precio
    tv.stock = stock
    tv.imagen = imagen

    db.session.commit()
    return television_schema.jsonify(tv)
#Enzo



class Heladera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    precio = db.Column(db.Float())
    stock = db.Column(db.Integer())
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, marca, precio, stock, imagen):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

with app.app_context():
    db.create_all() 


class HeladeraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'marca', 'precio', 'stock', 'imagen')


heladera_schema = HeladeraSchema()            
lista_heladeras_schema = HeladeraSchema(many=True)  


@app.route('/heladeras', methods=['GET'])
def get_Heladera():
    heladeras = Heladera.query.all()
    lista_heladeras = lista_heladeras_schema.dump(heladeras)
    return jsonify(lista_heladeras)


@app.route('/heladera/<id>', methods=['GET'])
def getByIdHeladera(id):
    heladera = Heladera.query.get(id)
    return heladera_schema.jsonify(heladera) 


@app.route('/heladera/<id>', methods=['DELETE'])
def delete_Heladera(id):
    heladera = Heladera.query.get(id)
    db.session.delete(heladera)
    db.session.commit()  
    return heladera_schema.jsonify(heladera)

@app.route('/heladera', methods=['POST'])
def createHeladera():
    nombre = request.json['nombre']
    marca = request.json['marca']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    nueva_heladera = Heladera(nombre, marca, precio, stock, imagen)
    db.session.add(nueva_heladera)
    db.session.commit()
    return heladera_schema.jsonify(nueva_heladera)
    
@app.route('/heladera/<id>', methods=['PUT'])
def updataHeladeraid(id):
    heladera = Heladera.query.get(id)

    nombre = request.json['nombre']
    marca = request.json['marca']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']

    heladera.nombre = nombre
    heladera.marca = marca
    heladera.precio = precio
    heladera.stock = stock
    heladera.imagen = imagen

    db.session.commit()
    return heladera_schema.jsonify(heladera)



if __name__ == '__main__':
    app.run(debug=True, port=5000)

