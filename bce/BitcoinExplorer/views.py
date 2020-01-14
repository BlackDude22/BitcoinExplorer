from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from BitcoinExplorer.session import *

def index(request):
    client = Client()
    client.create_session()
    latest_blocks = client.execute_command('python latest_blocks.py')
    client.close_session()
    template = loader.get_template('BitcoinExplorer/index.html')
    context = {
        'latest_blocks': latest_blocks,
    }
    return render(request, 'BitcoinExplorer/index.html', context)

def details(request, block_height):
    client = Client()
    client.create_session()
    block = client.execute_command('python block.py ' + str(block_height))
    client.close_session()
    context = {
    	'height': block[0],
    	'hash': block[1],
    	'previous_hash': block[2],
    	'time': block[3],
    	'confirmations': block[4],
    	'nonce': block[5],
    	'total_transactions': block[6],
    	'total_transacted': block[7],
    	'total_fee': block[8],
    }
    return render(request, 'BitcoinExplorer/block.html', context)