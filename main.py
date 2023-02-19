import telebot, constants
from time import sleep
from telebot import types

#chave bot
chave = "6138588097:AAGorL1uRJ_MQNX2kjbsec5iu6xGfV-ogb8"

bot = telebot.TeleBot(chave)
chat_id = 1829626918
lista = []


#comando pizza
@bot.message_handler(commands=["pizza", "Pizza"])
def pizza(mensagem):
  for c in lista:
    lista.pop()
    lista.pop()
  sabor = bot.send_message(mensagem.chat.id, "digite o sabor: ")
  bot.register_next_step_handler(sabor, Sabor)


def Sabor(mensagem):
  open("sabor.txt", "w").write(mensagem.text)
  bot.send_message(mensagem.chat.id, "Anotado!")
  lista.append(mensagem.text)

  #faz o input do endereço de entrega e inicia a função Endereço
  sent = bot.send_message(mensagem.chat.id, "Digite seu endereço: ")
  bot.register_next_step_handler(sent, Endereco)


def Endereco(mensagem):
  open("endereco.txt", "w").write(mensagem.text)
  bot.send_message(mensagem.chat.id, "obrigado!")
  lista.append(mensagem.text)

  #printa para o usuario o nome do cliente e o endereço de entrega da pizza
  bot.send_message(
    chat_id, """{} pediu pizza!!!
  Sabor: {}
  Entregar em: {}""".format(mensagem.chat.first_name, lista[0], lista[1]))


#comando abraço
@bot.message_handler(commands=["abraço", "abraco", "Abraço", "Abraco"])
def abraço(mensagem):
  texto = "abraço"
  bot.send_message(mensagem.chat.id, texto)
  #se alguma pessoa digitar /abraço o bot manda uma mensagempara o criador do bot
  bot.send_message(chat_id, "{} pediu abraço".format(mensagem.chat.first_name))


#comando chute
@bot.message_handler(commands=["chute", "Chute"])
def chute(mensagem):
  bot.send_message(chat_id, "{} te chutou".format(mensagem.chat.first_name))


#comando basico
def verificar(mensagem):
  return True


@bot.message_handler(func=verificar)
def responder(mensagem):
  texto = "Olá!"
  bot.reply_to(mensagem, texto)
  sleep(2)
  texto = """
  comandos disponiveis:
    /abraco
    /pizza
    /chute"""
  bot.send_message(mensagem.chat.id, texto)


bot.polling()
