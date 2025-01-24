# **Дипломная работа**
## **Дипломная работа по теме:** Анализ и сравнение написания web-приложений с использованием разных фреймворков
### **Автор:** Росолович Мария Андреевна

## **Оглавление дипломной работы:**
### 1. Введение
### 2. Основные понятия и определения
### 3. Методы и подходы к разработке.Х♲
### 4. Обзор популярных инструментов для разработки разработки веб-приложений на Python.
### 5. Разработка в соответствии с созданной документацией. ♲
### 6. Анализ и интерпретация результатов.
### 7. Заключение.


## 1. Введение
   
### ***Обоснование выбора темы:***
В современном мире информационные технологии имееют огромное значение для нынешнего человека. Сейчас рынок цифровых технологий широк, как никогда и он все еще продолжает расти.
Со временем он будет охватывать все больше и больше областей. А следовательно станет одной из важнейших, если не самой важной отраслью в мире. Что натолкивает на желание быть готовым к будующему,
быть способным ориентироваться в быстро меняющемся окружение и соответствовать нуждам рынка. Что приводит нас к теме "Анализ и сравнение написания web-приложений с использованием разных фреймворков",
которая позволяет углубить свои знания о том как именно был создан тот сайт на котором вы часто покупаете одежду, развить навыки, которые в свою очередь позволят вам быть способным самостоятельно создать сайт
пользующийся популярностью и приносящий пользу и выбрать фреймворк позволяющий работать с материалом лучше всего и наконец позволит получить собственный опыт в сфере написания web-приложений с использованием
разных фреймворков. В своей работе я буду рассматривать Django, Flask и FastAPI, поскольку они обладают наибольшей популярностью в сфере создания web-приложений на языке Python и следовательно являются самыми 
удобными. Изучение именно этих технологий для написания приложений позволит мне получить опыт для будующей работы и удовлетворить собственнуюю жажду знаний об этой сфере.

### ***Определение цели и задач исследования:***

#### ***Цель исследования:***
Создать приложение с использованием 3 разных фреймворков для сравнения их особенностей и определения плюсов и минусов каждого.

#### ***Задачи исследования:***
1. Провести обзор популярных инструментов для разработки веб-приложений на Python.
2. Проанализировать специфику работы каждого из исследуемых фреймворков.
3. Разработка прилжений с использованием нужных фреймворков.
4. Сравнить работу каждого из фреймворков с друг другом.
5. Опредение плюсов и минусов каждого из фреймворков.

## 2. Основные понятия и определения
1. **Фреймворк (Framework):** Программная платформа, которая предоставляет готовые компоненты и инструменты для разработки приложений. В контексте веб-приложений часто используются Django, FastAPI или Flask.
2. **Web-приложение:** 
3. **MVT(Model-View-Template):** Архитектурный принцип програмного обеспечения, который расшифровывается, как модель – представление – шаблон.
4. **ORM (Object-Relational Mapping):** 
5. **HTML-шаблон:** 
6. **URL-маршрутизация:** 
7. **“Батарейки в комплекте”:** 
8. **MVT:** 
9. **Jinja2:** 
10. **WSGI:** 
11. **API:** 
12. **Dependency Injection:** 
## 3. Методы и подходы к разработке.
Х
### ***Выбор фреймворка.***
Для анализа и сравнения написания web-приложений будут использованы самые популярные фреймворки используемые для этого, то есть Django, Flask и FastAPI.
### ***Архитектура веб-приложения.***
Frontend моего приложения будет написан при помощи HTML, а Backend будет реализован с помощью уже упомянутых Django, Flask и FastAPI.
### ***Обеспечение безопасности.***
X
## 4. Обзор популярных инструментов для разработки разработки веб-приложений на Python.
В этой главе я буду обозревать особенности и возможности фреймворков Django, Flask и FastAPI.
### ***Django.***
Django является фреймворком в свободном доступе для разработки приложений и сайтов в Python. Django следует принципу **MVT**, который означает **Model-View-Template**, что в свою очередь означает 
**модель – представление – шаблон**. В соответствии с этим принципом Django делит свою работу на **модель**, в которой определяется структура хранения данных в базе, **представление**, в котором 
происходит управление логикой запросов пользователей и наконец **шаблон**, который определяет каким образом данные будут показаны на сайте.
#### **Основные возможности:**
* Имеет встроенную админ панель позволяющую управлять данными
* Наличие ORM (Object-Relational Mapping) предостовляющий удобный способ для взаимодействия с базами данных
* Отличный шаблонизатор для HTML-шаблонов
* Гибкая система URL-маршрутизации
* Встроенная Аутентификация и авторизация
* Встроенная защита 
#### **Особенности:**
* “Батарейки в комплекте”, что означает большое количество встроенных функций
* ORM Django является одним из самых мощных и гибких в Python
### ***Flask.*** 
Flask является микрофреймворком, но это не означает, что у него меньше возможностей, чем у остальных фреймворков в подборке. Flask на самом деле не является фреймворком MVC,
но он очень хорошо подходит для него. Принцип **MVC**, который означает **Model-View-Controller**, что в свою очередь означает **модель-представление-контроллер**. В соответствии с этой архитектурой 
Flask делится на **модель**, которая используется для хранения и обработки данных, **представление**, который отображает данные пользователю и получает от него и сообщает о его взаимодействии с интерфейсом
и **контроллер**, который управляет взаимодействием данных между моделью и представлением.
#### **Основные возможности:**
* Имеет гибкую систему URL-маршрутизации
* Мощный и гибкий шаблонизатор Jinja2
* Легко расширяется с помощью различных библиотек и расширений
#### **Особенности:**
* Является крайне минималистичным, предоставляя только самые необходимые инструменты
* Дает полную свободу в выборе компонентов и архитектуре
* Прост для освоения и использования
* Стандарт WSGI
### ***FastAPI***
FastAPI является современным и высокопроизводительный фреймворком, который был разработан специально для создания API на основе стандартов OpenAPI и JSON Schema. 
Он использует асинхронное программирование и подсказки типов Python для обеспечения высокой скорости и производительности. 
#### **Основные возможности:**
* Имеет автоматическую валидацию данных
* Автоматическая генерация интерактивной документации OpenAPI
* Поддерживает ассинхронного програмирования
* Наличие Dependency Injection
#### **Особенности:**
* Исподьзование самых современных подходов
* Оптимизирован для работы с асинхронным кодом
* Фокусировка на создании API

