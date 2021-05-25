#!/usr/bin/python3
# encoding: utf-8

from flask import Flask, render_template
import platform, os
import socket, subprocess


app = Flask(__name__)
mensaje=[]

@app.route("/")

def index():
	return render_template('index.html',mensaje=['System Check',''])

@app.route("/<parametro>")

def mostrar(parametro):
	if parametro=="ip":
		return render_template('index.html', mensaje=['Dirección IP local real', socket.gethostbyname(socket.gethostname() + ".local")])

	elif parametro=="nombre":
		return render_template('index.html', mensaje=['Nombre de la máquina', socket.gethostname()])

	elif parametro=="reiniciar":
		return render_template('index.html', mensaje=['Reiniciar equipo', os.system("shutdown -r")])

	else:
		return render_update('index.html', mensaje=['Error', 'Parámetro no válido, haz clicl en el menú superior'])

if __name__ == "__main__":
	app.run(host="127.0.0.1", port= 8080, debug=True)

