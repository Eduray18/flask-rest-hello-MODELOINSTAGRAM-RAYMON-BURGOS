from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# 1. MODELO DE USUARIO
class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)

    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

# 2. MODELO DE POST (PUBLICACIÓN)
class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)

    comments = relationship("Comment", backref="post")
    media = relationship("Media", backref="post")

# 3. MODELO DE COMMENT (COMENTARIO)
class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('post.id'), nullable=False)

# 4. MODELO DE MEDIA (IMÁGENES O VIDEOS)
class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('post.id'), nullable=False)

## -- GENERAr EL PNG ---
import os
from eralchemy2 import render_er

try:
    render_er(db.Model, 'diagram.png')
    print("¡Éxito! El archivo diagram.png ha sido creado.")
except Exception as e:
    print(f"Error generando el diagrama: {e}")