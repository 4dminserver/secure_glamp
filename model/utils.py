#!/usr/bin/python
#-*-coding:utf-8-*-
#- utility class

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

import datetime

class logger(object):
	@staticmethod
	def write(mensaje, archivo= ''):
		#- Obtenmos el dia actual
		dia = str(datetime.datetime.now()).split(' ')[0]
		
		#- Abrimos el log general
		log = open('modules/secure_glamp/logs/' + archivo + '.log', 'a')

		#- Si el mensaje esta vacio escribe un salto de linea, sino escribe la fecha con el mensaje
		if mensaje != '\n':
			mensaje = "[" + str(datetime.datetime.now()).split('.')[0] + "]: " + mensaje
			#- Escribir el mensaje en el archivo
			log.write(mensaje + "\n")
		else:
			log.write("\n")
		#- Cerramos el archivo log
		log.close()