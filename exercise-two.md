<h1>Лабораторная работа №2. Условная компиляция. Тесты.</h1>

Воспользуйтесь приложением, разработанным в ходе лабораторной работы 1.
Можете создать новый проект или взять любой другой, на примере которого вы сможете продемонстрировать умение пользоваться предложенными в лабораторной инструментами.


Условная компиляция.
1.	Установите ключ компиляции, при сборке с которым будет выполняться автоматическое заполнение полей логин-пароль и клик по кнопке Вход.
2.	Реализуйте код, который отвечает за автоматическую авторизацию.
3.	Убедитесь, что при установленном ключе собирается версия приложения с прописанными Вами функционалом.
4.	Уберите ключ. Убедитесь, что возможность автоматического входа отсутствует.
5.	На основной форме реализуйте следующей условие: если вход был выполнен автоматически, то выведите красную надпись «Автоматический вход», в противном случае – выведите имя пользователя другим цветом.
6.	На основной форме реализуйте вывод соответствующих сообщений в следующих условиях: если установлен ваш ключ и debug-сборка; если ваш ключ не установлен и debug-сборка.
`TRY-CATCH`
	Обеспечьте полное покрытие своего кода блоками обработок ошибок.
`Тест`
      

Разработайте тест, который имитирует следующие ситуации:

1.	Попытку подбора пароля. Если ваше приложение реагирует на каждые три неудачные попытки, то сымитируйте, минимум 7 заведомо неудачных попыток.
2.	Попытка входа без заполнения полей логин/пароль. Убедитесь, что поля авторизации пустые.
3.	Попытка пользователя сменить пароль на пустое значение.
4.	Попытка администратора заблокировать несуществующего пользователя. Например, с момента открытия администратором формы настроек до нажатия до кнопки «Заблокировать» учетная запись была уже удалена.
5.	Придумайте какую-то другую нежелательную ситуацию. Проверьте, что Ваше приложение адекватно реагирует на внештатные ситуации.