BEGIN{
N = 420
k = 10000
c = 0
kflag=0;
}
{
#		print "Timestep: " $1
#                print $2
#                print $3
	if ((kflag==1)){
                if (c > 7){
                    print $0
                }
                if (c == 0){
                    print $1
                }
                c+=1
        }
        if ((c==N+8)){
                c=0
                kflag=0
                print "420"
        }
        if ($2 == "TIMESTEP"){
	#	print "k=" $3
	#	print $2
	#	print $3
                kflag=1
        }
}
END{
print ""
}