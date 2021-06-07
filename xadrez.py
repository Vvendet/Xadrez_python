import pygame
from pygame.locals import *
from sys import exit
from random import randint



pygame.init() # INICIA O PYGAME

######################################
# DEFININDO TELA

y = 700
x = 700
janela = pygame.display.set_mode((x,y))
#janela = pygame.display.set_mode((x,y), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption('XADREZ')
fonte = pygame.font.SysFont('arial',40,bold=True,italic = False)


################################
# DEFININDO TABULEIRO


fundo = pygame.image.load('board.png')
fundo = pygame.transform.scale(fundo, (500,500))

nomes_pecas_negras = ['pieces/bB.png','pieces/bK.png','piecesbN.png','pieces/bP.png','pieces/bQ.png','pieces/bR.png']
nomes_pecas_brancas = ['pieces/wB.png','pieces/wK.png','pieces/wN.png','pieces/wP.png','pieces/wQ.png','pieces/wR.png']

bispo_negras = pygame.image.load('pieces/bB.png')
bispo_negras = pygame.transform.scale(bispo_negras,(68,68))
peao_negras = pygame.image.load(nomes_pecas_negras[3])
peao_negras = pygame.transform.scale(peao_negras,(68,68))
torre_negras = pygame.image.load(nomes_pecas_negras[5])
torre_negras = pygame.transform.scale(torre_negras, (68,68))
rei_pretas = pygame.image.load(nomes_pecas_negras[1])
rei_pretas = pygame.transform.scale(rei_pretas, (68,68))
dama_pretas = pygame.image.load(nomes_pecas_negras[4])
dama_pretas = pygame.transform.scale(dama_pretas,(68,68))
cavalo_pretas = pygame.image.load('pieces/bN.png')
cavalo_pretas = pygame.transform.scale(cavalo_pretas,(68,68))

peao_brancas = pygame.image.load(nomes_pecas_brancas[3])
peao_brancas = pygame.transform.scale(peao_brancas, (68,68))

tabuleiro = [['a1','a2','a3','a4','a5','a6','a7','a8'],
			 ['b1','b2','b3','b4','b5','b6','b7','b8'],
			 ['c1','c2','c3','c4','c5','c6','c7','c8'],
			 ['d1','d2','d3','d4','d5','d6','d7','d8'],
			 ['e1','e2','e3','e4','e5','e6','e7','e8'],
			 ['f1','f2','f3','f4','f5','f6','f7','f8'],
			 ['g1','g2','g3','g4','g5','g6','g7','g8'],
			 ['h1','h2','h3','h4','h5','h6','h7','h8']]

coord_coluna_horizontal = ['a','b','c','d','e','f','g','h']
coord_coluna_vertical = ['1','2','3','4','5','6','7','8']

##################################################
# FAZER O JOGO RODAR
while True:
	

	###################################################
	## SAIR DO JOGO
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()



	#####################################################
	#### POSICAO DO MOUSE
	mouse = pygame.mouse.get_pos()
	posicio = str(mouse[0])
	posicio2 = str(mouse[1])
	mensagem = f'Posicao: {str(mouse)}'
	texto_formatado = fonte.render(mensagem, False, (255,255,255))
	#janela.blit(texto_formatado,(0,0))
	

	


	##################################################
	##### ESCREVER AS COORDENADAS AO ENTORNO DO TABULEIRO 
	contador = 0
	for j in coord_coluna_vertical[::-1]:
		coord = j
		text = fonte.render(coord,False, (255,255,255))
		janela.blit(text,(580,45+contador))
		contador += 66

	contador = 0
	for j in coord_coluna_horizontal:
		coord2 = j
		text2 = fonte.render(coord2, False, (255,255,255))
		janela.blit(text2,(60+contador,565))
		contador += 63


	

	

	################################################################
	### MONTANDO O TABULEIRO NA TELA

	janela.blit(fundo, (50,50))

	########## BISPOS_NEGROS
	janela.blit(bispo_negras, (50+2*62,50))
	janela.blit(bispo_negras, (50+2*62+3*62,50))

	######### PEOES_NEGROS
	contador = 0
	y = 50
	janela.blit(peao_negras, (y,50+62))
	while contador != 7:
		janela.blit(peao_negras, (y+62,50+62))
		y += 62
		contador += 1

	########### TORRE NEGRAS
	janela.blit(torre_negras,(50,50))
	janela.blit(torre_negras,(480,50))

	######### REI NEGRAS
	janela.blit(rei_pretas,((50+2*62+62,50)))

	########## DAMA NEGRAS
	janela.blit(dama_pretas,(50+4*62,50))

	########## CAVALOS NEGROS
	janela.blit(cavalo_pretas,(50+62,50))
	janela.blit(cavalo_pretas,(480-62,50))

	######## PEOES_BRANCOS
	contador = 0
	y = 50
	janela.blit(peao_brancas,(50,550-62*2 -7))
	while contador != 7:
		janela.blit(peao_brancas,(y+62,550-62*2 -7))
		y += 62
		contador += 1


	pygame.display.update()
