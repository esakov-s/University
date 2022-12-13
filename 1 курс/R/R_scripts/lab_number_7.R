{
#Задание 1
user_pow <- function(x, y, z = 1){
  if (is.na(as.numeric(x)) == T){
    print('x может быть только целым или действительным')
  }
  else if (is.na(as.numeric(y)) == T){
    print('y может быть только целым или действительным')
  }
  else if ((is.na(as.numeric(z)) == T) | (z == 0)){
    print('z может быть только целым или действительным, отличным от 0')
  }
  else{
    x <- as.numeric(x)
    y <- as.numeric(y)
    z <- as.numeric(z)
    print(x ^ y / z)
  }
}



result <- user_pow('8', 2, 4)


}


{
  #Задание 2 -> 3
check_day <- function(n, lang = 'ru', short = TRUE, qDebug = FALSE){
  if(qDebug == TRUE){
    print('Данные в режиме отладки:', quote = FALSE)
    print(paste('День недели:', n), quote = FALSE)
    print(paste('Язык ввода:', lang), quote = FALSE)
    print('', quote = FALSE)
  }
  if (n < 1){
    return (' ')
  }
  n <- (as.integer(n - 1) %% 7 + 1)
  ru_days <- c('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье', 'rus', 'ru', 'RU', 'рус', 'ру')
  eng_days <- c('Monday', 'Tueasday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Eng', 'eng', 'English', 'english', 'Англ', 'англ')

  if (lang %in% eng_days == T){
    return(eng_days[n])
  }
  return(ru_days[n])
}


day <- check_day(4, 'ru')
print(day, quote = FALSE)
}


{
  #Задание 4
  check_day <- function(n, lang = 'ru', short = FALSE, qDebug = FALSE){
    if(qDebug == TRUE){
      print('Данные в режиме отладки:', quote = FALSE)
      print(paste('День недели:', n), quote = FALSE)
      print(paste('Язык ввода:', lang), quote = FALSE)
      print(paste('Нужна ли краткая версия:', short), quote = FALSE)
      print('', quote = FALSE)
    }
    if (n < 1){
      return (' ')
    }
    n <- (as.integer(n - 1) %% 7 + 1)
    ru_days <- c('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье', 'rus', 'ru', 'RU', 'рус', 'ру')
    short_ru_days <- c('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
    eng_days <- c('Monday', 'Tueasday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Eng', 'eng', 'English', 'english', 'Англ', 'англ')
    short_eng_days <- c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    if (lang %in% eng_days == T){
      if (short == FALSE){
        return(eng_days[n])
      }else{
        return(short_eng_days[n])
      }
    }
    if (short == FALSE){
      return(ru_days[n])
    }else{
      return(short_ru_days[n])
    }
  }
  
  
  day <- check_day(4, 'Eng')
  print(day, quote = FALSE)
}

{
  #Задание 5
  check_day <- function(n, lang = 'ru', short = FALSE, qDebug = FALSE){
    if(qDebug == TRUE){
      print('Данные в режиме отладки:', quote = FALSE)
      print(paste('Номера дней недели недели:', n), quote = FALSE)
      print(paste('Язык ввода:', lang), quote = FALSE)
      print(paste('Нужна ли краткая версия:', short), quote = FALSE)
      print('', quote = FALSE)
    }
    nums <- n
    n <- 0
    ans <- c()
    for (n in nums){
      if (n < 1){
        ans <- c(ans, ' ')
        next
      }
      n <- (as.integer(n - 1) %% 7 + 1)
      ru_days <- c('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье', 'rus', 'ru', 'RU', 'рус', 'ру')
      short_ru_days <- c('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
      eng_days <- c('Monday', 'Tueasday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Eng', 'eng', 'English', 'english', 'Англ', 'англ')
      short_eng_days <- c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
      if (lang %in% eng_days == T){
        if (short == FALSE){
          ans <- c(ans, eng_days[n])
        }else{
          ans <- c(ans, short_eng_days[n])
        }
      }else{
        if (short == FALSE){
          ans <- c(ans, ru_days[n])
        }else{
          ans <- c(ans, short_ru_days[n])
        }
      }
    }
    return(ans)
  }
  
  
  day <- check_day(n = c(4, -1, -1, 12), 'ру')
  print(day, quote = FALSE)
}