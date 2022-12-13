#1
{
	a <- as.integer(readline())
	b <- as.integer(readline())
	print(a ^ b)
	print(b ^ a)
	print(a / b)
	print(a / 0)
}

#2
{
	n <- as.integer(readline())
	k <- as.integer(readline())
	print(paste('Каждый школьник получит:', k %/% n, 'яблок'))
}

#3
{
	n <- as.integer(readline())
	k <- as.integer(readline())
	print(paste('В корзине останется', k %% n, 'яблок'))
}

#4
{
	n <- as.integer(readline())
	print(paste('Последняя цифра:', n %% 10))
}

#5
{
	n <- as.integer(readline())
	print(paste('Число десятков:', n %/% 10))
}

#6
{
	n <- as.integer(readline())
	print(paste('Вторая с конца цифра:', (n %% 100) %/%10))
}

#7
{
	n <- as.integer(readline())
	print(paste('Сумма цифр:', n %/% 100 + (n %% 100) %/%10 + n %% 10))
}

#8 
{
	n <- as.integer(readline())
	n <- n %% 1440
	print(paste0('Время на часах: ', n %/% 60, ':', n %% 60))
}

#9
{
	n <- as.integer(readline())
	print((n + 1) %% 2)
}

#10
{
	n <- as.integer(readline())
	print(paste0('Следующее чётное число: ', (n %/% 2 + 1) * 2))
}

#11
{
	n <- as.integer(readline())
	a <- n %/% 1000
	b <- n %% 1000 %/% 100
	c <- n %% 100 %/% 10
	d <- n %% 10
	print(a + b - c - d + 1)
}

#12
{
	n <- as.integer(readline())
	m <- as.integer(readline())
	print(paste0('Количество дней, за которые будет пройден маршрут ', (m - 1) %/% n + 1))
}