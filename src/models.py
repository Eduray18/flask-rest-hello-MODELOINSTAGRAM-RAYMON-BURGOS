from eralchemy2 import render_er
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# TABLA QUE TE FALTA: Follower (Muchos a Muchos)


class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_from_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    user_to_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)

    # Esto dibuja las líneas en el diagrama
    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")


class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('user.id'), nullable=False)

    media = relationship("Media", backref="post")
    comments = relationship("Comment", backref="post")


class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('post.id'), nullable=False)


class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('post.id'), nullable=False)


# CÓDIGO PARA GENERAR EL DIAGRAMA
try:
    render_er(db.Model, 'diagram.png')
    print("¡Éxito! Ahora verás las flechas y la tabla Follower.")
except Exception as e:
    print(e)
