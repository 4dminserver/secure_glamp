#!/usr/bin/python
#-*-coding:utf-8-*-
#- secure_glamp Class

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

class add(object):
	#- @output.[option](default, error)(text) -> printed by stdout
	#- @translate.[option](init('nameTranslate')) -> initializes the translation file
	#- @log.[option](write)(text,*1) -> 1 is error -> saves information in the logs
	#- @installer -> module for install dependencies -> nonoperating

	def __init__(self, output, translate, log, installer,options):
		#- imports necessary
		import sys, os, ConfigParser
		sys.path.append('modules/secure_glamp/model')
		from launch import launch
		
		#- Operations
		#- Example:
		output.default('Securizame, un servidor seguro es la mejor opción')
		def explorar(ruta='.', search='.data'):
			lista_dic = {}
			contador = 0
			for root,dirs,files in os.walk(ruta):
				for file in [f for f in files if f.lower().endswith(search)]:
					if '.data' in file:
						config = ConfigParser.ConfigParser()
						if not config.read([root + '/' + file]):
							print "No existe el archivo de instalación"
							break

						order = config.get('orden','orden')
						name = config.get('nombre', 'titulo') + '(ig)' + file					
						lista_dic[order] = name

			return lista_dic

		menu = explorar('modules/secure_glamp/apps')
		
		menuVisualizacion = sorted(menu.items(), key=lambda x: x[0])
		for x in menuVisualizacion:
			output.default(str(x[0]) + ' - ' + str(x[1]).split('(ig)')[0])
			
		for items in menu:
		#	output.default(str(items) + ' - ' + str(menu[items]).split('(ig)')[0])
			elements_menu = len(menu)


		control = True
		while control == True:
			options.set_completer(help.complete)
			sentencia = raw_input("Secure_console >> ")
			try:
				if sentencia == 'exit':
					control = False
				elif sentencia == 'version':
					output.default(help.version())
				elif sentencia == 'info':
					output.default(help.info())
				elif int(sentencia) <= int(elements_menu):
					try:
						opcion = str(menu[sentencia]).split('(ig)')[1]
						start = launch(translate, output, opcion, log)
						start.install()
						start.configuration()
						start.view_log()
						menu = explorar('modules/secure_glamp/apps')
						menuVisualizacion = sorted(menu.items(), key=lambda x: x[0])
						for x in menuVisualizacion:
							output.default(str(x[0]) + ' - ' + str(x[1]).split('(ig)')[0])

						for items in menu:
							elements_menu = len(menu)

					except:
						output.default('Opción no valida')
				else:
					output.default('Opción no valida')
			except:
				output.default('Opción no valida')
		sys.exit()

class help(object):
	#- Commands default
	@staticmethod
	def complete(text, state):
		possibilities = ["exit", "version", "help", "info"]
		results = [x for x in possibilities if x.startswith(text)] + [None]
		return results[state]

	#- Help for menu
	@staticmethod
	def help(translate=''):
		return "Ayuda Secure GLAMP"

	@staticmethod
	def version(translate=''):
		return "Version 0.1"

	@staticmethod
	#- @translate.[option](init('nameTranslate')) -> initializes the translation file
	def info(translate = ''):
		return 'Secure Glamp'

	@staticmethod
	#- Especificamos si necesita el modulo paquetes adicionales.
	def package():
		#- List of extra dependencies needed by the module
		additionalPackage = []
		return additionalPackage
