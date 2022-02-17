path="/Users/luansimoes/recon/14-02-2022-15:24/"


for i in $(ls $path)
do
	file_path=$path$i/live_hosts.txt
	python3 main.py -w $file_path -o $i.txt -n $i
done;


