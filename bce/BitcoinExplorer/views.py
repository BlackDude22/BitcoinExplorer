from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_blocks = [["1", "hash1"], ["2", "hash2"]]
    template = loader.get_template('BitcoinExplorer/index.html')
    context = {
        'latest_blocks': latest_blocks,
    }
    return render(request, 'BitcoinExplorer/index.html', context)

def details(request, block_height):
    block = ["height", "hash", "previous_hash","time", "confirmations", "nonce", "total_transactions", "total_transacted", "total_fee"]
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