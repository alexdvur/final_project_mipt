!/bin/bash

module load gcc/9.2.0
module load mpi/openmpi4-x86_64




for vel in 1.0 2.0 3.0 4.0 5.0 
do 
    mkdir ~/final_project/data_files/Vel_$vel
    cd ~/final_project/data_files/Vel_$vel
    cp ~/final_project/lammps_initial_file/in.flow.c ./
    #sed "s/YYYY/$vel/g" in.flow.p > in.flow$vel
    sed "s/YYYY/$vel/g" in.flow.c > in.flow$vel
    srun -N 1 -p RT_build --ntasks-per-node=1 --comment="Dvur test" -J "lammps_test" ~/bin/lmp_mpi -in in.flow$vel
    cd ../../
done


#./temp.gpi
#./rdf.gpi


curl -s -X POST https://api.telegram.org/bot1661455578:AAFrGQLNOBbNRWYXjkx50xAwmDgHoJAd9C0/sendMessage -d chat_id=443270337 -d text="Everything is done"