is.interval <- function(a = c(0, 0)){
  if (length(a) > 2 | length(a) == 0){
    return (F)
  }
  return(T)
}

as.interval <- function(a){
  if(is.interval(a) == T){
    if (length(a) == 1){
      a <- c(a, a)
    }
    if(a[1] > a[2]){
      d <- a[2]
      a[2] <- a[1]
      a[1] <- d
    }
    return(a)
  }else{
    return (NULL)
  }
}

show.interval <- function(a){
  a <- as.interval(a)
  if (is.null(a) == T){
    print("Невозможно преобразовать к интервалу")
  }else{
    cat(paste0('[', a[1], ':', a[2], ']'))
  }
}

plus.i <- function(x, y){
  x <- as.interval(x)
  y <- as.interval(y)
  if (is.null(x) == T | is.null(y) == T){
    print("Операция неозможна")
    return(NULL)
  }
  res <- c(x[1] + y[1], x[2] + y[2])
  return (res)
}

minus.i <- function(x, y){
  x <- as.interval(x)
  y <- as.interval(y)
  if (is.null(x) == T | is.null(y) == T){
    print("Операция неозможна")
    return(NULL)
  }
  res <- c(x[1] - y[2], x[2] -  y[1])
  return (res)
}

multi.i <- function(x, y){
  x <- as.interval(x)
  y <- as.interval(y)
  if (is.null(x) == T | is.null(y) == T){
    print("Операция неозможна")
    return(NULL)
  }
  res <- c(min(x[1] * y[2], x[2] * y[1], x[1] * y[1], x[2] * y[2]), max(x[1] * y[2], x[2] * y[1], x[1] * y[1], x[2] * y[2]))
  return (res)
}

div.i <- function(x, y){
  x <- as.interval(x)
  y <- as.interval(y)
  if ((is.null(x) == T | is.null(y) == T) & (y[1] > 0 | y[2] < 0)){
    print("Операция неозможна")
    return(NULL)
  }
  res <- multi.i(x, c(1.0 / y[2], 1.0 / y[1]))
  return (res)
}