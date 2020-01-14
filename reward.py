from bitcoin.rpc import RawProxy
import sys

p = RawProxy()
block_hash = p.getblockhash(int(sys.argv[1]))
block = p.getblock(block_hash)
tx_id = block['tx'][0]
tx = p.getrawtransaction(tx_id)
decoded_tx = p.decoderawtransaction(tx)
total_out = 0
for vout in decoded_tx['vout']:
	total_out += vout['value']
multiplier = 1e-8
block_info = p.getblockstats(block_hash)
print(block_info['total_out']*multiplier)
print(block_info['total_fee']*multiplier)
print(total_out - block_info['total_fee']*multiplier)
