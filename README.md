# WebScraping

#Recopilacion masiva de noticias

1.- Se inicio un nuevo proyecto scrapy con el nombre de 'news'
	scrapy startproject news

2.- Al ingresar a la la ubicacion del proyecto en la seccion de la carpeta 'spiders'

3.- Configuramos nuestro archivos spiders para recolectar los titurales y el link de las noticias en los siguientes dominios: 
	-bbc.spiders.py //Pagina de la BBC
	-cnn.spiders.py //Pagina de CNN en español
	-co.spiders.py //Pagina de El Comercio
	-ev.spiders.py //Pagina de Ecuavisa	
	-rts.spiders.py // Pagina de RTS
	-ta.spiders.py // Pagina de Teleamazonas
	-tc.spiders.py //Pagina de TC
	-tg.spiders.py // Paginda de el Telegrago 
	-universo_spiders.py // Pagina de el Universo

4.-Recopilamos los datos hacia diferentes archivos json's
	scrapy crawl [news_name] -o [news_name].json -t json

5.-Finalmente se importaron los archivos a un servido Cluster de Atlas MongoDB (result.pdf)

6.- Al finalizar el proceso se obtuvo un total de 32599 documentos 

