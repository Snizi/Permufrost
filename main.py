import argparse


parser = argparse.ArgumentParser()


parser.add_argument('-w', type=str, help="Subdomains file to extract the subdomains", required=True)
parser.add_argument('-o', type=str, help="Output file", required=True)
parser.add_argument('-n', type=str, help="Domain name", required=True)
args = parser.parse_args()

file_name = args.w
output = args.o
domain = args.n


l = []


with open(file_name, "r") as f:
    subs = [x.strip("\n") for x in f.readlines()]
    subs = [x.replace("https://", '') for x in subs]
    subs = [x.replace("http://", '') for x in subs]
    subs = [x.replace(domain, '') for x in subs]

    subdomains = list(set(subs))
    
    for i in subdomains:
        i = i.split('.')
        for j in i:
            if j != '':
                l.append(j)


subdomains = set(l)

with open(output, 'w') as f:
    [f.write(x + '\n') for x in subdomains]

            