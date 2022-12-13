{
	spec <- c('#', '&', '$', '_', '@', '!', '=', '<', '>', '%', '*')
	rus_lib <- c('а', 'б', 'в', 'г', 'д', 'е', 'Є', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', '€')
	eng_lib <- c('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z') 
	lib <- c(rus_lib, toupper(rus_lib), eng_lib, toupper(eng_lib))
	glob_dict <- c(rep(lib, times = 22), rep(spec, times = 118))
	lng = length(glob_dict)
	n <- as.integer(readline("¬ведите n: "))

	password1 <- c(sample(x = glob_dict, size = 1), sample(x = spec, size = 1), sample(x = glob_dict, size = n - 2, replace = TRUE))
	password2 <- c(glob_dict[runif(n = 1, 1, lng)], spec[runif(n = 1, 1, length(spec)], glob_dict[runif(n = n - 2, 1, lng)])
	

	cat(paste0(password1), sep = '')
	cat('\n')
	cat(paste0(password2), sep = '')
	cat('\n')
}