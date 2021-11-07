## Отчет об использовании codestyle утилит

В качестве инструментов для проверки кода были выбраны:
   1. prospector - многофункциональный линтер, воспользуемся для общего анализа ошибок кода
   2. isort - утилита для сортировки importов 
   3. pycodestyle - стилистический линтер
   
#### 1. prospector
Воспользуемся следующей командой (параметр high взят потому что мне было интересно узнать все недочеты своего кода, в том числе незначительные):
``` prospector --strictness high ```

Вывод команды:
```Messages
========

file.py
  Line: 1
    pylint: import-error / Unable to import 'pandas'
  Line: 2
    pylint: wrong-import-order / standard import "import os" should be placed before "import pandas as pd"
  Line: 3
    pylint: import-error / Unable to import 'numpy'
    pylint: unused-import / Unused numpy imported as np
  Line: 4
    pylint: import-error / Unable to import 'matplotlib.pyplot'
    pylint: unused-import / Unused matplotlib.pyplot imported as plt
  Line: 5
    pylint: import-error / Unable to import 'seaborn'
    pylint: unused-import / Unused seaborn imported as sns
  Line: 6
    pylint: import-error / Unable to import 'definition'
  Line: 9
    pylint: import-error / Unable to import 'sklearn.model_selection'
    pylint: unused-import / Unused train_test_split imported from sklearn.model_selection
    pep8: E231 / missing whitespace after ',' (col 53)
  Line: 10
    pylint: import-error / Unable to import 'sklearn.preprocessing'
    pylint: unused-import / Unused StandardScaler imported from sklearn.preprocessing
  Line: 11
    pylint: import-error / Unable to import 'sklearn.preprocessing'
  Line: 12
    pep8: E225 / missing whitespace around operator (col 6)
  Line: 13
    pep8: E302 / expected 2 blank lines, found 0 (col 1)
  Line: 14
    pylint: unused-variable / Unused variable 'print_info' (col 4)
  Line: 15
    pylint: consider-using-f-string / Formatting a regular string which could be a f-string (col 14)
  Line: 16
    pylint: consider-using-f-string / Formatting a regular string which could be a f-string (col 14)
  Line: 17
    pylint: consider-using-f-string / Formatting a regular string which could be a f-string (col 14)
  Line: 18
    pylint: consider-using-f-string / Formatting a regular string which could be a f-string (col 14)
  Line: 19
    pylint: consider-using-f-string / Formatting a regular string which could be a f-string (col 14)
  Line: 20
    pylint: consider-using-f-string / Formatting a regular string which could be a f-string (col 14)
  Line: 42
    pep8: E225 / missing whitespace around operator (col 13)
  Line: 50
    pylint: unused-variable / Unused variable 'name_string' (col 8)
  Line: 51
    pep8: W605 / invalid escape sequence '\.' (col 68)
    pylint: anomalous-backslash-in-string / Anomalous backslash in string: '\.'. String constant might be missing an r prefix. (col 67)
  Line: 75
    pep8: E302 / expected 2 blank lines, found 0 (col 1)
    mccabe: MC0001 / new_features is too complex (18)
  Line: 80
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 8)
  Line: 81
    pylint: superfluous-parens / Unnecessary parens after 'if' keyword
  Line: 82
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 83
    pylint: superfluous-parens / Unnecessary parens after 'elif' keyword
  Line: 84
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 86
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 103
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 8)
  Line: 105
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 107
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 109
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 111
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 113
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 120
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 8)
  Line: 122
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 124
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 126
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 128
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 130
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 132
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 134
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 136
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 138
    pylint: invalid-name / Variable name "a" doesn't conform to snake_case naming style (col 12)
  Line: 143
    pep8: E305 / expected 2 blank lines after class or function definition, found 0 (col 1)
    pep8: E402 / module level import not at top of file (col 1)
    pylint: import-error / Unable to import 'sklearn.model_selection'
    pylint: wrong-import-position / Import "from sklearn.model_selection import StratifiedKFold" should be placed at the top of the module
  Line: 144
    pep8: E402 / module level import not at top of file (col 1)
    pylint: import-error / Unable to import 'sklearn.linear_model'
    pylint: wrong-import-position / Import "from sklearn.linear_model import LogisticRegression" should be placed at the top of the module
  Line: 145
    pep8: E402 / module level import not at top of file (col 1)
    pylint: import-error / Unable to import 'sklearn.metrics'
    pylint: wrong-import-position / Import "from sklearn.metrics import precision_score, recall_score, confusion_matrix" should be placed at the top of the module
    pep8: E231 / missing whitespace after ',' (col 44)
  Line: 146
    pep8: E402 / module level import not at top of file (col 1)
    pylint: import-error / Unable to import 'sklearn.metrics'
    pylint: wrong-import-position / Import "from sklearn.metrics import accuracy_score" should be placed at the top of the module
  Line: 147
    pep8: E402 / module level import not at top of file (col 1)
    pylint: import-error / Unable to import 'sklearn.model_selection'
    pylint: reimported / Reimport 'GridSearchCV' (imported line 9)
    pylint: wrong-import-position / Import "from sklearn.model_selection import GridSearchCV" should be placed at the top of the module
    pyflakes: F811 / redefinition of unused 'GridSearchCV' from line 9 (col 1)
  Line: 150
    pep8: N802 / function name 'logReg' should be lowercase (col 6)
    pep8: N803 / argument name 'X_train' should be lowercase (col 13)
    pep8: E231 / missing whitespace after ',' (col 19)
    pylint: invalid-name / Function name "logReg" doesn't conform to snake_case naming style
  Line: 152
    pep8: E231 / missing whitespace after ',' (col 23)
  Line: 153
    pep8: E225 / missing whitespace around operator (col 12)
  Line: 154
    pep8: E231 / missing whitespace after ',' (col 32)
  Line: 155
    pep8: E231 / missing whitespace after ',' (col 34)
  Line: 156
    pep8: E231 / missing whitespace after ',' (col 33)
  Line: 157
    pep8: E231 / missing whitespace after ',' (col 30)
  Line: 159
    pylint: unused-variable / Unused variable 'grid_search' (col 4)
  Line: 160
    pep8: N806 / variable 'C_vals' in function should be lowercase (col 10)
    pep8: E501 / line too long (121 > 99 characters) (col 100)
    pylint: invalid-name / Variable name "C_vals" doesn't conform to snake_case naming style (col 8)
  Line: 165
    pep8: E501 / line too long (120 > 99 characters) (col 100)
  Line: 172
    pep8: E501 / line too long (104 > 99 characters) (col 100)



Check Information
=================
         Started: 2021-11-07 16:30:59.310792
        Finished: 2021-11-07 16:31:00.025453
      Time Taken: 0.71 seconds
       Formatter: grouped
        Profiles: default, strictness_high, strictness_veryhigh, no_doc_warnings, no_test_warnings, no_member_warnings
      Strictness: high
  Libraries Used:
       Tools Run: dodgy, mccabe, pep8, profile-validator, pyflakes, pylint
  Messages Found: 87
  ```
  
