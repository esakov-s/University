# Задание 1
print_nums <- function(n){
  if (n == 0){
    print(0)
    return (-1)
  }
  if (n > 0){
    n <- as.integer(n)
    print_nums(n - 1)
  }else{
    n <- as.integer(n)
    print_nums(n + 1)
  }
  print(n)
}

a <- print_nums(0)


# Задание 2
print_nums <- function(l, r){
  print(l)
  if (l >= r){
    return (-1)
  }
  print_nums(l + 1, r)

}


l <- 17
l <- as.integer(l)
r <- 17.5
r <- as.integer(r)
a <- print_nums(min(l, r), max(l, r))


# Задание 3
check_pow <- function(n){
  if (n == 1){
    return (T)
  }
  if (n %% 2 == 1){
    return (F)
  }
  return(check_pow(n %/% 2))
  
}


n <- 32
a <- check_pow(n)
a


# Задание 4
nums_sum <- function(n){
  if (n == 0){
    return (n)
  }

  return(nums_sum(n %/% 10) + n %% 10)
  
}


n <- 1
a <- nums_sum(n)
a

{
# Задание 5
print_nums <- function(n){
  if (n == 0){
    return (n)
  }
  cat(n %% 10, sep = "\n")
  return(print_nums(n %/% 10))
  
}


n <- as.integer(readline())

a <- print_nums(n)
}
