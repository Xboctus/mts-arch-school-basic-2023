# ADR003.Переход на MongoDB
<!-- Название ADR состоит из [ADR.###] [Коротко суть принятого решения] -->

* Статус: Предложено
* Владелец: aipodolski@mts.ru

## Контекст
<!-- Описание проблемы, требующей решения, причин, побудивших принять решение, ограничений, действовавших на момент принятия решения -->
В рамках развития системы необходимо увеличить возможности по хранению комментариев слушателей конференции. Так же планируется развитие возмжностей базы с докладами - полнотекстовый поиск и возможность в полуавтоматическом режиме проверять доклады на оригинальность.

## Варианты решения
<!-- Описание рассмотренных вариантов c их плюсами и минусами -->
В рамках данного решения будет 

Сравнение вариантов приведено в соответсвие со шкалой: 
* 0 - полностью не удовлетворяет
* 1 - частично удовлетворяет
* 2 - удовлетворяет большинство подребностей
* 3 - полностью удовлетворяет 

Сравнение будет проходить по следующим критериям:
* Возможности полнотекстового поиска
* Возможности хранения неструктурированных данных (текстовые блоки)
* Удобство разработки backend
* Быстродействие
* Работа с реляционными данными

### Вариант 1. MongoDB
<!-- Описание варианта 1 -->

| Критерий                                        | Описание                                                 | Оценка   |
|-------------------------------------------------|----------------------------------------------------------|----------|
| Возможности полнотекстового поиска              | Есть возмжности, отсутствует tokinizer                   | 2        |
| Возможности хранения неструктурированных данных | Возможность хранить документы                            | 3        |
| Удобство разработки backend                     | Есть множество бибилиотек, поддерживающих СУБД           | 3        |
| Быстродействие                                  | Достаточное быстродействие, особенно на запись           | 3        |
| Работа с реляционными данными                   | Возможность связывать не-шардированные коллекции         | 3        |
| ----------------------------------------------- | -------------------------------------------------------- | -------- |
| Итог:                                           |                                                          | 14       |

### Вариант 2. ElasticSearch
<!-- Описание варианта 2 -->
| Критерий                                        | Описание                                                 | Оценка   |
|-------------------------------------------------|----------------------------------------------------------|----------|
| Возможности полнотекстового поиска              | Полная поддержка полнотекстового поиска                  | 3        |
| Возможности хранения неструктурированных данных | Возможность хранить документы                            | 3        |
| Удобство разработки backend                     | Есть множество бибилиотек, поддерживающих СУБД           | 3        |
| Быстродействие                                  | Есть нюансы при операциях на запись (Lucene)             | 2        |
| Работа с реляционными данными                   | Возможности вложенных и parent-child документов          | 2        |
| ----------------------------------------------- | -------------------------------------------------------- | -------- |
| Итог:                                           |                                                          | 13       |

### Вариант 3. PostgreSQL
<!-- Описание варианта 3 -->
| Критерий                                        | Описание                                                 | Оценка   |
|-------------------------------------------------|----------------------------------------------------------|----------|
| Возможности полнотекстового поиска              | Ограниченная поддержка по JSON                           | 1        |
| Возможности хранения неструктурированных данных | Ограниченная поддержка по JSON                           | 1        |
| Удобство разработки backend                     | Есть множество бибилиотек, поддерживающих СУБД           | 3        |
| Быстродействие                                  | Необходим дополнительный разбор данных на запись         | 1        |
| Работа с реляционными данными                   | Полностью поддерживает                                   | 3        |
| ----------------------------------------------- | -------------------------------------------------------- | -------- |
| Итог:                                           |                                                          | 9        |


## Решение
<!-- Описание выбранного решения. Решение должно быть сформулировано чётко ("Мы используем...", "Мы не используем", а не "Желательно.." или "Предлагается..."). 
Должна быть понятна связь между решением и проблемой, почему выбрали именно это решение из вариантов -->
В рамках планируемых изменений системы будет использоваться MongoDB - нюансы по полнотекстовому поиску не так существенны, как другие приемущества, которые она предоставляет (связность сущностей, операции записи)

## Последствия
<!-- Положительные и отрицательные последствия (trade-offs). Арх. решения, которые потребуется принять как следствие принятого решения. Если решение содержит риски, то описано, как с ними планируют поступить (за счет чего снижать, почему принять). -->
* Появляются возможности по недорогой реализации полнотекстового поиска.
* Потребуются переработки модели данных для оптимизации связи различных сущностей (конференция-доклад).