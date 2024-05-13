# PythonLabsPart2
------find_kth_largest------
Напишіть функцію для пошуку k-того найбільшого елемента в заданому масиві цілих чисел. Параметр k задається на вхід функції і визначає порядковий номер найбільшого елемента, який потрібно знайти. Наприклад, якщо k = 1, програма повинна знайти найбільший елемент в масиві. Якщо k = 2, програма повинна знайти другий за величиною елемент, і так далі.
Умови задачі:
Масив цілих чисел передається у вашу функцію. Розмір масиву повинен бути не менше k. Програма повинна вивести k-тий найбільший елемент і його позицію (індекс) в масиві. Приклад введення та виведення результату:
Вхідний масив:[15, 7, 22, 9, 36, 2, 42, 18] Задане k: 3 Знайдений 3-й найбільший елемент: 22 Позиція 3-го найбільшого елемента в масиві: 2

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest .


------min_eating_time------
Горила Джекі із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою.
Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.
Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.
Напишіть функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі банани на складі протягом Н годин, поки повернеться охорона.

Приклад 1: piles = [3,6,7,11], H = 8
Результат: 4

Приклад 2: piles = [30,11,23,4,20], H = 5
Результат: 30

Приклад 3: piles = [30,11,23,4,20], H = 6
Результат: 23

Важливо: 1 <= piles.length <= 10^4 piles.length <= H <= 10^9 1 <= piles[i] <= 10^9

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище

------max_diameter------
Для заданого бінарного дерева реалізуйте функцію, яка обчислює та повертає значення максимального діаметра у бінарному дереві - найвіддаленішу відстань між двома листками. Максимальний діаметр у бінарному дереві визначає найбільшу відстань між будь-якою парою листків (кінцевих вузлів) у дереві. Діаметр вимірюється як кількість ребер, які потрібно пройти, щоб дістатися одного листка від іншого. Максимальний діаметр не обов'язково має включати в себе кореневий вузол

Нехай у вас задане бінарне дерево такого вигляду:

        1
       /  \
      3    2
     / \
    7   4
   /     \
  8       5
 /         \
9           6
Для даного дерева максимальний діаметр становить 6: 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6 - для проходження від листка 9 до листка 6 слід пройти 6 ребер.

Реалізована вами функція binary_tree_diameter(tree: BinaryTree) -> int отримує на вхід корінь бінарного дерева та повертає максимальний діаметр дерева.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)


------heap_based_priority_queue------
Реалізуйте структуру даних "черга з пріоритетами" на основі бінарної купи binary heap, в якому кожен батьківський елемент має вищий пріоритет, ніж пріоритети його дітей.

Якщо у двох елементів однаковий пріоритет, то батьківський елемент може мати пріоритет, ідентичний пріоритету одного або обох його дітей.

Операції, які підтримує ваша черга:

Вставка елемента з заданим значенням та пріоритетом до черги.
Видалення та повернення елемента з найвищим пріоритетом з черги.
Перегляд черги без її зміни.
Для реалізації такої черги з пріоритетами слід використати окремий клас Node, де кожен елемент буде мати два поля: значення та пріоритет. При вставці елемента до черги, його потрібно розмістити у відповідному порядку з урахуванням пріоритету. При видаленні елемента з найвищим пріоритетом, на його місце слід розмістити елемент з наступним найвищим пріоритетом.


------find_islands------
Нехай дано двійкову матрицю, де 0 означає воду, а 1 — сушу, а з’єднані числа 1 утворюють острів, підрахуйте загальну кількість островів.
Наприклад, розглянемо таке зображення, де синім позначено воду (0), а сірим - сушу (1):

            [["1", "0", "1", "0", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "1", "0", "1", "0", "1", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "1", "0", "0", "0"],
            ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"],
            ["0", "1", "0", "1", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0"],
            ["0", "0", "0", "1", "0", "0", "1", "1", "1", "0"],
            ["1", "0", "1", "0", "1", "0", "0", "1", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"]]
Загалом у наведеній вище матриці присутні п’ять островів. 


------penguins_need_gas------
Критично важливим є постачання газу між сховищами та містами пінгвінів взимку. Вибух газопроводів може призвести до дефіциту палива та викликати значні проблеми у домівках бравих пінгвінів. Тому ряд газопроводів зараз відключили для ремонту.

Ви, як студент курсу Алгоритми і структури даних маєте бажання допомогти Пінгвінам. Ви готові написати для них алгоритм, який перевірить, чи існує спосіб транспортування палива з будь-якого сховища до будь якого міста з використанням газопроводів, які не вивели в ремонт. Зауважте, що газ по трубі можна транспортувати лише в одному напрямку.

Для розв'язання цієї задачі пінгвіни надали вам:

список міст

список газосховищ

список активних газопроводів, у форматі [ ['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2'] ], де ['Львів', 'Стрий'] означає наявність газопроводу між містами Львів та Стрий, де подача газу відбувається від Львова до Стрия

Ваша програма має повернути результат у форматі: [ 'газосховище', ['місто_1', 'місто_2'] , де:

газосховище - назва газосховища
['місто_1', 'місто_2'] - список міст, до яких неможливо подати газ з цього газосховища
Зауважте, що газ може подаватись з газосховища до будь якого міста транзитом через інші міста.

У випадку, якщо є зв'язок між усіма газосховищами та містами, поверніть пустий список


------trie------
Створити клас структури даних Trie (префіксне дерево), який містить методи вставки слова, пошуку слова та пошуку префіксу. Реалізувати функцію на мові програмування Python, яка отримує список стрічок patterns і повертає об'єкт класу Trie



------max_flow------
Компанія "Квітка" має у Львові багато магазинів, де вони продають квіти. Також, вони мають квіткові ферми, де ці квіти вирощують з метою продажу. Наближається день Матері, а згодом - свято останнього дзвоника. В них є інформація про всі дороги, що ведуть від їх ферм до магазинів, та максимальна кількість машин, які можуть проїхати цими дорогами протягом дня з урахуванням щільності руху. Власники компанії намагаються зрозуміти, скільки саме машин квітів вони зможуть доставити з своїх ферм до магазинів протягом одного дня і звернулись до вас за допомогою., щоб ви порахували яку максимальну кількість машин квітів власники компанії зможуть привезти за день.

Вхідні дані:

файл roads.csv, який містить:
список ферм F1, F2, F3 в першій лінійці
список магазинів S1, S2, S3, S4, S5 - в другій лінійці
список доріг між перехрестями та відстань між ними у форматі: Х1, Х2, 4. цей запис означає, що між перехрестями Х1 та Х2 за день максимально може проїхати 4 автомобілі. Запис Х2, S1, 10 означає, що від перехрестя Х2 до магазину S1 може проїхати 10 автомобілів за день.
Вихідні дані:

Максимальна кількість автомобілів, які зможуть проїхати протягом дня з квіткових ферм до квіткових магазинів.

