from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/plataforma_estudio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos
class Cursos(db.Model):
    __tablename__ = 'Cursos'  
    
    Id = db.Column(db.BigInteger, primary_key=True)
    Nombre = db.Column(db.String(255), nullable=False)
    Image = db.Column(db.Text, nullable=False)
    Descripcion = db.Column(db.Text, nullable=True)
    Precio = db.Column(db.Numeric(10, 2), default=0.00)
    Categoria = db.Column(db.String(50), nullable=False)
    Fecha_creacion = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {
            'Id': self.Id,
            'Nombre': self.Nombre,
            'Image': self.Image,
            'Descripcion': self.Descripcion,
            'Precio': str(self.Precio),
            'Categoria': self.Categoria,
            'Fecha_creacion': self.Fecha_creacion
        }

# Ruta para obtener los cursos en formato JSON
@app.route("/api/cursos")
def obtener_cursos():
    cursos = Cursos.query.all() 
    cursos_data = [curso.to_dict() for curso in cursos]  
    return jsonify(cursos_data)

if __name__ == '__main__':
    app.run(debug=True)