## 5. Разработка в соответствии с созданной документацией.

### ***Разработка приложения на Django.***
Для начала работы с  Django необходимо для начала установить его командой:   
```pip install Django```  
Чтобы создать проект в котором мы будем работать нужно ввести команду:   
``` django-admin startproject project_name ```   
вместо  ```project_name```  нужно написать название вашего проекта.   
После создания проекта необходимо перейти в него с помощью команды:   
```cd project_name```  
Затем мы создаем прложение при помощи команды:   
``` python manage.py startapp app__name ```   
вместо  ``` app__name```  нужно написать название вашего приложения.  
После выполнения всех этих действий будет содана директория при помощи, которой можно начать создавать приложение. В директории будут находиться следующие файлы:  
![рис.1](https://github.com/Mitchy-art/Diplom_work/blob/main/img_dip/Снимок%20экрана%202025-01-24%20232501.png)

### ***Разработка приложения на Flask.***

### ***Разработка приложения на FastAPI.***

## 6. Анализ и интерпретация результатов.
### ***Скорость Разработки (Time-to-Market)***

#### **Django:**
* **Плюсы:** Благодаря большому количеству “батареек в комплекте” (ORM, админ-панель, шаблонизатор, формы) Django обеспечивает очень быструю разработку сложных приложений.
* **Минусы:** Может потребовать некоторого времени для изучения конвенций и архитектуры, прежде чем начать эффективно использовать.
#### **Flask:**
* **Плюсы:** Простота и минимализм Flask позволяют быстро начать разработку, особенно для небольших проектов.
* **Минусы:** Меньшее количество готовых инструментов означает, что разработчику придется самому реализовывать многие функции, что может увеличить время разработки.
#### **FastAPI:**
* **Плюсы:** Автоматическая генерация документации, валидация данных и асинхронность позволяют быстро разрабатывать API.
* **Минусы:** Меньше готовых компонентов для веб-приложений (отсутствие встроенного шаблонизатора) может увеличить время для разработки полнофункционального сайта.
#### **Вывод:** 
   Django выигрывает в плане скорости разработки сложных приложений, Flask - для простых, а FastAPI для API.

### ***Масштабируемость:***

#### **Django:**
* **Плюсы:** Хорошо масштабируется за счет ORM, четкой архитектуры и возможности разделения приложения на модули. Подходит для крупных проектов с высокой нагрузкой.
* **Минусы:** Может быть избыточным для небольших приложений.
#### **Flask:**
* **Плюсы:** Хорошо подходит для микросервисов и API, может быть масштабирован с использованием сторонних инструментов.
* **Минусы:** Поддержка и масштабирование больших приложений может быть сложнее, чем с Django.
#### **FastAPI:**
* **Плюсы:** Высокая производительность и асинхронность позволяют эффективно обрабатывать большое количество запросов, что делает его идеальным для масштабируемых API.
* **Минусы:** Менее подходит для масштабирования полнофункциональных веб-сайтов.
#### **Вывод:** 
   Django - для крупных сайтов, Flask - для API и микросервисов, FastAPI - для масштабируемых API.

### ***Производительность:***

#### **Django:**
* **Плюсы:** Хорошая производительность, но может быть не самой быстрой для высоконагруженных API.
* **Минусы:** ORM может создавать дополнительные накладные расходы, если не использовать его правильно.
#### **Flask:**
* **Плюсы:** Небольшой overhead и хорошая производительность для простых приложений.
* **Минусы:** Производительность может стать узким местом при больших нагрузках.
#### **FastAPI:**
* **Плюсы:** Высокая производительность благодаря асинхронности, валидации данных и оптимизированному коду.
* **Минусы:** Требует асинхронных операций и больше опыта работы с ними.
#### **Вывод:** 
   FastAPI – самый быстрый для API, Flask - для простых приложений, Django – хорошая производительность, но может уступать в производительности для высоконагруженных API.

### ***Гибкость и Расширяемость:***

#### **Django:**
* **Плюсы:** Четкая структура, но немного меньше гибкости из-за следования конвенциям.
* **Минусы:** Строгие конвенции могут ограничивать свободу разработчика.
#### **Flask:**
* **Плюсы:** Максимальная гибкость и свобода выбора компонентов и подходов к разработке.
* **Минусы:** Требует большей работы от разработчика по выбору и настройке необходимых инструментов.
#### **FastAPI:**
* **Плюсы:** Гибкость при создании API, возможность внедрения зависимостей.
* **Минусы:** Ограничения по созданию полнофункциональных сайтов, меньше поддержки для шаблонов HTML.
#### **Вывод:** 
   Flask - самый гибкий, FastAPI - гибок для API, Django - наименее гибкий из-за конвенций.

### ***Простота Изучения и Использования:***

#### **Django:**
* **Плюсы:** Большое сообщество, подробная документация.
* **Минусы:** Может быть сложным для начинающих из-за большого количества концепций и возможностей.
#### **Flask:**
* **Плюсы:** Очень простой для освоения, минимальный набор концепций.
* **Минусы:** Требует от разработчика больше самостоятельной работы.
#### **FastAPI:**
* **Плюсы:** Хорошая документация, использование подсказок типов и валидации делает код понятным.
* **Минусы:** Требует понимания асинхронного программирования.
#### **Вывод:**
   Flask самый простой, FastAPI - прост, если есть опыт с асинхронным программированием, Django - сложнее для начинающих.

### ***Экосистема и Сообщество:***

#### **Django:**
* **Плюсы:** Огромное сообщество, множество готовых решений и библиотек.
* **Минусы:** Некоторые устаревшие подходы, которые сложно изменить.
#### **Flask:**
* **Плюсы:** Большое и активное сообщество, множество расширений.
* **Минусы:** Менее “готовый к использованию”, чем Django.
#### **FastAPI:**
* **Плюсы:** Быстрорастущее сообщество, современные подходы.
* **Минусы:** Меньше готовых решений по сравнению с Django и Flask.
#### **Вывод:** 
   **Django** и **Flask** – имеют большие сообщества, **FastAPI** - относительно новое сообщество.

### ***Вывод:***
  
**Django** – идеален для создания сложных, больших веб-сайтов, где важна скорость разработки и множество готовых инструментов. Он подойдет, если вы хотите создать полнофункциональное веб-приложение с минимальным временем на настройку, но готовы следовать его конвенциям.  
**Flask** – подходит для проектов, где требуется гибкость, простота и минимальный overhead. Идеален для API, микросервисов и небольших веб-сайтов. Flask будет хорошим выбором, если вы хотите сами контролировать архитектуру и компоненты вашего приложения.  
**FastAPI** – лучший выбор для создания высокопроизводительных, масштабируемых API. Этот фреймворк будет полезен, если вы делаете упор на быстродействие, валидацию данных и автоматическую генерацию документации.  

## 7. Заключение.

***Обзор выполненной работы.***

***Дальнейшие планы.***
