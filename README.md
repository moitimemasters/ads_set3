# Для работы программ необходимо:
1. Иметь python версии > `3.10`
2. Иметь компилятор раста `rustc 1.74`
3. Установить библиотеку `matplotlib`: `pip install matplotlib`

## Чтобы сгенерировать массивы для задачи A2, надо запустить файл `a2_generate.py`: `python a2_generate.py`
## Чтобы запустить сортирующую программу на сгенерированных файлах необходимо запустить скрипт `a2_run_and_plot.py`: `python a2_run_and_plot`
## Если есть необходимость запустить сортировку отдельно, то необхходимо скомпилировать и запустиь программу для сортировки:
```sh
> rustc a2.rs
> a2 standart/hybrid path_to_array_file insertion_sort_treshold/none
```
Пример запуска реального файла
```sh
> rustc a2.rs
> a2 standart generated_data/all_random_4000.txt
1400
```
или
```sh
> rustc a2.rs
> a2 hybrid generated_data/all_random_4000.txt 50
1400
```

Вывод программы -- количетсво микросекунд, которые заняла сторировка.
