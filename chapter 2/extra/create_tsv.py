import milksets.iris
import milksets.seeds
## module can be milksets.iris not str
def save_as_tsv(fname, module):
    features, labels = module.load()
    nlabels=map(str,[ell for ell in labels])
    with open(fname, 'w') as ofile:
        for f, n in zip(features, nlabels):
            print >>ofile, "\t".join(map(str, f) + [n])
        
save_as_tsv('iris.tsv', milksets.iris)            
save_as_tsv('seeds.tsv', milksets.seeds)