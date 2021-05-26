from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib


navegador = webdriver.Chrome
#   REALIZAR LOGIN


navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)
#Aqui estamos dando um parametro que nao exista na pagina de login, o qr. definimos que oq n existe lá
#é a parte lateral, onde fica os contatos, e colocamos ela aqui, para o navegador procurar.
#por isso o menor que 1. caso nao exista 0, ele verificará novamente.
#na linha de baixo o sleep, é pra ele tentar saber se existe algo =>1 a cada 1 segundo.

#   ENVIAR MENSAGENS

#No exemplo que eu tive acesso, ele manda mensagem com um texto, colocado tbm pelo excel.
#Achei bastante trabalhoso. aqui no python, podemos escrever a mensagem e modifica-la na hora que quisermos.

mensagem = 'O que vale é estudar'
pessoa = 'Francisgleydson'
#Caso o contato esteja salvo em um arquivo excel. faça pessoa = contatos_df.loc[i, 'Pessoa']

numero = 5581999999999
#Caso o contato esteja salvo em um arquivo excel. faça pessoa = contatos_df.loc[i, 'Pessoa']

#Mas o whatsapp só aceita texto em HTML, por isso vamos usar a biblioteca urllib
texto = urllib.parse.quote(f'Olá, {pessoa}! {mensagem}')
#Assim transformamos a mensagem em html, e ela já poderá ser enviada via web.


link = f'https://web.whatsapp.com/send?phone{numero}&text={texto}'

navegador.get(link)
while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)
navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
#Vou explicar oq rolou aqui. Executando o código sem essa ultima linha, a gente vai ver que ele escreve
#Pra todos, mas nao envia, apenas escreve! Com essa ultima linha ele vai apertar o entender logo após a escrita
#E assim enviaremos a mensagem contida na caixa de mensagem para pessoa
time.sleep(10)
#como é uma automacao é importante colocar um tempo para a automacao nao ter erro
#as vezes ele escrevera a mensagem em 1 segundo, outras vezes, n. entao vale a pena resguardar
#Fora o block do whatsapp, que n permite automacao!!