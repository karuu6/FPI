ITER=20
OUT=$1
OUT2=$2

for (( i=20; i<=$ITER; i++))
do
	for (( n=0; n<4; n++))
	do
    	`openssl prime -generate -bits $i >> $OUT`
    	`openssl prime -generate -bits $i >> $OUT2`
    done
done
