for vel in 1.0 2.0 3.0 4.0 5.0 
do 
echo "420">~/final_project/data_files/data$vel.xyz

temp1=$(awk -f get_coords_first.sh ~/final_project/data_files/Vel_$vel/dump.flow)
echo "$temp1">>~/final_project/data_files/data$vel.xyz

done
