<h1 id="-">Шифратор</h1>
<blockquote>
  <p>Шифратор - программа для шифрования текста несколькими способами, которые будут описаны ниже.</p>
</blockquote>
<h1 id="-">Гайд по запуску</h1>
<details>
  <summary><h3 id="-python-"><strong>Первый этап: установка python и нужных библиотек</strong></h3>
    <h5 id="-python3-pygame-">Если у вас уже установлен python3 и вы можете самостоятельно установить библиотеку tkinter
      — пропустите этот этап</h5></summary>
  <p><strong>1. Скачайте python3 с официального <a href="https://www.python.org/downloads/">сайта</a> и установите его.</strong>
    <strong>2. Во время установки <em>обязательно</em> поставьте галочку "Add Python 3.x to PATH".</strong></p>
  <p><img src="https://python-scripts.com/wp-content/uploads/2018/06/win-install-dialog.40e3ded144b0.png"
          alt="add path screenshot"></p>
  <p><strong>3. Запустите консоль Windows любым удобным для вас способом (например набрав в поиске приложений
    cmd)</strong></p>
  <p><strong>4. Установите нужные библиотеки используя команды</strong></p>
  <blockquote>
    <p>pip install tkinter</p>
  </blockquote>
</details>
<h3 id="-"><strong>Второй этап: запуск программы</strong></h3>
<p><strong>1. Скачайте проект с github любым удобным для вас способом (gitclone или по <a href="">ссылке</a>.</strong>
</p>
<p><strong>2. В консоли перейдите в папку с игрой при помощи команды cd.</strong></p>
<p><strong>3. Запустите игру при помощи команды</strong></p>
<blockquote>
  <p>python main.py</p>
</blockquote>
<p>для запуска в консоли, или</p>
<blockquote>
  <p>python main.py app</p>
</blockquote>
<p>для запуска гарфического интерфейса</p>
<p><strong>4. Зашифруйте весь текст на своем компьютере</strong></p>
<h1 id="-"><strong>Интерфейс программы и доступные виды шифрования</strong></h1>
<p>В программе доступно 3 вида шифрования:</p>
<ul>
  <li>
    <details>
      <summary>Шифр Цезаря</summary>
      Как работает: <a
      href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F">ссылка</a>
      <p>На вход подается файл с текстом, файл куда будет сохранен результат, и сдвиг</p>
      <p>В графическом интерфейсе на вход подается текст и сдвиг</p>
      <p>Также есть возможность расшифровать текст методом частотного анализа</p>
      <p><img src="https://d.radikal.ru/d23/2104/c0/4b7470a3f640.png" alt=""></p>
  </li>
  <li>
    <details>
      <summary>Шифр Виженера</summary>
      Как работает: <a
      href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0">ссылка</a>

      <p>На вход подается файл с текстом, файл, куда будет сохранен результат и ключевое слово</p>
      <p>В графическом интерфейсе на вход подается текст и ключевое слово</p>
      <p><img src="https://d.radikal.ru/d23/2104/c0/4b7470a3f640.png" alt=""></p>
  </li>
  <li>
    <details>
      <summary>Шифр Вернама</summary>
      Как работает: <a
      href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B5%D1%80%D0%BD%D0%B0%D0%BC%D0%B0">ссылка</a>
      <p>Работает почти как шифр Виженера, но генерирует случайный ключ (из сида) такой же по длинне как и шифруемый
        текст</p>
      <p>В графическом интерфейсе на вход подается текст и сид</p>
      <p><img src="https://d.radikal.ru/d23/2104/c0/4b7470a3f640.png" alt=""></p>
  </li>
</ul>
<h2 id="-">Несколько примеров работы шифратора</h2>
<p><strong>Шифр Виженера</strong></p>
<p><img src="https://b.radikal.ru/b19/2104/08/477f81f3b3f3.png" alt=""></p>
<p><img src="https://b.radikal.ru/b38/2104/3e/2f73366a885f.png" alt=""></p>
