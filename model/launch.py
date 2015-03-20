#!/usr/bin/python
#-*-coding:utf-8-*-
#- Process installer

#- Copyright (C) 2014 GoldraK & Interhack 
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 
# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>

# WebSite: http://adminserver.org/
# Email: contacto@adminserver.org
# Facebook: https://www.facebook.com/pages/Admin-Server/795147837179555?fref=ts
# Twitter: https://twitter.com/4dminserver

import sys,ConfigParser,datetime, subprocess,os
sys.path.append('model')
from teco import color
sys.path.append('modules/secure_glamp/model')
from utils import logger

class launch(object):

	def __init__(self,translate, output, data, log):
		self.translate = translate
		self.output = output
		self.log = log
		config = ConfigParser.ConfigParser()
		if not config.read('modules/secure_glamp/apps/' + data):
			output.default("No existe el archivo de instalación")
			sys.exit()
		self.delimitador = config.get('delimitador','key')
		self.nombre = config.get('nombre','titulo')
		self.instalacion = config.get('comandoinstalacion','opciones')
		self.configuracion = config.get('comandopostinstalacion','opciones')

	def install(self):
		self.output.default(color('verde','\nInstalando ' + self.nombre + '\n'))
		logger.write('Instalando ' + self.nombre, self.nombre)
		comandos = self.instalacion.split('\n')
		for comando in comandos:
			try:
				if(comando.split(self.delimitador)[0] !=''):
					self.output.default(comando.split(self.delimitador)[0].strip())
				
				self.output.default('Trabajando tomate una birra mientras tanto')
				os.system(comando.split(self.delimitador)[1].strip())
				#command = subprocess.Popen(comando.split(self.delimitador)[1].strip(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
				#command.stdout.read()
				#self.output.default(command_stdout)
				logger.write('Finalizada ',self.nombre)

			except:
				self.output.default('No esta bien formado el archivo')

	def configuration(self):
		self.output.default(color('verde', '\nConfigurando' + '\n'))
		logger.write('Configurando ' + self.nombre, self.nombre)
		comandos = self.configuracion.split('\n')
		for comando in comandos:
			try:
				if(comando.split(self.delimitador)[0] !=''):
					self.output.default(comando.split(self.delimitador)[0].strip())
				
				#self.output.default(comando.split(self.delimitador)[1].strip())
				command = subprocess.Popen(comando.split(self.delimitador)[1].strip(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
				command_stdout = command.stdout.read()
				self.output.default(command_stdout)
				logger.write(comando.split(self.delimitador)[1].strip(),self.nombre)

			except:
				self.output.default('No esta bien formado el archivo')

	def view_log(self):
		opcion = raw_input(color('azul','\nDeseas ver el log de instalacion [S/n]: '))
		
		if opcion == 'S' or opcion == 's' or opcion == '':
			log = open('modules/secure_glamp/logs/' + self.nombre + '.log', 'r')
			self.output.default(log.read())
