ru_count <- c('Франция', 'Украина', 'Мексика', 'Китай', 'Япония', 'Россия', 'Австралия', 'США', 'Италия', 'Испания', 'Аргентина', 'Египет', 'Болгария', 'Швеция', 'Греция', 'rus', 'ru', 'RU', 'рус', 'ру')
ru_caps <- c('Париж', 'Киев', 'Мехико', 'Пекин', 'Токио', 'Москва', 'Канберра', 'Вашингтон', 'Рим', 'Мадрид', 'Буэнос-Айрес', 'Каир', 'София',  'Стокгольм',  'Афины')
eng_count <- c('France', 'Ukrain', 'Mexico', 'China', 'Japan', 'Russia', 'Australia', 'USA', 'Italy', 'Spain', 'Argentina', 'Egypt', 'Bulgary', 'Sweden', 'Greece', 'eng', 'English', 'english', 'Англ', 'англ')
eng_caps <- c('Paris', 'Kiev', 'Mexico city', 'Beiging', 'Tokio', 'Moscow', 'Canberra', 'Washington', 'Rome', 'Madrid', 'Buenos-Aires', 'Cairo', 'Sophia', 'Stockholm', 'Atheens')
ru_facts <- c('удивительная', 'потрясающая', 'интересная', 'самобытная', 'величественная', 'развивающаяся', 'популярная')
eng_facts <- c('amazing', 'oustanding', 'interesting', 'old and spiritfull', 'glorious', 'developing', 'famous')
#Задание 5
defCapitalByCountry <- function(n, lang = 'ru', short = 1, qDebug = FALSE){
  if(qDebug == TRUE){
    print('Данные в режиме отладки:', quote = FALSE)
    print(paste('Страна:', n), quote = FALSE)
    print(paste('Язык ввода:', lang), quote = FALSE)
    print(paste('Какая версия вывода нужна:', short), quote = FALSE)
    print('', quote = FALSE)
  }

  searched <- 0
  if (lang %in% eng_count == T){
    for (i in c(1:length(eng_count))){
      if (eng_count[i] == n){
        searched <- eng_caps[i]
        break
      }
    }
    if (searched == 0){
      print('Bad request')
      return(-1)
    }
  }else{
    for (i in c(1:length(ru_count))){
      if (tolower(ru_count[i]) == tolower(n)){
        searched <- ru_caps[i]
        break
      }
    }
    if (searched == 0){
      print('Неверный запрос')
      return(-1)
    }
  }
  
  
  if (short == 0){
    print(searched)
  }else if (short == 1){
    print(paste(n, '-', searched))
  }
  
  if ((lang %in% eng_count == T) & (short == 2)){
      print(paste('Country', n, '-', 'capital', searched))
  }else if ((lang %in% eng_count == T) & (short == 2)){
    print(paste('Страна', n, '-', 'столица', searched))
  }else {
    
  }
}

defCountryByCapital <- function(n, lang = 'ru', short = 1, qDebug = FALSE){
  if(qDebug == TRUE){
    print('Данные в режиме отладки:', quote = FALSE)
    print(paste('Столица:', n), quote = FALSE)
    print(paste('Язык ввода:', lang), quote = FALSE)
    print(paste('Какая версия вывода нужна:', short), quote = FALSE)
    print('', quote = FALSE)
  }
  
  searched <- 0
  if (lang %in% eng_count == T){
    for (i in c(1:length(eng_caps))){
      if (eng_caps[i] == n){
        searched <- eng_count[i]
        break
      }
    }
    if (searched == 0){
      print('Bad request')
      return(-1)
    }
  }else{
    for (i in c(1:length(ru_caps))){
      if (tolower(ru_caps[i]) == tolower(n)){
        searched <- ru_count[i]
        break
      }
    }
    if (searched == 0){
      print('Неверный запрос')
      return(-1)
    }
  }
  
  
  if (short == 0){
    print(searched)
  }else if (short == 1){
    print(paste(n, '-', searched))
  }
  
  if ((lang %in% eng_count == T) & (short == 2)){
    print(paste('Country', n, '-', 'capital', searched))
  }else if ((lang %in% eng_count == T) & (short == 2)){
    print(paste('Страна', n, '-', 'столица', searched))
  }else {
    
  }
}

def.capital.country <- function(n, lang = 'ру', short = 1, qDebug = F, fact = 0){
  if (fact == 1){
    gen_rand_fact(lang)
  }
  if ((n %in% eng_caps) | (n %in% ru_caps)){
    return(defCountryByCapital(n, lang, short, qDebug))
  }else{
    return(defCapitalByCountry(n, lang, short, qDebug))
  }
}

gen_rand_fact <- function(lang = 'ру'){
  m <- sample(c(1:12), 1)
  n <- sample(c(1:7), 1)
  if (lang %in% eng_count == T){
    print('######')
    print('Interesting fact:')
    cat(eng_count[m], '-', eng_facts[n], 'country, its capital - ', eng_caps[m], '\n')
    print('######')
  }else{
    print('######')
    print('Интересный факт:')
    cat(ru_count[m], '-', ru_facts[n], 'страна, её столица - ', ru_caps[m], '\n')
    print('######')
  }
}

day <- def.capital.country('Atheens', 'eng', short = 0)
day <- def.capital.country('Аргентина', 'угиа', short = 0, fact = 1)
