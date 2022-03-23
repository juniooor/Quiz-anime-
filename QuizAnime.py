#quiz de perguntas e respostas tema de anime

respostas_certas=0

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Em Komi-san: Qual o objetivo da Komi?','respostas': {
            'a': 'Ter uma paixão',
            'b': 'Fazer 100 Amigos',
            'c': 'Conseguir socializar com os colegas de classe',}, 
            'resposta_certa': 'b',
        },
    'Pergunta 2': {
        'pergunta': 'Em Nanatsu No Taizai: Qual personagem tem desenhado um porco no pescoço?','respostas': {
            'a': 'Merlin',
            'b': 'Ban',
            'c': 'Diane',}, 
            'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Em shingeki no kiojin: Qual o nome das 3 MUralhas? ','respostas': {
            'a': 'Trost, Maria, Sina',
            'b': 'Sina, Maria, Rose',
            'c': 'Shiganshina, Maria, Trost',}, 
            'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Em Black Clover: O que reside na quinta folha do trevo no livro?','respostas': {
            'a': 'Dêmonio',
            'b': 'Mal Presságio',
            'c': 'Elfo',}, 
            'resposta_certa': 'a',
        },
    'Pergunta 5': {
        'pergunta': 'Em Demon Slayer: Qual o nome da 6ºLua inferior?','respostas': {
            'a': 'Akaza',
            'b': 'Uzui',
            'c': 'Rui',}, 
            'resposta_certa': 'c',
        },
     'Pergunta 6': {
        'pergunta': 'Em Tate no Yusha: Qual o nome do heroi da lança?','respostas': {
            'a': 'Motoyasu',
            'b': 'Naofumi',
            'c': 'Itsuki',}, 
            'resposta_certa': 'a',
        },
     'Pergunta 7': {
        'pergunta': 'Em Dr. Stone: Qual o nome da villa em que Senku vive?','respostas': {
            'a': 'Asagiri',
            'b': 'Ishigami',
            'c': 'Hokage',}, 
            'resposta_certa': 'b',
        },
     'Pergunta 8': {
        'pergunta': 'Em Black CLover: Qual o Esquadrão mais poderoso?','respostas': {
            'a': 'Alvorecer Dourado',
            'b': 'Touros Negros',
            'c': 'Rosa Azul',}, 
            'resposta_certa': 'a',
        },
     'Pergunta 9': {
        'pergunta': 'Em Jujutsu Kaisen: Quem são os companheiros de Itadori?','respostas': {
            'a': 'Mahito e Hanami',
            'b': 'Todou e Satoru',}, 
            'c': 'kugisaki e Fujiguro',
            'resposta_certa': 'c',
        },
     'Pergunta 10': {
        'pergunta': 'Em Jojo bizarre adventures... Giovanne giorno é:','respostas': {
            'a': 'ladrão',
            'b': 'Dançarino',}, 
            'c': 'Espião',
            'resposta_certa': 'a',
        },
    }

for pk , pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_user = str(input('Sua resposta:')).lower()

    if resposta_user == pv['resposta_certa']:
        print('VOCÊ ACERTOU!!!')
        respostas_certas +=1
    else: 
        print('IXIII ERROU!!')
    print() 

qtd_perguntas = len(perguntas)
porcentagem_acerto= respostas_certas / qtd_perguntas * 100

print(f'você acertou {respostas_certas} respostas')
print(f'sua porcentagem foi de {porcentagem_acerto}%')