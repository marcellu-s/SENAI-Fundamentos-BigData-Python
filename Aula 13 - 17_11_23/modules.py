def colors(text, cor: str):
    match str.lower(cor):
        case 'red':
            return (f'\033[1;31m{text}\033[m')
        case 'green':
            return (f'\033[1;32m{text}\033[m')
        case 'yellow':
            return (f'\033[1;33m{text}\033[m')
        case 'blue':
            return (f'\033[1;34m{text}\033[m')
        case 'purple':
            return (f'\033[1;35m{text}\033[m')
        case 'gray':
            return (f'\033[1;37m{text}\033[m')
        case _:
            return (f'{text}')


def inputFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except:
            print(f"{colors('ERRO: Digite um valor válido.', 'red')}")
            continue
        return valor


def inputInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except:
            print(f"{colors('ERRO: Digite um valor válido.', 'red')}")
            continue
        return valor


def menu(title, lista, min, max):
    '''
    * Gera um menu simpels com seleção e validação de opções
    * @param ordination Define se a ordenação será crescente(TRUE) ou decrescente(FALSE)
    * @param type Define o tipo da ordenação por nome do aluno (abc) ou por média individual (mean)
    * @returns void
    ''' 
                   
    print('='*50)   
    print(f'{title:^50}')
    print('='*50)

    for pos, c in enumerate(lista):
        print(f'{pos+1} - {c}')
    print('='*50)

    while True:
        try:
            op = int(input(f"{colors('Sua opção:', 'purple')}"))
        except:
            print(f"{colors('ERRO: valor inválido!', 'red')}")
            continue

        if min <= op <= max:
            return op
        else:
            print(f"{colors('ERRO: seleção inválida!', 'red')}")
