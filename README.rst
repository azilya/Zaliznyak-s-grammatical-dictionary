# Zaliznyak-s-grammatical-dictionary

This is a module for predicting grammatical markers for unknown Russian words, according to notation from A.A. Zaliznyak's "Grammar Dictionary of the Russian Language". 
It takes a text string as an input, and returns a list of unknown words with markers predicted for them.

Try it here: <http://web-corpora.net/wsgi3/GDictionary/>
(Web-source for the page is included in the code in the web-page_source folder)

**Important points**
* What we can do: analyze unknown verbs and nouns. </br>What we can't do: analyze other word classes.
* Noun tags denote the stem type and declination class. Verb tags denote only the stem type. You can find more info in the web version of "Grammatical Dictionary of Russian Language" by A.A. Zaliznyak at <a href="http://udarenieru.ru/index.php">this link</a>.
* Project description in Russian: <https://www.hse.ru/ma/ling/st-projects>

**Installation**
Way 1. If you do not want to change the code in any way, you can download the .whl file and then run ``pip install gdictionary-0.756a0-py3-none-any.whl`` from your command line.
Way 2. If you want to see the code and maybe even change it, you can clone this repository and use the modules "as is", or you can run ``python setup.py install`` in the folder and be able to import it whenever you use Python.

**Usage**: 

|``from gdictionary import rusgrab``
|``rusgrab.main("your input text")``

**Output**

* predicted.csv - results

* frequency.csv - "new words", sorted accordingly

**Prerequisites** 

* modules *pymorphy2* and *liac-arff* need to be installed.
* *mystem 3.0* and the *Weka* jar file are required in your working folder if you choose way 1 installation, and in the project folder if you choose way 2.

----------------

Это модуль для предсказания грамматических характеристик незнакомых слов, в соответствии с "Грамматическим словарем русского языка" А.А. Зализняка. Он принимает на вход текстовую строку, находит в ней слова, отсутствующие в словаре Зализняка и пытается предсказать для них лемму и ее тип склонения или спряжения в соответствии с нотацией Грамматичекого словаря.

Пример работы можно посмотреть на сайте <http://web-corpora.net/wsgi3/GDictionary/>
(Код сайта также выложен в репозитории в папке web-page_source)

**Важные замечания**
* Что может делать скрипт: делать предсказания для неизвестных существительных и глаголов. Чего не может делать скрипт: делать предсказания для других частей речи.
* Теги существительных обозначают тип основы и класс склонения. Типы глаголов обозначают тип основы.
* Описание проекта на сайте Высшей школы экономики: <https://www.hse.ru/ma/ling/st-projects>

**Установка**
Способ 1. Если вы не заинтересованы в просмотре и изменении кода, можно просто скачать .whl файл и установить его с помощью команды ``pip install gdictionary-0.756a0-py3-none-any.whl`` в консоли.
Способ 2. Если вас интересует код проекта, можно клонировать репозиторий себе на компьютер и либо пользоваться им из его папки, либо установить с помощью команды ``python setup.py install``. 

**Подробности**

Для работы модуля необходимы исполняемый файл *mystem* версии 3.0 и jar-архив программы *Weka* версии 3.7 и выше: в вашей рабочей папке, если модуль установлен способом 1, и в папке репозитория, если способом 2.
Также требуется установка библиотек *pymorphy2* и *liac-arff*.
Чтобы импортировать модуль: ``from gdictionary import rusgrab``.
Чтобы запустить модуль: ``rusgrab.main("your input text")``.

**Вывод:**

* predicted.csv - результат
* frequency.csv - "новые слова" (сортировка по частоте)

**Вложенные модули:**

* fileworks - кодировки
* kill_small - фильтрует итоговую выдачу
* freq - считает частотность
* write_freq - записывает частоты в файл
* morph - приводит словоформу к лемме
* postprocessing - правила постобработки лемматизации
* recalculation - пересчитывает частотность лемм после постобработки
* targetdata - генерирует признаки для предсказания
* ARFFconversion - генерирует arff для новых слов
* postARFF - объединяет набор признаков 
* predictor - делает предсказание с помощью Weka
* getfinal - собирает итоговый результат в файл
