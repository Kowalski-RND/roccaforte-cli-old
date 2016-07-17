import click
import requests
import pyperclip
from roccaforte.crypto_util import load_key, encrypt, decrypt


@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--potato', prompt='Your potato',
              help='The person to greet.')
def playground(name, potato):
    click.echo('Hello %s!' % name)
    r = requests.post('http://requestb.in/125ioji1', data={'name': name, 'thing': [potato]})
    pyperclip.copy('Test')
    print(r)


# @click.command()
# @click.option('--keyfile', prompt='Pem file location')
# @click.option('--passphrase', prompt='Your passphrase', hide_input=True)
def en(keyfile):
    key = load_key(open(keyfile, 'r').read(), None)
    return encrypt(key, 'Hello world')

def de(keyfile, passphrase, msg):
    key = load_key(open(keyfile, 'r').read(), passphrase)
    decrypted = decrypt(key, msg)
    return decrypted

# playground()
msg = en('/Users/brandon/Desktop/pubkey.pem')
print(msg)
decrypted = de('/Users/brandon/Desktop/private2.pem', 'brandon', msg)
print(decrypted)