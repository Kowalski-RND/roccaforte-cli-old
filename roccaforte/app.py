import click
import requests
import pyperclip
import roccaforte.asymmetric as asym
import roccaforte.aes as aes


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
    key = asym.load_key(open(keyfile, 'r').read())
    return asym.encrypt(key, 'I love potato salad')


def de(keyfile, passphrase, msg):
    key = asym.load_key(open(keyfile, 'r').read(), passphrase)
    decrypted = asym.decrypt(key, msg)
    return decrypted


def main():
    msg = en('/Users/brandon/Desktop/pubkey.pem')
    print(msg)
    decrypted = de('/Users/brandon/Desktop/private2.pem', 'brandon', msg)
    print(decrypted)
    pyperclip.copy(decrypted)


if __name__ == '__main__':
    # main()
    key = aes.otk()
    print(key)

    msg = 'I love potato salad'

    result = aes.encrypt(key, msg)
    print(result)

    decrypted = aes.decrypt(key, result[0], result[1])
    print(decrypted)
