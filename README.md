﻿# Тесты, что по треку заказа можно получить данные о заказе в Яндекс.Самокат с помощью API Яндекс.Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

  ## Описание проекта
  - проект выполнен в программе PyCharm
  - состоит из 3 файлов: configuration.py, data.py, main.py
  
      ### Версии
	  - тестирование проводилось в PyCharm 2022.3.3
	  - адрес тестового стенда https://c33981af-8b19-45da-85ac-e689bcc3af2b.serverhub.praktikum-services.ru/
	  
	  ### Автоматизируемый сценарий
	  - Клиент создает заказ
	  - Проверяется, что по треку заказа можно получить данные о заказе
	  	  
	      #### Шаги воспроизведения
	      - Выполнить запрос на создание заказа (ручка '/api/v1/orders/') 
	      - Сохранить номер трека заказа
	      - Выполнить запрос на получения заказа по треку заказа (ручка '/api/v1/orders/track/')
	      - Проверить, что код ответа равен 200
	  
 
  