Видим, что в коде много стилистических ошибок, таких как некрасивые названия переменных (a, C_vals, logReg), 
пропущенные пробелы, неиспользованная переменная name_string,
есть ошибки с импортами и предложения по изменению типов некоторых переменных. 
Также линтер ругается на слишком длинные строки.

#### 2. isort
В ML проектах часто приходится импортировать библиотеки, а порядок их импортирования нужно соблюдать.
В своем проекте я об этом не думала, поэтому следующий инструмент показался полезным.
Сначала проверим, что код несовершен:
```isort file.py --check-only
ERROR: /practic/file.py Imports are incorrectly sorted and/or formatted.
```
И исправим его командой
```
 isort file.py
Fixing /practic/file.py
```
Утилита успешно все пофиксила.

#### 3. pycodestyle
Используем команду:
```pycodestyle --first file.py
```
Вывод команды:
```file.py:9:53: E231 missing whitespace after ','
file.py:12:6: E225 missing whitespace around operator
file.py:13:1: E302 expected 2 blank lines, found 0
file.py:34:5: E266 too many leading '#' for block comment
file.py:51:68: W605 invalid escape sequence '\.'
file.py:51:80: E501 line too long (84 > 79 characters)
file.py:143:1: E305 expected 2 blank lines after class or function definition, found 0
file.py:143:1: E402 module level import not at top of file
```
Видим недочеты разного рода, которые стоит исправить.

### Статистика и выводы
Инструменты показали, что в коде присутствуют стилистические ошибки: ненужные символы, неудачные обозначения, 
не все строчки были на своих местах и иногда слишком длинные - все эти недочеты несложно исправить. 
Также инструменты часто выдавали import-errorы, но с ними на самом деле не должно быть проблем.

Самыми критичными ошибками можно назвать непоследовательные импорты (при переносе из ноутбуков в скрипты могла случайно нарушить порядок).
