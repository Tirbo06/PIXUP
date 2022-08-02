n_layout = 70
pickup_ascii = [
":"*n_layout,
"       8888888b. 8888888 Y88b   d88P 888     888 8888888b.  ",
"       888   Y88b  888    Y88b d88P  888     888 888   Y88b ",
"       888    888  888     Y88o88P   888     888 888    888 ",
"       888   d88P  888      Y888P    888     888 888   d88P ",
"       8888888P    888      d888b    888     888 8888888P   ",
"       888         888     d88888b   888     888 888        ",
"       888         888    d88P Y88b  Y88b. .d88P 888        ",
"       888       8888888 d88P   Y88b   Y88888P   888        ",
":"*n_layout,
"-"*n_layout,
"Welcome on PIXUP ! Here you can download the first 10",
"images from google images results. You can either use",
"a single QUERY like if you were making a regular search",
"on google image, or, you can pass a .csv file with a",
"list of words, references, product, queries...",
"-"*n_layout,
]

for line in pickup_ascii:
    print(line)